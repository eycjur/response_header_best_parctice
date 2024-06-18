<script setup lang="ts">
import { ref } from 'vue'

const backendApiUrl = "http://localhost:8080"

const newTodo = ref("")
const todos = ref(Array<string>())

const getTodos = async () => {
  const response = await fetch(`${backendApiUrl}/todos`)
  todos.value =  await response.json()
}
getTodos()

const addTodo = async () => {
  if (newTodo.value.trim() === "") return
  const response = await fetch(`${backendApiUrl}/todos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      todo: newTodo.value
    }),
  })
  if (!response.ok) {
    console.error("Failed to add todo")
    return
  }
  todos.value.push(newTodo.value)
  newTodo.value = ""
}

</script>

<template>
  <h1>ToDos</h1>
  <div v-for="todo in todos">
    <span>{{ todo }}</span>
  </div>
  <div>
    <input type="text" v-model="newTodo" />
    <button @click="addTodo">Add</button>
  </div>
</template>
