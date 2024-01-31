#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
