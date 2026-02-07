const createLi = (text) => {
  const li = document.createElement('li');
  if (text) {
    li.innerText = text;
  }
  return li;
};
const itemAddButton = document.querySelector('#add_item');
const list = document.querySelector('.my_list');
itemAddButton.addEventListener('click', () => {
  list.appendChild(createLi('Item'));
});
