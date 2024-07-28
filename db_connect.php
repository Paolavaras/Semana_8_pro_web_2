<?php
$servidor = "localhost";
$nombreusuario = "root";
$password = "";


// Crear conexión
$conexion = new mysqli($servidor, $nombreusuario, $password);

if($conexion->connect_error){
    die("conexion fallida:" . $connexion->connect_error);

}
$sql = "CREATE DATABASE agencia";
if($conexion->query($sql) === true) {
    echo "base de datos creada correctamente...";


}else{
    die("error al crear base de datos: " . $conexion->error);
    
}

?>
