// use jQuery to add a click event handler to div with ID 'toggle_header'
$('#toggle_header').click(function() {
  //Toggle the red and green classes of header when div is clicked
  $('header').toggleClass('red green');
});
