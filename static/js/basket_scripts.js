window.onload = function () {
    $(".basket_list").on("change", "input[type='number']", function (event) {
    // $(".basket_list input[type='number']").on("change", function (event) {
        var target = event.target;
        $.ajax({
            url: "/basket/update/" + target.name + "/" + target.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
    });
};