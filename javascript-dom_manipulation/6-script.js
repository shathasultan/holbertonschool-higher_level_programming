/**
  * it fetches the name of a Star Wars character from an API
  * @returns {Promise<str>} a Promise that resolves to the name of the character
  */
const fetchName = () => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const name = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      return data.name;
    })
    .catch((error) => {
      // log the error to the console
      console.log(error);
      // Rethrow the error to be handled by the caller if needed
      throw error;
    });
  return name;
};
// Fetch the name and update the DOM element with id 'character'
fetchName()
  .then((name) => {
    const character = document.querySelector('#character');
    character.innerText = name;
    return name;
  });
