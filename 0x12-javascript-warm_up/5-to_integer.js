#!/usr/bin/node

// console.log a number

const { argv } = require('node:process');
const num = parseInt(argv[2]));
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
