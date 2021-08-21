function enviarConAjax(form, ruta_destino) {
    for ([key, value] of form.entries()) {
        console.log(key, value);
    }
    console.log(ruta_destino)
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
                    cargarTabla();
                    $('#exampleModal').modal('hide')

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


