$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    },
    error: function () {
      $('#list_movies').text('Error fetching data');
    }
  });
});
