create database pythonDb2;
use pythonDb2;

create table usuarios(
    rut varchar(50)primary key not null,
	nombres varchar(50),
	apellidos varchar(50),
    telefono varchar(50),
    correo varchar(50),
    direccion varchar(50),
	sexo varchar(20)
);


insert into usuarios values ("2141977-6", "Joaquin", "Varas", "930120457", "joaquinvarascaceres2@gmail.com", "Pasaje san benito 1688", "Masculino");
select * from usuarios;

UPDATE usuarios SET usuarios.nombres = "Ricardo", usuarios.apellidos = "Alarcon", usuarios.sexo = "Masculino" WHERE usuarios.id = 2;

drop table usuarios;