/**
 * Created by me on 07.02.17.
 */

$(function () {
    var checked = localStorage.getItem("checked") || "";
    checked = checked.split(",");
    console.log(checked);

    $('.check_me').each(function () {
        if ($.inArray(this.id, checked) !== -1)
            $(this).addClass("checked");
    }).click(function () {
        if ($(this).hasClass("checked")) {
            checked.splice($.inArray(this.id, checked), 1);
        } else {
            checked.push(this.id);
        }

        $(this).toggleClass("checked");

        localStorage.setItem("checked", checked.join(","));
    })
});