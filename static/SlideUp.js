$(document).ready(function() {
    $('#MainMenu > li').click(function (e) {
        e.stopPropagation();
        var $el = $('ul', this);
        $('#MainMenu > li > ul').not($el).slideUp();
        $el.stop(true, true).slideToggle(400);
    });
    $("#MainMenu > li > ul > li").click(function (e) {
        e.stopImmediatePropagation();
    });
});