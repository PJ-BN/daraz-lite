function quantityChange(check, names, i) {
    var data = document.getElementById("quantity_" + names[i]);
    x = parseInt(data.textContent)
    console.log(x)

    if (x > 0) {

        if (check == 1) {
            x += 1
                // console.log(names)
                // console.log(i)

        }

    }
    if (x > 1) {

        if (check == 0) {
            x -= 1
                // console.log("sub" + names)

        }
    }
    console.log(x)
    data.textContent = x
}

function checkkbox() {
    let ab = []
    let cd = []
    for (key in page) {
        aaa = document.getElementById("page_checkbox_" + key)
        cd.push(key)
        ab.push(aaa)
    }

    for (let i = 0; i < ab.length; i++) {
        cartvalue(ab[i], cd[i])
    }

}

function cartvalue(pg, key) {
    pg.addEventListener("change", function() {

        if (pg.checked) {
            console.log("done");
            var val = true
        } else if (!pg.checked) {
            console.log("false")
            var val = false
        }
        productcheckbox(key, val)
    })
}

function productcheckbox(key, val) {
    product = page[key]
    for (var pro in product) {
        aaaa = document.getElementById(product[pro])
        aaaa.checked = val
    }

}


checkkbox()
    // console.log(addd, subt)
console.log(names)
for (let i = 0; i < names.length; i++) {
    document.getElementById("quantity_add_" + names[i]).addEventListener("click", function() {
        quantityChange(1, names, i)
    })
    document.getElementById("quantity_sub_" + names[i]).addEventListener("click", function() {
        quantityChange(0, names, i)
    })

}


function updateQuantity(quantity, name) {

    var updatedData = {
        names: name,
        new_quantity: quantity
    };

    fetch('/api/update_data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie(csrftoken)
            },
            body: JSON.stringify(updatedData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Update successful');
            } else {
                console.error('Update failed:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));

    // Function to get CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

}