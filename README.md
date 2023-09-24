# FastApi backend test

by [Juan Manuel Guerrero Castro](https://www.linkedin.com/in/juan-manuel-guerrero-castro-58062a15a)

## Requisitos Previos

Asegúrate de tener instalados los siguientes elementos en tu sistema antes de ejecutar el proyecto:

- Python 3.x: [Descargar Python](https://www.python.org/downloads/)
- pip (Administrador de paquetes de Python): Debería instalarse junto con Python.

## Configuración del Entorno Virtual (venv)

1. Clona este repositorio en tu PC.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando para crear el entorno virtual:

```bash
python -m venv venv
```

4. Activa el entorno virtual:

```bash
source venv/bin/activate
```

5. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

6. Ejecuta el proyecto:

```bash
uvicorn main:app --reload
```

## Documentación de la API

Se encuentra en la siguiente ruta: http://ip:puerto/docs

## Ejecución de pruebas unitarias

1. Ejecuta el siguiente comando:

```bash
pytest
```