#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size);
    this.size_ = size;
  }

  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.size_; i++) {
      const str = ch.repeat(this.size_).replace(' ', '');
      console.log(str);
    }
  }
}
module.exports = Square;
