<template>
  <div class="{{MODEL_NAME_LOWERCASE}}-form">
    <form @submit.prevent="submitForm">
      {{ FORM_FIELDS }}
      <div class="form-actions">
        <Button type="submit" label="Save" icon="pi pi-check" />
        <Button
          type="button"
          label="Cancel"
          icon="pi pi-times"
          class="p-button-secondary"
          @click="$emit('cancel')"
        />
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from 'vue'
import { use{{MODEL_NAME}}Store } from '@/stores/{{MODEL_NAME_LOWERCASE}}Store'
import { {{MODEL_NAME}}, Create{{MODEL_NAME}}DTO, Update{{MODEL_NAME}}DTO } from '@/types'
{{PRIME_VUE_IMPORTS}}

export default defineComponent({
  name: '{{MODEL_NAME}}Form',
  components: { {{PRIME_VUE_COMPONENTS}} },
  props: {
    modelValue: {
      type: Object as () => {{MODEL_NAME}} | null,
      default: null
    }
  },
  emits: ['update:modelValue', 'save', 'cancel'],
  setup(props, { emit }) {
    const {{MODEL_NAME_LOWERCASE}}Store = use{{MODEL_NAME}}Store()

    const state = reactive({
      {{MODEL_STATE}}
    })

    const submitForm = async () => {
      try {
        let result
        if (props.modelValue && props.modelValue.id) {
          const updateDto: Update{{MODEL_NAME}}DTO = { ...state }
          result = await {{MODEL_NAME_LOWERCASE}}Store.update{{MODEL_NAME}}(props.modelValue.id, updateDto)
        } else {
          const createDto: Create{{MODEL_NAME}}DTO = { ...state }
          result = await {{MODEL_NAME_LOWERCASE}}Store.create{{MODEL_NAME}}(createDto)
        }
        emit('save', result)
      } catch (error) {
        console.error('Error saving {{MODEL_NAME_LOWERCASE}}:', error)
        // Handle error (e.g., show error message)
      }
    }

    return {
      ...toRefs(state),
      submitForm
    }
  }
})
</script>

<style scoped>
.{{MODEL_NAME_LOWERCASE}}-form {
  max-width: 500px;
  margin: 0 auto;
}

.form-actions {
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}
</style>
