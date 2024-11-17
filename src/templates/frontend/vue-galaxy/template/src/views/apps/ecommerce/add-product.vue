<script>
import { ref, watch } from "vue";
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import DropZone from "@/components/widgets/dropZone";
import useVuelidate from "@vuelidate/core";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

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
    return {
      dropzoneFile,
      drop,
      selectedFile,
      v$: useVuelidate(),
      files
    };
  },
  data() {
    return {
      date1: null,
      datetimeConfig: {
        enableTime: true,
        dateFormat: "d.m.y",
        time_24hr: true,
      },
      value1: ["Scheduled"],
      value2: ["Hidden"],
      value3: ["Fashion"],
      editor: ClassicEditor,
      editorData: "<p>Tommy Hilfiger men striped pink sweatshirt. Crafted with cotton. Material composition is 100% organic cotton. This is one of the world’s leading designer lifestyle brands and is internationally recognized for celebrating the essence of classic American cool style, featuring preppy with a twist designs.</p><ul><li>Full Sleeve</li><li>Cotton</li><li>All Sizes available</li><li>4 Different Color</li></ul>",
      content: "<h1>Some initial content</h1>",
    };
  },
  components: {
    DropZone,
    Layout,
    PageHeader,
    ckeditor: CKEditor.component,
    Multiselect,
    flatPickr
  },
  methods: {
    deleteRecord(ele) {
      ele.target.parentElement.parentElement.parentElement.remove();
    },
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Create Product" pageTitle="Ecommerce" />

    <BRow>
      <BCol lg="8">
        <form>
          <BCard no-body>
            <BCardBody>
              <div class="mb-3">
                <label class="form-label" for="product-title-input">Product Title</label>
                <input type="text" class="form-control" id="product-title-input" placeholder="Enter product title" />
              </div>
              <div>
                <label>Product Description</label>
                <ckeditor v-model="editorData" :editor="editor"></ckeditor>
              </div>
            </BCardBody>
          </BCard>

          <BCard no-body>
            <BCardHeader>
              <h5 class="card-title mb-0">Product Gallery</h5>
            </BCardHeader>
            <BCardBody>
              <div class="mb-4">
                <h5 class="fs-14 mb-1">Product Image</h5>
                <p class="text-muted">Add Product main Image.</p>
                <input class="form-control" id="product-image-input" type="file"
                  accept="image/png, image/gif, image/jpeg" />
              </div>
              <div class="vstack gap-2">
                <h5 class="fs-14 mb-1">Product Gallery</h5>
                <p class="text-muted">Add Product Gallery Images.</p>
                <DropZone @drop.prevent="drop" @change="selectedFile" />

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
                      <BButton data-dz-remove="" variant="danger" size="sm" @click="deleteRecord">
                        Delete
                      </BButton>
                    </div>
                  </div>
                </div>
              </div>
            </BCardBody>
          </BCard>

          <BCard no-body>
            <BCardBody>
              <BTabs class="nav-tabs-custom card-header-tabs border-bottom-0">
                <BTab title="General Info" class="py-3 px-2">
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="mb-3">
                        <label class="form-label" for="manufacturer-name-input">Manufacturer Name</label>
                        <input type="text" class="form-control" id="manufacturer-name-input"
                          placeholder="Enter manufacturer name">
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="mb-3">
                        <label class="form-label" for="manufacturer-brand-input">Manufacturer Brand</label>
                        <input type="text" class="form-control" id="manufacturer-brand-input"
                          placeholder="Enter manufacturer brand">
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-3 col-sm-6">
                      <div class="mb-3">
                        <label class="form-label" for="stocks-input">Stocks</label>
                        <input type="text" class="form-control" id="stocks-input" placeholder="Stocks" required="">
                        <div class="invalid-feedback">Please Enter a product stocks.</div>
                      </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                      <div class="mb-3">
                        <label class="form-label" for="product-price-input">Price</label>
                        <div class="input-group has-validation mb-3">
                          <span class="input-group-text" id="product-price-addon">$</span>
                          <input type="text" class="form-control" id="product-price-input" placeholder="Enter price"
                            aria-label="Price" aria-describedby="product-price-addon" required="">
                          <div class="invalid-feedback">Please Enter a product price.</div>
                        </div>

                      </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                      <div class="mb-3">
                        <label class="form-label" for="product-discount-input">Discount</label>
                        <div class="input-group mb-3">
                          <span class="input-group-text" id="product-discount-addon">%</span>
                          <input type="text" class="form-control" id="product-discount-input" placeholder="Enter discount"
                            aria-label="discount" aria-describedby="product-discount-addon">
                        </div>
                      </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                      <div class="mb-3">
                        <label class="form-label" for="orders-input">Orders</label>
                        <input type="text" class="form-control" id="orders-input" placeholder="Orders" required="">
                        <div class="invalid-feedback">Please Enter a product orders.</div>
                      </div>
                    </div>
                    <!-- end col -->
                  </div>
                </BTab>

                <BTab title="Meta Data" class="py-3 px-2">
                  <BRow>
                    <BCol lg="6">
                      <div class="mb-3">
                        <label class="form-label" for="meta-title-input">Meta title</label>
                        <input type="text" class="form-control" placeholder="Enter meta title" id="meta-title-input" />
                      </div>
                    </BCol>

                    <BCol lg="6">
                      <div class="mb-3">
                        <label class="form-label" for="meta-keywords-input">Meta Keywords</label>
                        <input type="text" class="form-control" placeholder="Enter meta keywords"
                          id="meta-keywords-input" />
                      </div>
                    </BCol>
                  </BRow>

                  <div>
                    <label class="form-label" for="meta-description-input">Meta Description</label>
                    <textarea class="form-control" id="meta-description-input" placeholder="Enter meta description"
                      rows="3"></textarea>
                  </div>
                </BTab>
              </BTabs>
            </BCardBody>
          </BCard>
          <div class="text-end mb-3">
            <BButton type="button" variant="primary" class="w-sm">Submit</BButton>
          </div>
        </form>
      </BCol>

      <BCol lg="4">
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Publish</h5>
          </BCardHeader>
          <BCardBody>
            <div class="mb-3">
              <label for="choices-publish-status-input" class="form-label">Status</label>
              <Multiselect class="form-control" v-model="value1" :close-on-select="true" :searchable="true"
                :create-option="true" :options="[
                  { value: 'Published', label: 'Published' },
                  { value: 'Scheduled', label: 'Scheduled' },
                  { value: 'Draft', label: 'Draft' },
                ]" />
            </div>

            <div>
              <label for="choices-publish-visibility-input" class="form-label">Visibility</label>
              <Multiselect class="form-control" v-model="value2" :close-on-select="true" :searchable="true"
                :create-option="true" :options="[
                  { value: 'Public', label: 'Public' },
                  { value: 'Hidden', label: 'Hidden' },
                ]" />
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Publish Schedule</h5>
          </BCardHeader>
          <BCardBody>
            <div>
              <label for="datepicker-publish-input" class="form-label">Publish Date & Time</label>

              <flat-pickr v-model="date1" :config="datetimeConfig" placeholder="Enter publish date"
                class="form-control"></flat-pickr>
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Product Categories</h5>
          </BCardHeader>
          <BCardBody>
            <p class="text-muted mb-2">
              <BLink href="#" class="float-end text-decoration-underline">Add New</BLink>Select product category
            </p>

            <Multiselect class="form-control" v-model="value3" :close-on-select="true" :searchable="true"
              :create-option="true" :options="[
                { value: 'All', label: 'All' },
                { value: 'Appliances', label: 'Appliances' },
                { value: 'Fashion', label: 'Fashion' },
                { value: 'Electronics', label: 'Electronics' },
                { value: 'Grocery', label: 'Grocery' },
                { value: 'Home & Furniture', label: 'Home & Furniture' },
                { value: 'Kids', label: 'Kids' },
                { value: 'Mobiles', label: 'Mobiles' },
              ]" />
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Product Tags</h5>
          </BCardHeader>
          <BCardBody>
            <div class="hstack gap-3 align-items-start">
              <div class="flex-grow-1">
                <input class="form-control" data-choices data-choices-multiple-remove="true" placeholder="Enter tags"
                  type="text" value="Cotton" />
              </div>
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Product Short Description</h5>
          </BCardHeader>
          <BCardBody>
            <p class="text-muted mb-2">Add short description for product</p>
            <textarea class="form-control" placeholder="Must enter minimum of a 100 characters" rows="3"></textarea>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>