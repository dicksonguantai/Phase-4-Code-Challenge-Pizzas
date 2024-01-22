import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';

const RestaurantDetail = () => {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    const fetchRestaurantDetails = async () => {
      try {
        const response = await fetch(`/restaurants/${id}`);
        const data = await response.json();
        setRestaurant(data);
      } catch (error) {
        console.error('Error fetching restaurant details:', error);
      }
    };

    fetchRestaurantDetails();
  }, [id]);

  return (
    <div>
      {restaurant && (
        <div>
          <h2>{restaurant.name}</h2>
          <p>{restaurant.address}</p>
          <h3>Pizzas</h3>
          {restaurant.pizzas && restaurant.pizzas.length > 0 ? (
            <ul>
              {restaurant.pizzas.map((pizza) => (
                <li key={pizza.id}>
                  <strong>{pizza.name}</strong> - {pizza.ingredients}
                </li>
              ))}
            </ul>
          ) : (
            <p>No pizzas available</p>
          )}
        </div>
      )}
      <Link to="/restaurants">Back to Restaurants</Link>
    </div>
  );
};

export default RestaurantDetail;
