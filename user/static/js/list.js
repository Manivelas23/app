var tbl;

function cargarTabla() {
    tbl = $('.mydatatable').DataTable({
        responsive: true,
        autoWidth: true,
        destroy: false,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'accion': 'obtener_usuarios'},
            dataSrc: ""
        },
        columns: [
            {data: "id"},
            {data: "ubicacion"},
            {data: "cant_supervisores"},
            {data: "cant_computadoras"},
            {data: "activo"},
            {data: null},
        ],
        columnDefs: [{
            "orderable": false,
            targets: [-1],
            class: 'text-center',
            render: function (data, type, row, meta) {
                var botones = '<a rel="editar" class="btn bg-orange btn-xs text-white" >Modificar<span class="ml-1"></span><i class="far fa-edit"></i></a> ';
                botones += '<a rel="eliminar" class="btn btn-danger btn-xs"> <i class="far fa-trash-alt"></i></a>';
                return botones;
            }
        }],
    })
}

$(function () {
    cargarTabla();
});