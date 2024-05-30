$('document').ready(function() {
  const APIurl = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function() {
    $.get(APIurl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
