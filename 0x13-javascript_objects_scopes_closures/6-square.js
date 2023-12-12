#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    const ch = c || 'X';
    for (let i = 0; i < this.width; i++) {
      const str = ch.repeat(this.width).replace(' ', '');
      console.log(str);
    }
  }
}
module.exports = Square;
