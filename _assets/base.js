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
        if ($(this).hasClass("checked"))
            checked.push(this.id);
        else
            checked.splice($.inArray(this.id, checked), 1);

        $(this).toggleClass("checked");
        
        localStorage.setItem("checked", checked.join(","));
    })
});