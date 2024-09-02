<template>
  <div class="p-grid">
    <div class="p-col-12">
      <div class="card">
        <h1>{{ modelNamePascal }} Details</h1>
        <Messages ref="messages" />

        <div v-if="loading" class="p-d-flex p-jc-center">
          <ProgressSpinner />
        </div>

        <div v-else-if="error" class="p-d-flex p-jc-center">
          <Message severity="error" :content="error" />
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
            <Button
              label="Edit"
              icon="pi pi-pencil"
              class="p-button-primary p-mr-2"
              @click="navigateToEdit"
            />
            <Button
              label="Delete"
              icon="pi pi-trash"
              class="p-button-danger"
              @click="confirmDelete"
            />
          </div>
        </div>

        <div v-else class="p-d-flex p-jc-center">
          <Message severity="info" content="No data found" />
        </div>
      </div>
    </div>

    <Dialog
      v-model:visible="deleteDialogVisible"
      :header="`Confirm Delete ${modelNamePascal}`"
      :style="{ width: '350px' }"
    >
      <div class="p-m-0">
        Are you sure you want to delete this {{ modelNamePascal }}?
      </div>
      <template #footer>
        <Button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteDialogVisible = false"
        />
        <Button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteModel"
        />
      </template>
    </Dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from '@/stores/{{MODEL_NAME_CAMEL}}Store';
import type { {{MODEL_NAME_PASCAL}} } from '@/types';
import { Messages } from 'primevue/messages';
import { Message } from 'primevue/message';
import { ProgressSpinner } from 'primevue/progressspinner';
import { Dialog } from 'primevue/dialog';
import { Button } from 'primevue/button';

export default defineComponent({
  name: '{{MODEL_NAME_PASCAL}}Detail',
  components: {
    Messages,
    Message,
    ProgressSpinner,
    Dialog,
    Button,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();

    const modelData = ref<{{MODEL_NAME_PASCAL}} | null>(null);
    const loading = ref(true);
    const error = ref<string | null>(null);
    const deleteDialogVisible = ref(false);
    const messages = ref();

    const modelNamePascal = '{{MODEL_NAME_PASCAL}}';
    const modelNameCamel = '{{MODEL_NAME_CAMEL}}';
    const modelId = computed(() => route.params.id as string);

    onMounted(async () => {
      try {
        modelData.value = await store.fetch{{MODEL_NAME_PASCAL}}(modelId.value);
      } catch (err) {
        error.value = `Failed to load ${modelNameCamel} details`;
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
      router.push({ name: `Edit${modelNamePascal}`, params: { id: modelId.value } });
    };

    const confirmDelete = () => {
      deleteDialogVisible.value = true;
    };

    const deleteModel = async () => {
      try {
        await store.delete{{MODEL_NAME_PASCAL}}(modelId.value);
        messages.value.add({ severity: 'success', summary: 'Success', detail: `${modelNamePascal} deleted successfully`, life: 3000 });
        setTimeout(() => {
          router.push({ name: `List${modelNamePascal}` });
        }, 3000);
      } catch (err) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: `Failed to delete ${modelNamePascal}`, life: 3000 });
      } finally {
        deleteDialogVisible.value = false;
      }
    };

    return {
      modelNamePascal,
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
