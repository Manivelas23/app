function enviarConAjax(form, ruta_destino) {
for (var pair of form.entries()) {
    console.log(pair[0]+ ', ' + pair[1]);
}

    $.jAlert({
        'type': 'confirm',
        'title': 'Atencion!',
        'theme': 'blue',
        'confirmQuestion': `¿Desea ${form.get('accion')} el elemento?`,
        'confirmBtnText': 'SÍ',
        'denyBtnText': 'NO',
        'confirmAutofocus': 'confirmBtnText',
        'onConfirm': function () {
            $.ajax({
                url: ruta_destino,
                type: 'POST',
                data: form,
                processData: false,
                contentType: false,
                cache: false,
                dataType: 'json'
            }).done(function (data) {
                console.log(data.error)
                if (!data.hasOwnProperty('error')) {
                    tbl.destroy();
                    $('#exampleModal').modal('hide')
                    cargarTabla();
                } else {
                    $('.div-error').html(`
                    <div class="alert alert-warning alert-dismissible fade show" role="alert">
                         <strong>Error!</strong> ${data.error}
                          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                          </button>
                    </div>`)
                }
            }).fail(function (data) {
                alert(data)
            }).always(function (data) {
            });
        }, 'onDeny': function () {
        }
    });
}


