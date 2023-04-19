/* Función para validar que los correos electrónicos coincidan */
function validarEmails() {
    var email = document.getElementById("email").value;
    var confirmEmail = document.getElementById("confirm-email").value;
  
    if (email != confirmEmail) {
      alert("Los correos electrónicos no coinciden.");
      return false;
    } else {
      return true;
    }
  }
  
  /* Función para validar que las contraseñas coincidan */
  function validarContraseñas() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
  
    if (password != confirmPassword) {
      alert("Las contraseñas no coinciden.");
      return false;
    } else {
      return true;
    }
  }
  
  /* Función para validar el formulario completo */
  function validarFormulario() {
    var form = document.getElementsByTagName("form")[0];
  
    if (form.checkValidity() == false) {
      alert("Por favor, complete todos los campos requeridos.");
      return false;
    } else if (validarEmails() == false) {
      return false;
    } else if (validarContraseñas() == false) {
      return false;
    } else {
      return true;
    }
  }
  
  /* Evento que se ejecuta cuando se envía el formulario */
  var form = document.getElementsByTagName("form")[0];
  form.addEventListener("submit", function(event) {
    event.preventDefault();
    if (validarFormulario() == true) {
      form.submit();
    }
  });
  