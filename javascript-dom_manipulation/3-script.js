const header = document.querySelector('header');
const headerSwitch = document.querySelector('#toggle_header');
headerSwitch.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
