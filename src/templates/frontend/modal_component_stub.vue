<template>
  <Dialog
    :visible="modelValue"
    :style="{ width: '450px' }"
    :header="dialogTitle"
    :modal="true"
    class="p-fluid"
    :closable="false"
    @update:visible="updateVisible"
  >
    [% for field in FORM_FIELDS %]
    <div class="p-field">
      <label :for="[[field.name]]">[[field.label]]</label>
      [% if field.type == 'text' or field.type == 'number' %]
      <InputText
        :id="[[field.name]]"
        v-model.trim="v$.item.[[field.name]].$model"
        :required="[[field.required]]"
        [%
        if
        loop.first
        %]autofocus[%
        endif
        %]
        :class="{ 'p-invalid': v$.item.[[field.name]].$invalid && submitted }"
      />
      [% elif field.type == 'textarea' %]
      <Textarea
        :id="[[field.name]]"
        v-model.trim="v$.item.[[field.name]].$model"
        :required="[[field.required]]"
        :class="{ 'p-invalid': v$.item.[[field.name]].$invalid && submitted }"
      />
      [% elif field.type == 'checkbox' %]
      <Checkbox
        :id="[[field.name]]"
        v-model="v$.item.[[field.name]].$model"
        :binary="true"
      />
      [% elif field.type == 'date' or field.type == 'datetime' %]
      <Calendar
        :id="[[field.name]]"
        v-model="v$.item.[[field.name]].$model"
        :showTime="[[field.type == 'datetime']]"
        :dateFormat="[[field.format]]"
        :required="[[field.required]]"
        :class="{ 'p-invalid': v$.item.[[field.name]].$invalid && submitted }"
      />
      [% elif field.type == 'select' %]
      <Dropdown
        :id="[[field.name]]"
        v-model="v$.item.[[field.name]].$model"
        :options="[[field.options]]"
        optionLabel="label"
        optionValue="value"
        :required="[[field.required]]"
        :class="{ 'p-invalid': v$.item.[[field.name]].$invalid && submitted }"
      />
      [% endif %]
      <small
        v-if="v$.item.[[field.name]].$invalid && submitted"
        class="p-error"
      >
        [[field.label]] is required.
      </small>
    </div>
    [% endfor %]

    <template #footer>
      <Button
        label="Cancel"
        icon="pi pi-times"
        class="p-button-text"
        @click="hideDialog"
      />
      <Button
        label="Save"
        icon="pi pi-check"
        class="p-button-text"
        @click="saveItem"
      />
    </template>
  </Dialog>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { useStore } from '@/stores/[[MODEL_NAME_CAMEL]]Store';
import type { [[MODEL_NAME_PASCAL]] } from '@/types';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Checkbox from 'primevue/checkbox';
import Calendar from 'primevue/calendar';
import Dropdown from 'primevue/dropdown';

export default defineComponent({
  name: '[[MODEL_NAME_PASCAL]]Modal',
  components: {
    Dialog,
    Button,
    InputText,
    Textarea,
    Checkbox,
    Calendar,
    Dropdown,
  },
  props: {
    modelValue: {
      type: Boolean,
      required: true,
    },
    item: {
      type: Object as () => [[MODEL_NAME_PASCAL]] | null,
      default: null,
    },
  },
  emits: ['update:modelValue', 'save'],
  setup(props, { emit }) {
    const store = useStore();
    const submitted = ref(false);

    const modelNamePascal = computed(() => '[[MODEL_NAME_PASCAL]]');
    const modelNameCamel = computed(() => '[[MODEL_NAME_CAMEL]]');

    const item = ref<[[MODEL_NAME_PASCAL]]>(props.item || {} as [[MODEL_NAME_PASCAL]]);

    const rules = {
      item: {
        // Add validation rules dynamically based on FORM_FIELDS
        [% for field in FORM_FIELDS %]
        [[field.name]]: { required: [[field.required]] },
        [% endfor %]
      },
    };

    const v$ = useVuelidate(rules, { item });

    const dialogTitle = computed(() => {
      return item.value.id ? `Edit ${modelNamePascal.value}` : `Add ${modelNamePascal.value}`;
    });

    const hideDialog = () => {
      emit('update:modelValue', false);
    };

    const saveItem = async () => {
      submitted.value = true;
      const isFormCorrect = await v$.value.$validate();
      if (!isFormCorrect) return;

      if (item.value.id) {
        await store.update[[MODEL_NAME_PASCAL]](item.value.id, item.value);
      } else {
        await store.create[[MODEL_NAME_PASCAL]](item.value);
      }

      emit('save');
      hideDialog();
    };

    const updateVisible = (value: boolean) => {
      emit('update:modelValue', value);
    };

    return {
      v$,
      item,
      submitted,
      dialogTitle,
      modelNamePascal,
      modelNameCamel,
      hideDialog,
      saveItem,
      updateVisible,
    };
  },
});
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
