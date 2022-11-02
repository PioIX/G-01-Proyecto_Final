# Presupuesto

## Estructura de la base de datos:

	Tabla ‘Jugadores’:
		Campos:
		id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
		nombre	        TEXT UNIQUE NOT NULL
		contraseña 	TEXT NOT NULL
		victorias 	INTEGER NOT NULL
		url_foto	TEXT NOT NULL
    
## Reglas:

Nuestro proyecto consiste en hacer un juego online 1 contra 1, en el que a cada jugador se le da una sílaba (ya sea de 2 o 3 letras), y a partir de ello tienen que escribir una palabra que contenga dicha sílaba. La palabra debe existir en la API ([Spanish Random Words](https://rapidapi.com/AlexScigalszky/api/spanish-random-words/details)) de palabras que vamos a usar. Ingresar una palabra correctamente suma un punto al jugador, y se le da una nueva sílaba. Si un jugador no logra escribir una palabra en 10 segundos, se le da otra sílaba, pero no suma puntos. De esta forma, el jugador que más puntos consiga en un tiempo límite de 150 segundos (2 minutos y medio). 

Implementamos un sistema de inicio de sesión y registro de jugadores, que mediante el método POST, se encarga de añadir jugadores nuevos a la base de datos.

En cuanto al resto del programa, al iniciar aparece el menú principal en el que se encuentra el logo de nuestro juego, y cuatro botones.
* JUGAR: Te manda a una pantalla en la que se tiene que hacer conexión con otra computadora.
* ¿CÓMO JUGAR? / INSTRUCCIONES: Te manda a una pantalla en la que se explica las reglas del juego y cómo conectarte con otro jugador.
* RANKING: Te manda a una pantalla en la que muestra un ranking con los jugadores con más victorias acumuladas. En caso de empate, ambos se muestran con la misma posición, y se ordenan alfabéticamente. 
* CRÉDITOS: Te manda a una pantalla en la que se da créditos a los creadores (nosotros) y a otras personas de las que tomamos, por ejemplo JKLM (Juego del que nos inspiramos) o la API.

En nuestro programa, el admin tiene la capacidad de:
* Borrar jugadores de la tabla (DELETE).
* Modificar la cantidad de victorias de un jugador (PUT).
* Obtener id, nombre, contraseña y cantidad de victorias de un jugador (GET).

## Maqueta Html:

_Nota: Las ímagenes son un boceto; el diseño de la página puede sufrir posibles cambios._

### Logo:

<img src="https://i.postimg.cc/Pf9wWz4S/logo.png">

### Página: 

<img src="https://i.postimg.cc/BZ2Sgqjs/cap1.png">
<img src="https://i.postimg.cc/0yy9PDc2/cap2.png">
<img src="https://i.postimg.cc/tC59K2dM/cap4.png">
<img src="https://i.postimg.cc/0yXPQjBG/cap5.png">
<img src="https://i.postimg.cc/8CFDrG22/cap6.png">

