#!/usr/bin/node

if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])).replace(' ', ''));
  }
} else {
  console.log('Missing size');
}
