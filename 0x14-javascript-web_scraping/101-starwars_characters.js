#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    const fetchCharacterData = (index) => {
      if (index >= charactersUrls.length) {
        return;
      }

      request(charactersUrls[index], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
          fetchCharacterData(index + 1);
        } else {
          console.error(`Error fetching character data: ${error}`);
        }
      });
    };

    fetchCharacterData(0);
  } else {
    console.error(`Error: Unable to fetch movie data. Status code: ${response.statusCode}`);
  }
});
