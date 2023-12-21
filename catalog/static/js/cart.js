function main() {
    summary()
    checkkbox()
    quantities()
    document.getElementById("proceed").addEventListener("click", function() {
        p = document.getElementById("total").textContent
        buy(parseInt(p))
    })


}

main()

function buy(prices) {
    fetch("buy", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // Include CSRF token for security
        },
        body: JSON.stringify({
            // Add any data you want to send in the request body

            key1: prices,


            // ...
        })
    })


    console.log(prices)
    window.location.href = "/buy"


}

function quantityChange(check, id, i) {
    var data = document.getElementById("quantity_" + id[i]);
    x = parseInt(data.textContent)

    if (x > 0) {

        if (check == 1) {
            x += 1

        }

    }
    if (x > 1) {

        if (check == 0) {
            x -= 1

        }
    }
    data.textContent = x
    updateQuantity(x, id[i])
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
            var val = true
        } else if (!pg.checked) {
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



function quantities() {

    for (let i = 0; i < id.length; i++) {
        document.getElementById("quantity_add_" + id[i]).addEventListener("click", function() {
            quantityChange(1, id, i)
        })
        document.getElementById("quantity_sub_" + id[i]).addEventListener("click", function() {
            quantityChange(0, id, i)
        })

    }
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
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(updatedData)
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                console.error('Update failed:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));

}


function summary() {



    abc = []
    for (i = 0; i < id.length; i++) {
        abc.push(document.getElementById(checkboxx + id[i]))
        checkSummaryCheckbox(abc[i], i)
        deleteListnear(i)


    }


}

function checkSummaryCheckbox(a, i) {

    subtotal = document.getElementById("subtotal")
    total = document.getElementById("total")
    a.addEventListener("change", function() {


        if (a.checked) {

            subtotal_price = getSummaryValue(i)
            subtotal_value.push(subtotal_price)

        } else if (!a.checked) {
            subtotal_price = getSummaryValue(i)

            subtotal_value = subtotal_value.filter(item => item !== subtotal_price);
        }
        let sum = subtotal_value.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
        subtotal.textContent = sum
        total.textContent = sum

    })


}

function getSummaryValue(i) {
    let pp = parseInt(document.getElementById(price + id[i]).textContent)
    let qq = parseInt(document.getElementById(quant + id[i]).textContent)

    let subtotal_values = pp * qq
    return subtotal_values
}

function deleteData(id) {
    var deletedData = {
        id: id
    };

    fetch('/api/delete_data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(deletedData)
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                console.error('Update failed:', data.error);
            }
        })
        .catch(error => console.error('Error:', error));

}

function deleteListnear(i) {
    del.push(document.getElementById("del_" + id[i]))


    del[i].addEventListener('click', function() {
        deleteData(id[i])
    })
}