<?php
include 'db_connect.php';

// Obtener datos del formulario
$origen = $_POST['origen'];
$destino = $_POST['destino'];
$fecha = $_POST['fecha'];
$plazas = $_POST['plazas'];
$precio = $_POST['precio'];

// Validar datos
if (empty($origen) || empty($destino) || empty($fecha) || empty($plazas) || empty($precio)) {
    die("Todos los campos son obligatorios");
}

if (!is_numeric($plazas) || !is_numeric($precio)) {
    die("Plazas y precio deben ser números");
}

// Preparar y ejecutar la consulta
$stmt = $conn->prepare("INSERT INTO VUELO (origen, destino, fecha, plazas_disponibles, precio) VALUES (?, ?, ?, ?, ?)");
$stmt->bind_param("sssid", $origen, $destino, $fecha, $plazas, $precio);

if ($stmt->execute()) {
    echo "Vuelo agregado con éxito";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
