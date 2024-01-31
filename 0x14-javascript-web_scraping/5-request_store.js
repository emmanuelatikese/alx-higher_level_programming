#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const args = process.argv.slice(2);

req(args[0], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(args[1], body, err => {
    if (err) {
      console.log(err);
    }
  });
});
