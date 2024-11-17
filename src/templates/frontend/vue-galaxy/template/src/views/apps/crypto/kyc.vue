<script>
import { ref, watch } from "vue";
import useVuelidate from "@vuelidate/core";
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import DropZone from "@/components/widgets/dropZone";

import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/lupuorrc.json";

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
    return { dropzoneFile, drop, selectedFile, files, v$: useVuelidate() };
  },
  data() {
    return {
      modalShow: false,
      date: null,
      defaultOptions: { animationData: animationData },
      value: null,
    };
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    DropZone,
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
    <PageHeader title="KYC Application" pageTitle="Crypto" />

    <BRow class="justify-content-center">
      <BCol lg="6">
        <BCard no-body>
          <BCardBody>
            <div class="text-center">
              <BRow class="justify-content-center">
                <BCol lg="9">
                  <h4 class="mt-4 fw-semibold">KYC Verification</h4>
                  <p class="text-muted mt-3">
                    When you get your KYC verification process done, you have
                    given the crypto exchange in this case, information.
                  </p>
                  <div class="mt-4">
                    <BButton type="button" variant="primary" @click="modalShow = !modalShow">
                      Click here for Verification
                    </BButton>
                  </div>
                </BCol>
              </BRow>

              <BRow class="justify-content-center mt-5 mb-2">
                <BCol sm="7" cols="8">
                  <img src="@/assets/images/verification-img.png" alt="" class="img-fluid" />
                </BCol>
              </BRow>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>


    <BModal v-model="modalShow" body-class="p-0" header-class="p-3" title-class="text-uppercase" hide-footer
      title="Verify your Account" class="v-modal-custom" size="lg" centered>
      <form action="#" class="checkout-tab">
        <div class="modal-body p-0">
          <div class="step-arrow-nav">
          </div>
        </div>
        <div class="modal-body step-arrow-nav">
          <BTabs nav-class="nav-pills nav-justified custom-nav">
            <BTab active class="nav-item p-3">
              <template #title>
                <div class="nav-link">
                  Personal Info
                </div>
              </template>
              <BRow class="g-3">
                <BCol lg="6">
                  <div>
                    <label for="firstName" class="form-label">First Name</label>
                    <input type="text" class="form-control" id="firstName" placeholder="Enter your firstname" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div>
                    <label for="lastName" class="form-label">Last Name</label>
                    <input type="text" class="form-control" id="lastName" placeholder="Enter your lastname" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div>
                    <label for="phoneNumber" class="form-label">Phone</label>
                    <input type="text" class="form-control" id="phoneNumber" placeholder="Enter your phone number" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div>
                    <label for="dateofBirth" class="form-label">Date of Birth</label>
                    <flat-pickr v-model="date" placeholder="Enter your date of birth" class="form-control"></flat-pickr>
                  </div>
                </BCol>
                <BCol lg="4">
                  <div>
                    <label for="emailID" class="form-label">Email ID</label>
                    <input type="email" class="form-control" id="emailID" placeholder="Enter your email" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div>
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Enter your password" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div>
                    <label for="confirmPassword" class="form-label">Confirm Password</label>
                    <input type="password" class="form-control" id="confirmPassword"
                      placeholder="Enter your confirm password" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div>
                    <label for="vatNo" class="form-label">VAT/TIN No.</label>
                    <input type="text" class="form-control" id="vatNo" placeholder="Enter your VAT/TIN no" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div>
                    <label for="serviceTax" class="form-label">Service Tax No.</label>
                    <input type="text" class="form-control" id="serviceTax" placeholder="Enter your service tax no" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div>
                    <label for="country-select" class="form-label">Country</label>

                    <Multiselect class="form-control" v-model="value" :close-on-select="true" :searchable="true"
                      :create-option="true" :options="[
                        { value: '', label: 'Select country' },
                        { value: 'Argentina', label: 'Argentina' },
                        { value: 'Belgium', label: 'Belgium' },
                        { value: 'Brazil', label: 'Brazil' },
                        { value: 'Colombia', label: 'Colombia' },
                        { value: 'Denmark', label: 'Denmark' },
                        { value: 'France', label: 'France' },
                        { value: 'Germany', label: 'Germany' },
                        { value: 'Mexico', label: 'Mexico' },
                        { value: 'Russia', label: 'Russia' },
                        { value: 'Spain', label: 'Spain' },
                        { value: 'Syria', label: 'Syria' },
                        {
                          value: 'United Kingdom',
                          label: 'United Kingdom',
                        },
                        {
                          value: 'United States of America',
                          label: 'United States of America',
                        },
                      ]" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="d-flex align-items-start gap-3 mt-3">
                    <BButton type="button" variant="primary" class="btn-label right ms-auto nexttab"
                      data-nexttab="pills-bill-address-tab">
                      <i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2"></i>
                      Next Step
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </BTab>

            <BTab class="nav-item p-3">
              <template #title>
                <div class="nav-link">
                  Bank Details
                </div>
              </template>
              <BRow>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="banknameInput" class="form-label">Bank Name</label>
                    <input type="text" class="form-control" id="banknameInput" placeholder="Enter your bank name" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="branchInput" class="form-label">Branch</label>
                    <input type="text" class="form-control" id="branchInput" placeholder="Branch" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="mb-3">
                    <label for="accountnameInput" class="form-label">Account Holder Name</label>
                    <input type="text" class="form-control" id="accountnameInput"
                      placeholder="Enter account holder name" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="accountnumberInput" class="form-label">Account Number</label>
                    <input type="number" class="form-control" id="accountnumberInput"
                      placeholder="Enter account number" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="ifscInput" class="form-label">IFSC</label>
                    <input type="number" class="form-control" id="ifscInput" placeholder="IFSC" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="hstack align-items-start gap-3 mt-4">
                    <BButton variant="light" type="button" class="btn-label previestab"
                      data-previous="pills-bill-info-tab">
                      <i class="ri-arrow-left-line label-icon align-middle fs-16 me-2"></i>Back to Personal Info
                    </BButton>
                    <BButton variant="primary" type="button" class="btn-label right ms-auto nexttab"
                      data-nexttab="pills-payment-tab">
                      <i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2"></i>Next Step
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </BTab>

            <BTab class="nav-item p-3">
              <template #title>
                <div class="nav-link p-0 pt-2">
                 Document Verification
                </div>
              </template>
              <h5 class="mb-3">Choose Document Type</h5>

              <div class="d-flex gap-2">
                <div>
                  <input type="radio" class="btn-check" id="passport" checked name="choose-document" />
                  <label class="btn btn-outline-primary" for="passport">Passport</label>
                </div>
                <div>
                  <input type="radio" class="btn-check" id="aadhar-card" name="choose-document" />
                  <label class="btn btn-outline-primary" for="aadhar-card">Aadhar Card</label>
                </div>
                <div>
                  <input type="radio" class="btn-check" id="pan-card" name="choose-document" />
                  <label class="btn btn-outline-primary" for="pan-card">Pan Card</label>
                </div>
                <div>
                  <input type="radio" class="btn-check" id="other" name="choose-document" />
                  <label class="btn btn-outline-primary" for="other">Other</label>
                </div>
              </div>

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
              <div class="d-flex align-items-start gap-3 mt-4">
                <BButton type="button" variant="light" class="btn-label previestab"
                  data-previous="pills-bill-address-tab">
                  <i class="ri-arrow-left-line label-icon align-middle fs-16 me-2"></i>Back to Bank Details
                </BButton>
                <BButton type="button" variant="primary" class="btn-label right ms-auto nexttab"
                  data-nexttab="pills-finish-tab">
                  <i class="ri-save-line label-icon align-middle fs-16 ms-2"></i>Submit
                </BButton>
              </div>
            </BTab>

            <BTab class="nav-item p-3">
              <template #title>
                <div class="nav-link">
                  verified
                </div>
              </template>
              <BRow class="text-center justify-content-center">
                <BCol lg="11">
                  <div class="mb-4">
                    <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions" :height="120"
                      :width="120" />
                  </div>
                  <h5>Verification Completed</h5>
                  <p class="text-muted mb-4">
                    To stay verified, don't remove the meta tag form your
                    site's home page. To avoid losing verification, you may
                    want to add multiple methods form the
                    <span class="fw-medium">Crypto > KYC Application.</span>
                  </p>

                  <div class="hstack justify-content-center gap-2">
                    <BButton type="button" variant="ghost-success" @click="modalShow = false">
                      Done
                      <i class="ri-thumb-up-fill align-bottom me-1"></i>
                    </BButton>
                    <BButton type="button" variant="primary">
                      <i class="ri-home-4-line align-bottom ms-1"></i> Back
                      to Home
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </BTab>
          </BTabs>
        </div>
      </form>
    </BModal>
  </Layout>
</template>
