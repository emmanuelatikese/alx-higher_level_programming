#!/usr/bin/node

// factorial recursive ooh nooo

const { argv } = require('node:process');

function factorial(a) {
	if (!(a) || parseInt(a) <= 1) {
	  return (1);
	} else if (parseInt(a) && a.length <= 2) {
	  return (a * factorial(a - 1));
	} else {
	  return ('Infinity');
	}
}

console.log(factorial(argv[2]));
