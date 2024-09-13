import React from 'react';

function FuncionarioForm({ formData, handleChange }) {
    return (
        <div className="mb-4">
            <h2 className="text-center">Funcionario</h2>
            <div className="mb-3">
                <label htmlFor="nombre" className="form-label">Nombre</label>
                <input
                    type="text"
                    id="nombre"
                    name="nombre"
                    value={formData.nombre || ''}
                    onChange={handleChange}
                    className="form-control"
                    placeholder="Escribe el nombre del funcionario"
                    required
                />
            </div>
            <div className="mb-3">
                <label htmlFor="cargo" className="form-label">Cargo</label>
                <input
                    type="text"
                    id="cargo"
                    name="cargo"
                    value={formData.cargo || ''}
                    onChange={handleChange}
                    className="form-control"
                    placeholder="Escribe el cargo del funcionario"
                    required
                />
            </div>
        </div>
    );
}

export default FuncionarioForm;