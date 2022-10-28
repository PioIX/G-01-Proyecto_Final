function modificarFormAction(pagina) {
  var form = document.getElementById('formMenu');

  form.setAttribute("action", pagina);
  form.submit();
}