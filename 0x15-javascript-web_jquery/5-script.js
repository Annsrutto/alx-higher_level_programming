$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});
