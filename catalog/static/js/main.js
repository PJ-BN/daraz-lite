function cart() {
    fetch(myViewUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include CSRF token for security
            },
            body: JSON.stringify({
                // Add any data you want to send in the request body
                key1: name,
                key2: price,
                key3: image12,
                key4: quantity,
                key5: description,
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

document.getElementById("buy_now").addEventListener("click", cart)