#!/usr/bin/nodejs
// Defines a rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.width; idx++) {
      console.log('X'.repeat(this.height));
    }
  }
}

module.exports = Rectangle;
