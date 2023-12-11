#!/usr/bin/node
// working on argv

const { argv } = require('node:process');
let count = 0;

argv.map(x => count++);

if (count === 2) {
  console.log('No argument');
} else {
  const list = argv.slice(2, count);
  list.forEach(x => console.log(x));
}
