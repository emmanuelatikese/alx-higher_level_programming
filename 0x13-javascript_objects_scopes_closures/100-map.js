#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
let count = -1;
const l = list.map(x => {
  count++;
  return count * x;
});

console.log(l);
