#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w > 0 ? w : undefined;
    this.height = h > 0 ? h : undefined;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const str = 'X'.repeat(this.width).replace(' ', '');
      console.log(str);
    }
  }
 
  rotate () {
    const t = this.width;
    this.width = this.height;
    this.height = t;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
