import logo from "./logo.svg";
import "./App.css";
import "./components/css/common.css";
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Register from "./components/Register";
import FoodPost from "./components/FoodPost/FoodPost";
import FoodFeed from "./components/FoodFeed";
import NotFoundPage from "./components/NotFoundPage";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Login from "./components/Login";
function App() {
  return (
    <div className="App">
      <Navbar />
      <Router>
        <div>
          {/* <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
              <Link className="navbar-brand" to="/">
                🍽️ Food Share
              </Link>
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/">
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/register">
                    Register
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/login">
                    Login
                  </Link>
                </li>
              </ul>
            </div>
          </nav> */}

          {/* Define Routes */}
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/register" element={<Register />} />
            <Route path="/food-post" element={<FoodPost />} />
            <Route path="/food-feed" element={<FoodFeed />} />
            <Route path="/login-page" element={<Login />} />
            <Route path="/admin" element={<Login />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
