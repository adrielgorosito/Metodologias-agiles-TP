# 🔤 Ahorcado 🔤
Trabajo final para la materia "<a href = "https://www.frro.utn.edu.ar/repositorio/departamentos/sistemas/files/Fichas/66.html">Metodologías Ágiles en Desarrollo de Software</a>" de la carrera Ingeniería en Sistemas de Información de la UTN FRRo. El propósito principal del proyecto es desarrollar el clásico juego del Ahorcado de forma ágil, simulando sprints de SCRUM y aplicando técnicas de Extreme Programming (XP), tales como Pair Programming, TDD, Continuous integration, Simple design, etc.

## Objetivo del juego
El objetivo del juego es adivinar una palabra oculta antes de que se completen todas las partes del cuerpo del ahorcado, es decir, antes de que se acaben las vidas.

## Reglas
* Un jugador ingresa por teclado la palabra oculta.
* Otro jugador intenta adivinar la palabra oculta arriesgando letras o arriesgando una palabra.
* Al acertar una letra, revela las posiciones dentro de la palabra.
* Al errar una letra, suma una parte del cuerpo del ahorcado, hasta un máximo de siete partes.
* El jugador gana si adivina todas las letras o si arriesga correctamente la palabra.
* El jugador pierde si completa todas las partes del cuerpo del ahorcado.

## Imágenes
Debido a que el objeto principal del trabajo práctico es aplicar metodologías ágiles, se desarrolló tanto un backend como un frontend sencillos.

![imagen](https://github.com/adrielgorosito/Metodologias-agiles-TP/assets/70348592/7c9978b8-ab33-4cd2-8d01-1ee2753d7f50)

![imagen](https://github.com/adrielgorosito/Metodologias-agiles-TP/assets/70348592/82a05eb2-4016-4956-8b65-acaa48792ee2)

![imagen](https://github.com/adrielgorosito/Metodologias-agiles-TP/assets/70348592/89a0f982-fe6d-4222-8a88-45e4aadd025e)

<br>

# 🎮 Cómo jugar 🎮

## Requisitos
* Python 3.8
* Angular CLI

## Instalación
1. Clonar el repositorio localmente por medio de `git clone https://github.com/adrielgorosito/Metodologias-agiles-TP.git`.
2. Navegar a la carpeta **tp** y ejecutar `pip3 install -r requirements.txt` para instalar las dependencias de Python.
3. Iniciar el servidor de Python ejecutando `uvicorn main:app --reload` desde la carpeta tp.
4. Navegar a la carpeta **frontend** y ejecutar `npm install` para instalar las dependencias de Angular.
5. Iniciar la aplicación de Angular ejecutando `ng serve -o` desde la carpeta frontend.

Nota: modificar la url del backend dentro del servicio **AhorcadoService** en Angular a `http://127.0.0.1:8000`.

## Deploy de la aplicación
Alternativamente, se puede jugar visitando la página: <a href = "https://metodologias-agiles-tp.vercel.app/jugar">metodologias-agiles-tp.vercel.app</a>.

<br>

# 📖 Trabajo práctico 📖

## Requisitos
1. Unit Tests usando TDD.
2. Single Repository.
3. CI Server que solo compile (Github Actions, Azure DevOps, TravisCI, etc).
4. CI Server que ejecute los Unit tests.
5. CI Server que muestre resultados de Code Coverage.
6. Desarrollar UI Web con Acceptance tests.
7. CI Server que deploye a producción.
8. CI Server que ejecute Análisis Estático de Código.
9. CI Server que ejecute los Acceptance tests.

## Detalles
* El backend fue programado con **Python**, utilizando el framework **FastAPI**. El frontend se programó con **Angular**.
* Se utilizó el framework **unittest** de Python para desarrollar los tests unitarios.
* Se utilizó el framework **Cucumber** junto a **behave** y el lenguaje **Gherkin** para desarrollar los tests de aceptación.
* Se eligió **Github Actions** como servidor de integración continua para automatizar los UT y AT.
* Se utilizó **Render** para el deploy del backend y **Vercel** para el deploy del frontend.
* Se utilizó **SonarQube** para el análisis estático de código.

## Ejecutar Unit tests
1. Navegar a la carpeta tp.
2. Ejecutar el comando `coverage run unit_tests.py` para correr los tests unitarios.
3. Ejecutar el comando `coverage report` para obtener un reporte de test coverage.

## Ejecutar Acceptance tests
1. Navegar a la carpeta tp.
2. Ejecutar el comando `behave -f allure_behave.formatter:AllureFormatter -o at_results ./features` para correr los tests de aceptación.
3. Ejecutar el comando `allure generate at_results -o allure-report` para obtener un reporte del resultado de los tests.
4. Ejecutar el comando `allure open allure-report -h localhost` para ver el reporte de forma gráfica.

<br>

# 👥 Colaboradores 👥
Este proyecto fue desarrollado por:
* Ballestero, Martín Aníbal - <a href = "https://github.com/tincho425">@tincho425</a>
* Gorosito, Adriel Tomás - <a href = "https://github.com/adrielgorosito">@adrielgorosito</a>

Profesores:
* Joaquín, Andrés
* Cullen, Patricio
