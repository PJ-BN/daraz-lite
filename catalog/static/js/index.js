function cart() {
    fetch('{% url "home" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}' // Include CSRF token for security
            },
            body: JSON.stringify({
                // Add any data you want to send in the request body
                key1: 'value1',
                key2: 'value2',
                // ...
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Handle the response as needed
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}

// document.getElementById("buy_now").addEventListener("click", cart)