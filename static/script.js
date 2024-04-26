document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('prediction-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('result').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
