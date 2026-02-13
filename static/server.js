const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Serve static files (CSS, JS, images) from the 'static' folder
app.use(express.static(path.join(__dirname, 'static')));

// Route for the login page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'login.html'));
});

// Route for the signup page
app.get('/signup', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'signup.html'));
});

// Route for other pages (you can add more routes for other pages)
app.get('/other-page', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'other-page.html'));
});

// API endpoint to summarize documents
app.post('/summarize', (req, res) => {
    const documentText = req.body.document;

    // Simulate summarization logic (this can be replaced with actual logic)
    const summary = documentText.length > 100 ? documentText.slice(0, 100) + '...' : documentText;

    // Respond with the summary
    res.json({ summary });
});

// Error handling for 404
app.use((req, res, next) => {
    res.status(404).send('Page not found');
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
