# **🚀 Hackathon DAM: De Cero a Producción en 12h**

Este documento es vuestra hoja de ruta. Tenéis 12 horas para construir una aplicación web funcional. Recordad: la próxima semana, otros compañeros intentarán encontrar fallos de seguridad en vuestro código. **¡Construid con cuidado\!**

## **1\. Opciones de Proyectos (Elegid uno)**

Estas ideas están diseñadas para ser completadas en el tiempo previsto usando un stack sencillo (HTML/JS/Node o Python/Flask o PHP).

| Proyecto | Descripción Core |
| :---- | :---- |
| **Gestor de Notas Privadas** | Un usuario se registra, inicia sesión y escribe notas que solo él puede ver. |
| **Foro de Mensajes** | Un muro público donde cualquiera puede publicar mensajes sin registro. |
| **Mini-Tienda** | Un catálogo de productos donde se puede buscar por nombre y ver stock. |
| **Sistema de Subida de CVs** | Un formulario donde los usuarios suben un archivo .pdf con su currículum. |

---

**2\. Requisitos de Despliegue (Mínimos)**

Para que vuestra app sea evaluable, debe cumplir esta estructura básica:

### **A. Estructura de Datos**

* **Base de Datos:** Podéis usar SQLite o JSON (un archivo local, lo más rápido).  
* **Usuarios:** Debe haber al menos una tabla de usuarios con contraseñas (¡pensad si las guardáis en texto plano o con hash\!).

### **B. Infraestructura**

Podéis elegir uno de estos dos caminos para que la app sea accesible:

1. **Contenedor Docker:** Un Dockerfile que levante vuestro servidor web y la base de datos (todo en uno).  
2. **PaaS:** Despliegue directo en **Railway.app** o **Render.com** (conectando vuestro repo de GitHub).

--- 

**3\. Ejemplo de Arquitectura Sugerida**

Si no sabéis por dónde empezar, usad este esquema estándar:

**Frontend:** HTML5 \+ CSS (Framework como Pico.css o Bootstrap para no perder tiempo en diseño).

**Backend:** Express.js (Node) o Flask (Python).

**Persistencia:** Archivo JSON o SQLite.

---

**4\. Checklist de "Supervivencia"**

Antes de entregar, aseguraos de que vuestra app no cae ante lo más básico:

* \[ \] **Validación:** ¿Qué pasa si envío un formulario vacío?  
* \[ \] **Autenticación:** ¿Puedo acceder a una ruta simplemente escribiendo la URL sin loguearme?  
* \[ \] **Reducción:** ¿Mando únicamente la información necesaria o toda la disponible?  
* \[ \] **Control de Errores:** Si algo falla, ¿la app muestra el error feo del servidor con rutas de carpetas o un mensaje amigable?

---

**5\. Herramientas Útiles**

* **Para el desarrollo:** Visual Studio Code \+ Extensiones de lenguaje.  
* **Para bases de datos:** [DBeaver](https://dbeaver.io/) para visualizar vuestras tablas fácilmente.
