// src/components/CreateTask.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const CreateTask = () => {
    const [funcionarioForm, setFuncionarioForm] = useState([]);
    const [vehiculoForm, setVehiculoForm] = useState([]);

    useEffect(() => {
        axios.get('/create_task/')
            .then(response => {
                setFuncionarioForm(response.data.funcionario_form.fields);
                setVehiculoForm(response.data.vehiculo_form.fields);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleSubmit = (event) => {
        event.preventDefault();
        // Aquí agregarías la lógica para manejar el envío del formulario
        console.log('Form submitted');
    };

    return (
        <div className="container mt-5">
            <div className="card mx-auto" style={{ maxWidth: '700px' }}>
                <div className="card-body">
                    <h1 className="card-title text-center mb-4">Creación de Funcionario y Vehículo</h1>

                    <form onSubmit={handleSubmit}>
                        {/* Funcionario */}
                        <div className="mb-4">
                            <h2 className="h4">Funcionario</h2>
                            {funcionarioForm.map((field, index) => (
                                <div className="mb-3" key={index}>
                                    <label htmlFor={field.name} className="form-label">{field.label}</label>
                                    <input
                                        type={field.type}
                                        className="form-control"
                                        id={field.name}
                                        name={field.name}
                                    />
                                </div>
                            ))}
                        </div>

                        {/* Vehículo */}
                        <div className="mb-4">
                            <h2 className="h4">Vehículo</h2>
                            {vehiculoForm.map((field, index) => (
                                <div className="mb-3" key={index}>
                                    <label htmlFor={field.name} className="form-label">{field.label}</label>
                                    <input
                                        type={field.type}
                                        className="form-control"
                                        id={field.name}
                                        name={field.name}
                                    />
                                </div>
                            ))}
                        </div>

                        <div className="text-center">
                            <button type="submit" className="btn btn-primary btn-lg">Guardar</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default CreateTask;
