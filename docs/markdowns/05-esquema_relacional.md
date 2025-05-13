---
layout: page
title: Esquema E-R
permalink: /diagrama_E-R

---
## 🗺️ Diagrama Relacional

![Esquema relacional](../images/diagrama_ER.svg)

---
# Esquema Relacional de Datos

El módulo define nuevas tablas relacionadas entre sí para gestionar reservas de forma estructurada. Para proporcionar una mejor comprensión de la relación entre entidades, se detalla a continuación cada entidad y sus atributos principales.

---

## Cliente

| Campo             | Tipo        | Descripción           |
|-------------------|-------------|------------------------|
| `dni`             | varchar(9)  | Identificador único    |
| `nombre`          | varchar(45) | Nombre del cliente     |
| `telefono`        | varchar(12) | Teléfono de contacto   |
| `mail`            | varchar(60) | Correo electrónico     |
| `fecha_nacimiento`| date        | Fecha de nacimiento    |

---

## Hospedaje

| Campo                   | Tipo          | Descripción                             |
|------------------------|---------------|------------------------------------------|
| `cif`                  | varchar(9)    | Identificador único del hospedaje        |
| `nombre`               | varchar(100)  | Nombre del establecimiento               |
| `capacidad`            | int           | Número máximo de personas                |
| `admite_mascotas`      | boolean       | Si admite mascotas                       |
| `adaptado_mov_reduc`   | boolean       | Si está adaptado para personas con movilidad reducida |
| `telefono`             | varchar(12)   | Teléfono de contacto                     |
| `mail`                 | varchar(60)   | Correo electrónico                       |
| `descripcion`          | varchar(140)  | Breve descripción                        |

---

## Ruta

| Campo         | Tipo          | Descripción              |
|--------------|---------------|-------------------------- |
| `nombre`      | varchar(100)  | Nombre de la ruta        |
| `distancia`   | double        | Distancia total          |
| `url_maps`    | varchar(100)  | Enlace de Google Maps    |
| `descripcion` | varchar(140)  | Breve descripción        |
| `es_circular` | boolean       | Si la ruta es circular   |

---

## Pack

| Campo         | Tipo          | Descripción             |
|--------------|---------------|------------------------- |
| `nombre`      | varchar(100)  | Nombre del pack         |
| `precio`      | double        | Precio total            |
| `descripcion` | varchar(140)  | Breve descripción       |

---

## Item

| Campo         | Tipo          | Descripción             |
|--------------|---------------|------------------------- |
| `nombre`      | varchar(100)  | Nombre del item         |
| `precio`      | double        | Precio                  |
| `descripcion` | varchar(140)  | Breve descripción       |

---

## Viaje

Tabla intermedia que une cliente, ruta y pack, hace referencia a la reserva del viaje.

| Campo            | Tipo       | Clave     | Descripción                          |
|------------------|------------|-----------|--------------------------------------|
| `id_cliente`      | int        | FK        | Cliente que realiza el viaje         |
| `id_ruta`         | int        | FK        | Ruta seleccionada                    |
| `id_pack`         | int        | FK        | Pack contratado                      |
| `fecha`           | date       | -         | Fecha del viaje                      |
| `estado`          | selection  | -         | Determina el estado del viaje        |
| `nombre`          | varchar(100) | -       | Nombre del viaje                     |
| `hosp_count`      | int        | -         | Campo calculado que cuenta los hospedajes asignados |
| `con_mascota`     | boolean    | -         | Si viaja con mascota                 |
| `movilidad_reduc` | boolean    | -         | Si necesita accesibilidad especial   |

---

## Hito

Representa un punto de interés en una ruta.

| Campo            | Tipo        | Descripción                        |
|------------------|-------------|------------------------------------|
| `nombre`         | varchar(100)| Nombre del hito                    |
| `puntoX`         | double (PK) | Coordenada X del hito              |
| `puntoY`         | double (PK) | Coordenada Y del hito              |
| `tipo`           | varchar(12) | Tipo de hito                       |
| `orden_en_ruta`  | int         | Orden del hito en la ruta (atributo de la tabla intermedia)|
| `descripcion`    | varchar(140)| Descripción del punto              |