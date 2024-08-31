import { RouteRecordRaw } from 'vue-router'

const {{MODEL_NAME_LOWERCASE}}Routes: RouteRecordRaw[] = [
  {
    path: '/{{MODEL_NAME_PLURAL_LOWERCASE}}',
    name: '{{MODEL_NAME_PLURAL}}List',
    component: () => import('@/views/{{MODEL_NAME}}/List{{MODEL_NAME}}.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/{{MODEL_NAME_PLURAL_LOWERCASE}}/create',
    name: 'Create{{MODEL_NAME}}',
    component: () => import('@/views/{{MODEL_NAME}}/Create{{MODEL_NAME}}.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/{{MODEL_NAME_PLURAL_LOWERCASE}}/:id',
    name: '{{MODEL_NAME}}Details',
    component: () => import('@/views/{{MODEL_NAME}}/{{MODEL_NAME}}Details.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/{{MODEL_NAME_PLURAL_LOWERCASE}}/:id/edit',
    name: 'Edit{{MODEL_NAME}}',
    component: () => import('@/views/{{MODEL_NAME}}/Edit{{MODEL_NAME}}.vue'),
    meta: { requiresAuth: true }
  }
]

export default {{MODEL_NAME_LOWERCASE}}Routes