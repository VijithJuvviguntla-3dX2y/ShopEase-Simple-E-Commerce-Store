import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import API from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });

    setError("");
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");

    // Check passwords
    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    // Check password length
    if (formData.password.length < 6) {
      setError("Password must contain at least 6 characters.");
      return;
    }

    setLoading(true);

    try {
      const response = await API.post("auth/register/", {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      });

      console.log("Registration response:", response.data);

      alert("Registration successful!");

      navigate("/login");

    } catch (error) {
      console.error("Registration error:", error);

      // Server responded with an error
      if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);

        const data = error.response.data;

        if (data.username) {
          setError(
            `Username: ${data.username.join(", ")}`
          );
        } else if (data.email) {
          setError(
            `Email: ${data.email.join(", ")}`
          );
        } else if (data.password) {
          setError(
            `Password: ${data.password.join(", ")}`
          );
        } else if (data.error) {
          setError(data.error);
        } else if (data.detail) {
          setError(data.detail);
        } else {
          setError(
            `Registration failed. Server returned status ${error.response.status}.`
          );
        }

      // Request was sent but no response received
      } else if (error.request) {
        setError(
          "Could not connect to the Django server. Make sure Django is running on port 8000."
        );

      // Something else went wrong
      } else {
        setError(
          `Registration failed: ${error.message}`
        );
      }

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page">

      <div className="auth-card">

        <h1>Create Account</h1>

        <p>
          Register for your ShopEase account
        </p>

        {error && (
          <div
            style={{
              background: "#fee2e2",
              color: "#b91c1c",
              padding: "12px",
              borderRadius: "6px",
              marginTop: "15px",
              marginBottom: "10px",
              fontSize: "14px",
            }}
          >
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>

          <label>
            Username
          </label>

          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Enter username"
            required
          />

          <label>
            Email
          </label>

          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter email"
            required
          />

          <label>
            Password
          </label>

          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Enter password"
            required
          />

          <label>
            Confirm Password
          </label>

          <input
            type="password"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            placeholder="Confirm password"
            required
          />

          <button
            type="submit"
            disabled={loading}
          >
            {loading
              ? "Creating Account..."
              : "Register"}
          </button>

        </form>

        <p>
          Already have an account?{" "}
          <Link to="/login">
            Login
          </Link>
        </p>

      </div>

    </div>
  );
}

export default Register;