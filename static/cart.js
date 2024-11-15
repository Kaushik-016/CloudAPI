const cartItems = document.getElementById('cart-items');

// Mock cart items for demonstration
const cart = [
  { id: 1, name: "Apple", price: 1.2, quantity: 3 },
  { id: 2, name: "Banana", price: 0.5, quantity: 5 }
];

cart.forEach(item => {
  const itemDiv = document.createElement('div');
  itemDiv.classList.add('cart-item');
  itemDiv.innerHTML = `
    <p>${item.name} - $${item.price} x ${item.quantity}</p>
  `;
  cartItems.appendChild(itemDiv);
});

function checkout() {
  window.location.href = 'checkout.html';
}