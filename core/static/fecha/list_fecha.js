function limpiar_modal() {
    $("#successModal .modal-title").html();
    $("#successModal .modal-ul").html('');
}

function formatear_fecha(fecha) {
    moment.locale();
    moment.lang('es', {
        months: 'Enero_Febrero_Marzo_Abril_Mayo_Junio_Julio_Agosto_Septiembre_Octubre_Noviembre_Diciembre'.split('_'),
        monthsShort: 'Enero._Feb._Mar_Abr._May_Jun_Jul._Ago_Sept._Oct._Nov._Dec.'.split('_'),
        weekdays: 'Domingo_Lunes_Martes_Miercoles_Jueves_Viernes_Sabado'.split('_'),
        weekdaysShort: 'Dom._Lun._Mar._Mier._Jue._Vier._Sab.'.split('_'),
        weekdaysMin: 'Do_Lu_Ma_Mi_Ju_Vi_Sa'.split('_')
    });
    return moment(fecha).format('LLLL')
}

function rellenar_modal(obj_evento, fecha_modal) {
    ($("#successModal .modal-title").text(formatear_fecha(obj_evento.start)));
    $("#successModal .modal-ul").append(`
                            <li><strong class="text-primary">Id Fecha:</strong> ${obj_evento._def.publicId}</li>
                            <li><strong class="text-primary">Tipo de Prueba:</strong> ${obj_evento.title}</li>
                            <li><strong class="text-primary">Tipo de Licencia:</strong> ${obj_evento.extendedProps.LICENCIA}</li>
                            <li><strong class="text-primary">Ubicación:</strong> ${obj_evento.extendedProps.UBICACION}</li>
                            <li><strong class="text-primary">Curso:</strong> ${obj_evento.extendedProps.CURSO}</li>
                            <li><strong class="text-primary">Tipo de Curso:</strong> ${obj_evento.extendedProps.TIPO}</li>
                            <li><strong class="text-primary">Descripción del Curso:</strong> ${obj_evento.extendedProps.DESCRIPCION}</li>
    `);
}

function eliminar_fecha(id_evento) {
    data = {
        accion: 'eliminar',
        id_evento: id_evento
    }


    var form = new FormData();
    for (var key in data) {
        form.append(key, data[key]);
    }

    var ruta_destino = window.location.pathname
    enviarConAjax(form, ruta_destino)
}

function cargarPruebas() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'accion': 'cargar_pruebas'},
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            for (var i in data) {
                document.getElementById('select_prueba_Fecha').innerHTML += `
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

function cargarSedes() {
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

function seleccionar_sedes() {
    activado = false
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

function obtener_sedes() {
    var sedes_seleccinadas;
    $("form").submit(function (event) {
        event.preventDefault();
        sedes_seleccinadas = $('.sedes-btn:checkbox:checked');
        seleccionar_sedes();
    });
    return sedes_seleccinadas;
}

function mostrar_calendario(data) {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left: 'dayGridMonth,timeGridWeek,timeGridDay',
            center: 'title',
            right: 'prevYear,prev,next,nextYear'
        },
        eventTimeFormat: {
            hour: 'numeric',
            minute: '2-digit',
            meridiem: false
        },
        initialView: 'dayGridMonth',
        themeSystem: 'bootstrap',
        eventClick: function (info) {

            //obj data from backend
            var obj_evento = info.event;


            limpiar_modal()
            $("#successModal").modal("show");

            rellenar_modal(obj_evento, obj_evento.start);


            $('#successModal').on('click', 'button[rel="eliminar"]', function () {
                eliminar_fecha(obj_evento._def.publicId)
            });

            $('#successModal').on('click', 'button[rel="cerrar_modal"]', function () {
                $("#successModal").modal("hide");
            });

            $('#successModal').on('click', 'button[rel="cerrar_modal_btn"]', function () {
                $("#successModal").modal("hide");
            });

        },
        // eventSources: [
        //     {
        //         url: window.location.pathname,
        //         format: 'json',
        //         method: 'POST',
        //         color: 'blue',
        //         backgroundColor: 'lightblue',
        //         extraParams: {
        //             accion: 'cargar_fechas',
        //         },
        //         failure: function () {
        //             alert('Ha ocurrido al cargar las fechas');
        //         },
        //     },
        // ],
        events: data,
        loading: function (isLoading) {
            if (isLoading) {
                $('#loading').show();
            } else {
                $('#loading').hide();
            }
        },
        locale: 'cr',
    })
    calendar.render();
}

function filtrar_fechas_ajax(form, ruta_destino) {
    $.ajax(
        {
            url: ruta_destino,
            type: "POST",
            data: form,
            processData: false,
            contentType: false,
            cache: false,
            dataType: 'json'
        }).done(function (data) {
        mostrar_calendario(data)
        console.log(data)
    })
        .fail(function (data) {
            alert("error");
        })
}

$(function () {
    cargarPruebas();
    cargarSedes();
    seleccionar_sedes();
});
