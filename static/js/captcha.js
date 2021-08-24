$('.js-captcha-refresh').click(function () {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
});

// $('#id_captcha_1').attr("placeholder", gettext('Introduce the captcha.'));