#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.width; i++) {
      const str = ch.repeat(this.width).replace(' ', '');
      console.log(str);
    }
  }
}
module.exports = Square;
