import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const Tasks = () => {
    const [funcionarios, setFuncionarios] = useState([]);
    const [vehiculos, setVehiculos] = useState([]);

    useEffect(() => {
        // Fetch funcionarios and vehiculos from the API
        const fetchData = async () => {
            try {
                const [funcionarioResponse, vehiculoResponse] = await Promise.all([
                    axios.get('/api/funcionarios/'),
                    axios.get('/api/vehiculos/')
                ]);
                setFuncionarios(funcionarioResponse.data);
                setVehiculos(vehiculoResponse.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    return (
        <main className="container mt-5">
            {/* Lista de Funcionarios */}
            <div className="mb-5">
                <h1 className="text-center mb-4">Lista de Funcionarios</h1>
                <div className="card">
                    <ul className="list-group list-group-flush">
                        {funcionarios.length > 0 ? (
                            funcionarios.map(funcionario => (
                                <li className="list-group-item" key={funcionario.id}>
                                    <Link to={`/update_funcionario/${funcionario.id}`} className="text-decoration-none">
                                        {funcionario.nombre}
                                    </Link>
                                </li>
                            ))
                        ) : (
                            <li className="list-group-item">No hay funcionarios registrados.</li>
                        )}
                    </ul>
                </div>
            </div>

            {/* Lista de Vehículos */}
            <div className="mb-5">
                <h1 className="text-center mb-4">Lista de Vehículos</h1>
                <div className="card">
                    <ul className="list-group list-group-flush">
                        {vehiculos.length > 0 ? (
                            vehiculos.map(vehiculo => (
                                <li className="list-group-item" key={vehiculo.id}>
                                    <div className="d-flex flex-column">
                                        <strong>Placa:</strong> {vehiculo.placa}<br />
                                        <strong>Color:</strong> {vehiculo.color}<br />
                                        <strong>Modelo:</strong> {vehiculo.modelo}<br />
                                        <strong>Tipo de Vehículo:</strong> {vehiculo.tipoVehiculo}<br />
                                        {vehiculo.funcionario ? (
                                            <>
                                                <strong>Propietario:</strong> {vehiculo.funcionario.nombre} {vehiculo.funcionario.apellido}<br />
                                            </>
                                        ) : (
                                            <strong>Propietario:</strong> Sin propietario<br />
                                        )
                                        <strong>Hora de Entrada:</strong> {new Date(vehiculo.hora_entrada).toLocaleTimeString()}<br />
                                        <strong>Hora de Salida:</strong> {vehiculo.hora_salida ? new Date(vehiculo.hora_salida).toLocaleTimeString() : 'Sin salida'}<br />
                                    </div>
                                </li>
                            ))
                        ) : (
                            <li className="list-group-item">No hay vehículos registrados.</li>
                        )}
                    </ul>
                </div>
            </div>

            {/* Botón para crear una nueva tarea */}
            <div className="text-center mt-4">
                <Link to="/create_task" className="btn btn-primary">Crear Nueva Tarea</Link>
            </div>
        </main>
    );
};

export default Tasks;
