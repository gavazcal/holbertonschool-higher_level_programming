#!/usr/bin/nodejs
// prints out star wars characters in order using Promise

const request = require('request');
const path = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function doRequest (checkpath) {
  return Promise((resolve, reject) => {
    request(checkpath, (error, response, body) => {
      if (response.statusCode === 200 && !error) {
        const data = JSON.parse(body);
        resolve(data.name);
      } else {
        reject(error);
      }
    });
  });
}

async function main (movie) {
  const cast = movie.characters;

  for (const characterdata of cast) {
    const result = await doRequest(characterdata);
    console.log(result);
  }
}

request(path, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const movie = JSON.parse(body);

  main(movie);
});
