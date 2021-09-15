#!/usr/bin/nodejs
// returns number of tasks done by user id

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) return console.log(error);
  const data = JSON.parse(body);
  const done = {};
  let usercount;

  for (const count of data) {
    usercount = count.userId;
    if (count.done === true) {
      done[usercount] = (done[usercount] || 0) + 1;
    }
  }
  console.log(done);
});
