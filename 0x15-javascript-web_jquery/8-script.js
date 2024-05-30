$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movieTitles = data.results.map(movie => `<li>${movie.title}</li>`);
    $('UL#list_movies').append(movieTitles.join(''));
});
