<script setup>
    import { ref, onMounted } from "vue";
    let movies = ref([]);

    async function fetchMovies() {
    try {
        const response = await fetch('/api/v1/movies')
        const data = await response.json()
        movies.value = data.movies
 
    } catch (error) {
        console.error(error)
    }
}

onMounted(fetchMovies)
</script>

<template>
    <div class="movies">
    <div class="movie" v-for="movie in movies" :key="movie.id">
      <img :src="movie.poster" alt="Movie poster" />
      <h2>{{ movie.title }}</h2>
      <p>{{ movie.description }}</p>
    </div>
  </div>
</template>

