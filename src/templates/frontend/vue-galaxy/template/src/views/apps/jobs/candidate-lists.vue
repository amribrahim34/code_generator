<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { candidatelist } from "@/common/data";

export default {
  data() {
    return {
      searchQuery: null,
      page: 1,
      perPage: 8,
      pages: [],
      candidatelist: candidatelist
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.candidatelist);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.name.toLowerCase().includes(search) ||
            data.designation.toLowerCase().includes(search) ||
            data.type.toLowerCase().includes(search) ||
            data.ratingCount.toLowerCase().includes(search) ||
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
    candidatelist() {
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
    setPages() {
      let numberOfPages = Math.ceil(this.candidatelist.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(candidatelist) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return candidatelist.slice(from, to);
    }
  },
  components: {
    Layout,
    PageHeader,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="List View" pageTitle="Candidate Lists" />
    <BRow class="g-4 mb-4">
      <BCol sm="auto">
        <div>
          <BLink href="#!" class="btn btn-secondary"><i class="ri-add-line align-bottom me-1"></i> Add Candidate</BLink>
        </div>
      </BCol>
      <BCol sm>
        <div class="d-md-flex justify-content-sm-end gap-2">
          <div class="search-box ms-md-2 flex-shrink-0 mb-3 mb-md-0">
            <input type="text" class="form-control" id="searchJob" autocomplete="off"
              placeholder="Search for candidate name or designation..." v-model="searchQuery">
            <i class="ri-search-line search-icon"></i>
          </div>
          <div class="w-md">
            <select class="form-select" data-choices data-choices-search-false>
              <option value="All">All</option>
              <option value="Today">Today</option>
              <option value="Yesterday" selected>Yesterday</option>
              <option value="Last 7 Days">Last 7 Days</option>
              <option value="Last 30 Days">Last 30 Days</option>
              <option value="This Month">This Month</option>
              <option value="Last Year">Last Year</option>
            </select>
          </div>
        </div>
      </BCol>
    </BRow>

    <BRow class="gy-2 mb-2" id="candidate-list">
      <BCol lg="12" v-for="(data, index) of resultQuery" :key="index">
        <BCard no-body class="mb-0">
          <BCardBody>
            <div class="d-lg-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="avatar-sm rounded">
                  <img :src="data.img" alt="" class="member-img img-fluid d-block rounded">
                </div>
              </div>
              <div class="ms-3">
                <router-link to="/pages/profile">
                  <h5 class="fs-16 mb-2">{{ data.name }}</h5>
                </router-link>
                <p class="text-muted mb-0">{{ data.designation }}</p>
              </div>
              <div class="d-flex gap-4 mt-0 text-muted mx-auto">
                <div><i class="ri-map-pin-2-line text-primary me-1 align-bottom"></i> {{ data.location }}</div>
                <div><i class="ri-time-line text-primary me-1 align-bottom"></i> <span class="badge" :class="{
                  'bg-success-subtle text-success': data.type == 'Full Time',
                  'bg-danger-subtle text-danger': data.type == 'Part Time',
                  'bg-secondary-subtle text-secondary': data.type == 'Freelancer',
                }">{{ data.type }}</span></div>
              </div>
              <div class="d-flex flex-wrap gap-2 align-items-center mx-auto">
                <BBadge tag="div" variant="bg-success" class="text-bg-success"> <i class="mdi mdi-star me-1"></i>{{
                  data.rating
                }}</BBadge>
                <div class="text-muted">{{ data.ratingCount }} Ratings</div>
              </div>
              <div>
                <BLink href="#!" class="btn btn-soft-success me-1">View Details</BLink>
                <BLink href="#!" class="btn btn-ghost-danger btn-icon custom-toggle"
                  :class="{ 'active': data.bookmark == 'true', '': data.bookmark == 'false' }" data-bs-toggle="button"
                  aria-pressed="false">
                  <span class="icon-on"><i class="ri-bookmark-line align-bottom"></i></span>
                  <span class="icon-off"><i class="ri-bookmark-3-fill align-bottom"></i></span>
                </BLink>
              </div>
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