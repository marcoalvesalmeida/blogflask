$(function() {
  $('button#btnentrar').bind('click', function() {
    $.notify({
        message: "<b>Carregando...</b>"
    }, {
        type: 'warning',
        timer: 1000
    });
    $.getJSON($SCRIPT_ROOT + '/verifica_email', {
      email: $('input[name="email"]').val(),
      senha: $('input[name="senha"]').val()
    }, function(data) {
      if(data.result==1){
        $.notify({
            message: "<b>Sucesso...</b>"
        }, {
            type: 'success',
            timer: 1000
        });
      }
    });
    return false;
  });
});
