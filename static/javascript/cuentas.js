function repeticionContraseña() {
  contraseña = document.getElementById('contraseña').value;
  contraseñaRepetida = document.getElementById('repetirContraseña').value;

  if(contraseña != contraseñaRepetida) {
    document.getElementById('contraseña').value = "";
    document.getElementById('repetirContraseña').value = "";
    alert("Las contraseñas no coinciden. Vuelve a intentarlo.")
  }
  else {
    verificarRegistro()
  }
}

function verificarRegistro() {
  var nombre = document.getElementById('nombre').value
  var contraseña = document.getElementById('contraseña').value

  console.log(nombre, contraseña)
  $.ajax({
    url:"/sub_registro",
    type:"POST",
    data:{nombre: nombre, contraseña: contraseña},
    success: function(response) {
      if(response == 'True') {
        form = document.getElementById('formRegistro');
        form.removeAttribute('action');
        form.setAttribute("action", "/inicio")
        form.submit()
      }
      else {
        alert("Ese nombre de usuario ya está en uso!");
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
}

function verificarLogin() {
  var nombre = document.getElementById('nombre').value
  var contraseña = document.getElementById('contraseña').value

  console.log(nombre, contraseña)
  $.ajax({
    url:"/sub_login",
    type:"POST",
    data:{nombre: nombre, contraseña: contraseña},
    success: function(response) {
      datos = JSON.parse(response);
      datos = JSON.parse(datos);
      if(datos['sesion'] == true) {
        form = document.getElementById('formLogin');
        form.removeAttribute('action');
        form.setAttribute("action", `${datos['action']}`);
        form.submit()
      }
      else {
        alert("Usuario y/o Contraseña incorrectos!");
      }
    },
    error: function(error) {
      console.log(error);
    }
  });
}