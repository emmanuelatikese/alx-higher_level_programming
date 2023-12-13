#!/usr/bin/node

process.argv.length <= 3 ? console.log(0) : console.log(process.argv.slice(2, process.argv.length).sort((a, b) => b - a)[1]);
