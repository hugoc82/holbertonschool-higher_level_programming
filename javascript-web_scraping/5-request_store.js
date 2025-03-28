#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Récupérer les arguments de la ligne de commande
const url = process.argv[2];
const filePath = process.argv[3];

// Effectuer la requête GET vers l'URL
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  // Écrire le contenu dans le fichier
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    } else {
      console.log(`Content saved to ${filePath}`);
    }
  });
});
