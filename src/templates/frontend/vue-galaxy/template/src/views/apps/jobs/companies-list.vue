<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { companiesList } from "@/common/data";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
  data() {
    return {
      page: 1,
      perPage: 16,
      pages: [],
      companies: companiesList,

      defaultDateConfig: {
        dateFormat: "d M, Y",
        defaultDate: "04 Sep, 2023",
      },
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.companies);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.name.toLowerCase().includes(search) ||
            data.industry_type.toLowerCase().includes(search) ||
            data.vacancy.toLowerCase().includes(search) ||
            data.since.toLowerCase().includes(search) ||
            data.rating.toLowerCase().includes(search) ||
            data.location.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    companies() {
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
      document.querySelector('.company-logo').setAttribute('src', data.image_src);
      document.querySelector('.overview-companyname').innerHTML = data.name;
      document.querySelector('.overview-industryType').innerHTML = data.industry_type;
      document.querySelector('.overview-companydesc').innerHTML = data.company_info;
      document.querySelector('.overview-company_location').innerHTML = data.location;
      document.querySelector('.overview-employee').innerHTML = data.employee;
      document.querySelector('.overview-vacancy').innerHTML = data.vacancy;
      document.querySelector('.overview-rating').innerHTML = data.rating;
      document.querySelector('.overview-website').innerHTML = data.website;
      document.querySelector('.overview-email').innerHTML = data.email;
      document.querySelector('.overview-since').innerHTML = data.since;
    },

    setPages() {
      let numberOfPages = Math.ceil(this.companies.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(companies) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return companies.slice(from, to);
    },
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
    <PageHeader title="Companies List" pageTitle="Companies" />
    <BRow>
      <BCol xxl="9">
        <BCard no-body>
          <BCardBody>
            <BForm>
              <BRow class="g-3">
                <BCol xxl="5" sm="6">
                  <div class="search-box">
                    <input type="text" class="form-control search bg-light border-light" id="searchCompany"
                      placeholder="Search for company, industry type...">
                    <i class="ri-search-line search-icon"></i>
                  </div>
                </BCol>

                <BCol xxl="3" sm="6">
                  <flat-pickr v-model="date10" :config="defaultDateConfig"
                    class="form-control bg-light border-light  flatpickr-input"></flat-pickr>
                </BCol>

                <BCol xxl="2" sm="4">
                  <div class="input-light">
                    <select class="form-control bg-light border-light" data-choices data-choices-search-false
                      name="choices-single-default" id="idType">
                      <option value="all" selected>All</option>
                      <option value="Full Time">Full Time</option>
                      <option value="Part Time">Part Time</option>
                      <option value="Internship">Internship</option>
                      <option value="Freelance">Freelance</option>
                    </select>
                  </div>
                </BCol>

                <BCol xxl="2" sm="4">
                  <BButton type="button" variant="primary" class="w-100" >
                    <i class="ri-equalizer-fill me-1 align-bottom"></i> Filters
                  </BButton>
                </BCol>
              </BRow>
            </BForm>
          </BCardBody>
        </BCard>

        <BRow class="job-list-row" id="companies-list">

          <BCol xxl="3" md="6" v-for="(data, index) of resultQuery" :key="index">
            <BCard no-body class="companiesList-card">
              <BCardBody>
                <div class="avatar-sm mx-auto">
                  <div class="avatar-title bg-light rounded">
                    <img :src="data.image_src" alt="" class="avatar-xxs companyLogo-img">
                  </div>
                </div>
                <div class="text-center">
                  <BLink href="#!">
                    <h5 class="mt-3 company-name">{{ data.name }}</h5>
                  </BLink>
                  <div class="d-none company-desc">{{ data.company_info }}
                  </div>
                  <p class="text-muted industry-type">{{ data.industry_type }}</p>
                  <div class="d-none"> <span class="employee">{{ data.employee }}</span>
                    <span class="location">{{ data.location }}</span>
                    <span class="rating">{{ data.rating }}</span>
                    <span class="website">{{ data.website }}</span>
                    <span class="email">{{ data.email }}</span>
                    <span class="since">{{ data.since }}</span>
                  </div>
                </div>
                <div>
                  <BButton type="button" variant="soft-primary" class="w-100 viewcompany-list" @click="showdetail(data)">
                    <span class="vacancy">{{
                      data.vacancy
                    }}</span> Jobs Available</BButton>
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
                <BLink href="javascript:void(0);" class="page-link" id="page-prev" :disabled="page <= 1" @click="page--">
                  Previous</BLink>
              </div>
              <span id="page-num" class="pagination">

                <span id="page-num" class="pagination">
                  <div class="page-item" :class="{ active: pageNumber == page, disabled: pageNumber == '...', }"
                    v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber">
                    <BLink class="page-link clickPageNumber" href="javascript:void(0);">{{ pageNumber }}</BLink>
                  </div>
                </span>


              </span>
              <div class="page-item">
                <BLink href="javascript:void(0);" class="page-link" id="page-next" :disabled="page >= pages.length"
                  @click="page++">Next</BLink>
              </div>
            </div>
          </BCol>
        </BRow>
      </BCol>

      <BCol xxl="3">
        <BCard no-body id="company-overview">
          <BCardBody>
            <div class="avatar-lg mx-auto mb-3">
              <div class="avatar-title bg-light rounded">
                <img src="@/assets/images/companies/img-6.png" alt="" class="avatar-sm company-logo" id="company-logo">
              </div>
            </div>

            <div class="text-center">
              <BLink href="#!">
                <h5 class="overview-companyname" id="overview-companyname">Syntyce Solutions</h5>
              </BLink>
              <p class="text-muted overview-industryType" id="overview-industryType">IT Department</p>

              <ul class="list-inline mb-0">
                <li class="list-inline-item avatar-xs">
                  <BLink href="javascript:void(0);" class="avatar-title bg-success-subtle text-success fs-15 rounded">
                    <i class="ri-global-line"></i>
                  </BLink>
                </li>
                <li class="list-inline-item avatar-xs">
                  <BLink href="javascript:void(0);" class="avatar-title bg-danger-subtle text-danger fs-15 rounded">
                    <i class="ri-mail-line"></i>
                  </BLink>
                </li>
                <li class="list-inline-item avatar-xs">
                  <BLink href="javascript:void(0);" class="avatar-title bg-warning-subtle text-warning fs-15 rounded">
                    <i class="ri-question-answer-line"></i>
                  </BLink>
                </li>
              </ul>
            </div>
          </BCardBody>

          <BCardBody>
            <h6 class="text-muted text-uppercase fw-semibold mb-3">Information</h6>
            <p class="text-muted mb-4 overview-companydesc" id="overview-companydesc">The IT department of a company
              ensures that the network of
              computers within the organization are well-connected and functioning properly. All the other departments
              within the company rely on them to ensure that their respective functions can go on seamlessly.</p>

            <div class="table-responsive table-card">
              <table class="table table-borderless mb-4">
                <tbody>
                  <tr>
                    <td class="fw-medium" scope="row">Industry Type</td>
                    <td class="overview-industryType" id="overview-industryType">Chemical Industries</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Location</td>
                    <td class="overview-company_location" id="overview-company_location">Damascus, Syria</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Employee</td>
                    <td class="overview-employee" id="overview-employee">10-50</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Vacancy</td>
                    <td class="overview-vacancy" id="overview-vacancy">23</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Rating</td>
                    <td><span class="overview-rating" id="overview-rating">4.8</span> <i
                        class="ri-star-fill text-warning align-bottom"></i>
                    </td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Website</td>
                    <td>
                      <BLink href="javascript:void(0);" class="link-primary text-decoration-underline overview-website"
                        id="overview-website">www.syntycesolution.com</BLink>
                    </td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Contact Email</td>
                    <td class="overview-email" id="overview-email">info@syntycesolution.com</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Since</td>
                    <td class="overview-since" id="overview-since">1995</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="hstack gap-3">
              <BButton type="button" variant="soft-success" class="custom-toggle w-100" data-bs-toggle="button">
                <span class="icon-on"><i class="ri-add-line align-bottom me-1"></i> Follow</span>
                <span class="icon-off"><i class="ri-user-unfollow-line align-bottom me-1"></i> Unfollow</span>
              </BButton>
              <BLink href="#!" class="btn btn-primary w-100">More View <i class="ri-arrow-right-line align-bottom"></i>
              </BLink>
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body class="overflow-hidden shadow-none card-border-effect-none border-0">
          <BCardBody class="bg-danger-subtle">
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="avatar-sm">
                  <div class="avatar-title bg-danger-subtle text-danger rounded-circle fs-17">
                    <i class="ri-gift-line"></i>
                  </div>
                </div>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="fs-16">Free trial</h6>
                <p class="text-muted mb-0">28 days left</p>
              </div>
              <div>
                <router-link to="/pages/pricing" class="btn btn-danger">Upgrade</router-link>
              </div>
            </div>
          </BCardBody>
          <BCardBody class="bg-danger-subtle border-top border-danger border-opacity-25 border-top-dashed">
            <BLink href="#!" class="d-flex justify-content-between align-items-center text-body">
              <span>See benefits</span>
              <i class="ri-arrow-right-s-line fs-18"></i>
            </BLink>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>