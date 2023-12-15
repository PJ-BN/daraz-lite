function main() {
    checkkbox()
    quantities()

}

main()

function quantityChange(check, names, i) {
    var data = document.getElementById("quantity_" + names[i]);
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
    updateQuantity(x, names[i])
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

    for (let i = 0; i < names.length; i++) {
        document.getElementById("quantity_add_" + names[i]).addEventListener("click", function() {
            quantityChange(1, names, i)
        })
        document.getElementById("quantity_sub_" + names[i]).addEventListener("click", function() {
            quantityChange(0, names, i)
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