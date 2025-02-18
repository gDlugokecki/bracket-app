<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useFetch } from '@vueuse/core'
import Spinner from '@/components/Spinner.vue'

const route = useRoute()
const id = route.params.id
const apiUrl = import.meta.env.VITE_API_URL

const { data, error, isFetching } = useFetch(apiUrl + '/tournament').json()
</script>

<template>
  <Spinner />
  Tournament123 {{ $route.params.id }} {{ id }}
  <div class="bg-" v-if="data">{{ data }}</div>
  <div v-if="error">Error: {{ error }}</div>
</template>
