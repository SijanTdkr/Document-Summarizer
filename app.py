from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import hashlib
from db_config import get_db_connection  # Importing the function from db_config
from summa import summarizer  # TextRank Summarizer
import networkx as nx
import numpy as np
from datetime import datetime
import bcrypt



app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Simulating a database for user data (in-memory database)
users_db = {}
# Simulating user profile information (for the sake of the example)
user_profiles = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def handle_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    

    try:
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query user by email
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            # Compare the provided password with the stored hashed password
            stored_password_hash = user[0]
            if bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
                session['user_email'] = email
                
                # Successful login, redirect to the profile page
                cursor.close()
                connection.close()
                print(f"reached here")
                return jsonify(success=True, message='Great', redirect_url=url_for("fe"))

        
        # Invalid credentials
        cursor.close()
        connection.close()
        return "Invalid credentials. Please try again.", 400

    except Exception as e:
        # Log the error and avoid exposing sensitive info in production
        print(f"Error occurred: {e}")
        return "An error occurred during authentication. Please try again later.", 500


@app.route("/signup", methods=["POST"])
def handle_signup():
    print(f"reached here")
    try:
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        # image = request.files.get("image")  # Handling image upload

        if not email or not username or not password:
            return "All fields are required", 400


        # Hash the password securely using bcrypt
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the email already exists in the database
        cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return "Email already exists", 400

        # Insert the user into the database
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password.decode())
        )
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("login"))

    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred during signup. Please try again later.", 500

@app.route("/fe")
def fe():
    return render_template("fe.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    # Redirect directly to the profile.html page
    return render_template("profile.html")


@app.route("/update_profile", methods=["POST"])
def update_profile():
    try:
        data = request.get_json()
        new_name = data.get("name")
        email = session.get("user_email")  # Assume user email is stored in the session

        if not email:
            return jsonify({"error": "Unauthorized"}), 401

        # Update the username in the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET username = %s WHERE email = %s", (new_name, email))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Profile updated successfully"})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while updating the profile"}), 500

@app.route("/get_profile", methods=["GET"])
def get_profile():
    try:
        email = session.get("user_email")  # Assume user email is stored in the session

        if not email:
            return jsonify({"error": "Unauthorized"}), 401

        # Fetch user data from the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT username, email FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return jsonify({
                "success": True,
                "data": {
                    "username": user[0],
                    "email": user[1],
                }
            })
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while fetching the profile data"}), 500



# Function to implement TextRank summarization
def text_rank_summary(text):
    return summarizer.summarize(text)

# Function to implement a simple PageRank-based summarization
def page_rank_summary(text):
    sentences = text.split('.')
    graph = nx.Graph()
    for i, sentence1 in enumerate(sentences):
        for j, sentence2 in enumerate(sentences):
            if i != j:
                similarity = compute_similarity(sentence1, sentence2)
                graph.add_edge(i, j, weight=similarity)
    
    pagerank_scores = nx.pagerank(graph)
    ranked_sentences = sorted(pagerank_scores, key=pagerank_scores.get, reverse=True)
    summary = ' '.join([sentences[i] for i in ranked_sentences[:3]])  # Adjust to get top N sentences
    return summary

# Helper function to compute sentence similarity 
def compute_similarity(sentence1, sentence2):
    return np.random.random()  

# Function to apply summarization logic based on document length or complexity
def apply_summarization_logic(text):
    # Apply TextRank if the document is short, PageRank for longer documents
    if len(text.split()) < 300:  # Example condition: text with fewer than 300 words
        return text_rank_summary(text)
    else:
        return page_rank_summary(text)

# API route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    document = data['document']
    
    # Automatically apply the best summarization method based on the document's length
    summary = apply_summarization_logic(document)

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
