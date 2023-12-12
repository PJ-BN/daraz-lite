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

document.getElementById("quantity_adde").addEventListener("click", function() {
    quantityChange(1)
})
document.getElementById("quantity_subt").addEventListener("click", function() {
    quantityChange(0)
})

console.log(page_checkbox)
console.log(product_checkbox)


let ab = []
let cd = []

for (let i = 0; i < page_checkbox.length; i++) {

    ab.push(document.getElementById(page_checkbox[i]))
    ab[i].addEventListener('change', function() {
        cd.push(document.getElementById(product_checkbox[i]))
        if (ab[i].checked) {
            console.log("done");
            cd[i].checked = true

        } else {
            cd[i].checked = false

        }
    })
}