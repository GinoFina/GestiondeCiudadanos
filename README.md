# GestiondeCiudadanos
Sistema de procesamiento para procesar, limpiar y estructurar un lote de datos crudos de ciudadanos aplicando Programación Orientada a Objetos en Python.

## Arquitectura
La solución está modularizada en:
- `models.py`: Definición de la entidad inmutable `Persona`.
- `registry.py`: Lógica de negocio y procesamiento de registros.
- `data.py`: Lote de datos de prueba.
- `main.py`: Punto de entrada y ejecución.
- `tests/`: Testing unitario aislado.

## Requisitos previos
- Python 3.13.6 (o superior) instalado en el sistema.
- No se requieren librerías externas. Todo el código utiliza la biblioteca estándar de Python.

## Cómo ejecutar el script
- Para procesar el lote de datos y visualizar las métricas y segmentaciones por consola, ejecutar el siguiente comando en la raíz del proyecto:
python main.py
- Para la ejecución de las pruebas, ejecutar el siguiente comando en la raíz del proyecto:
python -m unittest discover tests
