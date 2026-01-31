#!/usr/bin/node

const x = process.argv[2];
const c = 'C is fun';

if (isNaN(parseInt(x)) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = parseInt(x); i > 0; i--) {
    console.log(c);
  }
}
