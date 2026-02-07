/**
  * it fetches the list of Star Wars movies from the Star Wars API
  * @returns {Promise<str>} a promise that resolves to an array of movie titles
  */
const fetchMovieTitles = () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const movieTitles = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // parse and return an array of movie titles
      return data.results.map((e) => e.title);
    })
    .catch((error) => {
      // Log the error
      console.log(error);
      // Rethrow the error to be handled by the caller if needed
      throw error;
    });
  return movieTitles;
};
const createLi = (text) => {
  const li = document.createElement('li');
  if (text) {
    li.innerText = text;
  }
  return li;
};
// After fetching the movie titles, update the DOM element with id 'list_movies'
fetchMovieTitles()
  .then((movieTitles) => {
    const moviesList = document.querySelector('#list_movies');
    movieTitles.forEach((title) => {
      moviesList.appendChild(createLi(title));
    });
  });
