$('document').ready(function(){
    $.ajax({
        url:"https://swapi-api.alx-tools.com/api/people/5/?format=json",
        type: "GET",
        dataType: "json"
    }).done (function(json){
        $('DIV#character').append(json.name);
    });

});