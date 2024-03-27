#!/usr/bin/node

const request = require('request');

const endUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(endUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
