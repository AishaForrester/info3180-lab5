<template>
  <div class="container mt-4">
    <h2>Movie Listings</h2>

    <div class="row">
      <div v-for="movie in movies" :key="movie.id" class="col-md-4 mb-3">
        <div class="card h-100">
          <img :src="movie.poster" class="card-img-top" alt="Movie Poster">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const movies = ref([]);

function fetchMovies() {
  fetch('/api/v1/movies')
    .then(response => response.json())
    .then(data => {
      movies.value = data.movies;
    })
    .catch(error => {
      console.error("Error fetching movies:", error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.card-img-top {
  height: 300px;
  object-fit: cover;
}
</style>
