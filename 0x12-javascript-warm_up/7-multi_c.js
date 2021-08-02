#!/usr/bin/nodejs
// prints a statement x amount of times

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurences');
} else {
  for (let idx = 1; idx <= arg; idx++) {
    console.log('C is fun');
  }
}
