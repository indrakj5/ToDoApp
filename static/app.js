$(document).ready(function () {
    $('#add-todo').click(function () {
        const todo_name = $('#todo').val();
        var that = this;
        $.post('/', { name: todo_name }, function (data) {
            $('.list-group').append(`
                <div class="list-group-item list-group-item-action d-flex gap-3 py-4" aria-current="true">
                    <div class="d-flex gap-2 w-100">
                        <h3 class="mb-0">${ data.name }</h3>
                    </div>
                    <i class="bi bi-circle text-success update-todo"
                        style="font-size: 25px; cursor: pointer;" class="" data-id="${ data.id }">
                    </i>
                    <i class="bi bi-x-circle text-danger delete-todo" style="font-size: 25px; cursor: pointer;"
                        data-id="${ data.id }">
                    </i>
                </div>
            `)
        })
    });

    $(document).on('click', '.update-todo', function () {
        const id = $(this).data('id');
        var that = this;
       
        $.ajax({
            url: `/update/${id}`,
            type: 'PUT',
            success: function(result) {
                if($(that).hasClass("bi-check-circle-fill")){
                    $(that).removeClass('bi-check-circle-fill');
                    $(that).addClass('bi-circle');
                } else {
                    $(that).removeClass('bi-circle');
                    $(that).addClass('bi-check-circle-fill');
                }
            }
        });
    });

    $(document).on('click', '.delete-todo', function () {
        var id = $(this).data('id');
        var that = this;
        $.ajax({
            url: `/delete/${id}`,
            type: 'DELETE',
            success: function(result) {
                $(that).closest('.list-group-item').remove();
            }
        });
    });
});