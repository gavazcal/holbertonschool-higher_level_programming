#!/usr/bin/nodejs
// returns the number of occurrences

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      occur++;
    }
  }
  return occur;
};
