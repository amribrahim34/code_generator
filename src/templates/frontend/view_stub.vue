<template>
  <div :class="`[[MODEL_NAME_KEBAB]]-list`">
    <h1>{{ modelNamePluralPascal }}</h1>
    <div class="card">
      <Toolbar class="mb-4">
        <template #start>
          <Button
            label="New"
            icon="pi pi-plus"
            class="p-button-success mr-2"
            @click="openNew"
          />
          <Button
            label="Delete"
            icon="pi pi-trash"
            class="p-button-danger"
            @click="confirmDeleteSelected"
            :disabled="!selectedItems.length"
          />
        </template>
        <template #end>
          <FileUpload
            mode="basic"
            accept=".csv"
            chooseLabel="Import"
            class="mr-2 inline-block"
            :auto="true"
            @upload="importCSV"
          />
          <Button
            label="Export"
            icon="pi pi-upload"
            class="p-button-help"
            @click="exportCSV"
          />
        </template>
      </Toolbar>

      <DataTable
        :value="items"
        v-model:selection="selectedItems"
        dataKey="id"
        :paginator="true"
        :rows="10"
        :filters="filters"
        filterDisplay="menu"
        :loading="loading"
        :globalFilterFields="[[GLOBAL_FILTER_FIELDS]]"
        responsiveLayout="scroll"
      >
        <template #header>
          <div class="flex justify-content-between">
            <Button
              icon="pi pi-filter-slash"
              label="Clear"
              class="p-button-outlined"
              @click="clearFilter()"
            />
            <span class="p-input-icon-left">
              <i class="pi pi-search" />
              <InputText
                v-model="filters['global'].value"
                placeholder="Keyword Search"
              />
            </span>
          </div>
        </template>

        <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>

        [[TABLE_COLUMNS]]

        <Column headerStyle="width:4rem">
          <template #body="{ data }">
            <Button
              icon="pi pi-pencil"
              class="p-button-rounded p-button-success mr-2"
              @click="editItem(data)"
            />
            <Button
              icon="pi pi-trash"
              class="p-button-rounded p-button-warning"
              @click="confirmDeleteItem(data)"
            />
          </template>
        </Column>
      </DataTable>
    </div>

    [[DIALOG_COMPONENT]]
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue'
import { useToast } from 'primevue/usetoast'
import { FilterMatchMode } from 'primevue/api'
import { useStore } from '@/stores/[[MODEL_NAME_CAMEL]]Store'
import type { [[MODEL_NAME_PASCAL]] } from '@/types'
import { Toolbar } from 'primevue/toolbar'
import { Button } from 'primevue/button'
import { FileUpload } from 'primevue/fileupload'
import { DataTable } from 'primevue/datatable'
import { Column } from 'primevue/column'
import { InputText } from 'primevue/inputtext'
[[DIALOG_IMPORT]]

export default defineComponent({
  name: '[[MODEL_NAME_PASCAL]]List',
  components: {
    Toolbar,
    Button,
    FileUpload,
    DataTable,
    Column,
    InputText,
    [[DIALOG_COMPONENT_IMPORT]]
  },
  setup() {
    const toast = useToast()
    const store = useStore()

    const items = ref<[[MODEL_NAME_PASCAL]][]>([])
    const selectedItems = ref<[[MODEL_NAME_PASCAL]][]>([])
    const modelDialog = ref(false)
    const deleteModelDialog = ref(false)
    const deleteModelsDialog = ref(false)
    const item = ref<[[MODEL_NAME_PASCAL]] | null>(null)
    const submitted = ref(false)
    const loading = ref(false)

    const modelNamePascal = computed(() => '[[MODEL_NAME_PASCAL]]')
    const modelNameCamel = computed(() => '[[MODEL_NAME_CAMEL]]')
    const modelNamePluralPascal = computed(() => '[[MODEL_NAME_PLURAL_PASCAL]]')
    const modelNamePluralCamel = computed(() => '[[MODEL_NAME_PLURAL_CAMEL]]')
    const modelNameKebab = computed(() => '[[MODEL_NAME_KEBAB]]')

    const filters = ref({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    })

    onMounted(async () => {
      loading.value = true
      await store.fetch[[MODEL_NAME_PLURAL_PASCAL]]()
      items.value = store.[[MODEL_NAME_PLURAL_CAMEL]]
      loading.value = false
    })

    const openNew = () => {
      item.value = {} as [[MODEL_NAME_PASCAL]]
      submitted.value = false
      modelDialog.value = true
    }

    const editItem = (editItem: [[MODEL_NAME_PASCAL]]) => {
      item.value = { ...editItem }
      modelDialog.value = true
    }

    const confirmDeleteItem = (deleteItem: [[MODEL_NAME_PASCAL]]) => {
      item.value = deleteItem
      deleteModelDialog.value = true
    }

    const confirmDeleteSelected = () => {
      deleteModelsDialog.value = true
    }

    const deleteItem = async () => {
      if (item.value?.id) {
        await store.delete[[MODEL_NAME_PASCAL]](item.value.id)
        items.value = items.value.filter(i => i.id !== item.value?.id)
        deleteModelDialog.value = false
        toast.add({ severity: 'success', summary: 'Successful', detail: `${modelNamePascal.value} Deleted`, life: 3000 })
      }
    }

    const deleteSelectedItems = async () => {
      for (const item of selectedItems.value) {
        if (item.id) {
          await store.delete[[MODEL_NAME_PASCAL]](item.id)
        }
      }
      items.value = items.value.filter(val => !selectedItems.value.includes(val))
      deleteModelsDialog.value = false
      selectedItems.value = []
      toast.add({ severity: 'success', summary: 'Successful', detail: 'Items Deleted', life: 3000 })
    }

    const importCSV = (event: any) => {
      const file = event.files[0]
      const reader = new FileReader()
      reader.onload = (e) => {
        if (e.target) {
          const csv = e.target.result as string
          const data = csv.split('\n').map(row => row.split(','))
          // Process the CSV data and add items
          // This is a placeholder, you'll need to implement the actual import logic
          console.log(data)
        }
      }
      reader.readAsText(file)
    }

    const exportCSV = () => {
      // This is a placeholder, you'll need to implement the actual export logic
      console.log('Exporting CSV')
    }

    const clearFilter = () => {
      filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      }
    }

    return {
      items,
      selectedItems,
      modelDialog,
      deleteModelDialog,
      deleteModelsDialog,
      item,
      submitted,
      loading,
      filters,
      modelNamePascal,
      modelNameCamel,
      modelNamePluralPascal,
      modelNamePluralCamel,
      modelNameKebab,
      openNew,
      editItem,
      confirmDeleteItem,
      confirmDeleteSelected,
      deleteItem,
      deleteSelectedItems,
      importCSV,
      exportCSV,
      clearFilter
    }
  }
})
</script>
