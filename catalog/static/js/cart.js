function main() {
    checkkbox()
    quantities()

}

main()

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

subtotal = document.getElementById("subtotal")
total = document.getElementById("total")


abc = []
for (i = 0; i < id.length; i++) {
    abc.push(document.getElementById(checkboxx + id[i]))
    aabb(abc[i], i)


}
console.log(abc)

function aabb(a, i) {

    pp = parseInt(document.getElementById(price + id[i]).textContent)
    qq = parseInt(document.getElementById(quant + id[i]).textContent)
    sb = parseInt(subtotal.textContent)
    console.log(pp, qq, sb)
    a.addEventListener("change", function() {

        if (a.checked) {
            subtotal_value = pp * qq
            console.log(subtotal_value)
            subtotal.textContent = subtotal_value
        } else {
            console.log(i + " is not checked")
        }
    })

}

console.log(id)