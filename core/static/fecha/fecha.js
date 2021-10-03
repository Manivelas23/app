var tbl;

function cargarTabla() {
    tbl = $('#universal_datatable_table').DataTable({
        responsive: true,
        autoWidth: false,
        deferRender: true,
        "processing": true,
        "serverSide": true,
        "ajax": function (data, callback, settings) {
            var current_url = window.location.pathname;
            $.post(current_url, {
                    limite: data.length,
                    inicio: data.start,
                    filtro: data.search.value,
                    accion: "obtener_fechas"
                }, function (res) {
                    callback({
                        recordsTotal: res.length,
                        recordsFiltered: res.length,
                        data: res.fechas
                    })
                }
            )
        },
        'columns': [
            {data: "id"},
            {data: "fecha_disponible"},
            {data: "ubicacion"},
            {data: "tipo_prueba"},
            {data: "tipo_licencia"},
            {data: "nomb_curso"},
            {data: "tipo_curso"},
            {data: "desc_curso"},
            {data: null},
        ],
        columnDefs: [{
            "orderable": false,
            targets: [-1],
            class: 'text-center',
            render: function (data, type, row, meta) {
                var content = `
                    <div class="dropdown dropdown-acciones position-static">
                      <button class="btn" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                       <i class="fas fa-ellipsis-v"></i>
                      </button>
                      <div class="dropdown-menu position-absolute" aria-labelledby="dropdownMenuButton">
                       <button rel="eliminar" class="dropdown-item bg-danger"><i class="fas fa-minus-circle"></i> Eliminar</button> 
                      </div>
                    </div>`
                return content
            },
        }]
    })
}

function datetimepicker_settings() {
    $('#date_timepicker_start').datetimepicker({
        onShow: function () {
            this.setOptions({
                maxDate: $('#date_timepicker_end').val() ? $('#date_timepicker_end').val() : false
            })
        },
        timepicker: true
    });

    $('#date_timepicker_end').datetimepicker({
        onShow: function () {
            this.setOptions({
                minDate: $('#date_timepicker_start').val() ? $('#date_timepicker_start').val() : false
            })
        },
        timepicker: true
    });
};

function cargarSedes() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'accion': 'cargar_sedes'},
        dataType: 'json'
    }).done(function (data) {
        console.log(data.error)
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

function cargarPruebas() {
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

function eliminar_fecha() {
    $('.table_template_table tbody').on('click', 'button[rel="eliminar"]', function () {
        var tr = tbl.cell($(this).closest('td, li')).index();
        var data = tbl.row(tr.row).data();
        data = Object.assign(data, {'accion': 'eliminar'})

        var form = new FormData();
        for (var key in data) {
            form.append(key, data[key]);
        }

        var ruta_destino = window.location.pathname
        enviarConAjax(form, ruta_destino)
    });
}


$(function () {
    cargarTabla();
    eliminar_fecha();

})

