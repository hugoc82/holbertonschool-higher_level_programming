// Importation du module fs
const fs = require('fs');

// Récupérer le chemin du fichier depuis les arguments
const filePath = process.argv[2];

// Lire le fichier en UTF-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
