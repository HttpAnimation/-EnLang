// Function to fetch and insert Markdown file contents
function insertMarkdownFileContents(filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(text => {
            // Insert Markdown file contents into the designated div
            document.getElementById('md-block').innerText = text;
        })
        .catch(error => {
            console.error('Error fetching Markdown file:', error);
        });
}

// Call the function with the path to your Markdown file
insertMarkdownFileContents('https://raw.githubusercontent.com/HttpAnimation/-EnLang/main/README.md');