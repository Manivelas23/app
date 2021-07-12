$(function () {
    $(document).ready(function () {
        $('.table').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {},
                dataSrc: ""
            },
            columns: [
                {data: "id"},
                {data: "ubicacion"},
                {data: null},
            ],
            columnDefs: [{
                "orderable": false,
                targets:[-1],
                class: 'text-center',
                render: function (data, type, row,meta) {
                        var botones = '<button type="button" id="editarBtn" class="btn btn-warning" > Editar </button> ';
                    botones += '<button type="button" id="borrarBtn" class="btn btn-danger"> <i class="far fa-trash-alt"></i></button>';
                    return botones;
                }
            }],
        })
    });
});
