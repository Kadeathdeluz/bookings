---
layout: page
title: Diagramas de flujo
permalink: /diagrama_de_flujo

--- 
# 🔄 Diagramas de Flujo Funcionales

## Crear y Consultar Reserva

Este diagrama representa el proceso que sigue el sistema para la creación de una reserva, incluye verificaciones auotmatizadas y la notificación al cliente.

![Diagrama de flujo: Crear y Consultar Reserva](../images/diagrama_flujo.svg)

---

**Breve explicación:**
- Se inicia con la selección del cliente, ruta y pack.
- Se comprueba la disponibilidad del hospedaje.
- Se comprueban los requisitos (mascota y mov. reducida).
- Si hay disponibilidad y se cumple con los requisitos, se registra la reserva.
- Finalmente, se notifica al cliente antes del inicio de la ruta.