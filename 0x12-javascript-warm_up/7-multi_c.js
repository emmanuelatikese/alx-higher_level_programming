#!/usr/bin/node

// number of times to print

const { argv } = require('node:process');

if (parseInt(argv[2])) {
  let i = 0;
  const num = parseInt(argv[2]);
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
