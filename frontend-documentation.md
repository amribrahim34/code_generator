# Frontend Documentation for Laravel Code Generator

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Key Technologies](#key-technologies)
4. [Generated Components](#generated-components)
   - [Main Application Files](#main-application-files)
   - [Views](#views)
   - [Components](#components)
   - [Stores](#stores)
   - [Types](#types)
   - [Routes](#routes)
5. [Customization](#customization)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)

## Introduction

The frontend part of the Laravel Code Generator project is designed to create a robust, type-safe, and user-friendly admin panel using Vue 3, TypeScript, and PrimeVue. This documentation will guide you through the structure and usage of the generated frontend code.

## Project Structure

The generated frontend project follows this structure:

```
src/
├── components/
│   └── [ModelName]Form.vue
├── views/
│   └── [ModelName]/
│       ├── List[ModelName].vue
│       ├── Create[ModelName].vue
│       └── Edit[ModelName].vue
├── stores/
│   └── [modelName]Store.ts
├── types/
│   ├── index.ts
│   └── [modelName]Types.ts
├── router/
│   └── index.ts
├── App.vue
├── main.ts
└── vite-env.d.ts
```

## Key Technologies

- Vue 3: Progressive JavaScript framework for building user interfaces
- TypeScript: Typed superset of JavaScript
- Pinia: State management library for Vue
- PrimeVue: UI component library for Vue
- Vite: Next-generation frontend tooling

## Generated Components

### Main Application Files

1. **main.ts**: Entry point of the application. It initializes Vue, Pinia, Vue Router, and PrimeVue.

2. **App.vue**: Root component of the application. It includes the main layout structure with header, sidebar, and main content area.

3. **vite-env.d.ts**: TypeScript declaration file for Vite-specific environment variables.

### Views

For each model, the following views are generated:

1. **List[ModelName].vue**: Displays a list of all instances of the model in a PrimeVue DataTable. It includes functionality for:
   - Pagination
   - Sorting
   - Filtering
   - Creating new instances
   - Editing existing instances
   - Deleting instances
   - Bulk actions (delete, export)
   - CSV import/export

2. **Create[ModelName].vue**: Form for creating a new instance of the model. This view is generated only if the model has more than 3 attributes.

3. **Edit[ModelName].vue**: Form for editing an existing instance of the model. This view is generated only if the model has more than 3 attributes.

### Components

For each model, a form component is generated:

**[ModelName]Form.vue**: Reusable form component for creating and editing model instances. It uses appropriate PrimeVue input components based on the attribute types.

### Stores

For each model, a Pinia store is generated:

**[modelName]Store.ts**: Contains state management logic and API calls for the model. It includes actions for fetching, creating, updating, and deleting model instances.

### Types

For each model, TypeScript types are generated:

**[modelName]Types.ts**: Contains TypeScript interfaces and types for the model, including:
- Main model interface
- DTO (Data Transfer Object) types for creating and updating instances

### Routes

The **router/index.ts** file is generated with routes for all models, including:
- List view
- Create view (if applicable)
- Edit view (if applicable)

## Customization

You can customize the generated code by modifying the stub files in the `templates` directory. The main areas for customization are:

1. Styling: Adjust the CSS in the Vue components to match your desired look and feel.
2. Layout: Modify the `App.vue` file to change the overall layout of the admin panel.
3. Additional functionality: Add new methods or computed properties to the generated components or stores as needed.

## Best Practices

1. **Type Safety**: Leverage TypeScript's type system to catch errors early and improve code quality.
2. **Component Reusability**: Use the generated form components across different views to maintain consistency and reduce code duplication.
3. **State Management**: Use the Pinia stores for all API calls and state management. Avoid making API calls directly from components.
4. **Responsive Design**: Utilize PrimeVue's responsive classes and Vue's reactive system to create a responsive user interface.
5. **Error Handling**: Implement proper error handling in the stores and display user-friendly error messages in the UI.

## Troubleshooting

1. **Component not found**: Ensure that all PrimeVue components used in your views are properly imported and registered in `main.ts`.
2. **Type errors**: If you encounter TypeScript errors, make sure your IDE is recognizing the `vite-env.d.ts` file and that all necessary types are properly imported.
3. **API calls failing**: Check that the API endpoints in the store files match your backend routes. Also, ensure that you're handling authentication properly if your API requires it.
4. **Styling issues**: If PrimeVue styles are not applied correctly, check that all necessary CSS files are imported in `main.ts`.

For more specific issues, refer to the documentation of the individual technologies used (Vue, Pinia, PrimeVue, etc.) or consult the community forums.
