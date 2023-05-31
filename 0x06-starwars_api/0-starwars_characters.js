#!/usr/bin/node
/* Prints all Casts of Star Wars movie
Read the README.md file for more info
*/

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/';
const endPoint = 'films/';
const movieID = process.argv[2].toString();

request(starWarsAPI + endPoint + movieID, function (error, _, body) {
  if (error) console.error(error);
  const objects = JSON.parse(body);
  const casts = objects.characters;
  Printresult(casts);
});

/* reculsively and synchronously request for each character
and prints out the casts */
function Printresult (casts, counter = 0) {
  request(casts[counter], function (error, _, body) {
    if (error) console.error(error);
    console.log(JSON.parse(body).name);
    if (++counter < casts.length) {
      Printresult(casts, counter++);
    }
  });
}
