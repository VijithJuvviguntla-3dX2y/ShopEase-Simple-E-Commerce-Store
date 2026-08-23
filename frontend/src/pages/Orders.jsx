import { useEffect, useState } from "react";

import API from "../services/api";

function Orders() {

  const [orders, setOrders] = useState([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const fetchOrders = async () => {

      try {

        const response = await API.get(
          "orders/"
        );

        setOrders(response.data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    };

    fetchOrders();

  }, []);

  if (loading) {

    return (
      <div className="empty-orders">
        <h2>
          Loading orders...
        </h2>
      </div>
    );
  }

  return (
    <div className="orders-page">

      <h1>
        My Orders
      </h1>

      {orders.length === 0 ? (

        <div className="empty-orders">

          <h2>
            No orders found.
          </h2>

          <p>
            Your orders will appear here.
          </p>

        </div>

      ) : (

        <div className="orders-list">

          {orders.map((order) => (

            <div
              className="order-card"
              key={order.id}
            >

              <div>

                <h3>
                  Order #{order.id}
                </h3>

                <p>
                  {new Date(
                    order.created_at
                  ).toLocaleDateString()}
                </p>

                <p>
                  {order.items.length} item(s)
                </p>

              </div>

              <div>

                <strong>
                  ₹{Number(
                    order.total_amount
                  ).toLocaleString("en-IN")}
                </strong>

                <p className="order-status">
                  {order.status}
                </p>

              </div>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default Orders;