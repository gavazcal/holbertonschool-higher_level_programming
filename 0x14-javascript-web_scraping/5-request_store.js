#!/usr/bin/nodejs
// takes the content of a website and writes it to a file

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', error => {
    if (error) {
      console.error(error);
    }
  });
});
