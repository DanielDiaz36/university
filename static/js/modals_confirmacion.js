function confirmation(msg_alerta, href) {

    swal({
        title: msg_alerta,
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Acept',
        cancelButtonText: 'Cancel',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        $.ajax({
            type: 'GET',
            url: href,
            success: function (response) {
                location.reload();
            },
            error: function (response) {
                console.log(response);
            }
        });
    });
}