/**
  * It fetches the word "hello" in French from a remote API
  * @returns {Promise<str>} a promise that resolves to the value of hello
  */
const fetchHello = () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const hello = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // parse and return the hello
      return data.hello;
    })
    .catch((error) => {
      // Log the error
      console.log(error);
      // Rethrow the error to be handled by the caller if needed
      throw error;
    });
  return hello;
};
// After fetching the hello, update the DOM element with id 'hello'
document.addEventListener('DOMContentLoaded', () => {
  fetchHello()
    .then((hello) => {
      const helloBox = document.querySelector('#hello');
      helloBox.innerText = hello;
    });
});
