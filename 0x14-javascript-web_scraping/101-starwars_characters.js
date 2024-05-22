#!/usr/bin/node
const request = require('request');
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(filmUrl, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    fetchAndPrintCharacters(characterUrls, 0);
  }
});

function fetchAndPrintCharacters (characterUrls, index) {
  request(characterUrls[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characterUrls.length) {
        fetchAndPrintCharacters(characterUrls, index + 1);
      }
    }
  });
}
