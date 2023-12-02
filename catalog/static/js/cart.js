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