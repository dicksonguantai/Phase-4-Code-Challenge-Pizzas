import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PizzasList = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    const fetchPizzas = async () => {
      try {
        const response = await axios.get('https://pizza-serve.onrender.com/pizzas');
        setPizzas(response.data);
      } catch (error) {
        console.error('Error fetching pizzas:', error);
      }
    };

    fetchPizzas();
  }, []);

  return (
    <div>
      <h2>Available Pizzas</h2>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            {pizza.name} - Ingredients: {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PizzasList;
