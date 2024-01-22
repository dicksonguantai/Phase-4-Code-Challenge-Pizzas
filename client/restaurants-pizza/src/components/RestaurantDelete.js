import React from 'react';
import axios from 'axios';
import { useParams,useNavigate} from 'react-router-dom';


const RestaurantDelete = ({ restaurantId, onDelete }) => {
  const navigate = useNavigate();
  const{id} = useParams()
  const handleDelete = async () => {
    try {
      await axios.delete(`https://pizza-serve.onrender.com/restaurants/${id}`);
      alert('Restaurant deleted')
      navigate('/restaurants')
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
