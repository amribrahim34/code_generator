<template>
  <div class="p-grid">
    <div class="p-col-12">
      <div class="card">
        <h1>{{ modelName }} Details</h1>
        <p-messages ref="messages" />

        <div v-if="loading" class="p-d-flex p-jc-center">
          <p-progressspinner />
        </div>

        <div v-else-if="error" class="p-d-flex p-jc-center">
          <p-message severity="error" :content="error" />
        </div>

        <div v-else-if="modelData">
          <div
            v-for="(value, key) in modelData"
            :key="key"
            class="p-field p-grid"
          >
            <label :for="key" class="p-col-fixed" style="width: 200px">{{
              formatLabel(key)
            }}</label>
            <div class="p-col">
              <span :id="key">{{ formatValue(value) }}</span>
            </div>
          </div>

          <div class="p-d-flex p-jc-end p-mt-4">
            <p-button
              label="Edit"
              icon="pi pi-pencil"
              class="p-button-primary p-mr-2"
              @click="navigateToEdit"
            />
            <p-button
              label="Delete"
              icon="pi pi-trash"
              class="p-button-danger"
              @click="confirmDelete"
            />
          </div>
        </div>

        <div v-else class="p-d-flex p-jc-center">
          <p-message severity="info" content="No data found" />
        </div>
      </div>
    </div>

    <p-dialog
      v-model:visible="deleteDialogVisible"
      header="Confirm Delete"
      :style="{ width: '350px' }"
    >
      <div class="p-m-0">
        Are you sure you want to delete this {{ modelName }}?
      </div>
      <template #footer>
        <p-button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteDialogVisible = false"
        />
        <p-button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteModel"
        />
      </template>
    </p-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { use{{modelName}}Store } from '@/stores/{{modelName.toLowerCase()}}Store';
import { {{modelName}} } from '@/types/{{modelName.toLowerCase()}}Types';

export default defineComponent({
  name: '{{modelName}}Detail',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const {{modelName.toLowerCase()}}Store = use{{modelName}}Store();

    const modelData = ref<{{modelName}} | null>(null);
    const loading = ref(true);
    const error = ref<string | null>(null);
    const deleteDialogVisible = ref(false);
    const messages = ref();

    const modelName = '{{modelName}}';
    const modelId = computed(() => route.params.id as string);

    onMounted(async () => {
      try {
        modelData.value = await {{modelName.toLowerCase()}}Store.fetch{{modelName}}(modelId.value);
      } catch (err) {
        error.value = 'Failed to load {{modelName.toLowerCase()}} details';
      } finally {
        loading.value = false;
      }
    });

    const formatLabel = (key: string) => {
      return key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
    };

    const formatValue = (value: any) => {
      if (value === null || value === undefined) return 'N/A';
      if (typeof value === 'boolean') return value ? 'Yes' : 'No';
      if (value instanceof Date) return value.toLocaleString();
      return value.toString();
    };

    const navigateToEdit = () => {
      router.push({ name: 'Edit{{modelName}}', params: { id: modelId.value } });
    };

    const confirmDelete = () => {
      deleteDialogVisible.value = true;
    };

    const deleteModel = async () => {
      try {
        await {{modelName.toLowerCase()}}Store.delete{{modelName}}(modelId.value);
        messages.value.add({ severity: 'success', summary: 'Success', detail: '{{modelName}} deleted successfully', life: 3000 });
        setTimeout(() => {
          router.push({ name: 'List{{modelName}}' });
        }, 3000);
      } catch (err) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete {{modelName}}', life: 3000 });
      } finally {
        deleteDialogVisible.value = false;
      }
    };

    return {
      modelName,
      modelData,
      loading,
      error,
      deleteDialogVisible,
      messages,
      formatLabel,
      formatValue,
      navigateToEdit,
      confirmDelete,
      deleteModel,
    };
  },
});
</script>

<style scoped>
.card {
  padding: 2rem;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(0, 0, 0, 0.12);
  border-radius: 4px;
  margin-bottom: 2rem;
}
</style>
