// src/components/SignupForm.js
import React, { useState } from 'react';
import './Signup.css'; // Archivo CSS para estilos personalizados

const SignupForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    password1: '',
    password2: '',
  });
  
  const [error, setError] = useState('');
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password1 !== formData.password2) {
      setError('Las contraseñas no coinciden');
      return;
    }
    
    // Aquí iría la lógica para enviar los datos al backend
    // const response = await fetch('/signup/', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(formData),
    // });
    // const result = await response.json();
    // console.log(result);
  };
  
  return (
    <div className="signup-container">
      <div className="signup-card">
        <h1 className="signup-title">Regístrate</h1>
        {error && <p className="error-message">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Nombre de usuaria:</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              placeholder="Escribe tu usuario"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password1">Contraseña:</label>
            <input
              type="password"
              id="password1"
              name="password1"
              value={formData.password1}
              onChange={handleChange}
              placeholder="Escribe tu contraseña"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password2">Confirma tu contraseña:</label>
            <input
              type="password"
              id="password2"
              name="password2"
              value={formData.password2}
              onChange={handleChange}
              placeholder="Confirma tu contraseña"
              required
            />
          </div>
          <button type="submit" className="btn btn-primary">Registrarse</button>
        </form>
      </div>
    </div>
  );
};

export default SignupForm;

