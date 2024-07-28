<?php
// Define database credentials
$servidor = "localhost";
$nombreusuario = "root";
$password = "";
$dbname = "Agencia"; // Nombre de la base de datos

// Crear conexión
$conn = new mysqli($servidor, $nombreusuario, $password);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Crear base de datos
$sql = "CREATE DATABASE IF NOT EXISTS $dbname"; // Se crea la base de datos si no existe
if ($conn->query($sql) === TRUE) {
    echo "Base de datos $dbname creada correctamente...<br>";
} else {
    die("Error al crear la base de datos $dbname: " . $conn->error . "<br>");
}

// Seleccionar la base de datos
$conn->select_db($dbname);

// Crear tabla VUELO
$sql = "CREATE TABLE IF NOT EXISTS VUELO (
    id_vuelo INT PRIMARY KEY AUTO_INCREMENT,
    origen VARCHAR(50) NOT NULL,
    destino VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    plazas_disponibles INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL
)";

if ($conn->query($sql) === TRUE) {
    echo "Tabla VUELO creada correctamente...<br>";
} else {
    die("Error al crear la tabla VUELO: " . $conn->error . "<br>");
}

// Crear tabla HOTEL
$sql = "CREATE TABLE IF NOT EXISTS HOTEL (
    id_hotel INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100) NOT NULL,
    habitaciones_disponibles INT NOT NULL,
    tarifa_noche DECIMAL(10,2) NOT NULL
)";

if ($conn->query($sql) === TRUE) {
    echo "Tabla HOTEL creada correctamente...<br>";
} else {
    die("Error al crear la tabla HOTEL: " . $conn->error . "<br>");
}

// Crear tabla RESERVA
$sql = "CREATE TABLE IF NOT EXISTS RESERVA (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    id_vuelo INT NOT NULL,
    id_hotel INT NOT NULL,
    FOREIGN KEY (id_vuelo) REFERENCES VUELO(id_vuelo),
    FOREIGN KEY (id_hotel) REFERENCES HOTEL(id_hotel)
)";

if ($conn->query($sql) === TRUE) {
    echo "Tabla RESERVA creada correctamente...<br>";
} else {
    die("Error al crear la tabla RESERVA: " . $conn->error . "<br>");
}

// Cerrar conexión
$conn->close();
?>