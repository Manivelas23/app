var tblSede;

function cargarTabla() {
    tblSede = $('.mydatatable').DataTable({
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
            data: {'accion': 'obtener_pruebas'},
            dataSrc: ""
        },
        columns: [
            {data: "id"},
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
                var botones = '<a rel="editar" class="btn btn-info btn-xs" >Modificar<span class="ml-1"></span><i class="far fa-edit"></i></a> ';
                botones += '<a rel="eliminar" class="btn btn-danger btn-xs"> <i class="far fa-trash-alt"></i></a>';
                return botones;
            }
        }],
    })
};

$(function () {
    cargarTabla();

    //funcion para obtener el id del elemento y editarlo
    $('.mydatatable tbody').on('click', 'a[rel="editar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        $('input[name="accion"]').val('editar')
        $('input[name="id"]').val(data.id)
        $('select:hidden[name="id_curso"]').val(data.id_curso)
        $('input[name="tipo_prueba"]').val(data.tipo_prueba)
        $('input[name="nomb_curso"]').val(data.nomb_curso)
        $('input[name="tipo_curso"]').val(data.tipo_curso)
        $('input[name="desc_curso"]').val(data.desc_curso)
        $('#exampleModal').modal('show')
    });

    //funcion para obtener el id del elemento y eliminarlo
    $('.mydatatable tbody').on('click', 'a[rel="eliminar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        data = Object.assign(data, {'accion': 'eliminar'})

        var form = new FormData();
        for (var key in data) {
            form.append(key, data[key]);
        }

        var ruta_destino = window.location.pathname
        enviarConAjax(form, ruta_destino)
    });

    $('#exampleModal').on('hidden.bs.modal', function () {
        $(this).find('form').trigger('reset');
        $('.div-error').hide();
    })

});