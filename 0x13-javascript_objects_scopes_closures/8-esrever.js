#!/usr/bin/nodejs
// returns the reversed version of a list

exports.esrever = function (list) {
  const reversed = [];
  for (let idx = list.length; idx--;) {
    reversed.push(list[idx]);
  }
  return reversed;
};
