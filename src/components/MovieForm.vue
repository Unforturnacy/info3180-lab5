<template>
   
        <form action="POST" @submit.prevent="saveMovie" id = "movieForm" enctype="multipart/form-data">
      
              
                <label for="title" class="movie-title">Movie Title</label><br>
                <input type="text" name="title" class="movie-input" />
                <br>
                <label for="description" class="movie-title">Movie Description</label><br>
                <input type="text" name="description" class="description-input" />
                <br>
                <label for="poster"  class="movie-title">Movie Image</label><br>
                <input type="file" name="poster" id = "image-file" class="upload-button" />
                <br><br>
                <input type="submit" value="Submit" class ="submit-button">
           
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
 <style>
form {
 padding:10px;
 margin:20px;
}

.movie-title {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 10px;
}

.movie-input {
  padding: 10px;
  font-size: 16px;
  border: 2px solid #ccc;
  border-radius: 5px;
  width: 25%;
  margin-bottom: 20px;
}


.description-input {
  padding: 10px;
  font-size: 16px;
  border: 2px solid #ccc;
  border-radius: 5px;
  width: 45%;
  margin-bottom: 20px;
}


.upload-button {
  padding: 10px;
  background-color: DodgerBlue;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  margin-right: 10px;
}



.submit-button {
  padding: 10px;
  background-color: #008CBA;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

</style>