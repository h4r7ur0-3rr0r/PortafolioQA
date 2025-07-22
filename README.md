**Descripción del Proyecto**

Este proyecto automatiza pruebas en MercadoLibre utilizando:

**Lenguaje:** Python

**Framework:** Pytest

**Navegador:** Chrome (vía Selenium WebDriver)


**Funcionalidades**

1.-Navega a MercadoLibre México
2.-Busca "PlayStation 5"
3.-Filtra por condición "Nuevo" y ubicación "CDMX"
4.-Ordena por precio (mayor a menor)
5.-Obtiene los 5 primeros resultados
6.-Genera reportes HTML con evidencias

Ejecución
Para ejecutar el proyecto se debe realizar lo siguiente 
1.-Clonar el repositorio:
   git clone (https://github.com/h4r7ur0-3rr0r/PortafolioQA)
   cd mercado_libre_test
2.-Crear y activar entorno virtual:
    python -m venv venv
    venv\Scripts\activate
3.-Instalar dependencias:
    pip install -r requirements.txt
4.- Para ejecutar las pruebas y generar reporte HTML:
    pytest tests/test_mercadolibre.py -v --html=reports/report.html --self-contained-html
El reporte se generará en reports/report.html y las capturas de pantalla se guardarán en la misma carpeta.
