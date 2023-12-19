function cart() {
    console.log(quantity)

    alert(" Added to the cart")

    fetch(myViewUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include CSRF token for security
            },
            body: JSON.stringify({
                // Add any data you want to send in the request body

                key1: quantity,
                key2: data,


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

function quantityChange(check) {
    var x = document.getElementById("quantity");

    if (quantity > 0) {

        if (check == 1) {
            quantity += 1
        }

    }
    if (quantity > 1) {

        if (check == 0) {
            quantity -= 1
        }
    }

    x.textContent = quantity
}

document.getElementById("add_to_cart").addEventListener("click", cart)

document.getElementById("quantity_add").addEventListener("click", function() {
    quantityChange(1)
})
document.getElementById("quantity_sub").addEventListener("click", function() {
    quantityChange(0)
})

document.getElementById("buy_now").addEventListener("click", function() {
    alert("order successfull")
})