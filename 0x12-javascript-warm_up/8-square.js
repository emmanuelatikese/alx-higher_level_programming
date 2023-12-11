#!/usr/bin/node

// square things

const { argv } = require('node:process');

const num = parseInt(argv[2]);

if (num) {
  let i = 0;
  let str = '';
  while (i < num) {
    str = str + 'X';
    i++;
  }
  i = 0;
  while (i < num) {
    console.log(str);
    i++;
  }
} else {
  console.log('Missing size');
}
