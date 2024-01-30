#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');

req.get(args[0])
  .on('response', (res) => {
    console.log('code: ' + res.statusCode);
  });
