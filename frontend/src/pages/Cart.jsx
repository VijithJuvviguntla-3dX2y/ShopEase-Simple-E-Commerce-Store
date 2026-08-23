import { Link } from "react-router-dom";
import CartItem from "../components/CartItem";
import { useCart } from "../context/CartContext";

function Cart() {
  const {
    cartItems,
    cartTotal,
    clearCart,
  } = useCart();

  if (cartItems.length === 0) {
    return (
      <div className="empty-cart">

        <h1>Your Cart is Empty</h1>

        <p>
          Add some products to your cart to continue shopping.
        </p>

        <Link to="/" className="shop-btn">
          Continue Shopping
        </Link>

      </div>
    );
  }

  return (
    <div className="cart-page">

      <h1>Shopping Cart</h1>

      <div className="cart-layout">

        <div className="cart-items">

          {cartItems.map((item) => (
            <CartItem
              key={item.id}
              item={item}
            />
          ))}

          <button
            className="clear-cart-btn"
            onClick={clearCart}
          >
            Clear Cart
          </button>

        </div>

        <div className="cart-summary">

          <h2>Order Summary</h2>

          <div className="summary-row">
            <span>Items</span>
            <span>{cartItems.length}</span>
          </div>

          <div className="summary-row">
            <span>Subtotal</span>
            <span>
              ₹{cartTotal.toLocaleString("en-IN")}
            </span>
          </div>

          <div className="summary-row">
            <span>Shipping</span>
            <span>Free</span>
          </div>

          <hr />

          <div className="summary-total">
            <span>Total</span>
            <span>
              ₹{cartTotal.toLocaleString("en-IN")}
            </span>
          </div>

          <Link
            to="/checkout"
            className="checkout-btn"
          >
            Proceed to Checkout
          </Link>

        </div>

      </div>

    </div>
  );
}

export default Cart;