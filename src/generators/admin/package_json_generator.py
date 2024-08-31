import json

class PackageJsonGenerator:
    def __init__(self, project_name, project_description):
        self.project_name = project_name
        self.project_description = project_description

    def generate(self, model):
        package_json = {
            "name": self.project_name,
            "version": "0.1.0",
            "private": True,
            "description": self.project_description,
            "scripts": {
                "dev": "vite",
                "build": "vue-tsc --noEmit && vite build",
                "preview": "vite preview",
                "lint": "eslint . --ext .vue,.js,.jsx,.cjs,.mjs,.ts,.tsx,.cts,.mts --fix --ignore-path .gitignore"
            },
            "dependencies": {
                "vue": "^3.3.4",
                "vue-router": "^4.2.4",
                "pinia": "^2.1.6",
                "primevue": "^3.32.2",
                "primeicons": "^6.0.1",
                "primeflex": "^3.3.1",
                "axios": "^1.4.0"
            },
            "devDependencies": {
                "@rushstack/eslint-patch": "^1.3.3",
                "@tsconfig/node18": "^18.2.0",
                "@types/node": "^18.17.5",
                "@vitejs/plugin-vue": "^4.3.1",
                "@vue/eslint-config-prettier": "^8.0.0",
                "@vue/eslint-config-typescript": "^11.0.3",
                "@vue/tsconfig": "^0.4.0",
                "eslint": "^8.46.0",
                "eslint-plugin-vue": "^9.16.1",
                "prettier": "^3.0.1",
                "sass": "^1.66.1",
                "typescript": "~5.1.6",
                "vite": "^4.4.9",
                "vue-tsc": "^1.8.8"
            }
        }
        
        return {"package.json": json.dumps(package_json, indent=2)}

def generate_package_json(project_name, project_description):
    generator = PackageJsonGenerator(project_name, project_description)
    return generator.generate()

if __name__ == "__main__":
    project_name = "my-admin-panel"
    project_description = "Auto-generated admin panel using PrimeVue and Pinia"
    package_json_content = generate_package_json(project_name, project_description)
    print(package_json_content)