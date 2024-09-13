import React, { useState } from 'react';
import FuncionarioForm from './FuncionarioForm';
import VehiculoForm from './VehiculoForm';

function CrearFuncionarioVehiculo() {
    const [formData, setFormData] = useState({
        nombre: '',
        cargo: '',
        marca: '',
        modelo: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí puedes enviar formData al servidor
        console.log('Datos enviados:', formData);
    };

    return (
        <main className="container mt-5">
            <h1 className="text-center mb-4">Creación de Funcionario y Vehículo</h1>

            <form onSubmit={handleSubmit} className="card card-body mx-auto" style={{ maxWidth: '600px' }}>
                <div className="mb-4">
                    <h2 className="text-center">Funcionario</h2>
                    <FuncionarioForm formData={formData} handleChange={handleChange} />
                </div>

                <div className="mb-4">
                    <h2 className="text-center">Vehículo</h2>
                    <VehiculoForm formData={formData} handleChange={handleChange} />
                </div>

                <div className="text-center">
                    <button type="submit" className="btn btn-primary">Guardar</button>
                </div>
            </form>
        </main>
    );
}

export default CrearFuncionarioVehiculo;
