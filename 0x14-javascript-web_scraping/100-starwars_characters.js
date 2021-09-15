#!/usr/bin/nodejs
// prints out star wars characters

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
const path = URL + '/films';
const movienumber = process.argv[2] - 1;

request(path, (error, response, body) => {
  if (error || movienumber < 0) return console.log(error);

  const allfilmdata = JSON.parse(body);
  const specificfilmdata = allfilmdata.results[movienumber];
  const cast = specificfilmdata.characters;

  for (const character of cast) {
    request(character, (error, response, body) => {
      if (error) return console.log(error);
      const filmcast = JSON.parse(body);
      console.log(filmcast.name);
    });
  }
});
