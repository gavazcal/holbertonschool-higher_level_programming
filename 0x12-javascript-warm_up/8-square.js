#!/usr/bin/nodejs
// prints a square

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let length = 1; length <= size; length++) {
    for (let width = 1; width <= size; width++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
