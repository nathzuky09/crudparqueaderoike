// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home'; // Asegúrate de que Home.js está en el mismo directorio
import Signup from './components/Signup'; // Asegúrate de que Signup.js está en el mismo directorio
import Login from './components/Login'; // Asegúrate de que Login.js está en el mismo directorio
import CrearFuncionarioVehiculo from './components/CrearFuncionarioVehiculo'; // Asegúrate de que CrearFuncionarioVehiculo.js está en el mismo directorio
import 'bootstrap/dist/css/bootstrap.min.css'; // Importa Bootstrap para estilos

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/signup" element={<Signup />} />
                <Route path="/" element={<Home />} />
                <Route path="/inicio_sesion" element={<Login />} />
                <Route path="/crear-funcionario-vehiculo" element={<CrearFuncionarioVehiculo />} />
                <Route path="/crear-tarea" element={<CreateTask />} /> {/* Ruta para CreateTask */}
                {/* Agrega otras rutas según sea necesario */}
            </Routes>
        </Router>
    );
}

export default App;