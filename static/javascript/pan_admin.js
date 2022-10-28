function completarSelect(jugadores, sel) {
  var select = document.getElementById(sel);
  if(select.innerHTML == '') {
    for(let i = 0 ; i < jugadores.length ; i++) {
    select.innerHTML +=
    `
    <option value='${jugadores[i]}'>${jugadores[i]}</option>
    `
    }
  }
}

function devolverJugador() {
  var jug = document.getElementById('devolver').value
  
  $.ajax({
    url: "/recepcionAjax",
    type: "GET",
    success: function(response) {
      datos = JSON.parse(response);
      datos = JSON.parse(datos);
      for(let i = 0 ; i < datos.length ; i++) {
        if(datos[i]['nombre'] == jug) {
          console.log(`Información del jugador:\n
id: ${datos[i]['id']}\n
nombre: ${datos[i]['nombre']}\n
contraseña: ${datos[i]['contraseña']}\n
victorias: ${datos[i]['victorias']}\n\n`)
        }
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
}

function modificarJugador() {
  var jug = document.getElementById('modificar').value;
  var vic = document.getElementById('modVictorias').value;
  
  $.ajax({
    url: "/recepcionAjax",
    type: "PUT",
    data: {nomModificar: jug, modVictorias: vic},
    success: function(response) {
      alert(`El nuevo valor de victorias del jugador '${jug}' ahora ha pasado a ser: '${vic}'`);
    },
    error: function(response) {
      console.log(error)
    }
  });
}

function borrarJugador() {
  var jug = document.getElementById('borrar').value;
  
  $.ajax({
    url: "/recepcionAjax",
    type: "DELETE",
    data: {nomBorrar: jug},
    success: function(response) {
      alert(`El jugador '${jug}' ha sido borrado correctamente`);
      location.reload(true);
    },
    error: function(error) {
      console.log(error);
    }
  });
}
