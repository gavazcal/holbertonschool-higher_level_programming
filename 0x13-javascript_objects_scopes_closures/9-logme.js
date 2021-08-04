#!/usr/bin/nodejs
// prints the number of args already printed and the new arg value

let argc = 0;
exports.logMe = function (item) {
  console.log('%d: %s', argc, item);
  argc++;
};
