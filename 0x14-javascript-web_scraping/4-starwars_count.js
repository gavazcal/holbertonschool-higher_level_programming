#!/usr/bin/nodejs
// Prints out the number of Star Wars films containing a character

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) return console.log(error);
  const data = JSON.parse(body);
  const films = data.results;
  let filmcount = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.slice(-4) === '/18/') {
        filmcount += 1;
      }
    }
  }
  console.log(filmcount);
});
