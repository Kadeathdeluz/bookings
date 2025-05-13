---
layout: page
title: Diagramas de flujo
permalink: /diagrama_de_flujo

--- 
# 🔄 Diagramas de Flujo Funcionales

## Crear y Consultar Reserva

Este diagrama representa el proceso que sigue el sistema para la creación de una reserva, incluye verificaciones auotmatizadas.

![Diagrama de flujo: Crear y Consultar Reserva](../images/diagrama_flujo.svg)

---

**Breve explicación:**
- Se inicia con la selección del cliente, ruta y pack.
- Se filtran los alojamientos que estén en dicha ruta y asociados con dicho pack.
- Se comprueban los requisitos (mascota y mov. reducida).
- Si se cumple con los requisitos, se muestran los alojamientos disponibles antes de guardar.