<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/msoeawqm.json";
import { cryptoOrders } from "@/common/data";

export default {
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Multiselect,
    flatPickr,
  },
  data() {
    return {
      rangeDateconfig: {
        mode: "range",
        dateFormat: "d M, Y",
      },
      date: null,
      date2: null,
      value: null,
      value2: null,
      status: null,
      status1: null,
      searchQuery: null,
      posts: cryptoOrders,
      page: 1,
      perPage: 10,
      pages: [],
      defaultOptions: { animationData: animationData },
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.posts);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.coinName.toLowerCase().includes(search) ||
            data.date[0].toLowerCase().includes(search) ||
            data.date[1].toLowerCase().includes(search) ||
            data.type.toLowerCase().includes(search) ||
            data.quantity.toLowerCase().includes(search) ||
            data.orderValue.toLowerCase().includes(search) ||
            data.avgPrice.toLowerCase().includes(search) ||
            data.price.toLowerCase().includes(search) ||
            data.status.toLowerCase().includes(search)
          );
        });
      } else if (this.status !== null || this.value !== null) {
        return this.displayedPosts.filter((data) => {
          if (this.status != null && this.value != null) {
            if (this.status === data.status) {
              if (this.value === data.type) {
                return data;
              }
            }
          } else if (this.status === data.status) {
            return data;
          } else if (this.value === data.type) {
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
    posts() {
      this.setPages();
    },
  },
  created() {
    this.setPages();
  },
  filters: {
    trimWords(value) {
      return value.split(" ").splice(0, 20).join(" ") + "...";
    },
  },
  methods: {
    setPages() {
      let numberOfPages = Math.ceil(this.posts.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(posts) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return posts.slice(from, to);
    },
    SearchData() {
      this.resultQuery;
      this.status = this.status1;
      this.value = this.value2;
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.posts];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.posts = sortedArray;
    },

    
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Orders" pageTitle="Crypto" />
    <BRow id="contactList">
      <BCol lg="12">
        <BCard no-body>
          <BCardHeader class="d-flex align-items-center border-0">
            <h5 class="card-title mb-0 flex-grow-1">All Orders</h5>
            <div class="flex-shrink-0">
              <div class="flax-shrink-0 hstack gap-2">
                <BButton variant="primary">Today's Orders</BButton>
                <BButton variant="soft-secondary">Past Orders</BButton>
              </div>
            </div>
          </BCardHeader>
          <BCardBody class="border border-dashed border-end-0 border-start-0">
            <BRow class="g-2">
              <BCol xl="4" md="6">
                <div class="search-box">
                  <input type="text" class="form-control search" placeholder="Search to orders..."
                    v-model="searchQuery" />
                  <i class="ri-search-line search-icon"></i>
                </div>
              </BCol>
              <BCol xl="3" md="6">
                <div class="input-group">
                  <span class="input-group-text" id="basic-addon1"><i class="ri-calendar-2-line"></i></span>

                  <flat-pickr v-model="date" :config="rangeDateconfig" class="form-control" id="range-datepicker">
                  </flat-pickr>
                </div>
              </BCol>
              <BCol xl="2" md="4">
                <Multiselect class="form-control" v-model="value2" :close-on-select="true" placeholder="Select Type"
                  :searchable="true" :create-option="true" name="idType" id="idType" :options="[
                    { value: 'Buy', label: 'Buy' },
                    { value: 'Sell', label: 'Sell' },
                  ]" />
              </BCol>
              <BCol xl="2" md="4">
                <Multiselect class="form-control" v-model="status1" :close-on-select="true" placeholder="Select Status"
                  :searchable="true" :create-option="true" name="idStatus" id="idStatus" :options="[
                    { value: 'Successful', label: 'Successful' },
                    { value: 'Cancelled', label: 'Cancelled' },
                    { value: 'Pending', label: 'Pending' },
                  ]" />
              </BCol>
              <BCol xl="1" md="4">
                <BButton variant="primary" class="w-100" @click="SearchData">Filters</BButton>
              </BCol>
            </BRow>
          </BCardBody>
          <BCardBody>
            <div class="table-responsive table-card">
              <table class="table align-middle table-nowrap" id="customerTable">
                <thead class="table-light text-muted">
                  <tr>
                    <th class="sort" data-sort="time" scope="col" @click="onSort('date')">
                      Date
                    </th>
                    <th class="sort" data-sort="currency_name" scope="col" @click="onSort('coinName')">
                      Name
                    </th>
                    <th class="sort" data-sort="type" scope="col" @click="onSort('typeClass')">Type</th>
                    <th class="sort" data-sort="quantity_value" scope="col" @click="onSort('quantity')">
                      Quantity
                    </th>
                    <th class="sort" data-sort="or_value" scope="col" @click="onSort('orderValue')">
                      Order Value
                    </th>
                    <th class="sort" data-sort="sort-avg_price" scope="col" @click="onSort('avgPrice')">
                      Avg Price
                    </th>
                    <th class="sort" data-sort="sort-price" scope="col" @click="onSort('price')">Price</th>
                    <th class="sort" data-sort="status" scope="col" @click="onSort('status')">Status</th>
                  </tr>
                </thead>
                <tbody class="list form-check-all">
                  <tr v-for="(data, index) of resultQuery" :key="index">
                    <td class="order_date time" data-timestamp="1641945600">
                      {{ data.date[0] }}
                      <small class="text-muted">{{ data.date[1] }}</small>
                    </td>
                    <td class="id" style="display: none">
                      <BLink href="javascript:void(0);" class="fw-medium link-primary">#VZ001</BLink>
                    </td>
                    <td>
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                          <img :src="data.img" alt="" class="avatar-xxs" />
                        </div>
                        <BLink href="javascript:void(0);" class="currency_name flex-grow-1 ms-2 currency_name">{{
                          data.coinName
                        }}</BLink>
                      </div>
                    </td>
                    <td :class="`type text-${data.typeClass}`">
                      {{ data.type }}
                    </td>
                    <td class="quantity_value">{{ data.quantity }}</td>
                    <td class="order_value or_val" data-orderval="370683.20">{{ data.orderValue }}</td>
                    <td class="avg_price sort-avg_price" data-av-price="46154.30">{{ data.avgPrice }}</td>
                    <td class="price sort-price" data-price="46335.40">{{ data.price }}</td>
                    <td class="status">
                      <span
                        :class="{ 'badge bg-success-subtle text-success text-uppercase': data.status == 'Successful', 'badge bg-danger-subtle text-danger text-uppercase': data.status == 'Cancelled', 'badge bg-warning-subtle text-warning text-uppercase': data.status == 'Pending' }">{{
                          data.status }}</span>
                    </td>
                  </tr>
                </tbody>
              </table>
              <div class="noresult" v-if="resultQuery.length < 1">
                <div class="text-center">
                  <lottie class="avatar-xl" colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions"
                    :height="75" :width="75" />
                  <h5 class="mt-2">Sorry! No Result Found</h5>
                  <p class="text-muted mb-0">
                    We've searched more than 150+ orders We did not find any
                    orders for you search.
                  </p>
                </div>
              </div>
            </div>

            <div class="d-flex justify-content-end mt-3" v-if="resultQuery.length >= 1">
              <div class="pagination-wrap hstack gap-2" v-if="page != 1 || resultQuery.length >= 10">
                <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--">
                  Previous
                </BLink>

                <ul class="pagination listjs-pagination mb-0">
                  <li :class="{
                    active: pageNumber == page,
                    disabled: pageNumber == '...',
                  }" v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber">
                    <BLink class="page" href="#">{{ pageNumber }}</BLink>
                  </li>
                </ul>
                <BLink class="page-item pagination-next" href="#" :disabled="page >= pages.length" @click="page++">
                  Next
                </BLink>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
