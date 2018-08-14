$(document).ready(function() {
  // jQuery getJSON call
  $.getJSON("http://saad1.khashashin.com/api/v2/pages/3/?format=json", function(data){
    $.each(data, function(key, val){
      $('#mybody').append("<p>" + val + '</p>');
    });
  });
  // Handlebars
  var source = $("#entry-template").html();
  var template = Handlebars.compile(source);
  var context =   $.getJSON("http://saad1.khashashin.com/api/v2/pages/3/?format=json", function(data){
      $.each(data, function(key, val){
        $('#mybody').append("<p>" + val + '</p>');
      });
    });
  var context2 = {
    title: "Собаке Качалова",
    author: {
      id: 47,
      name: "Сергей Есенин"
    }
  };
  var html = template(context2);
  $("#mybody2").html(html);
});
