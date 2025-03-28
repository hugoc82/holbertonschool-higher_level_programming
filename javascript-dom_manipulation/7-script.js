// Utilisation de Fetch pour récupérer les films depuis l'API
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json()) // Convertir la réponse en JSON
  .then((data) => {
    // Sélectionner l'élément avec l'id 'list_movies'
    const movieList = document.getElementById("list_movies");

    // Parcourir chaque film et ajouter son titre à la liste
    data.results.forEach((movie) => {
      // Créer un nouvel élément li
      const listItem = document.createElement("li");
      listItem.textContent = movie.title; // Ajouter le titre du film
      movieList.appendChild(listItem); // Ajouter l'élément li à la liste
    });
  })
  .catch((error) => {
    // En cas d'erreur, afficher un message dans la console
    console.log("Erreur:", error);
  });
