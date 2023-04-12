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

<style>
.movies {
  display: grid;
  row-gap: 15px;
  grid-template-columns: auto auto;
  column-gap:0px;
  
  padding: 50px;
}
.movie  {
 
  font-size: 30px;
  text-align: center;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 10px 36px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px;
  height:270px;
  width:78%;

}

.movie img{
  width:53%;
  height:100%;
  float:left;
}

.movie h2{
  padding:2px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
  letter-spacing: 2px;
  color: #333;
  margin: 0 0 20px 0;
}

.movie p{
  font-size: 18px;
  text-align: center;
  line-height: 1.5;
  margin: 0 0 40px 0;
  padding:2px;
}
</style>



