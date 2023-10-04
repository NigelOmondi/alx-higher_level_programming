// Use jQuery to make an AJAX GET request to SWAPI URL
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  // update the content of <div id="character"> element with chartacter name
  $('#character').text(data.name);
});
