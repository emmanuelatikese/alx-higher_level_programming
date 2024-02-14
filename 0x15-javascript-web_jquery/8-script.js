$('document').ready(function(){
    $.ajax({
        url:'https://swapi-api.alx-tools.com/api/films/?format=json',
        dataType:'json',
        type:'GET',
    }).done(function(res){
        res.results.map(x => $('<li>').text(x.title).appendTo($('UL#list_movies')));
    })
});