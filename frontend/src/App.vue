<script setup>
import { ref, onMounted } from 'vue'

const apiMessage = ref('Loading connection to backend...')

// Fetch data from the Django container when the component loads
onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/test/')
    const data = await response.json()
    apiMessage.value = data.message
  } catch (error) {
    apiMessage.value = 'Failed to connect to backend server.'
    console.error(error)
  }
})
</script>

<template>
  <main style="display: grid; place-items: center; height: 100vh; font-family: sans-serif;">
    <div style="text-align: center; border: 2px solid #42b883; padding: 2rem; border-radius: 8px;">
      <h1 style="color: #42b883;">Vue 3 Frontend</h1>
      <p style="font-size: 1.2rem; color: #2c3e50; margin-top: 1rem;">
        Status: <strong>{{ apiMessage }}</strong>
      </p>
    </div>
  </main>
</template>

<style scoped></style>
