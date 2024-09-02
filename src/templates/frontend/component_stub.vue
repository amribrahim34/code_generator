<template>
  <div :class="`${modelNameKebab}-form`">
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
import { defineComponent, reactive, toRefs, computed } from 'vue'
import { useStore } from '@/stores/{{MODEL_NAME_CAMEL}}Store'
import type { {{MODEL_NAME_PASCAL}}, Create{{MODEL_NAME_PASCAL}}DTO, Update{{MODEL_NAME_PASCAL}}DTO } from '@/types'
{{PRIME_VUE_IMPORTS}}

export default defineComponent({
  name: '{{MODEL_NAME_PASCAL}}Form',
  components: { {{PRIME_VUE_COMPONENTS}} },
  props: {
    modelValue: {
      type: Object as () => {{MODEL_NAME_PASCAL}} | null,
      default: null
    }
  },
  emits: ['update:modelValue', 'save', 'cancel'],
  setup(props, { emit }) {
    const store = useStore()

    const state = reactive({
      {{MODEL_STATE}}
    })

    const modelNameKebab = computed(() => '{{MODEL_NAME_KEBAB}}')

    const submitForm = async () => {
      try {
        let result
        if (props.modelValue?.id) {
          const updateDto: Update{{MODEL_NAME_PASCAL}}DTO = { ...state }
          result = await store.update{{MODEL_NAME_PASCAL}}(props.modelValue.id, updateDto)
        } else {
          const createDto: Create{{MODEL_NAME_PASCAL}}DTO = { ...state }
          result = await store.create{{MODEL_NAME_PASCAL}}(createDto)
        }
        emit('save', result)
      } catch (error) {
        console.error('Error saving {{MODEL_NAME_CAMEL}}:', error)
        // TODO: Handle error (e.g., show error message)
      }
    }

    return {
      ...toRefs(state),
      modelNameKebab,
      submitForm
    }
  }
})
</script>

<style scoped>
.{{MODEL_NAME_KEBAB}}-form {
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
