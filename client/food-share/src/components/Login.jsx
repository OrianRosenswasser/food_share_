import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;

      const response = await axios.post(
        "/login/",
        {
          email,
          password,
        },
        {
          headers: {
            "X-CSRFToken": csrfToken,
          },
        }
      );

      console.log("Login successful:", response);
      window.location.href = "/";
    } catch (err) {
      console.error("Login failed:", err.response?.data);
      setError(err.response?.data?.detail || "Login failed. Please try again.");
    }
  };

  return (
    <div className="form-container">
      <h1 className="emoji">🎉 Login</h1>
      <form onSubmit={handleLogin}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Email
          </label>
          <input
            type="email"
            id="email"
            className="form-control"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            id="password"
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        {error && <div className="alert alert-danger">{error}</div>}

        <button type="submit" className="btn btn-lg w-100">
          🎈 Log In
        </button>
      </form>

      <div className="text-center mt-3">
        <a href="/register">Don't have an account? Register here 👉</a>
      </div>

      <style>{`
        .form-container {
          max-width: 400px;
          margin: 50px auto;
          padding: 20px;
          background-color: #fff;
          border-radius: 8px;
          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        .form-label {
          font-weight: bold;
        }

        .btn {
          background-color: #4CAF50;
          color: white;
          padding: 10px;
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }

        .btn:hover {
          background-color: #45a049;
        }

        .emoji {
          text-align: center;
          margin-bottom: 20px;
        }

        a {
          color: #4CAF50;
          text-decoration: none;
        }

        a:hover {
          text-decoration: underline;
        }
      `}</style>
    </div>
  );
};

export default Login;
