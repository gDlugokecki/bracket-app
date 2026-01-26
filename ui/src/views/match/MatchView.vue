<script setup lang="ts">
import { useRoute } from 'vue-router'

import { useFetch } from '@vueuse/core'

const route = useRoute()
const id = route.params.id
const apiUrl = import.meta.env.VITE_API_URL

const { data, error } = useFetch(apiUrl + '/hello').json()
</script>

<template>
  MatchView {{ $route.params.id }} {{ id }}
  <div v-if="data">{{ data }}</div>
  <div v-if="error">Error: {{ error }}</div>
</template>
