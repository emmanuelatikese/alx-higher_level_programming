#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  process.argv.length > 3 ? console.log('Arguments found') : console.log('Argument found');
}
