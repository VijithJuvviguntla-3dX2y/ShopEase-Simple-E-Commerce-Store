import { useEffect, useState } from "react";

import ProductCard from "../components/ProductCard";
import API from "../services/api";

function Home() {

  const [products, setProducts] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {

    const fetchProducts = async () => {

      try {

        const response = await API.get(
          "products/"
        );

        setProducts(response.data);

      } catch (error) {

        console.error(error);

        setError(
          "Unable to load products."
        );

      } finally {

        setLoading(false);

      }
    };

    fetchProducts();

  }, []);

  if (loading) {
    return (
      <div className="empty-cart">
        <h2>Loading products...</h2>
      </div>
    );
  }

  if (error) {
    return (
      <div className="empty-cart">
        <h2>{error}</h2>
      </div>
    );
  }

  return (
    <div className="home-page">

      <section className="hero">

        <div className="hero-content">

          <h1>
            Welcome to ShopEase
          </h1>

          <p>
            Discover quality products
            at affordable prices.
          </p>

          <button
            onClick={() =>
              document
                .getElementById("products")
                .scrollIntoView({
                  behavior: "smooth",
                })
            }
          >
            Shop Now
          </button>

        </div>

      </section>

      <section
        className="products-section"
        id="products"
      >

        <h2>Our Products</h2>

        <div className="products-grid">

          {products.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
            />
          ))}

        </div>

      </section>

    </div>
  );
}

export default Home;