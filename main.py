from flask import Flask, render_template, session, request, json
import sqlite3

app = Flask(__name__)
app.secret_key = "juego_de_generar_una_palabra_a_partir_de_dos_letras"

@app.route('/')
def index():
  return render_template('./html/index.html')
  
@app.route('/iniciar_sesion')
def iniciarSesion():
  return render_template('./html/login.html')

@app.route('/registrarse')
def registrarUsuario():
  return render_template('./html/registro.html')

@app.route('/sub_login', methods=['GET', 'POST'])
def verificarUsuario():
  session['nomUsuario'] = request.form['nombre']
  session['conUsuario'] = request.form['contraseña']

  conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
  cur = conn.cursor()

  q = f"""
        SELECT *
        FROM Jugadores
        WHERE nombre = '{session['nomUsuario']}' AND contraseña = '{session['conUsuario']}'
        ;
      """

  cur.execute(q)
  usu = cur.fetchall()
  conn.close()

  if session['nomUsuario'] == 'admin':
    session['jugAdministrador'] = True
  else:
    session['jugAdministrador'] = False
  
  if usu != []:
    if session['jugAdministrador']:
      return json.dumps('{"sesion":true, "action":"/admin"}')
    else:
      return json.dumps('{"sesion":true, "action":"/inicio"}')
      
  else:
    return json.dumps('{"sesion":false, "action":"/"}')

@app.route('/sub_registro', methods=['GET', 'POST'])
def confirmarRegistro():
  session['nomUsuario'] = request.form['nombre']
  session['conUsuario'] = request.form['contraseña']

  conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
  cur = conn.cursor()

  q = f"""
        SELECT *
        FROM Jugadores
        WHERE nombre = '{session['nomUsuario']}'
        ;
      """

  cur.execute(q)
  usu = cur.fetchall()
  conn.close()

  if usu == []:
    conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')

    q = f"""
          INSERT INTO Jugadores (nombre, contraseña, victorias)
          VALUES ('{session['nomUsuario']}', '{session['conUsuario']}', 0)
          ;
        """

    conn.execute(q)
    conn.commit()
    conn.close()

    return 'True'
  else:
    return 'False'

@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
  return render_template('./html/menu.html')

@app.route('/admin', methods=['GET', 'POST', 'PUT', 'DELETE'])
def panelAdministrador():
  return render_template('./html/panelAdministrador.html', listaJugadores = devolverJugadores())

def devolverJugadores():
  conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
  lista = []
  
  q = """
        SELECT nombre
        FROM Jugadores
        ORDER BY id ASC
        ;
      """

  resu = conn.execute(q)
  for fila in resu:
    lista.append(fila[0])

  conn.close()

  return lista

@app.route('/recepcionAjax', methods=['GET', 'POST', 'PUT', 'DELETE'])
def atencionAjax():
  if request.method == 'GET':
    conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
    lista = []
    
    q = """
          SELECT *
          FROM Jugadores
          ;
        """

    resu = conn.execute(q)
    for fila in resu:
      lista.append(fila)
    conn.close()
    texto = '['
    i = 0
    while i < len(lista)-1:
      texto += '{"id": "' + str(lista[i][0]) + '", "nombre": "' + lista[i][1] + '", "contraseña": "' + lista[i][2] + '", "victorias": "' + str(lista[i][3]) + '"}, '
      i += 1
    texto += '{"id": "' + str(lista[i][0]) + '", "nombre": "' + lista[i][1] + '", "contraseña": "' + lista[i][2] + '", "victorias": "' + str(lista[i][3]) + '"}]'
    
    return json.dumps(texto)

  elif request.method == 'PUT':
    conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')

    q = f"""
          UPDATE Jugadores
          SET victorias = '{request.form['modVictorias']}'
          WHERE nombre = '{request.form['nomModificar']}'
          ;
        """

    conn.execute(q)
    conn.commit()

    conn.close()

    return 'true'
    
  elif request.method == 'DELETE':
    conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
  
    q = f"""
          DELETE FROM Jugadores
          WHERE nombre = '{request.form['nomBorrar']}'
          ;
        """

    conn.execute(q)
    conn.commit()

    conn.close()
    
    return 'true'

@app.route('/juego', methods=['GET', 'POST'])
def juego():
  return render_template('./html/juego.html')

@app.route('/instrucciones', methods=['GET', 'POST'])
def instrucciones():
  return render_template('./html/instrucciones.html')

@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
  return render_template('./html/ranking.html')

@app.route('/sub_ranking', methods=['GET', 'POST'])
def devolverRanking():
  conn = sqlite3.connect('./BaseDeDatos/base_de_datos.db')
  lista = []
    
  q = """
        SELECT nombre, victorias
        FROM Jugadores
        ORDER BY victorias DESC
        LIMIT 10
      """

  resu = conn.execute(q)

  for fila in resu:
    lista.append(fila)

  conn.close()

  texto = '['
  i = 0
  while i < len(lista)-1:
    texto += '{"nombre": "' + lista[i][0] + '", "victorias": ' + str(lista[i][1]) + '}, '
    i += 1
  texto += '{"nombre": "' + lista[i][0] + '", "victorias": ' + str(lista[i][1]) + '}]'

  return json.dumps(texto)

@app.route('/creditos')
def creditos():
  return render_template('./html/creditos.html')


  
app.run(host='0.0.0.0', port=81)
