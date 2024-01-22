import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await axios.get('https://pizza-serve.onrender.com/restaurants');
        setRestaurants(response.data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    };

    fetchRestaurants();
  }, []);

  return (
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            {restaurant.name} - {restaurant.address}{' '}
            <Link to={`/restaurants/${restaurant.id}`}>Details</Link>{' '}
            <Link to={`/restaurant/${restaurant.id}/delete`}>Delete</Link>
          </li>
        ))}
      </ul>
            <Link to="/restaurants_pizzas">Restaurant Pizzas</Link>{' '}<br></br>
            <Link to="/pizzas">Pizzas</Link>{' '}<br></br>
            <Link to="/restaurant_pizzas">Adding Pizzas to A Restaurant</Link>{' '}
            
    </div>
  );
};

export default RestaurantList;
