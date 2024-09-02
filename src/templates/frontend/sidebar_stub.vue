<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <img src="/logo.png" alt="Logo" class="logo" />
      <h2>[[ appName ]]</h2>
    </div>
    <nav>
      <ul>
        <li v-for="item in menuItems" :key="item.path">
          <router-link
            :to="item.path"
            class="sidebar-link"
            :class="{ active: isActive(item.path) }"
          >
            <i :class="item.icon"></i>
            <span>[[ item.name ]]</span>
          </router-link>
        </li>
      </ul>
    </nav>
    <div class="sidebar-footer">
      <button @click="logout" class="logout-button">
        <i class="pi pi-sign-out"></i>
        <span>Logout</span>
      </button>
    </div>
  </aside>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAuthStore } from "@/stores/authStore";

interface MenuItem {
  name: string;
  path: string;
  icon: string;
}

export default defineComponent({
  name: "Sidebar",
  setup() {
    const router = useRouter();
    const route = useRoute();
    const authStore = useAuthStore();

    const appName = import.meta.env.VITE_APP_NAME || "Admin Panel";

    const menuItems = ref<MenuItem[]>([
      { name: "Dashboard", path: "/dashboard", icon: "pi pi-home" },
      // Add more menu items here
      [[MENU_ITEMS]],
    ]);

    const isActive = (path: string) => route.path.startsWith(path);

    const logout = async () => {
      await authStore.logout();
      router.push("/login");
    };

    return {
      appName,
      menuItems,
      isActive,
      logout,
    };
  },
});
</script>

<style scoped>
/* ... (styles remain unchanged) ... */
</style>
