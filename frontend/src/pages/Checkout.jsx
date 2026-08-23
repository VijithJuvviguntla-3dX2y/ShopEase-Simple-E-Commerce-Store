import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useCart } from "../context/CartContext";
import API from "../services/api";

function Checkout() {
  const navigate = useNavigate();

  const {
    cartItems,
    cartTotal,
    clearCart,
  } = useCart();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
    city: "",
    state: "",
    pincode: "",
  });

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {

    event.preventDefault();

    try {

      const response = await API.post(
        "orders/create/",
        {
          customer: formData,
          items: cartItems,
        }
      );

      console.log(
        "Order created:",
        response.data
      );

      clearCart();

      alert(
        "Order placed successfully!"
      );

      navigate("/orders");

    } catch (error) {

      console.error(error);

      if (
        error.response?.status === 401
      ) {

        alert(
          "Please login before placing an order."
        );

        navigate("/login");

        return;
      }

      alert(
        error.response?.data?.error ||
        "Unable to place order."
      );
    }
  };

  if (cartItems.length === 0) {
    return (
      <div className="empty-cart">
        <h2>Your cart is empty.</h2>
      </div>
    );
  }

  return (
    <div className="checkout-page">

      <h1>Checkout</h1>

      <div className="checkout-layout">

        <form
          className="checkout-form"
          onSubmit={handleSubmit}
        >

          <h2>Shipping Information</h2>

          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={formData.name}
            onChange={handleChange}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <input
            type="tel"
            name="phone"
            placeholder="Phone Number"
            value={formData.phone}
            onChange={handleChange}
            required
          />

          <textarea
            name="address"
            placeholder="Address"
            value={formData.address}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="city"
            placeholder="City"
            value={formData.city}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="state"
            placeholder="State"
            value={formData.state}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="pincode"
            placeholder="PIN Code"
            value={formData.pincode}
            onChange={handleChange}
            required
          />

          <button type="submit">
            Place Order
          </button>

        </form>

        <div className="checkout-summary">

          <h2>Order Summary</h2>

          {cartItems.map((item) => (
            <div
              className="summary-row"
              key={item.id}
            >
              <span>
                {item.name} × {item.quantity}
              </span>

              <span>
                ₹{(
                  item.price * item.quantity
                ).toLocaleString("en-IN")}
              </span>
            </div>
          ))}

          <hr />

          <div className="summary-total">
            <span>Total</span>

            <span>
              ₹{cartTotal.toLocaleString("en-IN")}
            </span>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Checkout;