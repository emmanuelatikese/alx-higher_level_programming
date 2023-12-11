#!/usr/bin/node

// searching for the second biggest

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {

  let list = argv.slice(2, argv.length).sort((a, b) => b - a);

  console.log(list[1]);
}
