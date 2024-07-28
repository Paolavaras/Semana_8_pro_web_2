<?php
include 'db_connect.php';

// Obtener datos del formulario
$nombre = $_POST['nombre'];
$ubicacion = $_POST['ubicacion'];
$habitaciones = $_POST['habitaciones'];
$tarifa = $_POST['tarifa'];

// Validar datos
if (empty($nombre) || empty($ubicacion) || empty($habitaciones) || empty($tarifa)) {
    die("Todos los campos son obligatorios");
}

if (!is_numeric($habitaciones) || !is_numeric($tarifa)) {
    die("Habitaciones y tarifa deben ser números");
}

// Preparar y ejecutar la consulta
$stmt = $conn->prepare("INSERT INTO HOTEL (nombre, ubicación, habitaciones_disponibles, tarifa_noche) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssdi", $nombre, $ubicacion, $habitaciones, $tarifa);

if ($stmt->execute()) {
    echo "Hotel agregado con éxito";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
