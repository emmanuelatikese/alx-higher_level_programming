#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const search = 'https://swapi-api.alx-tools.com/api/people/18/';

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const list = JSON.parse(body).results;
  const ans = list.filter(x => {
    const chr = x.characters;
    return chr.includes(search);
  });
  console.log(ans.length);
});
