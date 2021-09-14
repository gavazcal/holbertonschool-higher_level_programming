#!/usr/bin/nodejs
// writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf8', function (err) {
  if (err) return console.log(err);
  console.log('string > file');
});
