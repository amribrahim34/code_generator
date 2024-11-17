<script>
import { ref, watch } from "vue";
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import DropZone from "@/components/widgets/dropZone";
import useVuelidate from "@vuelidate/core";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
  setup() {
    let files = ref([]);
    let dropzoneFile = ref("");
    const drop = (e) => {
      dropzoneFile.value = e.dataTransfer.files[0];
      files.value.push(dropzoneFile.value);
    };
    const selectedFile = () => {
      dropzoneFile.value = document.querySelector(".dropzoneFile").files[0];
      files.value.push(dropzoneFile.value);
    };
    watch(
      () => [...files.value],
      (currentValue) => {
        return currentValue;
      }
    );
    return { dropzoneFile, files, drop, selectedFile, v$: useVuelidate() };
  },
  data() {
    return {
      value: ["C#", "HTML", "CSS"],
      value3: ["Private"],
      value4: ["Designing"],
      value5: ["Ellen Smith"],
      value1: ["Inprogress"],
      value2: ["High"],
      editor: ClassicEditor,
      editorData:
        "<p>It will be as simple as occidental in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is. The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary.</p><ul><li>Product Design, Figma (Software), Prototype</li><li>Four Dashboards : Ecommerce, Analytics, Project etc.</li><li>Create calendar, chat and email app pages.</li><li>Add authentication pages</li></ul>",
      content: "<h1>Some initial content</h1>",
    };
  },
  methods: {
    deleteRecord(ele) {
      ele.target.parentElement.parentElement.parentElement.remove();
    },
  },
  components: {
    DropZone,
    Layout,
    PageHeader,
    ckeditor: CKEditor.component,
    Multiselect,
    flatPickr
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Create Project" pageTitle="Projects" />
    <BRow>
      <BCol lg="8">
        <BCard no-body>
          <BCardBody>
            <div class="mb-3">
              <label class="form-label" for="project-title-input">Project Title</label>
              <input type="text" class="form-control" id="project-title-input" placeholder="Enter project title" />
            </div>

            <div class="mb-3">
              <label class="form-label" for="project-thumbnail-img">Thumbnail Image</label>
              <input class="form-control" id="project-thumbnail-img" type="file"
                accept="image/png, image/gif, image/jpeg" />
            </div>

            <div class="mb-3">
              <label class="form-label">Project Description</label>
              <ckeditor v-model="editorData" :editor="editor"></ckeditor>
            </div>

            <BRow>
              <BCol lg="4">
                <div class="mb-3 mb-lg-0">
                  <label for="choices-priority-input" class="form-label">Priority</label>

                  <Multiselect v-model="value2" :close-on-select="true" :searchable="true" :create-option="true"
                    :options="[
                      { value: 'High', label: 'High' },
                      { value: 'Medium', label: 'Medium' },
                      { value: 'Low', label: 'Low' },
                    ]" />
                </div>
              </BCol>
              <BCol lg="4">
                <div class="mb-3 mb-lg-0">
                  <label for="choices-status-input" class="form-label">Status</label>

                  <Multiselect v-model="value1" :close-on-select="true" :searchable="true" :create-option="true"
                    :options="[
                      { value: 'Inprogress', label: 'Inprogress' },
                      { value: 'Completed', label: 'Completed' },
                    ]" />
                </div>
              </BCol>
              <BCol lg="4">
                <div>
                  <label for="datepicker-deadline-input" class="form-label">Deadline</label>

                  <flat-pickr v-model="date" :config="config" class="form-control flatpickr-input"></flat-pickr>
                </div>
              </BCol>
            </BRow>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Attached files</h5>
          </BCardHeader>
          <BCardBody>
            <div>
              <p class="text-muted">Add Attached files here.</p>

              <DropZone @drop.prevent="drop" @change="selectedFile" class="mb-2" />
              <div class="vstack gap-2">
                <div class="border rounded" v-for="(file, index) of files" :key="index">
                  <div class="d-flex align-items-center p-2">
                    <div class="flex-grow-1">
                      <div class="pt-1">
                        <h5 class="fs-14 mb-1" data-dz-name="">
                          {{ file.name }}
                        </h5>
                        <p class="fs-13 text-muted mb-0" data-dz-size="">
                          <strong>{{ file.size / 1024 }}</strong> KB
                        </p>
                        <strong class="error text-danger" data-dz-errormessage=""></strong>
                      </div>
                    </div>
                    <div class="flex-shrink-0 ms-3">
                      <BButton variant="danger" size="sm" data-dz-remove="" @click="deleteRecord">
                        Delete
                      </BButton>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
        <div class="text-end mb-4">
          <BButton type="button" variant="danger" class="w-sm me-1">Delete</BButton>
          <BButton type="submit" variant="secondary" class="w-sm me-1"> Draft </BButton>
          <BButton type="submit" variant="primary" class="w-sm">Create</BButton> 
        </div>
      </BCol>
      <BCol lg="4">
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Privacy</h5>
          </BCardHeader>
          <BCardBody>
            <div>
              <label for="choices-privacy-status-input" class="form-label">Status</label>
              <Multiselect v-model="value3" :close-on-select="true" :searchable="true" :create-option="true" :options="[
                { value: 'Private', label: 'Private' },
                { value: 'Team', label: 'Team' },
                { value: 'Public', label: 'Public' },
              ]" />
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Tags</h5>
          </BCardHeader>
          <BCardBody>
            <div class="mb-3">
              <label for="choices-categories-input" class="form-label">Categories</label>
              <Multiselect v-model="value4" :close-on-select="true" :searchable="true" :create-option="true" :options="[
                { value: 'Designing', label: 'Designing' },
                { value: 'Development', label: 'Development' },
              ]" />
            </div>

            <div>
              <label for="choices-text-input" class="form-label">Skills</label>
              <Multiselect class="form-control" v-model="value" mode="tags" :close-on-select="true" :searchable="true"
                :create-option="true" :options="[
                  { value: 'UI/UX', label: 'UI/UX' },
                  { value: 'Figma', label: 'Figma' },
                  { value: 'HTML', label: 'HTML' },
                  { value: 'CSS', label: 'CSS' },
                  { value: 'Javascript', label: 'Javascript' },
                  { value: 'C#', label: 'C#' },
                  { value: 'Nodejs', label: 'Nodejs' },
                ]" />
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Members</h5>
          </BCardHeader>
          <BCardBody>
            <div class="mb-3">
              <label for="choices-lead-input" class="form-label">Team Lead</label>
              <Multiselect v-model="value5" :close-on-select="true" :searchable="true" :create-option="true" :options="[
                { value: 'Brent Gonzalez', label: 'Brent Gonzalez' },
                { value: 'Darline Williams', label: 'Darline Williams' },
                { value: 'Sylvia Wright', label: 'Sylvia Wright' },
                { value: 'Ellen Smith', label: 'Ellen Smith' },
                { value: 'Jeffrey Salazar', label: 'Jeffrey Salazar' },
                { value: 'Mark Williams', label: 'Mark Williams' },
              ]" />
            </div>

            <div>
              <label class="form-label">Team Members</label>
              <div class="avatar-group">
                <BLink href="javascript: void(0);" class="avatar-group-item" v-b-tooltip.hover title="Brent Gonzalez">
                  <div class="avatar-xs">
                    <img src="@/assets/images/users/avatar-3.jpg" alt="" class="rounded-circle img-fluid" />
                  </div>
                </BLink>
                <BLink href="javascript: void(0);" class="avatar-group-item" v-b-tooltip.hover title="Sylvia Wright">
                  <div class="avatar-xs">
                    <div class="avatar-title rounded-circle bg-primary">
                      S
                    </div>
                  </div>
                </BLink>
                <BLink href="javascript: void(0);" class="avatar-group-item" v-b-tooltip.hover title="Ellen Smith">
                  <div class="avatar-xs">
                    <img src="@/assets/images/users/avatar-4.jpg" alt="" class="rounded-circle img-fluid" />
                  </div>
                </BLink>
                <BLink href="javascript: void(0);" class="avatar-group-item" v-b-tooltip.hover title="Add Members">
                  <div class="avatar-xs" data-bs-toggle="modal" data-bs-target="#inviteMembersModal">
                    <div class="avatar-title fs-16 rounded-circle bg-light border-dashed border text-primary">
                      +
                    </div>
                  </div>
                </BLink>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
