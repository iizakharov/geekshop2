window.onload = function () {
    $(".basket_list").on("change", "input[type='number']", function (event) {
        var target = event.target;
        $.ajax({
            url: "/basket/update/" + target.name + "/" + target.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
    });
};