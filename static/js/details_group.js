function create_modal__details_group(group_id) {
    // $('.content_details_group').html('');

    var loading_div = $('.loading_div'),
        loading_html = '' +
        '<p class="loading_p" style="display: inline; padding-left: 45%;"></p>' +
        '<img class="loading_img" src="' + loading_div.data('img_url') + '" alt="">';

    loading_div.html(loading_html);

    $.ajax({
        type: 'get',
        data: {'group_id': group_id},
        url: '/groups/details/',
        success: function (result) {
            $('#name').text(result['name']);
            $('#professor_guide').text(result['professor_guide']);
            $('#is_deleted').text(result['is_deleted']);
            $('#created_by').text(result['created_by']);
            $('#created_at').text(result['created_at']);
            $('#updated_by').text(result['updated_by']);
            $('#updated_at').text(result['updated_at']);

            $('.loading_p').addClass('hidden_element');
            $('.loading_img').addClass('hidden_element');
        }
    });
}


function get_state_color(state) {
    if (state === 'Enable'){
        return 'enable';
    }
    else if (state === 'Disabled') {
        return 'disable';
    }
    return '';
}