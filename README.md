# PlaygroundFinalProject-LGonzalez
Este es mi proyecto final o "Playground" del curso Python Flex de Coderhouse 2023. 

<h3>Video</h3>
https://drive.google.com/file/d/1HIK2L27kYCIUk9ILOhMsSBf0gUMnw8o7/view?usp=sharing

<h3>Casos de Prueba</h3>
https://docs.google.com/spreadsheets/d/1aZvQw1N6iWEQSgme9v2xEPQQ-_i7LM9tTHmgKzo8qoY/edit?usp=sharing

## Instrucciones
Para el correcto funcionamiento de este proyecto, tras clonar el repositorio desde aquí, es recomendable seguir los siguientes pasos:

1) Primero deberás clonar este repositorio. Para eso en tu terminal de, por ejemplo, Visual Studio Code, deberás escribir: <i>git clone https://github.com/luisinago/PlaygroundFinalProject-LGonzalez.git</i>
1) <b>Opcional:</b> Crear un "entorno virtual". En Windows, en la terminal, se hace escribiendo: <i>python -m venv myvenv</i> (en myvenv iría el nombre que desees ponerle) y activándolo con: <i>.\myvenv\Scripts\activate</i> (ídem el punto anterior, en "myvenv" iría el nombre del entorno creado previamente).

2) Revisar el archivo <b>requirements.txt</b> y corroborar que tienes instaladas todas las librerías. En caso de no ser así escribe en la terminal: <i>pip install -r requirements.txt</i>

3) Una vez tengas todo instalado, desde la terminal escribe: <i>python manage.py runserver</i> para correr el servidor (la página)

## Funcionalidades
Al entrar a la página te encontrarás con un "Sobre Mi", el cual está predeterminado como pantalla de inicio. También se puede acceder aquí desde el menú superior y desde el "logo" en la esquina superior izquierda.
La idea principal de la página es poder crear Magical Girls. Para ello se debe elegir un show en el menú superior (las opciones son: W.I.T.C.H, Winx y Sailor Moon).
Cada una de estas páginas mostrará una lista de personajes creados y debajo opciones para ver detalle, borrar o eliminar.

#### Funcionalidades restringidas
Para las siguientes funcionalidades se requiere tener un usuario creado:

* Editar Magical Girl
* Borrar Magical Girl
* Cambiar nombre, apellido, email y avatar de cuenta
