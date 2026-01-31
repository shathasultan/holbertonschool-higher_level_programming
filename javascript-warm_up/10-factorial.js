#!/usr/bin/node

const x = process.argv[2];

function factorial (n) {
  if (isNaN(parseInt(n)) || parseInt(n) === 0 || parseInt(n) === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(x));
