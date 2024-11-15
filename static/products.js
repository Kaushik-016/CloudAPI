const productList = document.getElementById('product-list');

const products = [
  { id: 1, name: "Apple", price: 1.2 },
  { id: 2, name: "Banana", price: 0.5 },
  { id: 3, name: "Carrot", price: 0.3 }
];

products.forEach(product => {
  const productDiv = document.createElement('div');
  productDiv.classList.add('product-item');
  productDiv.innerHTML = `
    <h3>${product.name}</h3>
    <p>$${product.price}</p>
    <button onclick="addToCart(${product.id})">Add to Cart</button>
  `;
  productList.appendChild(productDiv);
});

function addToCart(productId) {
  alert(`Product ${productId} added to cart!`);
}