$('document').ready(function(){
function fun1() {
    $('header').addClass('red');
}

function fun2() {
    $('header').addClass('green');
}

$('DIV#toggle_header').click(function() {
    if ($('header').hasClass('green')){
        $('header').removeClass('green').addClass('red');
    }
    else{
        $('header').removeClass('red').addClass('green');
    }
});
});