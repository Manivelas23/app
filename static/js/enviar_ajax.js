function enviarConAjax(form, ruta_destino) {
    $.ajax({
        url: ruta_destino,
        type: 'POST',
        data: form,
        processData: false,
        contentType: false,
        cache: false,
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
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
}
