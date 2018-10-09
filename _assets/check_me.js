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
    });

    var eles = document.getElementsByClassName("show_solution");
    for (var i = 0; i < eles.length; i++) {
        var ele = eles[i];
        ele.onclick = function () {
            var parts = this.href.split("#");
            var e = document.getElementById(parts[1]);
            if (e.classList.contains("hidden")) {
                e.classList.remove("hidden");
                ele.innerHTML = "Lösung verstecken";
            } else {
                e.classList.add("hidden");
                ele.innerHTML = "Lösung anzeigen";
            }
        };
    }
});