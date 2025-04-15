---
layout: page
title: Entidad Relacion
permalink: /diagrama_E-R/

---
## 🗺️ Diagrama Relacional

![Esquema relacional](../../images/diagrama_ER.svg)

---
# Esquema Relacional de Datos

El módulo define nuevas tablas relacionadas entre sí para gestionar reservas de forma estructurada. Para proporcionar una mejor comprensión de la relación entre entidades, se detalla a continuación cada entidad y sus atributos principales.

---

## Cliente

| Campo             | Tipo         | Descripción            |
|------------------|--------------|------------------------|
| `id_cliente`      | int (PK)     | Identificador único    |
| `nombre`          | varchar(45)  | Nombre del cliente     |
| `telefono`        | varchar(12)  | Teléfono de contacto   |
| `mail`            | varchar(60)  | Correo electrónico     |
| `fecha_nacimiento`| date         | Fecha de nacimiento    |

---

## Hospedaje

| Campo                   | Tipo          | Descripción                              |
|------------------------|---------------|------------------------------------------|
| `id_hosp`              | int (PK)      | Identificador del hospedaje              |
| `nombre`               | varchar(100)  | Nombre del establecimiento               |
| `capacidad`            | int           | Número máximo de personas                |
| `admite_mascotas`      | boolean       | Si admite mascotas                       |
| `adaptado_mov_reduc`   | boolean       | Si está adaptado para personas con movilidad reducida |
| `telefono`             | varchar(12)   | Teléfono de contacto                     |
| `mail`                 | varchar(60)   | Correo electrónico                       |

---

## Ruta

| Campo         | Tipo          | Descripción              |
|--------------|---------------|--------------------------|
| `id_ruta`     | int (PK)      | Identificador de la ruta |
| `nombre`      | varchar(100)  | Nombre de la ruta        |
| `distancia`   | double        | Distancia total          |
| `url_maps`    | varchar(100)  | Enlace de Google Maps     |
| `descripcion` | varchar(140)  | Breve descripción        |

---

## Pack

| Campo         | Tipo          | Descripción             |
|--------------|---------------|-------------------------|
| `id_pack`     | int (PK)      | Identificador del pack  |
| `nombre`      | varchar(100)  | Nombre del pack         |
| `precio`      | double        | Precio total            |
| `descripcion` | varchar(140)  | Breve descripción             |

---

## Item

| Campo         | Tipo          | Descripción             |
|--------------|---------------|-------------------------|
| `id_item`     | int (PK)      | Identificador del item  |
| `nombre`      | varchar(100)  | Nombre del item         |
| `precio`      | double        | Precio                  |
| `descripcion` | varchar(140)  | Breve descripción             |

---

## Viaje

Tabla intermedia que une cliente, ruta y pack, hace referencia a la reserva del viaje.

| Campo            | Tipo       | Clave     | Descripción                          |
|------------------|------------|-----------|--------------------------------------|
| `id_cliente`      | int        | FK        | Cliente que realiza el viaje         |
| `id_ruta`         | int        | FK        | Ruta seleccionada                    |
| `id_pack`         | int        | FK        | Pack contratado                      |
| `fecha`           | date       | -         | Fecha del viaje                      |
| `nombre`          | varchar(100) | -       | Nombre del viaje                     |
| `con_mascota`     | boolean    | -         | Si viaja con mascota                 |
| `movilidad_reduc` | boolean    | -         | Si necesita accesibilidad especial   |

---

## Hito

Representa un punto de interés en una ruta.

| Campo            | Tipo        | Descripción                        |
|------------------|-------------|------------------------------------|
| `puntoX`         | double (PK) | Coordenada X del hito              |
| `puntoY`         | double (PK) | Coordenada Y del hito              |
| `tipo`           | varchar(12) | Tipo de hito (merendero, tienda, escultura, punto de paso, etc.)                       |
| `orden_en_ruta`  | int         | Orden del hito en la ruta          |
| `descripcion`    | varchar(140)| Descripción del punto              |