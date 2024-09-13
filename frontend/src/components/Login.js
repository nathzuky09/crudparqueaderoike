import React, { useState } from 'react'; // Importa React y useState para el manejo del estado
import Home from './components/Home'; // Asegúrate de que esta ruta sea correcta

const Login = () => {
  // Define el estado local para almacenar los valores de nombre de usuario y contraseña
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // Maneja el envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario
    // Aquí puedes añadir la lógica para manejar el inicio de sesión, como enviar datos a un servidor
    console.log('Username:', username); // Muestra el nombre de usuario en la consola
    console.log('Password:', password); // Muestra la contraseña en la consola
  };

  return (
    <div className="container mt-5">
      <h1>Iniciar Sesión</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">Nombre de usuario</label>
          <input
            type="text"
            className="form-control"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)} // Actualiza el estado cuando el usuario cambia el valor
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Contraseña</label>
          <input
            type="password"
            className="form-control"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)} // Actualiza el estado cuando el usuario cambia el valor
          />
        </div>
        <button type="submit" className="btn btn-primary">Iniciar Sesión</button>
      </form>
    </div>
  );
};

export default Login;


