#!/usr/bin/node
const req = require('request');
const args = process.argv.slice(2);
const newDict = {};

async function myFunc () {
  for (let i = 1; i < 11; i++) {
    const url = `${args[0]}/?userId=${i}`;

    const getData = () => {
      return new Promise((resolve, reject) => {
        req(url, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body));
          }
        });
      });
    };

    try {
      const ans = await getData();
      const key = '' + i;
      newDict[key] = ans.filter(x => x.completed === true).length;
    } catch (err) {
      console.error(err);
    }
  }

  console.log(newDict);
}
myFunc();
