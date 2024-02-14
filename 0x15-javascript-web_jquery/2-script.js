$('document').ready(function(){
  $('DIV#red_header').css('cursor', 'pointer');
  $('DIV#red_header').click(function(){
    $('header').css('color', '#FF0000');
  });
});