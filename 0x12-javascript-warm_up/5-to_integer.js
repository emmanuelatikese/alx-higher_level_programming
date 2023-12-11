#!/usr/bin/node

// console.log a number

const { argv } = require('node:process');

if (Number(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
