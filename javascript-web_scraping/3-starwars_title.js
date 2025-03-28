#!/usr/bin/node

const request = require('request');

// Récupère l'ID de l'épisode depuis les arguments de la ligne de commande
const episodeId = process.argv[2];

// URL de l'API Star Wars
const url = `https://swapi-api.hbtn.io/api/films/${episodeId}/`;

// Effectue une requête GET sur l'API Star Wars pour récupérer les informations du film
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    // Parse la réponse JSON et affiche le titre du film
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    // Si le code de statut n'est pas 200, affiche une erreur
    console.log('Failed to fetch the movie title');
  }
});
