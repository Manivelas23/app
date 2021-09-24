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
            data: {'accion': 'obtener_sedes'},
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
};

$(function () {
    cargarTabla();

    $('.mydatatable tbody').on('click', 'a[rel="editar"]', function () {
        var tr = tbl.cell($(this).closest('td, li')).index();
        var data = tbl.row(tr.row).data();
        $('input[name="accion"]').val('editar')
        $('input[name="id"]').val(data.id)
        $('input[name="ubicacion"]').val(data.ubicacion)
        $('input[name="cant_supervisores"]').val(data.cant_supervisores)
        $('input[name="cant_computadoras"]').val(data.cant_computadoras)
        $('select[name="activo"]').val(data.activo)
        $('#exampleModal').modal('show')
    });

    $('.mydatatable tbody').on('click', 'a[rel="eliminar"]', function () {
        var tr = tbl.cell($(this).closest('td, li')).index();
        var data = tbl.row(tr.row).data();
        data = Object.assign(data, {'accion': 'eliminar'})

        var form = new FormData();

        //agregar la accion del formulario al formdata
        for (var key in data) {
            form.append(key, data[key]);
        }

        var ruta_destino = window.location.pathname
        enviarConAjax(form, ruta_destino)

    })


    $('#exampleModal').on('hidden.bs.modal', function () {
        $(this).find('form').trigger('reset');
        $('.div-error').hide();
    })

});