// script.js

document.getElementById("upload-form").addEventListener("submit", (event) => {
  event.preventDefault(); // prevent the form from reloading the page
  // check if a file has been selected
  if (document.getElementById("image-upload").files.length === 0) {
    // no file has been selected
    return;
  }
  // get the selected file
  const file = document.getElementById("image-upload").files[0];
  // create a new FormData object to send the file to the server
  const formData = new FormData();
  formData.append("file", file);
  
  // send the file to the server
  fetch("http://127.0.0.1:8080/predict", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    // get the search results container
    const searchResults = document.getElementById("search-results");
    // clear the existing search results
    searchResults.innerHTML = "";

    // get the template for the search results
    const template = document.getElementById("result-template");

    // loop through the image_urls and create an HTML element for each image
    data.image_urls.forEach(image_url => {
        // clone the template
        const result = template.content.cloneNode(true);

        // set the src of the image element
        result.querySelector(".result-image").src = image_url;

        // append the result to the search results div
        searchResults.appendChild(result);
    });
  })
  .catch(error => {
    console.error(error);
  });
});