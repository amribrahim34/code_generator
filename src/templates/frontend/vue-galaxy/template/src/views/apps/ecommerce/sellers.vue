<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { sellersList } from "@/common/data";
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/msoeawqm.json";

export default {
  data() {
    return {
      modalShow: false,
      searchQuery: null,
      date: null,
      value: null,
      chartOptions: {
        chart: {
          type: "area",
          height: 50,
          sparkline: {
            enabled: true,
          },
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [20, 100, 100, 100],
          },
        },
        stroke: {
          curve: "smooth",
          width: 2,
        },
        colors: ["#f44336"],
        tooltip: {
          fixed: {
            enabled: false,
          },
          x: {
            show: false,
          },
          y: {
            title: {
              formatter: function () {
                return "";
              },
            },
          },
          marker: {
            show: false,
          },
        },
      },
      defaultOptions: {
        animationData: animationData
      },
      sellersList: sellersList,
    };
  },
  components: {
    Layout,
    PageHeader,
    Multiselect,
    flatPickr,
    lottie: Lottie,
  },
  computed: {
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.sellersList.filter((data) => {
          return (
            data.balance.toLowerCase().includes(search) ||
            data.label.toLowerCase().includes(search) ||
            data.name.toLowerCase().includes(search)
          );
        });
      } else {
        return this.sellersList;
      }
    },
  }
};
</script>

<template>
  <Layout>
    <PageHeader title="Sellers" pageTitle="Ecommerce" />
    <BCard no-body>
      <BCardHeader class="border-0 rounded">
        <BRow class="g-2">
          <BCol xl="3">
            <div class="search-box">
              <input type="text" class="form-control search" placeholder="Search for sellers & owner name or something..."
                v-model="searchQuery" />
              <i class="ri-search-line search-icon"></i>
            </div>
          </BCol>
          <BCol xxl="3" class="ms-auto">
            <div>
              <Multiselect class="form-control" v-model="value" :close-on-select="true" :searchable="true"
                :create-option="true" :options="[
                  { value: '', label: 'Select Categories' },
                  { value: 'All', label: 'All' },
                  { value: 'Retailer', label: 'Retailer' },
                  { value: 'Health & Medicine', label: 'Health & Medicine' },
                  { value: 'Manufacturer', label: 'Manufacturer' },
                  { value: 'Food Service', label: 'Food Service' },
                  { value: 'Computers & Electronics', label: 'Computers & Electronics' },

                ]" />
            </div>
          </BCol>
          <BCol lg="auto">
            <div class="hstack gap-2">
              <BButton type="button" variant="secondary">
                <i class="ri-equalizer-fill me-1 align-bottom"></i> Filters
              </BButton>
              <BButton variant="primary" @click="modalShow = !modalShow">
                <i class="ri-add-fill me-1 align-bottom"></i> Add Seller
              </BButton>
            </div>
          </BCol>
        </BRow>
      </BCardHeader>
    </BCard>

    <BRow class="mt-4">
      <BCol xl="3" lg="6" v-for="(item, index) of resultQuery" :key="index">
        <BCard no-body class="ribbon-box right overflow-hidden">
          <BCardBody class="text-center p-4">
            <div class="ribbon ribbon-info ribbon-shape trending-ribbon" v-if="item.isTrending == true">
              <i class="ri-flashlight-fill text-white align-bottom"></i>
              <span class="trending-ribbon-text">Trending</span>
            </div>
            <img :src="item.img" alt="" height="45" />
            <h5 class="mb-1 mt-4">
              <router-link to="/ecommerce/seller-details" class="link-primary">{{ item.label }}</router-link>
            </h5>
            <p class="text-muted mb-4">{{ item.name }}</p>
            <BRow class="justify-content-center">
              <BCol lg="8">
                <apexchart class="apex-charts" dir="ltr" height="50" :series="item.series"
                  :options="{ ...chartOptions, ...{ colors: [item.chartcolor] } }"></apexchart>
              </BCol>
            </BRow>
            <BRow class="mt-4">
              <BCol lg="6" class="border-end-dashed border-end">
                <h5>{{ item.stock }}</h5>
                <span class="text-muted">Item Stock</span>
              </BCol>
              <BCol lg="6">
                <h5>{{ item.balance }}</h5>
                <span class="text-muted">Wallet Balance</span>
              </BCol>
            </BRow>
            <div class="mt-4">
              <router-link to="/ecommerce/seller-details" class="btn btn-light w-100">View Details</router-link>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow class="g-0 text-center text-sm-start align-items-center mb-3">
      <BCol sm="6">
        <div>
          <p class="mb-sm-0">Showing 1 to 8 of 12 entries</p>
        </div>
      </BCol>
      <BCol sm="6">
        <ul class="pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0">
          <li class="page-item disabled">
            <BLink href="#" class="page-link"><i class="mdi mdi-chevron-left"></i></BLink>
          </li>
          <li class="page-item active">
            <BLink href="#" class="page-link">1</BLink>
          </li>
          <li class="page-item">
            <BLink href="#" class="page-link"><i class="mdi mdi-chevron-right"></i></BLink>
          </li>
        </ul>
      </BCol>
    </BRow>

    <div id="noresult" class="d-none">
      <div class="text-center py-4">
        <lottie class="avatar-xl" colors="primary:#405189,secondary:#0ab39c" :options="defaultOptions" :height="75"
          :width="75" />
        <h5 class="mt-2">Sorry! No Result Found</h5>
        <p class="text-muted mb-0">We've searched more than 150+ sellers We did not find any sellers for you search.</p>
      </div>
    </div>

    <BModal v-model="modalShow" hide-footer body-class="p-0" title="Add Seller" size="lg" content-class="border-0 mt-3"
      modal-class="zoomIn" class="v-modal-custom" centered>
      <div class="modal-content border-0 mt-3">
      </div>
      <div class="modal-body">
        <BTabs nav-class="nav-tabs-custom nav-success p-2 pb-0 bg-light">
          <BTab title="Personal Details" class="nav-link py-3" active>
            <b-form action="#">
              <BRow>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="firstnameInput" class="form-label">First Name</label>
                    <input type="text" class="form-control" id="firstnameInput" placeholder="Enter your firstname" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="lastnameInput" class="form-label">Last Name</label>
                    <input type="text" class="form-control" id="lastnameInput" placeholder="Enter your lastname" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="contactnumberInput" class="form-label">Contact Number</label>
                    <input type="number" class="form-control" id="contactnumberInput" placeholder="Enter your number" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="phonenumberInput" class="form-label">Phone Number</label>
                    <input type="number" class="form-control" id="phonenumberInput" placeholder="Enter your number" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="emailidInput" class="form-label">Email</label>
                    <input type="email" class="form-control" id="emailidInput" placeholder="Enter your email" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="birthdayidInput" class="form-label">Date of Birth</label>
                    <flat-pickr v-model="date" placeholder="Enter your date of birth"
                      class="form-control flatpickr-input">
                    </flat-pickr>
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="cityidInput" class="form-label">City</label>
                    <input type="text" class="form-control" id="cityidInput" placeholder="Enter your city" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="countryidInput" class="form-label">Country</label>
                    <input type="text" class="form-control" id="countryidInput" placeholder="Enter your country" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="zipcodeidInput" class="form-label">Zip Code</label>
                    <input type="text" class="form-control" id="zipcodeidInput" placeholder="Enter your zipcode" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">Description</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
                      placeholder="Enter description"></textarea>
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="hstack gap-2 justify-content-end">
                    <BButton type="button" variant="link" class="link-success text-decoration-none fw-medium"
                      @click="modalShow = false">
                      <i class="ri-close-line me-1 align-middle"></i> Close
                    </BButton>
                    <BButton type="button" variant="primary">
                      <i class="ri-save-3-line align-bottom me-1"></i> Save
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </b-form>
          </BTab>
          <BTab title="Business Details" class="nav-link py-3">
            <b-form action="#">
              <BRow>
                <BCol lg="12">
                  <div class="mb-3">
                    <label for="companynameInput" class="form-label">Company Name</label>
                    <input type="text" class="form-control" id="companynameInput" placeholder="Enter your company name" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="choices-single-default" class="form-label">Company Type</label>
                    <select class="form-control" data-trigger name="choices-single-default" id="choices-single-default">
                      <option value="">Select type</option>
                      <option value="All" selected>All</option>
                      <option value="Merchandising">Merchandising</option>
                      <option value="Manufacturing">Manufacturing</option>
                      <option value="Partnership">Partnership</option>
                      <option value="Corporation">Corporation</option>
                    </select>
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="pancardInput" class="form-label">Pan Card Number</label>
                    <input type="text" class="form-control" id="pancardInput" placeholder="Enter your pan-card number" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="websiteInput" class="form-label">Website</label>
                    <input type="url" class="form-control" id="websiteInput" placeholder="Enter your URL" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="faxInput" class="form-label">Fax</label>
                    <input type="text" class="form-control" id="faxInput" placeholder="Enter your fax" />
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="mb-3">
                    <label for="companyemailInput" class="form-label">Email</label>
                    <input type="email" class="form-control" id="companyemailInput" placeholder="Enter your email" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="worknumberInput" class="form-label">Number</label>
                    <input type="number" class="form-control" id="worknumberInput" placeholder="Enter your number" />
                  </div>
                </BCol>
                <BCol lg="6">
                  <div class="mb-3">
                    <label for="companylogoInput" class="form-label">Company Logo</label>
                    <input type="file" class="form-control" id="companylogoInput" />
                  </div>
                </BCol>
                <BCol lg="12">
                  <div class="hstack gap-2 justify-content-end">
                    <BButton variant="link" class="link-success text-decoration-none fw-medium"
                      @click="modalShow = false">
                      <i class="ri-close-line me-1 align-middle"></i> Close
                    </BButton>
                    <BButton type="submit" variant="primary">
                      <i class="ri-save-3-line align-bottom me-1"></i> Save
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </b-form>
          </BTab>
          <BTab title="Bank Details" class="nav-link py-3">
            <b-form action="#">
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
                  <div class="hstack gap-2 justify-content-end">
                    <BButton variant="link" class="link-success text-decoration-none fw-medium"
                      @click="modalShow = false">
                      <i class="ri-close-line me-1 align-middle"></i> Close
                    </BButton>
                    <BButton type="submit" variant="primary">
                      <i class="ri-save-3-line align-bottom me-1"></i> Save
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </b-form>
          </BTab>
        </BTabs>
      </div>
    </BModal>
  </Layout>
</template>
