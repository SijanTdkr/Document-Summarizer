async function summarizeDocument() {
    const documentText = document.getElementById('document').value;
    const summarizeBtn = document.getElementById('summarizeBtn');
    const resummarizeBtn = document.getElementById('resummarizeBtn');

    // Disable button while processing
    summarizeBtn.disabled = true;

    // Send document text to the server for summarization
    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ document: documentText })
    });

    const result = await response.json();

    // Display the summary in the output box
    const summaryBox = document.getElementById('summary');
    if (result.summary) {
        summaryBox.textContent = result.summary;
        summarizeBtn.style.display = 'none';
        resummarizeBtn.style.display = 'inline-block'; // Show re-summarize button after first summary
    } else {
        summaryBox.textContent = 'Error: ' + result.error;
    }

    // Re-enable the button after processing
    summarizeBtn.disabled = false;
}

function toggleDarkMode() {
    const darkModeButton = document.getElementById('darkModeButton');
    if (document.body.classList.contains('dark-mode')) {
        document.body.classList.remove('dark-mode');
        darkModeButton.textContent = 'Dark Mode';
    } else {
        document.body.classList.add('dark-mode');
        darkModeButton.textContent = 'Light Mode';
    }
}
