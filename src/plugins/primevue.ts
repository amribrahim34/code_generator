// src/plugins/primevue.ts

import { App } from "vue";
import PrimeVue from "primevue/config";
import ToastService from "primevue/toastservice";
import ConfirmationService from "primevue/confirmationservice";

import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import InputText from "primevue/inputtext";
import Toolbar from "primevue/toolbar";
import Dialog from "primevue/dialog";
import Toast from "primevue/toast";
import Dropdown from "primevue/dropdown";
import ConfirmDialog from "primevue/confirmdialog";

import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

export function setupPrimeVue(app: App) {
  app.use(PrimeVue);
  app.use(ToastService);
  app.use(ConfirmationService);

  app.component("Button", Button);
  app.component("DataTable", DataTable);
  app.component("Column", Column);
  app.component("InputText", InputText);
  app.component("Toolbar", Toolbar);
  app.component("Dialog", Dialog);
  app.component("Toast", Toast);
  app.component("Dropdown", Dropdown);
  app.component("ConfirmDialog", ConfirmDialog);
}
