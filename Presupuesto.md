# Presupuesto

### Estructura de la base de datos:

	Tabla ‘Jugadores’:
		Campos:
		id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
		nombre	        TEXT UNIQUE NOT NULL
		contraseña 	TEXT NOT NULL
		victorias 	INTEGER NOT NULL
    
### Reglas:

Nuestro proyecto consiste en hacer un juego online 1 contra 1, en el que a cada jugador se le da una sílaba (ya sea de 2 o 3 letras), y a partir de ello tienen que escribir una palabra que contenga dicha sílaba. La palabra debe existir en la API ([Spanish Random Words](https://rapidapi.com/AlexScigalszky/api/spanish-random-words/details)) de palabras que vamos a usar. Ingresar una palabra correctamente suma un punto al jugador, y se le da una nueva sílaba. Si un jugador no logra escribir una palabra en 10 segundos, se le da otra sílaba, pero no suma puntos. De esta forma, el jugador que más puntos consiga en un tiempo límite de 150 segundos (2 minutos y medio). 

En cuanto al resto del programa, al iniciar aparece el menú principal en el que se encuentra el logo de nuestro juego, y cuatro botones.
JUGAR: Te manda a una pantalla en la que se tiene que hacer conexión con otra computadora.
¿CÓMO JUGAR? / INSTRUCCIONES: Te manda a una pantalla en la que se explica las reglas del juego y cómo conectarte con otro jugador.
RANKING: Te manda a una pantalla en la que muestra un ranking con los jugadores con más victorias acumuladas. En caso de empate, ambos se muestran con la misma posición, y se ordenan alfabéticamente. 
CRÉDITOS: Te manda a una pantalla en la que se da créditos a los creadores (nosotros) y a otras personas de las que tomamos, por ejemplo JKLM (Juego del que nos inspiramos) o la API.
En nuestro programa, el admin tiene la capacidad de borrar jugadores de la tabla (DELETE), modificar algunas reglas del juego (como por ejemplo, el tiempo de la partida, el tiempo antes de cambiar de sílaba, etc) (PUT), obtener el nombre u otros datos de algún jugador (GET) y agregar reglas (POST).

### Maqueta Html:

**Logo:**

<img src="docs/logo.png" alt="logo/>
