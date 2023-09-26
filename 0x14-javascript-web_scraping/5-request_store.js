#!/usr/bin/node


const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Content saved to ${fileName}`);
      }
    });
  } else {
    console.error(`Error: Unable to fetch webpage. Status code: ${response.statusCode}`);
  }
});
