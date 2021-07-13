function enviarConAjax(form, ruta_destino, ruta_redirecion) {
    var accion = form.get('accion');
    if (accion == 'agregar') {
        $.ajax({
            url: ruta_destino,
            type: 'POST',
            data: form,
            processData: false,
            contentType: false,
            cache: false,
            dataType: 'json',
            enctype: 'multipart/form-data',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                window.location.href = ruta_redirecion
                return false;
            }
        }).fail(function (data) {
            alert(data)
        }).always(function (data) {
        });
    }
}
