function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode < 48 || charCode > 57) {
        evt.preventDefault();
    }
}
