import React, { useState } from "react";
import axios from "axios";

const FoodPost = () => {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    quantity: "",
    expiration_date: "",
    whatsapp_link: "",
    collection_point: "",
    photo: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleFileChange = (e) => {
    setFormData({
      ...formData,
      photo: e.target.files[0],
    });
  };

  const submitFoodPost = async () => {
    const csrfToken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    )?.value;

    const data = new FormData();
    data.append("title", formData.title);
    data.append("description", formData.description);
    data.append("quantity", formData.quantity);

    if (formData.expiration_date) {
      data.append("expiration_date", formData.expiration_date);
    } else {
      alert("Please select an expiration date.");
      return;
    }

    data.append("whatsapp_link", formData.whatsapp_link);
    data.append("collection_point", formData.collection_point);
    if (formData.photo) {
      data.append("photo", formData.photo);
    }

    try {
      const response = await axios.post("/post_food/", data, {
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "multipart/form-data",
        },
      });
      alert("Food post created successfully!");
      setFormData({
        title: "",
        description: "",
        quantity: "",
        expiration_date: "",
        whatsapp_link: "",
        collection_point: "",
        photo: null,
      });
    } catch (error) {
      console.error("Error creating food post:", error);
      alert("Failed to create food post. Please try again.");
    }
  };

  return (
    <div>
      <h1>Post Food</h1>
      <form>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={formData.title}
          onChange={handleChange}
          required
        />
        <br />
        <textarea
          name="description"
          placeholder="Description"
          value={formData.description}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="number"
          name="quantity"
          placeholder="Quantity"
          value={formData.quantity}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="datetime-local"
          name="expiration_date"
          value={formData.expiration_date}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="text"
          name="whatsapp_link"
          placeholder="WhatsApp Link"
          value={formData.whatsapp_link}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="text"
          name="collection_point"
          placeholder="Collection Point"
          value={formData.collection_point}
          onChange={handleChange}
          required
        />
        <br />
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <br />
        <button type="button" onClick={submitFoodPost}>
          Submit Post
        </button>
      </form>
    </div>
  );
};

export default FoodPost;
