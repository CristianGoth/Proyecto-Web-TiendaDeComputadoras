let cartItems = [];

function addToCart(productName, price, imageSrc) {
  const existingItem = cartItems.find(item => item.name === productName);

  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    const item = {
      name: productName,
      price: price,
      imageSrc: imageSrc,
      quantity: 1
    };
    cartItems.push(item);
  }

  localStorage.setItem('cartItems', JSON.stringify(cartItems));
  updateCart();
}

function removeCartItem(index) {
  cartItems.splice(index, 1);
  localStorage.setItem('cartItems', JSON.stringify(cartItems));
  updateCart();
}

function increaseQuantity(index) {
  cartItems[index].quantity += 1;
  localStorage.setItem('cartItems', JSON.stringify(cartItems));
  updateCart();
}

function decreaseQuantity(index) {
  if (cartItems[index].quantity > 1) {
    cartItems[index].quantity -= 1;
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    updateCart();
  }
}

function updateCart() {
  const cartList = document.getElementById('cart-list');
  cartList.innerHTML = '';

  let totalPrice = 0;

  cartItems.forEach((item, index) => {
    const li = document.createElement('li');
    li.classList.add('product-item');

    const image = document.createElement('img');
    image.src = item.imageSrc;
    li.appendChild(image);

    const name = document.createElement('span');
    name.innerText = item.name;
    li.appendChild(name);

    const price = document.createElement('span');
    price.innerText = `$${item.price.toFixed(2)}`;
    li.appendChild(price);

    const quantity = document.createElement('span');
    quantity.innerText = `Cantidad: ${item.quantity}`;
    li.appendChild(quantity);

    const increaseBtn = document.createElement('button');
    increaseBtn.innerText = '+';
    increaseBtn.addEventListener('click', () => {
      increaseQuantity(index);
    });
    li.appendChild(increaseBtn);

    const decreaseBtn = document.createElement('button');
    decreaseBtn.innerText = '-';
    decreaseBtn.addEventListener('click', () => {
      decreaseQuantity(index);
    });
    li.appendChild(decreaseBtn);

    const removeBtn = document.createElement('button');
    removeBtn.innerText = 'Eliminar';
    removeBtn.addEventListener('click', () => {
      removeCartItem(index);
    });
    li.appendChild(removeBtn);

    cartList.appendChild(li);
    totalPrice += item.price * item.quantity;
  });

  const cartTotal = document.getElementById('cart-total');
  cartTotal.innerText = `$${totalPrice.toFixed(2)}`;
}

function checkout() {
  alert('Gracias por tu compra!');
  cartItems = [];
  localStorage.removeItem('cartItems');
  updateCart();
}

function clearCart() {
  cartItems = [];
  localStorage.removeItem('cartItems');
  updateCart();
}

window.addEventListener('DOMContentLoaded', () => {
  const addToCartButtons = document.querySelectorAll('.add-to-cart');
  addToCartButtons.forEach(button => {
    button.addEventListener('click', () => {
      const productName = button.getAttribute('data-name');
      const price = parseFloat(button.getAttribute('data-price'));
      const imageSrc = button.getAttribute('data-image');
      addToCart(productName, price, imageSrc);
      updateCart();
    });
  });

  const storedCartItems = JSON.parse(localStorage.getItem('cartItems'));
  if (storedCartItems && storedCartItems.length > 0) {
    cartItems = storedCartItems;
    updateCart();
  }

  if (window.location.pathname.includes('carrito.html')) {
    const checkoutBtn = document.getElementById('checkout-btn');
    checkoutBtn.addEventListener('click', checkout);

    const clearBtn = document.getElementById('clear-btn');
    clearBtn.addEventListener('click', clearCart);
  }
});
