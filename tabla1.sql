-- Crear la base de datos
CREATE DATABASE semana8;

-- Usar la base de datos
USE semana 8;

-- Crear la tabla FaunaFlora
CREATE TABLE FaunaFlora (
    ID INT PRIMARY KEY,
    NombreCientifico VARCHAR(100),
    Habitat VARCHAR(50),
    EstadoConservacion VARCHAR(20),
    RegionGeografica VARCHAR(50)
);

-- Insertar registros en la tabla FaunaFlora
INSERT INTO FaunaFlora (ID, NombreCientifico, Habitat, EstadoConservacion, RegionGeografica)
VALUES
    (1, 'Panthera leo', 'Sabana', 'Vulnerable', 'África'),
    (2, 'Quercus robur', 'Bosque Templado', 'Preocupación Menor', 'Europa'),
    (3, 'Phalaenopsis amabilis', 'Selva Tropical', 'En Peligro', 'Sudeste Asiático');