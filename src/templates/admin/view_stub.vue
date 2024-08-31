<template>
  <div class="{{MODEL_NAME_LOWERCASE}}-list">
    <h1>{{ MODEL_NAME_PLURAL }}</h1>
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
        :globalFilterFields="['{{GLOBAL_FILTER_FIELDS}}']"
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

        {{ TABLE_COLUMNS }}

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

    {{ DIALOG_COMPONENT }}
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useToast } from 'primevue/usetoast'
import { FilterMatchMode } from 'primevue/api'
import { use{{MODEL_NAME}}Store } from '@/stores/{{MODEL_NAME_LOWERCASE}}Store'
import { {{MODEL_NAME}} } from '@/types'
{{DIALOG_IMPORT}}

export default defineComponent({
  name: '{{MODEL_NAME}}List',
  components: { {{DIALOG_COMPONENT_IMPORT}} },
  setup() {
    const toast = useToast()
    const {{MODEL_NAME_LOWERCASE}}Store = use{{MODEL_NAME}}Store()

    const items = ref<{{MODEL_NAME}}[]>([])
    const selectedItems = ref<{{MODEL_NAME}}[]>([])
    const {{MODEL_NAME_LOWERCASE}}Dialog = ref(false)
    const delete{{MODEL_NAME}}Dialog = ref(false)
    const delete{{MODEL_NAME}}sDialog = ref(false)
    const item = ref<{{MODEL_NAME}} | null>(null)
    const submitted = ref(false)
    const loading = ref(false)

    const filters = ref({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    })

    onMounted(async () => {
      loading.value = true
      await {{MODEL_NAME_LOWERCASE}}Store.fetch{{MODEL_NAME_PLURAL}}()
      items.value = {{MODEL_NAME_LOWERCASE}}Store.{{MODEL_NAME_PLURAL_LOWERCASE}}
      loading.value = false
    })

    const openNew = () => {
      item.value = {} as {{MODEL_NAME}}
      submitted.value = false
      {{MODEL_NAME_LOWERCASE}}Dialog.value = true
    }

    const editItem = (editItem: {{MODEL_NAME}}) => {
      item.value = { ...editItem }
      {{MODEL_NAME_LOWERCASE}}Dialog.value = true
    }

    const confirmDeleteItem = (deleteItem: {{MODEL_NAME}}) => {
      item.value = deleteItem
      delete{{MODEL_NAME}}Dialog.value = true
    }

    const confirmDeleteSelected = () => {
      delete{{MODEL_NAME}}sDialog.value = true
    }

    const deleteItem = async () => {
      if (item.value && item.value.id) {
        await {{MODEL_NAME_LOWERCASE}}Store.delete{{MODEL_NAME}}(item.value.id)
        items.value = items.value.filter(i => i.id !== item.value?.id)
        delete{{MODEL_NAME}}Dialog.value = false
        toast.add({ severity: 'success', summary: 'Successful', detail: '{{MODEL_NAME}} Deleted', life: 3000 })
      }
    }

    const deleteSelectedItems = async () => {
      for (const item of selectedItems.value) {
        if (item.id) {
          await {{MODEL_NAME_LOWERCASE}}Store.delete{{MODEL_NAME}}(item.id)
        }
      }
      items.value = items.value.filter(val => !selectedItems.value.includes(val))
      delete{{MODEL_NAME}}sDialog.value = false
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
      {{MODEL_NAME_LOWERCASE}}Dialog,
      delete{{MODEL_NAME}}Dialog,
      delete{{MODEL_NAME}}sDialog,
      item,
      submitted,
      loading,
      filters,
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
