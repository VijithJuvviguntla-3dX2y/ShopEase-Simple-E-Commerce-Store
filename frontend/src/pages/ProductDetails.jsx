import { useEffect, useState } from "react";

import {
  Link,
  useParams,
} from "react-router-dom";

import { useCart } from "../context/CartContext";

import API from "../services/api";

function ProductDetails() {

  const { id } = useParams();

  const { addToCart } = useCart();

  const [product, setProduct] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const fetchProduct = async () => {

      try {

        const response = await API.get(
          `products/${id}/`
        );

        setProduct(response.data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    };

    fetchProduct();

  }, [id]);

  if (loading) {

    return (
      <div className="empty-cart">
        <h2>Loading...</h2>
      </div>
    );
  }

  if (!product) {

    return (
      <div className="not-found">

        <h2>
          Product not found
        </h2>

        <Link to="/">
          Back to Home
        </Link>

      </div>
    );
  }

  return (
    <div className="product-details">

      <div className="product-details-image">

        <img
          src={
            product.image ||
            "https://placehold.co/600x500?text=No+Image"
          }
          alt={product.name}
        />

      </div>

      <div className="product-details-info">

        <p className="product-category">
          {product.category}
        </p>

        <h1>
          {product.name}
        </h1>

        <h2>
          ₹{Number(product.price).toLocaleString("en-IN")}
        </h2>

        <p>
          {product.description}
        </p>

        <p>
          Available stock: {product.stock}
        </p>

        <button
          className="add-cart-btn large"
          disabled={product.stock === 0}
          onClick={() =>
            addToCart(product)
          }
        >
          {product.stock > 0
            ? "Add to Cart"
            : "Out of Stock"}
        </button>

      </div>

    </div>
  );
}

export default ProductDetails;