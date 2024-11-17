<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { jobgrid } from "@/common/data";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
  data() {
    return {
      searchQuery: null,
      page: 1,
      perPage: 7,
      value: null,
      value1: null,
      status: null,
      status1: null,
      pages: [],
      jobgrid: jobgrid,

      rangeDateconfig: {
        mode: "range",
        dateFormat: "d M, Y",
      },
    };

  },
  computed: {
    displayedPosts() {
      return this.paginate(this.jobgrid);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.name.toLowerCase().includes(search) ||
            data.designation.toLowerCase().includes(search) ||
            data.postDate.toLowerCase().includes(search) ||
            data.description.toLowerCase().includes(search) ||
            data.location.toLowerCase().includes(search)
          );
        });
      } else if (this.status !== null || this.value !== null) {
        return this.displayedPosts.filter((data) => {
          if (this.status != null && this.value != null) {
            if (data.tags.includes(this.value)) {
              if (this.status == data.status) {
                return data;
              } else if (this.status == 'All') {
                return data;
              }
            } else if (this.value == 'All' && this.status == 'All') {
              return data;
            } else if (this.value == 'All') {
              if (data.status == this.status) {
                return data;
              }
            }
          } else if (this.status === data.status) {
            return data;
          } else if (data.tags.includes(this.value)) {
            return data;
          }
          else {
            return null;
          }
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    jobgrid() {
      this.setPages();
    },
  },
  created() {
    this.setPages();
  },
  mounted() {
    document.querySelectorAll(".float-end").forEach((item) => {

      item.addEventListener('click', function () {
        if (item.classList.contains("active")) {
          item.classList.remove("active")
        } else {
          item.classList.add("active")
        }
      });
    })
  },
  methods: {
    SearchData() {
      this.resultQuery;
      this.status = this.status1;
      this.value = this.value1;
    },
    setPages() {
      let numberOfPages = Math.ceil(this.jobgrid.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(jobgrid) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return jobgrid.slice(from, to);
    }
  },
  components: {
    Layout,
    PageHeader,
    flatPickr
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Job Grid Lists" pageTitle="Jobs" />
    <BRow>
      <BCol lg="12">
        <BCard no-body>
          <BCardBody class="bg-light-subtle">
            <BForm>
              <BRow class="g-3">
                <BCol xxl="4" sm="12">
                  <div class="search-box">
                    <input type="text" class="form-control search bg-light border-light" id="searchJob" autocomplete="off"
                      placeholder="Search for jobs or companies..." v-model="searchQuery">
                    <i class="ri-search-line search-icon"></i>
                  </div>
                </BCol>

                <BCol xxl="3" sm="4">
                  <flat-pickr v-model="date6" :config="rangeDateconfig" class="form-control bg-light border-light"
                    placeholder="Select date"></flat-pickr>
                </BCol>

                <BCol xxl="2" sm="4">
                  <div class="input-light">
                    <select class="form-control bg-light border-light" data-choices data-choices-search-false name="choices-idType" id="idType"
                      v-model="value1">
                      <option value="All" selected>All</option>
                      <option value="Full Time">Full Time</option>
                      <option value="Part Time">Part Time</option>
                      <option value="Internship">Internship</option>
                      <option value="Freelance">Freelance</option>
                    </select>
                  </div>
                </BCol>
                <BCol xxl="2" sm="4">
                  <div class="input-light">
                    <select class="form-control bg-light border-light" data-choices data-choices-search-false name="choices-single-default"
                      id="idStatus" v-model="status1">
                      <option value="All" selected>All</option>
                      <option value="Active">Active</option>
                      <option value="New">New</option>
                      <option value="Close">Close</option>
                    </select>
                  </div>
                </BCol>
                <BCol xxl="1" sm="4">
                  <BButton type="button" variant="primary" class="w-100" @click="SearchData">
                    <i class="ri-equalizer-fill me-1 align-bottom"></i> Filters
                  </BButton>
                </BCol>
              </BRow>
            </BForm>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
    <BRow>
      <BCol lg="12">
        <div class="d-flex align-items-center mb-4">
          <div class="flex-grow-1">
            <p class="text-muted fs-14 mb-0">Result: <span id="total-result">{{ resultQuery.length }}</span></p>
          </div>
          <div class="flex-shrink-0">

            <div class="d-flex flex-wrap gap-3">
              <BDropdown variant="link" text="All View" class="text-muted">
                <BDropdownItem href="#">Action</BDropdownItem>
                <BDropdownItem href="#">Another action</BDropdownItem>
                <BDropdownItem href="#">Something else here</BDropdownItem>
              </BDropdown>
            </div>
          </div>
        </div>
      </BCol>
    </BRow>
    <BRow id="job-list">
      <BCol lg="3" md="6" id="job-widget" style="display: block;">
        <BCard no-body class="card-height-100 bg-info bg-job">
          <BCardBody class="p-5">
            <h2 class="lh-base text-white">Velzon invites young professionals for an Internship!</h2>
            <p class="text-white text-opacity-75 mb-0 fs-14">Don't miss your opportunity to improve your skills!</p>
            <div class="mt-5 pt-2">
              <BButton type="button" variant="light" class="w-100">
                View More
                <i class="ri-arrow-right-line align-bottom"></i>
              </BButton>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol lg="3" md="6" v-for="(data, index) of resultQuery" :key="index">
        <BCard no-body>
          <BCardBody>
            <BButton type="button" variant="soft-primary" class="btn-icon float-end" data-bs-toggle="button"
              aria-pressed="true">
              <i class="mdi mdi-cards-heart fs-16"></i>
            </BButton>
            <div class="avatar-sm mb-4">
              <div class="avatar-title bg-light rounded"> <img :src="data.img" alt="" class="avatar-xxs"> </div>
            </div>
            <BLink href="#!">
              <h5>{{ data.designation }}</h5>
            </BLink>
            <p class="text-muted">{{ data.name }}</p>
            <div class="d-flex gap-4 mb-3">
              <div><i class="ri-map-pin-2-line text-primary me-1 align-bottom"></i>{{ data.location }}</div>
              <div><i class="ri-time-line text-primary me-1 align-bottom"></i>{{ data.postDate }}</div>
            </div>
            <p class="text-muted">{{ data.description }}</p>
            <div class="hstack gap-2">
              <span v-for="(tag, index) of data.tags" :key="index">
                &nbsp;<span class="badge" :class="{
                  'bg-success-subtle text-success': tag == 'Full Time',
                  'bg-warning-subtle text-warning': tag == 'Part Time',
                  'bg-danger-subtle text-danger': tag == 'Urgent',
                  'bg-primary-subtle text-primary': tag == 'Freelance',
                  'bg-info-subtle text-info': tag == 'Private'
                }"> {{ tag }}</span>
              </span>
            </div>
            <div class="mt-4 hstack gap-2">
              <BLink href="#!" class="btn btn-soft-primary w-100">Apply Job</BLink>
              <router-link to="/jobs/details" class="btn btn-soft-success w-100">Overview</router-link>
            </div>
          </BCardBody>
        </BCard>
      </BCol>


    </BRow>
    <BRow class="g-0 justify-content-end mb-4" id="pagination-element">
      <BCol sm="6">
        <div
          class="pagination-block pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
          v-if="pages.length > 1">
          <div class="page-item">
            <BLink href="#" class="page-link" id="page-prev" :disabled="page <= 1" @click="page--">Previous</BLink>
          </div>
          <span id="page-num" class="pagination">
            <div class="page-item" :class="{ active: pageNumber == page, disabled: pageNumber == '...', }"
              v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber">
              <BLink class="page-link clickPageNumber" href="javascript:void(0);">{{ pageNumber }}</BLink>
            </div>
          </span>
          <div class="page-item">
            <BLink href="#" class="page-link" id="page-next" :disabled="page >= pages.length" @click="page++">Next</BLink>
          </div>
        </div>
      </BCol>
    </BRow>
  </Layout>
</template>