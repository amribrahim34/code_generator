<template>
  <div class="app-container">
    <AppHeader />
    <div class="main-content">
      <Sidebar />
      <main>
        <router-view></router-view>
      </main>
    </div>
    <AppFooter />
    <Toast />
    <ConfirmDialog />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AppHeader from "@/components/AppHeader.vue";
import Sidebar from "@/components/Sidebar.vue";
import AppFooter from "@/components/AppFooter.vue";

export default defineComponent({
  name: "App",
  components: {
    AppHeader,
    Sidebar,
    AppFooter,
  },
});
</script>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  display: flex;
  flex-grow: 1;
}

main {
  flex-grow: 1;
  padding: 20px;
}

/* Global styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

/* You can add more global styles here */
</style>
