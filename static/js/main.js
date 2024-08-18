document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    const resultDiv = document.getElementById('result');
    const progressBar = document.querySelector('.progress-bar-fill');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        try {
            resultDiv.innerHTML = '<p>Processing video... This may take a while.</p>';
            progressBar.style.width = '0%';
            
            const response = await fetch('/process', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Server error');
            }
            
            const result = await response.json();
            
            resultDiv.innerHTML = `
                <h2>Processing Complete</h2>
                <p>Dubbed Video: <a href="/download/${encodeURIComponent(result.output_video)}" download>Download</a></p>
                <p>Subtitles: <a href="/download/${encodeURIComponent(result.subtitles)}" download>Download</a></p>
            `;
            progressBar.style.width = '100%';
        } catch (error) {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>An error occurred: ${error.message}</p>`;
            progressBar.style.width = '0%';
        }
    });
});