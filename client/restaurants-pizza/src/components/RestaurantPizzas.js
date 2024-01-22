import React, { useState, useEffect } from 'react';

const RestaurantPizzas = () => {
  const [restaurantPizzas, setRestaurantPizzas] = useState([]);

  useEffect(() => {
    const fetchRestaurantPizzas = async () => {
      try {
        const response = await fetch('/restaurant_pizzas');
        const data = await response.json();
        setRestaurantPizzas(data);
        console.log(restaurantPizzas)
      } catch (error) {
        console.error('Error fetching restaurant pizzas:', error);
      }
    };

    fetchRestaurantPizzas();
  }, [restaurantPizzas]);

    return (
    <div>
      <h2>Restaurant Pizzas with Prices</h2>
      <ul>
        {restaurantPizzas.map((restaurantPizza) => (
          <li key={restaurantPizza.id}>
            <strong>ID:</strong> {restaurantPizza.id}, 
            <strong> Price:</strong> ${restaurantPizza.price}
            <strong> Restaurant:</strong> ${restaurantPizza.restaurant_id}
            <strong> Pizza:</strong> ${restaurantPizza.pizza_id}


          </li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantPizzas;
