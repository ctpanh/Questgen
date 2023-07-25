<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- component -->
  <header class="header sticky top-0 bg-white shadow-md flex items-center justify-between px-8 py-02">
    <!-- logo -->
    <h1 class="w-3/12">
      <RouterLink to="/">
        <svg viewBox="0 0 248 31" class="h-6 w-auto hover:text-green-500 duration-200">
          <path
            d="M25.517 0C18.712 0 14.46 3.382 12.758 10.146c2.552-3.382 5.529-4.65 8.931-3.805 1.941.482 3.329 1.882 4.864 3.432 2.502 2.524 5.398 5.445 11.722 5.445 6.804 0 11.057-3.382 12.758-10.145-2.551 3.382-5.528 4.65-8.93 3.804-1.942-.482-3.33-1.882-4.865-3.431C34.736 2.92 31.841 0 25.517 0zM12.758 15.218C5.954 15.218 1.701 18.6 0 25.364c2.552-3.382 5.529-4.65 8.93-3.805 1.942.482 3.33 1.882 4.865 3.432 2.502 2.524 5.397 5.445 11.722 5.445 6.804 0 11.057-3.381 12.758-10.145-2.552 3.382-5.529 4.65-8.931 3.805-1.941-.483-3.329-1.883-4.864-3.432-2.502-2.524-5.398-5.446-11.722-5.446z"
            fill="#22C55E"> </path>
        </svg>
      </RouterLink>
    </h1>
    <!-- navigation -->
    <nav class="nav font-semibold text-lg">
      <ul class="flex items-center">
        <li
          class="p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer active">
          <RouterLink to="/">Home</RouterLink>
        </li>
        <li
          class="p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer">
          <RouterLink to="/app">App</RouterLink>
        </li>
      </ul>
    </nav>

    <!-- buttons --->
    <div class="w-3/12 flex justify-end">
      <a href="">
        Account
      </a>
    </div>
  </header>
  <RouterView />
</template>
