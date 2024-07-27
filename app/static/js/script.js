document.addEventListener('DOMContentLoaded', () => {
    const classifyBtn = document.getElementById('classifyBtn');
    const imageUpload = document.getElementById('imageUpload');
    const result = document.getElementById('result');
    const uploadedImage = document.getElementById('uploadedImage');

    imageUpload.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                uploadedImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    classifyBtn.addEventListener('click', () => {
        const file = imageUpload.files[0];
        if (!file) {
            result.innerHTML = '<div class="alert alert-warning" role="alert">Please select an image first.</div>';
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('/classify', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                result.innerHTML = `<div class="alert alert-danger" role="alert">Error: ${data.error}</div>`;
            } else {
                result.innerHTML = `
                    <div class="alert alert-success" role="alert">
                        Prediction: ${data.prediction}<br>
                        Confidence: ${(data.confidence * 100).toFixed(2)}%
                    </div>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            result.innerHTML = '<div class="alert alert-danger" role="alert">An error occurred during classification.</div>';
        });
    });
});