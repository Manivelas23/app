var tbl;

function cargarTabla() {
    tbl = $('.table_template_table').DataTable({
        responsive: true,
        autoWidth: true,
        destroy: false,
        deferRender: true,
        fixedColumns: {
            heightMatch: 'none'
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'accion': 'obtener_fechas'},
            dataSrc: ""
        },
        columns: [
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
                return '<a rel="eliminar" class="btn btn-danger btn-xs"> <i class="far fa-trash-alt"></i></a>';
            }
        }],
    })
};


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
};

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


$(function () {
    cargarTabla()
});