function confirmacion_eliminar(id) {
    var btn_eliminar = $('#btn_eliminar_' + id);

    swal({
        title: btn_eliminar.data('text'),
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        $.ajax({
            type: 'GET',
            url: btn_eliminar.data('href'),
            success: function (response) {
                location.reload();
                // if (response.redirect_to) {
                //     window.location.replace('../../');
                // } else {
                //     location.reload(true);
                // }
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
}

function confirmacion(msg_alerta, href) {

    swal({
        title: msg_alerta,
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        $.ajax({
            type: 'GET',
            url: href,
            success: function (response) {
                location.reload();
                // if (response.redirect_to) {
                //     window.location.replace('../../');
                // } else {
                //     location.reload(true);
                // }
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
}