#!/usr/bin/node

const request = require('request');

// Récupère l'URL passée en argument
const url = process.argv[2];

// Effectue une requête GET sur l'URL
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    // Affiche le code de statut
    console.log(`code: ${response.statusCode}`);
  }
});
