import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

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

  if (!restaurant) {
    return <div>Loading...</div>;
  }
  console.log(restaurant)
const name_restaurant = restaurant[0]['name'];
const address_restaurant = restaurant[0]['address'];
const pizzas = restaurant[0]['pizzas'];

  return (
    <div>
      <h2>{name_restaurant}</h2>
      <p>{address_restaurant}</p>

      {/* <h3>Pizzas:</h3>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong> - {pizza.ingredients}
          </li>
        ))}
      </ul> */}
    </div>
  );
};

export default RestaurantDetail;
