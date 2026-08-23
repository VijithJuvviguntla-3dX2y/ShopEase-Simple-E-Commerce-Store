import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

function Navbar() {
  const { cartCount } = useCart();

  return (
    <nav className="navbar">
      <div className="nav-container">

        <Link to="/" className="logo">
          ShopEase
        </Link>

        <div className="nav-links">
          <Link to="/">Home</Link>

          <Link to="/cart">
            Cart
            <span className="cart-badge">
              {cartCount}
            </span>
          </Link>

          <Link to="/orders">
            Orders
          </Link>

          <Link to="/login">
            Login
          </Link>

          <Link to="/register" className="register-btn">
            Register
          </Link>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;