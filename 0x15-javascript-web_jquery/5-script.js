// Use jQuery to add a click event handler to div with ID 'add item'
$('DIV#add_item').click(function() {
  // Append the new item to the UL with class 'my_list'
  $('ul.my_list').append('<li>Item</li>');
});
