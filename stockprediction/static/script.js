document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const stockSymbol = document.getElementById('symbol').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symbol: stockSymbol })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').innerText = `Predicted Price for next closing: $${data.prediction.toFixed(2)}`;
    })
    .catch(error => console.error('Error:', error));
});
