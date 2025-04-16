---
layout: page
title: Comunicacion
permalink: /comunicacion

---
# 🔄 Comunicación con otros módulos

El módulo de Reservas se comunica con otros módulos de forma interna utilizando el sistema ORM de Odoo.

## Características de la comunicación

- **Formato**: Interno de Odoo (ORM).
- **Estructura del mensaje**: Uso de métodos estándar como:
  - `env['modelo'].search()` para obtener información de otros modelos.
  - `message_post()` para enviar notificaciones automáticas a los clientes.

- **Protocolo**: XML-RPC / ORM interno de Odoo.

## Ejemplo de código

```python
cliente = env['res.partner'].search([('id', '=', id_cliente)])
cliente.message_post(body="Reserva confirmada para su ruta.")
```
---