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
        accion: 'eliminar_fecha',
        id_evento: id_evento
    }


    var form = new FormData();
    for (var key in data) {
        form.append(key, data[key]);
    }

    var ruta_destino = window.location.pathname
    enviarConAjax(form, ruta_destino)
}


function mostrar_calendario() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
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
        eventSources: [
            {
                url: window.location.pathname,
                format: 'json',
                method: 'POST',
                color: 'purple',
                extraParams: {
                    accion: 'cargar_fechas',
                },
                failure: function () {
                    alert('Ha ocurrido al cargar las fechas');
                },
            },
        ],
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


$(function () {
    mostrar_calendario();
});
