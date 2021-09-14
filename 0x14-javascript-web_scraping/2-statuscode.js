#!/usr/bin/nodejs
// returns status code using request method

const URL = process.argv[2];
const request = require('request');
request(URL, function (error, response, body) {
  if (error) return console.log(error);
  console.log('code:', response.statusCode);
});
