var tbl;

function cargarTabla() {
    tbl = $('.mydatatable').DataTable({
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
            data: {'accion': 'obtener_citas'},
            dataSrc: ""
        },
        columns: [
            {data: "id"},
            {data: "fecha_disponible"},
            {data: "numero_identificacion"},
            {data: "tipo_prueba"},
            {data: "tipo_licencia"},
            {data: "tipo_curso"},
            {data: "desc_curso"},
            {data: null},
        ],
        columnDefs: [{
            "orderable": false,
            targets: [-1],
            class: 'text-center',
            render: function (data, type, row, meta) {
                var botones = '<a rel="imprimir" class="btn bg-gradient-orange btn-xs" href="imprimir/' + row.id + '" target="_blank"> Imprimir<span class="ml-1"></span><i class="fas fa-print"></i></a> ';
                botones += '<a rel="eliminar" class="btn btn-danger btn-xs"> <i class="far fa-trash-alt"></i></a>';
                return botones;
            }
        }],
    })
}


function cargar_fechas() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {'accion': 'cargar-fechas-select'},
        dataType: 'json'
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            for (var i in data) {
                document.getElementById('select_fechas_citas').innerHTML += `
                 <option value="${data[i].id}">
                  ${data[i].fecha_disponible} 
                    ${data[i].tipo_prueba} 
                    ${data[i].tipo_licencia}
                    ${data[i].nomb_curso}
                    ${data[i].tipo_curso}
                    ${data[i].desc_curso}
                    ${data[i].ubicacion}`
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
    $('.table_template_table tbody').on('click', 'a[rel="eliminar"]', function () {
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
    $(".select2").select2({
        "theme": 'boostrap4'
    });

    eliminar_fecha();

})