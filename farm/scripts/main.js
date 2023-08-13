// JavaScript code for adding items to the cart
var cart = [];

function addToCart(item) {
    cart.push(item);
    alert(item + " added to cart!");
}

function viewCart() {
    var items = cart.join(", ");
    alert("Items in cart: " + items);
}
