var tblSede;

function cargarTabla() {
    tblSede = $('.table').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'accion': 'obtener_pruebas'},
            dataSrc: ""
        },
        columns: [
            {data: "id"},
            {data: "tipo_prueba"},
            {data: "tipo_licencia"},
            {data: null},
        ],
        columnDefs: [{
            "orderable": false,
            targets: [-1],
            class: 'text-center',
            render: function (data, type, row, meta) {
                var botones = '<a rel="editar" class="btn btn-warning" > Editar </a> ';
                botones += '<a rel="eliminar" class="btn btn-danger"> <i class="far fa-trash-alt"></i></a>';
                return botones;
            }
        }],
    })
};

$(function () {
    cargarTabla()

        //funcion para obtener el id del elemento y editarlo
        $('.table tbody').on('click', 'a[rel="editar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        $('input[name="accion"]').val('editar')
        $('input[name="id"]').val(data.id)
        $('input[name="tipo_prueba"]').val(data.tipo_prueba)
        $('input[name="tipo_licencia"]').val(data.tipo_licencia)
        $('#exampleModal').modal('show')
    });

    //funcion para obtener el id del elemento y eliminarlo
    $('.table tbody').on('click', 'a[rel="eliminar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        data = Object.assign(data, {'accion': 'eliminar'})

        var form = new FormData();
        for (var key in data) {
            form.append(key, data[key]);
        }

        var ruta_destino = window.location.pathname
        enviarConAjax(form, ruta_destino)
    })
});