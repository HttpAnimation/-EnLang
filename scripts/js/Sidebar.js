document.addEventListener('keydown', (event) => {
    // Check if the pressed key is 'F'
    if (event.key === 'F' || event.key === 'f') {
        const sidebar = document.getElementById('sidebar');
        // Toggle the visibility of the sidebar
        sidebar.style.display = (sidebar.style.display === 'none' || sidebar.style.display === '') ? 'block' : 'none';
    }
});