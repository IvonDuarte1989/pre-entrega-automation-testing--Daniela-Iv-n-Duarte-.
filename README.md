#  Proyecto de Automatización QA – SauceDemo

##  Propósito del Proyecto
Este proyecto forma parte de la **pre-entrega del curso de Automatización QA**.  
Su objetivo es **automatizar flujos básicos de navegación y validación funcional** en el sitio [SauceDemo](https://www.saucedemo.com/) utilizando **Selenium WebDriver** y **Python**, aplicando los conocimientos adquiridos en las clases 6 a 8 del curso.

El flujo automatizado replica la interacción de un usuario real:
1. Login con credenciales válidas.  
2. Validación de acceso al inventario.  
3. Comprobación de productos visibles y sus precios.  
4. Agregado de un producto al carrito.  
5. Verificación del contador de carrito y contenido correcto.  

Este proyecto demuestra habilidades en:
- Automatización de interfaz (UI testing).  
- Uso de selectores CSS y XPath.  
- Manejo de esperas explícitas e implícitas.  
- Validación de estados y flujos en la web.  

---

##  Tecnologías Utilizadas

+ **Python 3.x** -->Lenguaje principal de programación.
+ **Pytest**--> Framework de testing utilizado para estructurar los casos de prueba. 
+ **Selenium WebDriver 4.x** --> Librería para automatización del navegador. 
+ **ChromeDriver** --> Driver de control del navegador Google Chrome. 
+ **HTMLTestReport / pytest-html** --> Generación de reporte HTML de ejecución. 
+ **Git y GitHub** --> Control de versiones y repositorio del proyecto. 

---

## Estructura del Proyecto

+ pre-entrega-automation-testing-DanielaDuarte/
  - tests/
    - test_login.py
    - test_inventory.py
    - test_products.py
  - utils/
    - login.py
  - run_tests.py
  - conftest.py
  - README.md

## Instalaciòn de las dependencias requeridas:

pip install -r requirements.txt

pip install selenium pytest pytest-html

Descargar el ChromeDriver correspondiente a la versión del navegador y asegurarse de que esté en tu PATH.

## Ejecución de las Pruebas

Para ejecutar todas las pruebas del proyecto y generar un reporte en HTML:

pytest tests/ --html=report.html --self-contained-html -v

O bien, ejecuta el script que las agrupa:

python run_tests.py


## Esto ejecutará:

test_login.py → Verifica login y redirección al inventario.

test_inventory.py → Valida productos, precios, filtros y menú.

test_products.py → Agrega un producto al carrito y comprueba el flujo completo.

El reporte se generará como report.html en la raíz del proyecto.

## Consideraciones Técnicas

Se utilizaron esperas explícitas (WebDriverWait) para sincronizar elementos dinámicos como el botón Add to cart y el badge del carrito.

Se implementaron aserciones (assert) para validar la correcta navegación, presencia de elementos y actualización del carrito.

Cada test cierra correctamente el navegador con driver.quit() en el bloque finally.

Se usaron selectores CSS robustos en lugar de rutas XPath absolutas, según las buenas prácticas del curso.

## Autor

Daniela Ivón Duarte
Estudiante QA Tester – Pre-Entrega de Automatización
Buenos Aires, Argentina

## Licencia

Proyecto de práctica educativa, sin fines comerciales.
Basado en el sitio demo público https://www.saucedemo.com
