# 📄 Document Summarizer

Document Summarizer is a web-based application designed to simplify the process of converting lengthy text into concise and meaningful summaries. The system leverages advanced Natural Language Processing (NLP) techniques to ensure contextual accuracy and high-quality output.

---

## 🚀 Tech Stack

### 🎨 Frontend
- 🌐 HTML5
- 🎨 CSS3 (Responsive Design)
- 📜 JavaScript (Dynamic UI & API Communication)

### ⚙️ Backend
- 🐍 Python
- 🔥 Flask (Web Framework)
- 🧠 NLP Algorithms (TextRank & PageRank)
- 🔐 Flask-Login (Authentication Management)
- 🗃️ SQLAlchemy (ORM)

### 🗄️ Database
- 🐬 MySQL

---

## 🧠 Project Overview

The Document Summarizer intelligently converts long documents into structured summaries that highlight key information.

- 📑 Uses **TextRank algorithm** for shorter documents
- 📊 Uses **PageRank algorithm** for longer and complex texts
- 🎯 Optimizes summarization based on input characteristics
- ✨ Ensures contextual relevance and correctness

The system reduces the time and effort required for manual text analysis, making it ideal for students, researchers, and professionals.

---

## 🖥️ Frontend Design

The frontend is developed using HTML, CSS, and JavaScript with a focus on simplicity and usability.

### Key Features:
- 📤 Document upload form
- ⚙️ Summarization settings (e.g., summary length)
- 📄 Summary results displayed on the same page
- 🔄 Seamless communication with backend (no page refresh)
- 📱 Fully responsive design (Desktop, Tablet, Mobile)

JavaScript dynamically handles user input and communicates with backend APIs for smooth user experience.

---

## ⚙️ Backend Architecture

The backend is implemented in Python using the Flask framework due to its simplicity and flexibility.

### Core Functionalities:
- 👤 User Registration
- 🔐 User Login & Logout
- 👤 Profile Management
- 📤 Document Upload
- 🧠 Text Summarization API

Flask manages:
- User requests
- Document processing
- Database communication

---

## 🧠 Summarization Engine

The system supports both:

### ✂️ Extractive Summarization
- Selects important sentences directly from the original text.

### 🧬 Abstractive Summarization
- Generates a refined version of the content using advanced deep learning techniques.

### Process Flow:
1. 📄 User uploads document (.txt supported)
2. 🔍 Backend extracts text content
3. 🧠 Algorithm analyzes phrases and key sentences
4. 📊 Summary generated based on user preference (e.g., length)
5. 📤 Summary sent back to frontend for display

---

## 📂 Document Upload & Processing

- Users upload documents via HTML form.
- Currently supports `.txt` format.
- Future scalability:
  - 📕 PDF support using PyPDF2
  - 📝 DOCX support using python-docx

After extraction, the summarization engine processes the content and returns a structured summary.

---

## 🗄️ Database Structure

MySQL is used for secure and efficient data storage.

### Tables Include:
- 👤 User Profiles (username, email, hashed password)
- 📄 Document-related data
- 🔐 Authentication details

SQLAlchemy ORM ensures:
- Secure database interaction
- Efficient query execution
- Clean data modeling

---

## 🔐 Authentication & Security

- Flask-Login manages user sessions.
- Passwords are encrypted and securely stored.
- Secure login and logout functionality ensures data protection.

---

## 🎯 Target Audience

- 🎓 Students
- 🔬 Researchers
- 💼 Professionals

The application enhances productivity by simplifying large-scale text analysis in the digital era.

---

## 📌 Project Objective

This project demonstrates:

- 🧠 Implementation of NLP algorithms (TextRank & PageRank)
- 🔥 Backend development with Flask
- 🌐 Interactive frontend development
- 🗄️ Database integration
