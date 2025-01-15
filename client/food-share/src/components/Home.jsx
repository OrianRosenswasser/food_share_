import React from "react";

const Home = () => {
  return (
    <div style={{ textAlign: "center" }}>
      <h1>Welcome to Food Share!</h1>
      <p>
        🍽️ Join our community and connect with people through food sharing 🍽️
      </p>

      <div style={{ marginTop: "20px" }}>
        <video width="640" height="360" autoPlay loop muted>
          <source src="/static/videos/food_share.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
};

export default Home;
