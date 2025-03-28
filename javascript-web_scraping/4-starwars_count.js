#!/usr/bin/node

const request = require('request');

// Récupère l'URL de l'API depuis les arguments
const apiUrl = process.argv[2];

// ID de "Wedge Antilles"
const wedgeAntillesId = 18;

// Effectue une requête GET pour récupérer la liste des films
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    // Parse la réponse JSON
    const films = JSON.parse(body);
    
    // Filtrer les films où "Wedge Antilles" est présent
    let count = 0;

    // Vérifier chaque film et voir si Wedge Antilles (ID 18) est dans les personnages
    films.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    // Afficher le nombre de films où "Wedge Antilles" est présent
    console.log(count);
  } else {
    console.log('Error:', response.statusCode);
  }
});
