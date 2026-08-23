import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../services/api";

function Login() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: "",
    password: "",
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
        "auth/login/",
        {
          username: formData.username,
          password: formData.password,
        }
      );

      localStorage.setItem(
        "access_token",
        response.data.access
      );

      localStorage.setItem(
        "refresh_token",
        response.data.refresh
      );

      alert("Login successful!");

      navigate("/");

    } catch (error) {

      console.error(error);

      alert(
        "Invalid username or password."
      );
    }
  };

  return (
    <div className="auth-page">

      <div className="auth-card">

        <h1>Login</h1>

        <p>
          Login to your ShopEase account
        </p>

        <form onSubmit={handleSubmit}>

          <label>Username</label>

          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Enter username"
            required
          />

          <label>Password</label>

          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Enter password"
            required
          />

          <button type="submit">
            Login
          </button>

        </form>

        <p>
          Don't have an account?{" "}
          <Link to="/register">
            Register
          </Link>
        </p>

      </div>

    </div>
  );
}

export default Login;