#!/usr/bin/nodejs
// prints a message depending on the number of args passed

const argc = process.argv.length;
if (argc <= 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
