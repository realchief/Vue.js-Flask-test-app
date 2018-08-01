<template>
<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link to="/" class='navbar-item' style="margin-left: 10px;">
      <button class="button is-light">
        Test App
      </button>
    </router-link>
    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div class="navbar-menu">
    <div class="navbar-start">
      <router-link class="navbar-item" to="/">
        Home
      </router-link>
      <router-link class="navbar-item" to="/variations">
        Variations
      </router-link>
    </div>
  </div>
</nav>
</template>

<script>
  
</script>

<style lang="scss">
  
</style>