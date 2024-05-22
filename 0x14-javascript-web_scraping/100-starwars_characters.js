#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + filmId, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  for (const characterUrl of characterUrls) {
    request.get(characterUrl, function (error, response, characterBody) {
      if (error) {
        console.log(error);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  }
});
