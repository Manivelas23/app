export function cargar_sedes() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'accion': 'cargar_sedes'},
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            for (var i in data) {
                document.getElementById('sedes_container_fecha').innerHTML += `
                       <input type="checkbox" class="btn-check sedes-btn"
                            id="btncheck${data[i].id}" value="${data[i].id}" autocomplete="off">
                        <label class="btn btn-outline-primary" for="btncheck${data[i].id}"> ${data[i].ubicacion} </label>
                `
            }
        } else {
            alert("Ha ocurrido un Error")
        }
    }).fail(function (data) {
        alert(data)
    }).always(function (data) {
    });
}

export function seleccionar_sedes() {
    var activado = false
    $('#flexCheckDefault').on('click', function () {
        if (activado) {
            $(".btn-check").prop('disabled', false);
            $(".btn-check").prop('checked', false).parent().addClass('active');
            activado = false;
        } else {
            $(".btn-check").prop('disabled', true);
            $(".btn-check").prop('checked', true).parent().addClass('active');
            activado = true
        }
    });
    var reset_sedes = [$(".btn-check").prop('disabled', false), $(".btn-check").prop('checked', false).parent().addClass('active')]
    return reset_sedes;
}

export function obtener_sedes_seleccionadas() {
    var sedes_seleccinadas;
    $("form").submit(function (event) {
        event.preventDefault();
        sedes_seleccinadas = $('.sedes-btn:checkbox:checked');
        seleccionar_sedes();
    });
    return sedes_seleccinadas;
}

export function cargar_pruebas() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'accion': 'cargar_pruebas'},
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            for (var i in data) {
                document.getElementById('select_prueba_formFecha').innerHTML += `
                 <option value="${data[i].id}"> 
                    ${data[i].tipo_prueba} 
                    ${data[i].tipo_licencia}
                    ${data[i].nomb_curso}
                    ${data[i].tipo_curso}
                    ${data[i].desc_curso}`
            }
        } else {
            alert("Ha ocurrido un Error")
        }
    }).fail(function (data) {
        alert(data)
    }).always(function (data) {
    });
}


