#!/usr/bin/node

// factorial recursive ooh nooo

const { argv } = require('node:process');

function factorial(a) {
	const num = parseInt(a);
	if (!(num) || num < 1) {
	  return (1);
	} else {
	    return (num * factorial(num - 1));
	}
}

console.log(factorial(argv[2]));
