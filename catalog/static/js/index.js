function cart() {
    var form_data = "helloworld";
    console.log(form_data)
    $.ajax({
        url: "{% url 'cart' %}",
        type: "POST",
        data: form_data,
        cache: false
    }).done(function(data) {
        if (data.result === true) {
            alert(data.message);

        }
    });

}

document.getElementById("buy_now").addEventListener("click", cart)