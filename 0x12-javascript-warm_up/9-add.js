#!/usr/bin/nodejs
// prints the sum of 2 ints

function add (a, b) {
  return a + b;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
