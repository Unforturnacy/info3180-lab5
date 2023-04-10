<template>
   
        <form action="POST" @submit.prevent="saveMovie" id = "movieForm" enctype="multipart/form-data">
      
              
                <label for="title" class="form-label">Movie Title</label><br>
                <input type="text" name="title" class="formcontrol" />
                <br>
                <label for="description" class="form-label">Movie Description</label><br>
                <input type="text" name="description" class="formcontrol" />
                <br>
                <label for="poster"  class="form-label">Movie Image</label><br>
                <input type="file" name="poster" id = "image-file" class="formcontrol" />
                <br><br>
                <input type="submit" value="Submit">
           
        </form>
      

  </template>
  
  
  <script setup>
  import { ref, onMounted } from "vue";
onMounted(() => {
 getCsrfToken();
});
function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
 headers: {
 'X-CSRFToken': csrf_token.value
 }

    })
    .then(function (response) {
    return response.json();
    })
    .then(function (data) {
    // display a success message
    console.log(data);
    })
    .catch(function (error) {
    console.log(error);
    });
}




let csrf_token = ref("");
    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
 })
 }
  </script>