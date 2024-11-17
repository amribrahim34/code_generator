<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { candidategrid } from "@/common/data";

export default {
  data() {
    return {
      searchQuery: null,
      page: 1,
      perPage: 20,
      pages: [],
      candidategrid: candidategrid
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.candidategrid);
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
    candidategrid() {
      this.setPages();
    },
  },
  created() {
    this.setPages();
  },
  methods: {
    setPages() {
      let numberOfPages = Math.ceil(this.candidategrid.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(candidategrid) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return candidategrid.slice(from, to);
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
    <PageHeader title="Grid View" pageTitle="Candidate Lists" />
    <BRow class="g-4 mb-3">
      <BCol sm="auto">
        <div>
          <BLink href="#!" class="btn btn-primary"><i class="ri-add-line align-bottom me-1"></i> Add Candidate</BLink>
        </div>
      </BCol>
      <BCol sm>
        <div class="d-md-flex justify-content-sm-end gap-2">
          <div class="search-box ms-md-2 flex-shrink-0 mb-3 mb-md-0">
            <input type="text" class="form-control" id="searchJob"
              placeholder="Search for candidate name or designation..." autocomplete="off" v-model="searchQuery">
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

    <BRow class="job-list-row" id="candidate-list">

      <BCol xxl="3" md="6" v-for="(data, index) of resultQuery" :key="index">
        <BCard no-body>
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="avatar-lg rounded">
                  <img :src="data.img" alt="" class="member-img img-fluid d-block rounded">
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <router-link to="/pages/profile">
                  <h5 class="fs-16 mb-1">{{ data.name }}</h5>
                </router-link>
                <p class="text-muted mb-2">{{ data.designation }}</p>
                <div class="d-flex flex-wrap gap-2 align-items-center">
                  <BBadge variant="success" class="text-bg-success"><i class="mdi mdi-star me-1"></i>{{ data.rating
                  }}</BBadge>
                  <div class="text-muted">{{ data.ratingCount }} Ratings</div>
                </div>
                <div class="d-flex gap-4 mt-2 text-muted">
                  <div> <i class="ri-map-pin-2-line text-primary me-1 align-bottom"></i> {{ data.location }}</div>
                  <div> <i class="ri-time-line text-primary me-1 align-bottom"></i>
                    <span class="badge" :class="{
                      'bg-success-subtle text-success': data.type == 'Full Time',
                      'bg-danger-subtle text-danger': data.type == 'Part Time',
                      'bg-primary-subtle text-primary': data.type == 'Freelancer',
                    }">{{ data.type }}</span>
                  </div>
                </div>
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