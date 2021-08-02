#!/usr/bin/nodejs
// prints a statement converted to int

const arg = parseInt(process.argv[2], 10);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
