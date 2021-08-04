#!/usr/bin/nodejs
// defines a Rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const lavababy = this.width;
    this.width = this.height;
    this.height = lavababy;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
