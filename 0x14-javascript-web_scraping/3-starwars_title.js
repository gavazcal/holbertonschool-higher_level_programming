#!/usr/bin/nodejs
// prints the title of a Star Wars movie

const episode = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const request = require('request');
request(episode, function (error, message, body) {
  if (error) return console.log(error);
  const data = JSON.parse(body);
  console.log(data.title);
});
