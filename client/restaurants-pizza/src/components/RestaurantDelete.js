import React from 'react';
import axios from 'axios';

const RestaurantDelete = ({ restaurantId, onDelete }) => {
  const handleDelete = async () => {
    try {
      await axios.delete(`/restaurants/${restaurantId}`);
      onDelete();
    } catch (error) {
      console.error('Error deleting restaurant:', error);
    }
  };

  return (
    <div>
      <h2>Delete Restaurant</h2>
      <button onClick={handleDelete}>Delete Restaurant</button>
    </div>
  );
};

export default RestaurantDelete;
