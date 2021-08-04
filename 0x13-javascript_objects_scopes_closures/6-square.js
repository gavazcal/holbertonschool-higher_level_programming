#!/usr/bin/nodejs
// defines a Square class that inherits from the previous class

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
