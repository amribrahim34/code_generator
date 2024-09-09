# React Native Code Generator Specifications

## Overview

This document outlines the specifications for generating React Native code from a schema input. The goal is to create a flexible, modular system that can generate natural UIs that closely resemble those created by UI developers.

## Input Schema

### Structure

The input schema is divided into two main parts:

1. **Mobile App Configuration**
2. **Screens Definition**

### Example Schema

```json
{
  "mobile_app": {
    "framework": "expo",
    "expo_version": "44.0.0",
    "design_system": "react-native-paper",
    "state_management": "redux-toolkit",
    "navigation": "react-navigation",
    "api_client": "axios",
    "theme": {
      "primaryColor": "#6200ee",
      "accentColor": "#03dac4"
    }
  },
  "screens": [
    {
      "name": "HomeScreen",
      "layout": {
        "type": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "flex-start"
      },
      "components": [
        {
          "type": "Header",
          "props": {
            "title": "Home",
            "style": {
              "fontSize": 24,
              "fontWeight": "bold",
              "color": "#333333",
              "marginBottom": 10
            }
          }
        },
        {
          "type": "List",
          "dataSource": "products",
          "itemComponent": "ProductListItem",
          "style": {
            "borderRadius": 8,
            "backgroundColor": "#f8f8f8",
            "padding": 10,
            "width": "90%"
          }
        },
        {
          "type": "Button",
          "props": {
            "title": "Add Product",
            "onPress": "navigateToAddProduct",
            "style": {
              "backgroundColor": "#6200ee",
              "color": "#ffffff",
              "borderRadius": 5,
              "padding": 10,
              "width": "50%"
            }
          }
        }
      ]
    }
  ]
}
```

## Component Customization

### Positioning and Layout

- **layout:** Defines the overall layout of the screen (e.g., `flex`, `grid`, etc.).
- **style:** Provides detailed control over each component’s appearance (e.g., `fontSize`, `borderRadius`, `padding`, etc.).
- **width/height:** Allows percentage-based or fixed sizing for components.
- **Responsive Design:** Implement breakpoints for different screen sizes to ensure the layout adapts to different devices.

### Styling

- Allow customization of key UI properties like margins, padding, rounded edges, font styles, colors, and sizes.
- Utilize a consistent theming system that allows global styles to be applied across all components.

## Python Code Generation

### Schema Parsing and Component Generation

- **Schema Structure:** Write Python classes that parse the input JSON schema and map it to UI components in React Native.
- **Style Application:** Translate the style properties from the schema into React Native styles.

#### Example Python Code

```python
class ReactNativeComponentGenerator:
    def generate_component(self, component_schema: dict) -> str:
        component_type = component_schema['type']
        props = component_schema.get('props', {})
        style = component_schema.get('style', {})

        # Generate JSX code for the component
        jsx = f"<{component_type} style={self.convert_style(style)}"

        for prop, value in props.items():
            jsx += f" {prop}={self.convert_prop(value)}"

        jsx += f">"
        jsx += f"</{component_type}>"
        return jsx

    def convert_style(self, style_dict: dict) -> str:
        # Convert Python dict to React Native style object
        style = "{"
        for key, value in style_dict.items():
            style += f"{key}: '{value}', "
        style += "}"
        return style

    def convert_prop(self, prop_value):
        # Convert props to appropriate JSX format
        if isinstance(prop_value, str):
            return f"'{prop_value}'"
        return str(prop_value)
```

## System Design

### Modular and Scalable Architecture

- **Component Generators:** Implement different generators for each type of component (e.g., `ButtonGenerator`, `ListGenerator`, etc.) that handle specific logic for each component type.
- **Layout Management:** Create a layout manager that understands how to position components based on the specified layout system (e.g., flex, grid).
- **Theme Integration:** Use a theme provider system that allows global themes to be applied consistently across all components.

#### Example Layout Manager

```python
class LayoutManager:
    def apply_layout(self, layout_schema: dict, components: list) -> str:
        layout_type = layout_schema.get('type', 'flex')
        if layout_type == 'flex':
            return self.generate_flex_layout(layout_schema, components)
        # Additional layout types (e.g., grid) can be handled here

    def generate_flex_layout(self, layout_schema: dict, components: list) -> str:
        direction = layout_schema.get('flexDirection', 'column')
        justify = layout_schema.get('justifyContent', 'flex-start')
        align = layout_schema.get('alignItems', 'stretch')

        # Convert layout to JSX
        layout_jsx = f"<View style={{flexDirection: '{direction}', justifyContent: '{justify}', alignItems: '{align}'}}>"
        for component in components:
            layout_jsx += component
        layout_jsx += "</View>"

        return layout_jsx
```

### Configuration Flexibility

Allow users to specify which parts of the application they want to generate (e.g., screens, Redux, API services, theme configurations).

```json
{
  "generate": {
    "screens": true,
    "redux": true,
    "api": false,
    "theme": true
  }
}
```

## Summary

This approach provides a flexible, modular system for generating React Native code that mimics natural UI development. By integrating detailed styling options, layout management, and a scalable architecture, the generated code can closely resemble what a UI developer would create while offering extensive customization options.

=======================================================================================

second doc

# Writing the documentation into a .md file

documentation_content = """

# React Native Code Generator Specifications

## Overview

This document outlines the specifications for building a **React Native Code Generator** that generates code based on a given schema input. The goal is to create a modular and scalable system that produces clean, maintainable, and developer-friendly code that mimics natural UI development practices. The system should support flexible UI layouts, comprehensive styling options, and integration with popular libraries such as Redux Toolkit, React Navigation, Axios, and React Native Paper.

## Input Schema

### Structure

The input schema is divided into two main parts:

1. **Mobile App Configuration**: Defines the global configuration for the mobile app, including the framework, design system, state management, navigation, and API client.
2. **Screens Definition**: Describes the individual screens of the app, their layouts, components, and actions.

### Example Schema

\`\`\`json
{
"mobile_app": {
"framework": "expo",
"expo_version": "44.0.0",
"design_system": "react-native-paper",
"state_management": "redux-toolkit",
"navigation": "react-navigation",
"api_client": "axios",
"theme": {
"primaryColor": "#6200ee",
"accentColor": "#03dac4"
}
},
"screens": [
{
"name": "HomeScreen",
"layout": {
"type": "flex",
"flexDirection": "column",
"alignItems": "center",
"justifyContent": "flex-start"
},
"components": [
{
"type": "Header",
"props": {
"title": "Home",
"style": {
"fontSize": 24,
"fontWeight": "bold",
"color": "#333333",
"marginBottom": 10
}
}
},
{
"type": "List",
"dataSource": "products",
"itemComponent": "ProductListItem",
"style": {
"borderRadius": 8,
"backgroundColor": "#f8f8f8",
"padding": 10,
"width": "90%"
}
},
{
"type": "Button",
"props": {
"title": "Add Product",
"onPress": "navigateToAddProduct",
"style": {
"backgroundColor": "#6200ee",
"color": "#ffffff",
"borderRadius": 5,
"padding": 10,
"width": "50%"
}
}
}
]
}
]
}
\`\`\`

### Detailed Breakdown

- **Mobile App Configuration**: Defines high-level settings for the mobile app, including framework, version, design system, state management, navigation, API client, and theming.

  - **framework**: The mobile framework used, e.g., \`expo\` or \`react-native\`.
  - **expo_version**: Specifies the Expo SDK version if using Expo.
  - **design_system**: The design system library, e.g., \`react-native-paper\`.
  - **state_management**: The state management solution, e.g., \`redux-toolkit\`.
  - **navigation**: The navigation library, e.g., \`react-navigation\`.
  - **api_client**: The HTTP client for API interactions, e.g., \`axios\`.
  - **theme**: Global theme settings, including colors, fonts, and styles.

- **Screens Definition**: Describes the structure and content of each screen, including layout, components, and actions.

  - **layout**: Defines the overall layout of the screen, such as \`flex\` or \`grid\`.
  - **components**: Specifies the UI elements on the screen (e.g., buttons, text, lists), along with their properties and styles.

## Component Customization

### Positioning and Layout

- **layout**: Controls the arrangement of components within a screen.
  - **type**: Specifies the layout type (e.g., \`flex\`, \`grid\`).
  - **flexDirection**: Defines the main axis direction (\`row\` or \`column\` for flex).
  - **alignItems**: Aligns components along the cross-axis (e.g., \`center\`, \`stretch\`).
  - **justifyContent**: Aligns components along the main axis (e.g., \`flex-start\`, \`center\`).

### Styling

- **style**: Defines visual properties for each component, such as colors, margins, paddings, fonts, and sizes.
  - **Responsive Design**: Implement breakpoints or media queries to adapt layouts and styles to different screen sizes.

### Theming

- **Theme System**: Integrate a consistent theming system that allows global styles to be applied across all components.
  - Define color schemes, typography, and spacing.
  - Allow theme overrides for specific components.

## Python Code Generation

### Schema Parsing and Component Generation

The code generation process will parse the input schema and map it to React Native components. The generator will handle the creation of JSX code for each component, applying styles, properties, and actions as specified in the schema.

#### Example Python Code

\`\`\`python
class ReactNativeComponentGenerator:
def generate_component(self, component_schema: dict) -> str:
component_type = component_schema['type']
props = component_schema.get('props', {})
style = component_schema.get('style', {})

        # Generate JSX code for the component
        jsx = f"<{component_type} style={self.convert_style(style)}"

        for prop, value in props.items():
            jsx += f" {prop}={self.convert_prop(value)}"

        jsx += f">"
        jsx += f"</{component_type}>"
        return jsx

    def convert_style(self, style_dict: dict) -> str:
        # Convert Python dict to React Native style object
        style = "{"
        for key, value in style_dict.items():
            style += f"{key}: '{value}', "
        style += "}"
        return style

    def convert_prop(self, prop_value):
        # Convert props to appropriate JSX format
        if isinstance(prop_value, str):
            return f"'{prop_value}'"
        return str(prop_value)

\`\`\`

### Layout Management

A layout manager will handle the arrangement of components based on the specified layout (e.g., flex, grid). It will ensure that components are positioned correctly and adhere to the layout constraints.

#### Example Layout Manager

\`\`\`python
class LayoutManager:
def apply_layout(self, layout_schema: dict, components: list) -> str:
layout_type = layout_schema.get('type', 'flex')
if layout_type == 'flex':
return self.generate_flex_layout(layout_schema, components) # Additional layout types (e.g., grid) can be handled here

    def generate_flex_layout(self, layout_schema: dict, components: list) -> str:
        direction = layout_schema.get('flexDirection', 'column')
        justify = layout_schema.get('justifyContent', 'flex-start')
        align = layout_schema.get('alignItems', 'stretch')

        # Convert layout to JSX
        layout_jsx = f"<View style={{flexDirection: '{direction}', justifyContent: '{justify}', alignItems: '{align}'}}>"
        for component in components:
            layout_jsx += component
        layout_jsx += "</View>"

        return layout_jsx

\`\`\`

## Redux Toolkit Integration

### State Management

The generator will create Redux slices based on the input schema. The schema will define the state structure and actions that need to be handled by Redux.

- **State Structure**: Automatically generate the initial state based on the models defined in the schema.
- **Actions**: Define actions for updating state, triggered by UI events (e.g., form submissions, button clicks).
- **Reducers**: Create reducers to handle state changes based on actions.

#### Example Redux Slice Generation

\`\`\`python
def generate_redux_slice(model_name: str, attributes: list) -> str: # Generate initial state
initial_state = {attr['name']: None for attr in attributes}

    # Create slice template
    slice_template = f"""
    import {{ createSlice }} from '@reduxjs/toolkit';

    const initialState = {initial_state};

    const {model_name}Slice = createSlice({{
      name: '{model_name}',
      initialState,
      reducers: {{
        update{model_name}(state, action) {{
          Object.assign(state, action.payload);
        }}
      }}
    }});

    export const {{ update{model_name} }} = {model_name}Slice.actions;
    export default {model_name}Slice.reducer;
    """
    return slice_template

\`\`\`

## Navigation with React Navigation

### Screen Navigation

The generator will use React Navigation to create navigation routes based on the screen definitions in the schema. This will involve generating the navigation container, stacks, and linking screens to navigation routes.

- **Stacks and Navigators**: Create navigation stacks for screen flows.
- **Route Definitions**: Define navigation paths between screens.

#### Example Navigation Setup

\`\`\`python
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './screens/HomeScreen';
import AddProductScreen from './screens/AddProductScreen';

const Stack = createStackNavigator();
