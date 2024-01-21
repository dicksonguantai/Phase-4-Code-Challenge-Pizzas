import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RestaurantList from './components/RestaurantList';
import RestaurantPizzaForm from './components/RestaurantPizzaForm';
import RestaurantDelete from './components/RestaurantDelete';
import PizzasList from './components/PizzasList';
import RestaurantDetail from './components/RestaurantDetail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/pizzas" element={<PizzasList />} />
        <Route path="/restaurants" element={<RestaurantList />} />
        <Route path="/restaurant_pizzas" element={<RestaurantPizzaForm />} />
        <Route path="/restaurants/:id" element={<RestaurantDetail />} />
        <Route path="/restaurants/:id/delete" element={<RestaurantDelete />} />
      </Routes>
    </Router>
  );
}

export default App;
