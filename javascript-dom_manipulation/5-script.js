const header = document.querySelector('header');
const headerUpdateButton = document.querySelector('#update_header');
headerUpdateButton.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});
