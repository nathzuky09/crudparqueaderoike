import React from 'react';
import './Home.css'; 
import './Signup.css' // Crea este archivo para estilos personalizados si es necesario

function Home() {
    return (
        <main className="container py-5">
            <section className="card card-body">
                <h1 className="display-2 text-center">IkeParks</h1>
                <p>
                    IkeParq es el parqueadero ideal para tu empresa, combinando seguridad, eficiencia y comodidad en un solo lugar.
                    Con vigilancia 24/7, espacios de estacionamiento, IkeParq garantiza la protección de tus vehículos y la tranquilidad
                    de tu equipo. Además, su ubicación estratégica y sus opciones de pago flexibles hacen que estacionar sea sencillo
                    y accesible. Elige IkeParq y descubre cómo un buen parqueadero puede mejorar la movilidad y productividad de tu empresa.
                </p>

                <div className="text-center">
                    <a className="btn btn-secondary" href="/inicio_sesion/">
                        Inicia Sesión
                    </a>
                    <a className="btn btn-primary" href="/signup/">
                        Registrate!
                    </a>
                </div>
            </section>
        </main>
    );
}

export default Home;

