<template>
  <div class="p-grid">
    <div class="p-col-12">
      <div class="card">
        <h1>{{ [[MODEL_NAME_PLURAL_PASCAL]] }}</h1>
        <Messages ref="messages" />

        <div class="p-d-flex p-jc-between p-mb-4">
          <div>
            <Button
              label="Create"
              icon="pi pi-plus"
              class="p-button-success p-mr-2"
              @click="navigateToCreate"
            />
            <Button
              label="Delete Selected"
              icon="pi pi-trash"
              class="p-button-danger"
              @click="confirmDeleteSelected"
              :disabled="!selectedItems.length"
            />
          </div>
          <div>
            <FileUpload
              mode="basic"
              choose-label="Import CSV"
              :customUpload="true"
              @uploader="importCsv"
              :auto="true"
              accept=".csv"
            />
            <Button
              label="Export CSV"
              icon="pi pi-download"
              class="p-button-help"
              @click="exportCsv"
            />
          </div>
        </div>

        <DataTable
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
              <InputText
                v-model="filters['global'].value"
                placeholder="Search..."
              />
            </div>
          </template>

          <template #empty> No {{ modelNamePluralCamel }} found. </template>

          <template #loading>
            Loading {{ modelNamePluralCamel }}... Please wait.
          </template>

          <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>

          <!-- Dynamic columns based on model attributes -->
          <Column
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
          </Column>

          <Column header="Actions" :exportable="false" style="min-width: 8rem">
            <template #body="slotProps">
              <Button
                icon="pi pi-pencil"
                class="p-button-rounded p-button-success p-mr-2"
                @click="editItem(slotProps.data)"
              />
              <Button
                icon="pi pi-trash"
                class="p-button-rounded p-button-warning"
                @click="confirmDeleteItem(slotProps.data)"
              />
            </template>
          </Column>
        </DataTable>
      </div>
    </div>

    <Dialog
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
        <Button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteItemDialog = false"
        />
        <Button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteItem"
        />
      </template>
    </Dialog>

    <Dialog
      v-model:visible="deleteItemsDialog"
      header="Confirm Delete"
      :style="{ width: '450px' }"
    >
      <div class="confirmation-content">
        <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
        <span
          >Are you sure you want to delete the selected
          {{ modelNamePluralCamel }}?</span
        >
      </div>
      <template #footer>
        <Button
          label="No"
          icon="pi pi-times"
          class="p-button-text"
          @click="deleteItemsDialog = false"
        />
        <Button
          label="Yes"
          icon="pi pi-check"
          class="p-button-text"
          @click="deleteSelectedItems"
        />
      </template>
    </Dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { FilterMatchMode } from 'primevue/api';
import { useStore } from '@/stores/[[MODEL_NAME_CAMEL]]Store';
import type { [[MODEL_NAME_PASCAL]], [[MODEL_NAME_PASCAL]]ListParams } from '@/types';
import { DataTable } from 'primevue/datatable';
import { Column } from 'primevue/column';
import { Button } from 'primevue/button';
import { InputText } from 'primevue/inputtext';
import { Dialog } from 'primevue/dialog';
import { FileUpload } from 'primevue/fileupload';
import { Messages } from 'primevue/messages';

export default defineComponent({
  name: '[[MODEL_NAME_PASCAL]]List',
  components: {
    DataTable,
    Column,
    Button,
    InputText,
    Dialog,
    FileUpload,
    Messages,
  },
  setup() {
    const router = useRouter();
    const store = useStore();

    const items = ref<[[MODEL_NAME_PASCAL]][]>([]);
    const selectedItems = ref<[[MODEL_NAME_PASCAL]][]>([]);
    const loading = ref(true);
    const totalRecords = ref(0);
    const itemToDelete = ref<[[MODEL_NAME_PASCAL]] | null>(null);
    const deleteItemDialog = ref(false);
    const deleteItemsDialog = ref(false);
    const messages = ref();

    const modelNamePascal = '[[MODEL_NAME_PASCAL]]';
    const modelNameCamel = '[[MODEL_NAME_CAMEL]]';
    const modelNamePluralPascal = '[[MODEL_NAME_PLURAL_PASCAL]]';
    const modelNamePluralCamel = '[[MODEL_NAME_PLURAL_CAMEL]]';

    const fields = ['id', 'name', 'created_at', 'updated_at']; // Add or remove fields as needed
    const globalFilterFields = ['name']; // Add fields that should be included in global search

    const filters = ref({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    });

    const loadItems = async (params: [[MODEL_NAME_PASCAL]]ListParams) => {
      try {
        loading.value = true;
        const result = await store.fetch[[MODEL_NAME_PLURAL_PASCAL]](params);
        items.value = result.data;
        totalRecords.value = result.total;
      } catch (error) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: `Failed to load ${modelNamePluralCamel}`, life: 3000 });
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
      router.push({ name: `Create${modelNamePascal}` });
    };

    const editItem = (item: [[MODEL_NAME_PASCAL]]) => {
      router.push({ name: `Edit${modelNamePascal}`, params: { id: item.id } });
    };

    const confirmDeleteItem = (item: [[MODEL_NAME_PASCAL]]) => {
      itemToDelete.value = item;
      deleteItemDialog.value = true;
    };

    const deleteItem = async () => {
      if (itemToDelete.value) {
        try {
          await store.delete[[MODEL_NAME_PASCAL]](itemToDelete.value.id);
          items.value = items.value.filter(item => item.id !== itemToDelete.value?.id);
          messages.value.add({ severity: 'success', summary: 'Success', detail: `${modelNamePascal} deleted`, life: 3000 });
        } catch (error) {
          messages.value.add({ severity: 'error', summary: 'Error', detail: `Failed to delete ${modelNamePascal}`, life: 3000 });
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
        await store.deleteMultiple[[MODEL_NAME_PLURAL_PASCAL]](selectedItems.value.map(item => item.id));
        items.value = items.value.filter(item => !selectedItems.value.includes(item));
        messages.value.add({ severity: 'success', summary: 'Success', detail: `Selected ${modelNamePluralCamel} deleted`, life: 3000 });
        selectedItems.value = [];
      } catch (error) {
        messages.value.add({ severity: 'error', summary: 'Error', detail: `Failed to delete selected ${modelNamePluralCamel}`, life: 3000 });
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
      modelNamePascal,
      modelNameCamel,
      modelNamePluralPascal,
      modelNamePluralCamel,
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
