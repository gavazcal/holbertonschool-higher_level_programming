#!/usr/bin/nodejs
// computes a factorial of x

const x = parseInt(process.argv[2]);

function factorial (x) {
  if (x === 0 || (isNaN(x))) {
    return 1;
  }
  return (x * factorial(x - 1));
}
console.log(factorial(x));
