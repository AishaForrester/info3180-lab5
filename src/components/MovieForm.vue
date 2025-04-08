<!-- This is where we have our reusable components such as our input field, forms, modals cards etc -->

<template>
    <!-- Success message -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Error messages -->
    <div v-if="errors.length" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">

    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input v-model="movie.title" type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea v-model="movie.description" name="description" class="form-control"></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input @change="handleFileUpload" type="file" name="poster" class="form-control"/>
    </div>

    <button type="submit" class="btn btn-primary">Upload Movie</button>
    </form>
</template>

<script setup>
import { ref, onMounted } from "vue";
let csrf_token = ref("");
let successMessage = ref("");
let errors = ref([]);

onMounted(() => {
 getCsrfToken();
});


function getCsrfToken() {
 fetch('/api/v1/csrf-token')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
 })
 }


const movie = ref({
    title: "",
    description: "",
    poster: null,
});

const handleFileUpload = (event) => {
  movie.value.poster = event.target.files[0];
};

const saveMovie = () => {   //the AJAX allows front-end to speak with backend without refreshing the page
  let movieForm = document.getElementById('movieForm')
  let form_data = new FormData(movieForm);
  

 fetch("/api/v1/movies", { //this is where we are sending the data to the flask api endpoint
  method: "POST",
  body: form_data,
  headers: {
    'X-CSRFToken':csrf_token.value
  }
 })
    .then(function(response) { //this is where we await a response from the endpoint
      return response.json().then(data => {
        if (response.ok) {
          successMessage.value = "Movie uploaded sucessfully!";
          errors.value = [];
          console.log(data);
        } else {
          successMessage.value = "";
          errors.value = data.errors || ["An error has occured. Please try again."];
          console.log(data);
        }
      }); //convert JSON string to json object that we can use
    })
    .catch(function(error) {
      successMessage.value = "";
      errors.value = ["Something went wrong. Please try again later"];
      console.log(errors);
    });

    
};
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
</style>