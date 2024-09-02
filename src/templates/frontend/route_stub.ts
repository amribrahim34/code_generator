import { RouteRecordRaw } from 'vue-router';

const [[MODEL_NAME_CAMEL]]Routes: RouteRecordRaw[] = [
  {
    path: '/[[MODEL_NAME_PLURAL_CAMEL]]',
    name: '[[MODEL_NAME_PLURAL_PASCAL]]',
    component: () => import('@/views/[[MODEL_NAME_PASCAL]]List.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/[[MODEL_NAME_PLURAL_CAMEL]]/create',
    name: 'Create[[MODEL_NAME_PASCAL]]',
    component: () => import('@/views/[[MODEL_NAME_PASCAL]]Form.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/[[MODEL_NAME_PLURAL_CAMEL]]/:id/edit',
    name: 'Edit[[MODEL_NAME_PASCAL]]',
    component: () => import('@/views/[[MODEL_NAME_PASCAL]]Form.vue'),
    meta: { requiresAuth: true }
  }
];

export default [[MODEL_NAME_CAMEL]]Routes;