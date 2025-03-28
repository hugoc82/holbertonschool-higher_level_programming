// Utilisation de Fetch pour récupérer les données depuis l'API
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => response.json()) // Convertir la réponse en JSON
  .then((data) => {
    // Sélectionner l'élément avec l'id 'character' et y ajouter le nom
    document.getElementById("character").textContent = data.name;
  })
  .catch((error) => {
    // Si une erreur se produit, afficher un message dans la console
    console.log("Erreur :", error);
  });
