import React from 'react';

function VehiculoForm({ formData, handleChange }) {
    return (
        <div className="mb-4">
            <h2 className="text-center">Vehículo</h2>
            <div className="mb-3">
                <label htmlFor="marca" className="form-label">Marca</label>
                <input
                    type="text"
                    id="marca"
                    name="marca"
                    value={formData.marca || ''}
                    onChange={handleChange}
                    className="form-control"
                    placeholder="Escribe la marca del vehículo"
                    required
                />
            </div>
            <div className="mb-3">
                <label htmlFor="modelo" className="form-label">Modelo</label>
                <input
                    type="text"
                    id="modelo"
                    name="modelo"
                    value={formData.modelo || ''}
                    onChange={handleChange}
                    className="form-control"
                    placeholder="Escribe el modelo del vehículo"
                    required
                />
            </div>
        </div>
    );
}

export default VehiculoForm;
