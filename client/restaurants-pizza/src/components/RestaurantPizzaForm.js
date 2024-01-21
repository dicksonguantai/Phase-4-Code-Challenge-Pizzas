import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RestaurantPizzaForm = ({ onSuccess }) => {
  const [price, setPrice] = useState('');
  const [restaurantId, setRestaurantId] = useState('');
  const [pizzaId, setPizzaId] = useState('');
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await axios.get('/restaurants');
        setRestaurants(response.data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    };

    const fetchPizzas = async () => {
      try {
        const response = await axios.get('/pizzas');
        setPizzas(response.data);
      } catch (error) {
        console.error('Error fetching pizzas:', error);
      }
    };

    fetchRestaurants();
    fetchPizzas();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post('http://your-flask-api-url/restaurant_pizzas', {
        price,
        restaurant_id: restaurantId,
        pizza_id: pizzaId,
      });
      setPrice('');
      setRestaurantId('');
      setPizzaId('');
      onSuccess();
    } catch (error) {
      console.error('Error creating restaurant pizza:', error);
    }
  };

  return (
    <div>
      <h2>Add Restaurant Pizza</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Price:
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>
        <br />
        <label>
          Restaurant:
          <select value={restaurantId} onChange={(e) => setRestaurantId(e.target.value)}>
            <option value="">Select a restaurant</option>
            {restaurants.map((restaurant) => (
              <option key={restaurant.id} value={restaurant.id}>
                {restaurant.name}
              </option>
            ))}
          </select>
        </label>
        <br />
        <label>
          Pizza:
          <select value={pizzaId} onChange={(e) => setPizzaId(e.target.value)}>
            <option value="">Select a pizza</option>
            {pizzas.map((pizza) => (
              <option key={pizza.id} value={pizza.id}>
                {pizza.name}
              </option>
            ))}
          </select>
        </label>
        <br />
        <button type="submit">Add Restaurant Pizza</button>
      </form>
    </div>
  );
};

export default RestaurantPizzaForm;
