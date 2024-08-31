<template>
  <div class="p-grid">
    <div class="p-col-12">
      <div class="card">
        <h1>{{ modelNamePlural }}</h1>
        <p-messages ref="messages" />

        <div class="p-d-flex p-jc-between p-mb-4">
          <div>
            <p-button
              label="Create"
              icon="pi pi-plus"
              class="p-button-success p-mr-2"
              @click="navigateToCreate"
            />
            <p-button
              label="Delete Selected"
              icon="pi pi-trash"
              class="p-button-danger"
              @click="confirmDeleteSelected"
              :disabled="!selectedItems.length"
            />
          </div>
          <div>
            <p-fileupload
              mode="basic"
              choose-label="Import CSV"
              :customUpload="true"
              @uploader="importCsv"
              :auto="true"
              accept=".csv"
            />
            <p-button
              label="Export CSV"
              icon="pi pi-download"
              class="p-button-help"
              @click="exportCsv"
            />
          </div>
        </div>

        <p-data-table
          :value="items"
          :loading="loading"
          v-model:selection="selectedItems"
          :paginator="true"
          :rows="10"
          :rowsPerPageOptions="[10, 20, 50]"
          :filters="filters"
          :globalFilterFields="globalFilterFields"
          dataKey="id"
          :lazy="true"
          :totalRecords="totalRecords"
          :rowsPerPageOptions="[10, 20, 50]"
          @page="onPage($event)"
          @sort="onSort($event)"
          @filter="onFilter($event)"
        >
          <template #header>
            <div class="p-d-flex p-jc-between">
              <p-input-text
                v-model="filters['global'].value"
                placeholder="Search..."
              />
            </div>
          </template>

          <template #empty>
            No {{ modelNamePlural.toLowerCase() }} found.
          </template>

          <template #loading>
            Loading {{ modelNamePlural.toLowerCase() }}... Please wait.
          </template>

          <p-column
            selectionMode="multiple"
            headerStyle="width: 3rem"
          ></p-column>

          <!-- Dynamic columns based on model attributes -->
          <p-column
            v-for="field in fields"
            :key="field"
            :field="field"
            :header="formatHeader(field)"
            sortable
            :filter-field="field"
          >
            <template #body="slotProps">
              {{ formatValue(slotProps.data[field]) }}
            </template>
          </p-column>

          <p-column
            header="Actions"
            :exportable="false"
            style="min-width: 8rem"
          >
            <template #body="slotProps">
              <p-button
                icon="pi pi-pencil"
                class="p-button-rounded p-button-success p-mr-2"
                @click="editItem(slotProps.data)"
              />
              <p-button
                icon="pi pi-trash"
                class="p-button-rounded p-button-warning"
                @click="confirmDeleteItem(slotProps.data)"
              />
            </template>
          </p-column>
        </p-data-table>
      </div>
    </div>

    <p-dialog
      v-model:visible="deleteItemDialog"
      header="Confirm Delete"
      :style="{ width: '450px' }"
    >
      <div class="confirmation-content">
        <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
        <span v-if="itemToDelete"
          >Are you sure you want to delete <b>{{ itemToDelete.name }}</b
          >?</span
        >
      </div>
      <template #footer>
        <p-button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteItemDialog = false"
        />
        <p-button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteItem"
        />
      </template>
    </p-dialog>

    <p-dialog
      v-model:visible="deleteItemsDialog"
      header="Confirm Delete"
      :style="{ width: '450px' }"
    >
      <div class="confirmation-content">
        <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
        <span
          >Are you sure you want to delete the selected
          {{ modelNamePlural.toLowerCase() }}?</span
        >
      </div>
      <template #footer>
        <p-button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteItemsDialog = false"
        />
        <p-button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteSelectedItems"
        />
      </template>
    </p-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { FilterMatchMode } from 'primevue/api';
import { use{{modelName}}Store } from '@/stores/{{modelName.toLowerCase()}}Store';
import { {{modelName}}, {{modelName}}ListParams } from '@/types/{{modelName.toLowerCase()}}Types';

export default defineComponent({
  name: '{{modelName}}List',
  setup() {
    const router = useRouter();
    const {{modelName.toLowerCase()}}Store = use{{modelName}}Store();

    const items = ref<{{modelName}}[]>([]);
    const selectedItems = ref<{{modelName}}[]>([]);
    const loading = ref(true);
    const totalRecords = ref(0);
    const itemToDelete = ref<{{modelName}} | null>(null);
    const deleteItemDialog = ref(false);
    const deleteItemsDialog = ref(false);
    const messages = ref();

    const modelName = '{{modelName}}';
    const modelNamePlural = '{{modelNamePlural}}';

    const fields = ['id', 'name', 'created_at', 'updated_at']; // Add or remove fields as needed
    const globalFilterFields = ['name']; // Add fields that should be included in global search

    const filters = ref({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    });

    const loadItems = async (params: {{modelName}}ListParams) => {
      try {
        loading.value = true;
        const result = await {{modelName.toLowerCase()}}Store.fetch{{modelNamePlural}}(params);
        items.value = result.data;
        totalRecords.value = result.total;
      } catch (error) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: 'Failed to load {{modelNamePlural.toLowerCase()}}', life: 3000 });
      } finally {
        loading.value = false;
      }
    };

    onMounted(() => {
      loadItems({ page: 1, limit: 10 });
    });

    const onPage = (event: any) => {
      loadItems({ page: event.page + 1, limit: event.rows });
    };

    const onSort = (event: any) => {
      loadItems({ sortField: event.sortField, sortOrder: event.sortOrder });
    };

    const onFilter = (event: any) => {
      loadItems({ filters: event.filters });
    };

    const navigateToCreate = () => {
      router.push({ name: 'Create{{modelName}}' });
    };

    const editItem = (item: {{modelName}}) => {
      router.push({ name: 'Edit{{modelName}}', params: { id: item.id } });
    };

    const confirmDeleteItem = (item: {{modelName}}) => {
      itemToDelete.value = item;
      deleteItemDialog.value = true;
    };

    const deleteItem = async () => {
      if (itemToDelete.value) {
        try {
          await {{modelName.toLowerCase()}}Store.delete{{modelName}}(itemToDelete.value.id);
          items.value = items.value.filter(item => item.id !== itemToDelete.value?.id);
          messages.value.add({ severity: 'success', summary: 'Success', detail: '{{modelName}} deleted', life: 3000 });
        } catch (error) {
          messages.value.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete {{modelName}}', life: 3000 });
        } finally {
          deleteItemDialog.value = false;
          itemToDelete.value = null;
        }
      }
    };

    const confirmDeleteSelected = () => {
      deleteItemsDialog.value = true;
    };

    const deleteSelectedItems = async () => {
      try {
        await {{modelName.toLowerCase()}}Store.deleteMulty{{modelNamePlural}}(selectedItems.value.map(item => item.id));
        items.value = items.value.filter(item => !selectedItems.value.includes(item));
        messages.value.add({ severity: 'success', summary: 'Success', detail: 'Selected {{modelNamePlural.toLowerCase()}} deleted', life: 3000 });
        selectedItems.value = [];
      } catch (error) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete selected {{modelNamePlural.toLowerCase()}}', life: 3000 });
      } finally {
        deleteItemsDialog.value = false;
      }
    };

    const importCsv = (event: any) => {
      const file = event.files[0];
      // Implement CSV import logic here
      console.log('Importing CSV:', file);
    };

    const exportCsv = () => {
      // Implement CSV export logic here
      console.log('Exporting to CSV');
    };

    const formatHeader = (header: string) => {
      return header.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
    };

    const formatValue = (value: any) => {
      if (value === null || value === undefined) return 'N/A';
      if (typeof value === 'boolean') return value ? 'Yes' : 'No';
      if (value instanceof Date) return value.toLocaleString();
      return value.toString();
    };

    return {
      items,
      selectedItems,
      loading,
      totalRecords,
      deleteItemDialog,
      deleteItemsDialog,
      itemToDelete,
      messages,
      modelName,
      modelNamePlural,
      fields,
      globalFilterFields,
      filters,
      onPage,
      onSort,
      onFilter,
      navigateToCreate,
      editItem,
      confirmDeleteItem,
      deleteItem,
      confirmDeleteSelected,
      deleteSelectedItems,
      importCsv,
      exportCsv,
      formatHeader,
      formatValue,
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
