#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.ch = c !== undefined ? c : 'X';
    for (let i = 0; i < this.height; i++) {
      const str = (this.ch).repeat(this.width).replace(' ', '');
      console.log(str);
    }
  }
}
module.exports = Square;
