// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import './Signup.css'
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';

// Asegúrate de que el contenedor con id 'root' está presente en tu archivo HTML
const root = ReactDOM.createRoot(document.getElementById('react-root'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Si quieres medir el rendimiento de tu app, puedes pasar una función
// para registrar los resultados (por ejemplo: reportWebVitals(console.log))
reportWebVitals();

