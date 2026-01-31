#!/usr/bin/node

const x = process.argv[2];
let result = '';

if (isNaN(parseInt(x)) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      result = result + 'X';
    }
    console.log(result);
    result = '';
  }
}
