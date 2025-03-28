// Select the element with the id 'update_header'
document.getElementById("update_header").addEventListener("click", function () {
  // Select the header element
  const header = document.querySelector("header");

  // Update the text
  header.textContent = "New Header!!!";
});
