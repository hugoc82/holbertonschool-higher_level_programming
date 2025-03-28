// Utilisation de Fetch pour récupérer le message "hello" en français depuis l'API
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => response.json()) // Convertir la réponse en JSON
  .then((data) => {
    // Sélectionner l'élément avec l'id 'hello' et y afficher le message
    document.getElementById("hello").textContent = data.hello;
  })
  .catch((error) => {
    // En cas d'erreur, afficher un message d'erreur dans la console
    console.log("Erreur:", error);
  });
