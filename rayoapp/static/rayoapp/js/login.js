// Formulario login desplegable

$(function() {
    var button = $('#loginButton');
    var box = $('#loginBox');
    var form = $('#loginForm');
    button.removeAttr('href');
    button.mouseup(function(login) {
        box.toggle();
        button.toggleClass('active');
    });
    form.mouseup(function() { 
        return false;
    });
    $(this).mouseup(function(login) {
        if(!($(login.target).parent('#loginButton').length > 0)) {
            button.removeClass('active');
            box.hide();
        }
    });
    
});

// Validaciones
$(document).ready(function () {

  'use strict';

  var usernameError = true,
      emailError    = true,
      passwordError = true,
      passConfirm   = true;


  if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
      $('.form form label').addClass('fontSwitch');
  }

  $('input').focus(function () {

      $(this).siblings('label').addClass('active');
  });


  $('input').blur(function () {

      // USUARIO
      if ($(this).hasClass('name')) {
          if ($(this).val().length === 0) {
              $(this).siblings('span.error').text('Por favor escriba su nombre completo').fadeIn().parent('.form-group').addClass('hasError');
              usernameError = true;
          } else if ($(this).val().length > 1 && $(this).val().length <= 4) {
              $(this).siblings('span.error').text('El largo minimo debe se de 4 caracteres').fadeIn().parent('.form-group').addClass('hasError');
              usernameError = true;
          } else {
              $(this).siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
              usernameError = false;
          }
      }
      // CORREO
      if ($(this).hasClass('email')) {
          if ($(this).val().length == '') {
              $(this).siblings('span.error').text('Por favor escriba su correo electronico').fadeIn().parent('.form-group').addClass('hasError');
              emailError = true;
          } else {
              $(this).siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
              emailError = false;
          }
      }

      // CLAVE
      if ($(this).hasClass('pass')) {
          if ($(this).val().length < 8) {
              $(this).siblings('span.error').text('El largo minimo debe se de 8 caracteres').fadeIn().parent('.form-group').addClass('hasError');
              passwordError = true;
          } else {
              $(this).siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
              passwordError = false;
          }
      }

      // CONFIRMAR CLAVE
      if ($('.pass').val() !== $('.passConfirm').val()) {
          $('.passConfirm').siblings('.error').text('Las claves no coinciden').fadeIn().parent('.form-group').addClass('hasError');
          passConfirm = false;
      } else {
          $('.passConfirm').siblings('.error').text('').fadeOut().parent('.form-group').removeClass('hasError');
          passConfirm = false;
      }

       if ($(this).val().length > 0) {
          $(this).siblings('label').addClass('active');
      } else {
          $(this).siblings('label').removeClass('active');
      }
  });


    // BOTON 
  $('form.signup-form').submit(function (event) {
      event.preventDefault();

      if (usernameError == true || emailError == true || passwordError == true || passConfirm == true) {
          $('.name, .email, .pass, .passConfirm').blur();
      } else {
          $('.signup, .login').addClass('switched');

          setTimeout(function () { $('.signup, .login').hide(); }, 700);
          setTimeout(function () { $('.brand').addClass('active'); }, 300);
          setTimeout(function () { $('.heading').addClass('active'); }, 600);
          setTimeout(function () { $('.form').hide(); }, 700);
      }
  });


});