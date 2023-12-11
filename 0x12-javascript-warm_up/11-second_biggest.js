#!/usr/bin/node

// searching for the second biggest

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
  return;
}

let list = argv.slice(2, argv.length);

list.sort((a, b) => b - a);

console.log(list[1]);
