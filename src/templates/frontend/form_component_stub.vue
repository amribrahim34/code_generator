<template>
  <div :class="`${modelNameKebab}-form`">
    <form @submit.prevent="submitForm">
      <div v-for="field in fields" :key="field.name" class="form-field">
        <label :for="field.name">{{ formatLabel(field.name) }}</label>
        <component
          :is="getFieldComponent(field.type)"
          :id="field.name"
          v-model="formData[field.name]"
          :class="{ 'p-invalid': v$.formData[field.name].$invalid }"
        />
        <small v-if="v$.formData[field.name].$error" class="p-error">
          {{ v$.formData[field.name].$errors[0].$message }}
        </small>
      </div>
      <div class="form-actions">
        <Button
          type="submit"
          label="Save"
          icon="pi pi-check"
          :loading="loading"
        />
        <Button
          type="button"
          label="Cancel"
          icon="pi pi-times"
          class="p-button-secondary"
          @click="cancel"
        />
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, PropType } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required, email, helpers } from '@vuelidate/validators'
import { useStore } from '@/stores/[[MODEL_NAME_CAMEL]]Store'
import type { [[MODEL_NAME_PASCAL]] } from '@/types'
import { Button } from 'primevue/button'
import { InputText } from 'primevue/inputtext'
import { InputNumber } from 'primevue/inputnumber'
import { Calendar } from 'primevue/calendar'
import { Dropdown } from 'primevue/dropdown'
import { formatLabel } from '@/utils/stringUtils'

export interface FormField {
  name: string;
  type: string;
  required: boolean;
}

export default defineComponent({
  name: '[[MODEL_NAME_PASCAL]]Form',
  components: {
    Button,
    InputText,
    InputNumber,
    Calendar,
    Dropdown,
  },
  props: {
    modelValue: {
      type: Object as PropType<[[MODEL_NAME_PASCAL]] | null>,
      default: null
    },
    fields: {
      type: Array as PropType<FormField[]>,
      required: true
    }
  },
  emits: ['update:modelValue', 'save', 'cancel'],
  setup(props, { emit }) {
    const store = useStore()
    const loading = ref(false)

    const modelNamePascal = computed(() => '[[MODEL_NAME_PASCAL]]')
    const modelNameCamel = computed(() => '[[MODEL_NAME_CAMEL]]')
    const modelNameKebab = computed(() => '[[MODEL_NAME_KEBAB]]')

    const formData = ref<Partial<[[MODEL_NAME_PASCAL]]>>(props.modelValue || {})

    const rules = computed(() => {
      const fieldRules: Record<string, any> = {}
      props.fields.forEach(field => {
        fieldRules[field.name] = {}
        if (field.required) {
          fieldRules[field.name].required = helpers.withMessage(`${formatLabel(field.name)} is required`, required)
        }
        if (field.type === 'email') {
          fieldRules[field.name].email = helpers.withMessage('Invalid email address', email)
        }
        // Add more validations as needed
      })
      return { formData: fieldRules }
    })

    const v$ = useVuelidate(rules, { formData })

    const getFieldComponent = (type: string) => {
      switch (type) {
        case 'number':
          return 'InputNumber'
        case 'date':
          return 'Calendar'
        case 'select':
          return 'Dropdown'
        default:
          return 'InputText'
      }
    }

    const submitForm = async () => {
      const isFormCorrect = await v$.value.$validate()
      if (!isFormCorrect) return

      loading.value = true
      try {
        let result
        if (props.modelValue?.id) {
          result = await store.update[[MODEL_NAME_PASCAL]](props.modelValue.id, formData.value)
        } else {
          result = await store.create[[MODEL_NAME_PASCAL]](formData.value as [[MODEL_NAME_PASCAL]])
        }
        emit('save', result)
      } catch (error) {
        console.error(`Error saving ${modelNameCamel.value}:`, error)
        // Handle error (e.g., show error message)
      } finally {
        loading.value = false
      }
    }

    const cancel = () => {
      emit('cancel')
    }

    return {
      formData,
      v$,
      loading,
      modelNamePascal,
      modelNameCamel,
      modelNameKebab,
      getFieldComponent,
      submitForm,
      cancel,
      formatLabel
    }
  }
})
</script>

<style scoped>
.form-field {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-actions {
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}

.p-invalid {
  border-color: #f44336;
}

.p-error {
  color: #f44336;
}
</style>
