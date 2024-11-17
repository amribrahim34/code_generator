<script>
import getChartColorsArray from "@/common/getChartColorsArray";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";
import { joblist } from "@/common/data";

export default {
  data() {
    return {
      createJobModal: false,
      searchQuery: null,
      jobvalue: null,
      tagvalue: null,
      tagoption: [{
        value: 'Design',
        label: 'Design'
      },
      {
        value: 'Remote',
        label: 'Remote'
      },
      {
        value: 'UI/UX Designer',
        label: 'UI/UX Designer'
      },
      {
        value: 'Designer',
        label: 'Designer'
      },
      ],
      page: 1,
      perPage: 3,
      pages: [],
      joblist: joblist,

      series: [98, 63, 35],
      chartOptions: {
        labels: ["New Application", "Approved", "Rejected"],
        chart: {
          height: 300,
          type: "donut",
        },
        legend: {
          position: "bottom",
        },
        stroke: {
          show: false,
        },
        dataLabels: {
          dropShadow: {
            enabled: false,
          },
        },
        colors: getChartColorsArray('["--vz-info", "--vz-primary", "--vz-danger", "--vz-danger", "--vz-info"]'),
      },
      //
      submitted: false,
      event: {
        id: "",
        img: "",
        logo: "",
        designation: "",
        name: "",
        description: "",
        tags: [],
        type: "",
        experience: "",
        location: "",
        applied: "",
        post: "",
        salary: ""
      },

      //
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.joblist);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.designation.toLowerCase().includes(search) ||
            data.name.toLowerCase().includes(search) ||
            data.description.toLowerCase().includes(search) ||
            data.type.toLowerCase().includes(search) ||
            data.experience.toLowerCase().includes(search) ||
            data.location.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },

  watch: {
    joblist() {
      this.setPages();
    },
  },
  created() {
    this.setPages();
  },
  mounted() {
    document.querySelectorAll(".custom-toggle").forEach((item) => {

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
    showdetail(data) {
      document.getElementById('cover-img').setAttribute('src', data.img);
      document.querySelector('.view-companylogo').setAttribute('src', data.logo);
      document.querySelector('.view-title').innerHTML = data.designation;
      document.querySelector('.view-companyname').innerHTML = data.name;
      document.querySelector('.view-location').innerHTML = data.location;
      document.querySelector('.view-desc').innerHTML = data.description;
      document.querySelector('.view-type').innerHTML = data.type;
      document.querySelector('.view-postdate').innerHTML = data.postDate;
      document.querySelector('.view-experience').innerHTML = data.experience;
    },

    setPages() {
      let numberOfPages = Math.ceil(this.joblist.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },

    paginate(joblist) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return joblist.slice(from, to);
    },

    // 
    handleSubmit() {
      this.submitted = true;
      if (this.submitted && (this.event.name && this.event.designation && this.event.experience && this.event.location && this.event.type && this.event.tags && this.event.salary && this.event.description)) {
        const data = {
          id: (Math.floor(Math.random() * 100 + 20) - 20),
          img: require("@/assets/images/small/img-9.jpg"),
          logo: require("@/assets/images/users/multi-user.jpg"),
          applied: "0 Applied",
          postDate: new Date().toUTCString().slice(5, 16),
          ...this.event
        };
        this.joblist.unshift(data);
        this.createJobModal = false;
      }
    },

    toggleModal() {
      this.createJobModal = true;
      this.event = {};

      this.submitted = false;
    },
    //
  },
  components: {
    Layout,
    PageHeader,
    Multiselect
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Job Lists" pageTitle="Base UI" />
    <BRow>
      <BCol lg="12">
        <BCard no-body>
          <BCardBody class="bg-light-subtle">
            <div class="d-flex align-items-center">
              <h6 class="card-title mb-0 flex-grow-1">Search Jobs</h6>
              <div class="flex-shrink-0">
                <BButton variant="primary" @click="toggleModal"><i class="ri-add-line align-bottom me-1"></i> Create New
                  Job</BButton>
              </div>
            </div>

            <BRow class="mt-3 gy-3">
              <BCol xxl="10" md="6">
                <div class="search-box">
                  <input type="text" class="form-control search bg-light border-light" id="searchJob" autocomplete="off"
                    placeholder="Search for jobs or companies..." v-model="searchQuery">
                  <i class="ri-search-line search-icon"></i>
                </div>
              </BCol>
              <BCol xxl="2" md="6">
                <div class="input-light">
                  <select class="form-control" data-choices data-choices-search-false name="choices-single-default"
                    id="idStatus">
                    <option value="All">All Selected</option>
                    <option value="Newest" selected>Newest</option>
                    <option value="Popular">Popular</option>
                    <option value="Oldest">Oldest</option>
                  </select>
                </div>
              </BCol>
              <BCol xl="12" id="found-job-alert" v-if="resultQuery >= 0">
                <div class="alert alert-success mb-0 text-center" role="alert">
                  <strong id="total-result">{{ resultQuery.length }}</strong> jobs found
                </div>
              </BCol>
            </BRow>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="9">
        <div id="job-list">
          <BCard no-body class="joblist-card" v-for="(data, index) of resultQuery" :key="index">
            <BCardBody>
              <div class="d-flex mb-4">
                <div class="avatar-sm">
                  <div class="avatar-title bg-light rounded"> <img :src="data.logo" alt=""
                      class="avatar-xxs companyLogo-img"> </div>
                </div>
                <div class="ms-3 flex-grow-1"> <img :src="data.img" alt="" class="d-none cover-img">
                  <BLink href="#!">
                    <h5 class="job-title">{{ data.designation }}</h5>
                  </BLink>
                  <p class="company-name text-muted mb-0">{{ data.name }}</p>
                </div>
                <div>
                  <BButton type="button" variant="ghost-primary" class="btn-icon custom-toggle" data-bs-toggle="button">
                    <span class="icon-on"><i class="ri-bookmark-line"></i></span>
                    <span class="icon-off"><i class="ri-bookmark-fill"></i></span>
                  </BButton>
                </div>
              </div>
              <p class="text-muted job-description">{{ data.description }}</p>
              <div>
                <span v-for="(tag, index) of data.tags" :key="index">
                  &nbsp;<BBadge variant="primary-subtle" class="bg-primary-subtle text-primary me-1"> {{ tag }}</BBadge>
                </span>
              </div>
            </BCardBody>
            <BCardFooter class="border-top-dashed">
              <div class="d-flex justify-content-between align-items-center flex-wrap gap-3">
                <div><i class="ri-briefcase-2-line align-bottom me-1"></i> <span class="job-type">{{ data.type }}</span>
                </div>
                <div class="d-none"><span class="job-experience">{{ data.experience }}</span></div>
                <div><i class="ri-map-pin-2-line align-bottom me-1"></i> <span class="job-location">{{ data.location
                }}</span></div>
                <div><i class="ri-user-3-line align-bottom me-1"></i> {{ data.applied }}</div>
                <div><i class="ri-time-line align-bottom me-1"></i> <span class="job-postdate">{{ data.postDate
                }}</span>
                </div>
                <div>
                  <BLink href="#!" class="btn btn-primary viewjob-list" @click="showdetail(data)">View More <i
                      class="ri-arrow-right-line align-bottom ms-1"></i></BLink>
                </div>
              </div>
            </BCardFooter>
          </BCard>

        </div>
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
                <BLink href="#" class="page-link" id="page-next" :disabled="page >= pages.length" @click="page++">Next
                </BLink>
              </div>
            </div>
          </BCol>
        </BRow>
      </BCol>

      <BCol xxl="3">
        <BCard no-body class="job-list-view-card overflow-hidden" id="job-overview">
          <img src="@/assets/images/small/img-10.jpg" alt="" id="cover-img" class="img-fluid background object-fit-cover">
          <BCardBody>
            <div class="avatar-md mt-n5">
              <div class="avatar-title bg-light rounded-circle">
                <img src="@/assets/images/companies/img-7.png" alt="" class="avatar-xs view-companylogo">
              </div>
            </div>
            <div class="mt-3">
              <h5 class="view-title">Product Designer</h5>
              <div class="hstack gap-3 mb-3">
                <span class="text-muted"><i class="ri-building-line me-1 align-bottom"></i> <span
                    class="view-companyname">Themesbrand</span></span>
                <span class="text-muted"><i class="ri-map-pin-2-line me-1 align-bottom"></i> <span
                    class="view-location">United Kingdom</span></span>
              </div>
              <p class="text-muted view-desc">A UI/UX designer's job is to create user-friendly interfaces that enable
                users to understand how to use complex technical products. If you're passionate about the latest
                technology trends and devices, you'll find great fulfillment in being involved in the design process for
                the next hot gadget.</p>
              <div class="py-3 border border-dashed border-start-0 border-end-0 mt-4">
                <BRow>
                  <BCol lg="4" sm="6">
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">Job Type</p>
                      <h5 class="fs-14 mb-0 view-type">Full Time</h5>
                    </div>
                  </BCol>
                  <BCol lg="4" sm="6">
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">Post Date</p>
                      <h5 class="fs-14 mb-0 view-postdate">15 Sep, 2022</h5>
                    </div>
                  </BCol>
                  <BCol lg="4" sm="6">
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">Experience</p>
                      <h5 class="fs-14 mb-0 view-experience">0 - 5 Year</h5>
                    </div>
                  </BCol>
                </BRow>
              </div>
            </div>

            <div class="mt-4">
              <h5 class="mb-3">Application Summary</h5>

              <div>
                <apexchart class="apex-charts" dir="ltr" height="300" :series="series" :options="chartOptions">
                </apexchart>
              </div>
            </div>
            <div class="mt-4">
              <BButton type="button" variant="success" class="w-100">Apply Now</BButton>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>


    <BModal v-model="createJobModal" id="CreateJobModal" size="lg" hide-footer hide-header class="v-modal-custom"
      centered>
      <BForm id="createjobform" autocomplete="off" class="needs-validation" novalidate>
        <input type="hidden" id="id-field" />
        <BRow class="g-3">
          <BCol lg="12">
            <div class="px-1 pt-1">
              <div class="modal-team-cover position-relative mb-0 mt-n4 mx-n4 rounded-top overflow-hidden">
                <img src="@/assets/images/small/img-9.jpg" alt="" id="modal-cover-img" class="img-fluid">

                <div class="d-flex position-absolute start-0 end-0 top-0 p-3">
                  <div class="flex-grow-1">
                    <h5 class="modal-title text-white" id="exampleModalLabel">Create New Job</h5>
                  </div>
                  <div class="flex-shrink-0">
                    <div class="d-flex gap-3 align-items-center">
                      <div>
                        <label for="cover-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="top"
                          title="Select Cover Image">
                          <div class="avatar-xs">
                            <div class="avatar-title bg-light border rounded-circle text-muted cursor-pointer">
                              <i class="ri-image-fill"></i>
                            </div>
                          </div>
                        </label>
                        <input class="form-control d-none" value="" id="cover-image-input" type="file"
                          accept="image/png, image/gif, image/jpeg">
                      </div>
                      <BButton class="btn-close btn-close-white" id="close-jobListModal" @click="createJobModal = false">
                      </BButton>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="text-center mb-4 mt-n5 pt-2">
              <div class="position-relative d-inline-block">
                <div class="position-absolute bottom-0 end-0">
                  <label for="companylogo-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="right"
                    title="Select Image">
                    <div class="avatar-xs cursor-pointer">
                      <div class="avatar-title bg-light border rounded-circle text-muted">
                        <i class="ri-image-fill"></i>
                      </div>
                    </div>
                  </label>
                  <input class="form-control d-none" value="" id="companylogo-image-input" type="file"
                    accept="image/png, image/gif, image/jpeg">
                </div>
                <div class="avatar-lg p-1">
                  <div class="avatar-title bg-light rounded-circle">
                    <img src="@/assets/images/users/multi-user.jpg" id="companylogo-img"
                      class="avatar-md rounded-circle object-fit-cover" />
                  </div>
                </div>
              </div>
              <h5 class="fs-13 mt-3">Company Logo</h5>
            </div>
            <div>
              <label for="jobtitle-field" class="form-label">Job Title</label>
              <input type="text" id="jobtitle-field" class="form-control" placeholder="Enter job title"
                v-model="event.designation" :class="{ 'is-invalid': submitted && !event.designation }" />
              <div class="invalid-feedback">Please enter a designation.</div>
            </div>
          </BCol>
          <BCol lg="6">
            <div>
              <label for="companyname-field" class="form-label">Company Name</label>
              <input type="text" id="companyname-field" class="form-control" placeholder="Enter company name"
                v-model="event.name" :class="{ 'is-invalid': submitted && !event.name }" />
              <div class="invalid-feedback">Please enter a company name.</div>
            </div>
          </BCol>
          <BCol lg="6">
            <div>
              <label for="job_type-field" class="form-label">Job Type</label>
              <Multiselect placeholder="Select Job Type" :options="['Full Time', 'Part Time', 'Freelance', 'Internship']"
                v-model="event.type" :class="{ 'is-invalid': submitted && !event.type }" />
              <div class="invalid-feedback">Please select a job type.</div>
            </div>
          </BCol>
          <BCol lg="4">
            <div>
              <label for="experience-field" class="form-label">Experience</label>
              <input type="text" id="experience-field" class="form-control" placeholder="Enter experience"
                v-model="event.experience" :class="{ 'is-invalid': submitted && !event.experience }" />
              <div class="invalid-feedback">Please enter a experience.</div>
            </div>
          </BCol>
          <BCol lg="4">
            <div>
              <label for="location-field" class="form-label">Location</label>
              <input type="text" id="location-field" class="form-control" placeholder="Enter location"
                v-model="event.location" :class="{ 'is-invalid': submitted && !event.location }" />
              <div class="invalid-feedback">Please enter a location.</div>
            </div>
          </BCol>
          <BCol lg="4">
            <div>
              <label for="Salary-field" class="form-label">Salary</label>
              <input type="number" id="Salary-field" class="form-control" placeholder="Enter salary"
                v-model="event.salary" :class="{ 'is-invalid': submitted && !event.salary }" />
              <div class="invalid-feedback">Please enter a salary.</div>
            </div>
          </BCol>
          <BCol lg="12">
            <div>
              <label for="website-field" class="form-label">Tags</label>
              <Multiselect mode="tags" :close-on-select="true" :searchable="true" id="taginput-choices"
                :create-option="false" :options="tagoption" v-model="event.tags"
                :class="{ 'is-invalid': submitted && !event.tags }" />
              <div class="invalid-feedback">Please select a tags.</div>
            </div>
          </BCol>
          <BCol lg="12">
            <div>
              <label for="description-field" class="form-label">Description</label>
              <textarea class="form-control" id="description-field" rows="3" placeholder="Enter description"
                v-model="event.description" :class="{ 'is-invalid': submitted && !event.description }"></textarea>
              <div class="invalid-feedback">Please enter a description.</div>
            </div>
          </BCol>
        </BRow>
        <div class="hstack gap-2 justify-content-end mt-3">
          <BButton type="button" variant="light" @click="createJobModal = false" id="edtclosemodal">Close</BButton>
          <BButton type="button" variant="success" id="add-btn" @click="handleSubmit">Add Job</BButton>
        </div>
      </BForm>
    </BModal>
  </Layout>
</template>