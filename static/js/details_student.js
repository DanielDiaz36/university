function create_modal__details_student(student_id) {

    var loading_div = $('.loading_div'),
        loading_html = '' +
        '<p class="loading_p" style="display: inline; padding-left: 45%;"></p>' +
        '<img class="loading_img" src="' + loading_div.data('img_url') + '" alt="">';

    loading_div.html(loading_html);

    $.ajax({
        type: 'get',
        data: {'student_id': student_id},
        url: $('.content_details_student').data('url'),
        success: function (result) {
            $('#name').text(result['name']);
            $('#age').text(result['age']);
            $('#gender').text(result['gender']);
            $('#email').text(result['email']);
            $('#date_birthday').text(result['date_birthday']);
            $('#city_birthday').text(result['city_birthday']);
            $('#group').text(result['group']);
            $('#is_active').text(result['is_active']);
            $('#created_by').text(result['created_by']);
            $('#created_at').text(result['created_at']);
            $('#updated_by').text(result['updated_by']);
            $('#updated_at').text(result['updated_at']);

            $('.loading_p').addClass('hidden_element');
            $('.loading_img').addClass('hidden_element');
        }
    });
}
