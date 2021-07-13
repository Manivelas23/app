// fomulario con ajax para guardar
function enviarConAjax(form, ruta, ruta_redirecion) {
    $(document).ready(function () {
        alert('hola')
        console.log('fnuainfa')
    });
    // $('form').on('submit', function (e) {
    //     e.preventDefault();
    //     var formdata = new FormData(this);
    //     var accion = formdata.get('accion');
    //
    //     if (accion == 'agregar') {
    //         $.ajax({
    //             url: ruta,
    //             type: 'POST',
    //             data: formdata,
    //             dataType: 'json'
    //         }).done(function (data) {
    //             if (!data.hasOwnProperty('error')) {
    //                 window.location.href = ruta_redirecion
    //                 return false;
    //             }
    //         }).fail(function (data) {
    //             console.log(data);
    //         }).always(function (data) {
    //         });
    //     }
    // });
}
