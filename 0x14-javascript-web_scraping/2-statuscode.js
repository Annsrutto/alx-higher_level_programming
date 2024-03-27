#!/usr/bin/node

const request = require('request');

const GET = process.argv[2];

request(GET, (error, response) => {
  if (!error) {
    console.log('code: ', response.statusCode);
  }
});
