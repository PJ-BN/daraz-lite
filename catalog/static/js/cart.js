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

document.getElementById("quantity_adde").addEventListener("click", function() {
    quantityChange(1)
})
document.getElementById("quantity_subt").addEventListener("click", function() {
    quantityChange(0)
})

checkkbox()