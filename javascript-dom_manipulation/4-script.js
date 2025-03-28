// Select the element with the id 'add_item'
document.getElementById("add_item").addEventListener("click", function () {
  // Select the <ul> element with the class 'my_list'
  const list = document.querySelector(".my_list");

  // Create a new <li> element
  const newItem = document.createElement("li");

  // Set the text content of the new <li> element
  newItem.textContent = "Item";

  // Append the new <li>
  list.appendChild(newItem);
});
