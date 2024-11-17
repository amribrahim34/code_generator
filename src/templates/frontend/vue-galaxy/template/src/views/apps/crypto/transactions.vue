<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import { CountTo } from "vue3-count-to";

import { Autoplay } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import "swiper/css/autoplay";

import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/fhtaantg.json";
import animationData1 from "@/components/widgets/qhviklyi.json";
import animationData2 from "@/components/widgets/msoeawqm.json";
import animationData3 from "@/components/widgets/yeallgsa.json";
import animationData4 from "@/components/widgets/vaeagfzc.json";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import { transactions } from "@/common/data";

export default {
  components: {
    Layout,
    PageHeader,
    CountTo,
    Swiper,
    SwiperSlide,
    lottie: Lottie,
    Multiselect
  },
  data() {
    return {
      value2: null,
      transactions: transactions,
      page: 1,
      perPage: 9,
      pages: [],
      searchQuery: null,
      defaultOptions: { animationData: animationData },
      defaultOptions1: { animationData: animationData1 },
      defaultOptions2: { animationData: animationData2 },
      defaultOptions3: { animationData: animationData3 },
      defaultOptions4: { animationData: animationData4 },
      Autoplay
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.transactions);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.date.toLowerCase().includes(search) ||
            data.time.toLowerCase().includes(search) ||
            data.from.toLowerCase().includes(search) ||
            data.to.toLowerCase().includes(search) ||
            data.details.toLowerCase().includes(search) ||
            data.amount.toLowerCase().includes(search) ||
            data.amount1.toLowerCase().includes(search) ||
            data.status.toLowerCase().includes(search) ||
            data.type.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    transactions() {
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
      let numberOfPages = Math.ceil(this.transactions.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(transactions) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return transactions.slice(from, to);
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.transactions];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.transactions = sortedArray;
    },

  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Transactions" pageTitle="Crypto" />
    <BRow>
      <BCol xxl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-grow-1">
                <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions" :height="55" :width="55"
                  class="me-auto m-0" />
              </div>
              <div class="flex-shrink-0">
                <BLink href="javascript:void(0);" class="badge bg-warning-subtle text-warning badge-border me-1">BTC
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-info-subtle text-info badge-border me-1">ETH</BLink>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary badge-border me-1">USD
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-danger-subtle text-danger badge-border">EUR</BLink>
              </div>
            </div>
            <h3 class="mb-2">
              $ <count-to :duration="5000" :startVal="0" :endVal="74854"></count-to><small
                class="text-muted fs-13">.68k</small>
            </h3>
            <h6 class="text-muted mb-0">Available Balance (USD)</h6>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xxl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-grow-1">
                <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions1" :height="55" :width="55"
                  class="me-auto m-0" />
              </div>
              <div class="flex-shrink-0">
                <BLink href="javascript:void(0);" class="badge bg-warning-subtle text-warning badge-border me-1">BTC
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-info-subtle text-info badge-border me-1">ETH</BLink>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary badge-border me-1">USD
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-danger-subtle text-danger badge-border">EUR</BLink>
              </div>
            </div>
            <h3 class="mb-2">
              $<count-to :duration="5000" :startVal="0" :endVal="74361"></count-to><small
                class="text-muted fs-13">.34k</small>
            </h3>
            <h6 class="text-muted mb-0">Send (Previous Month)</h6>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xxl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-grow-1">
                <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions3" :height="55" :width="55"
                  class="me-auto m-0" />
              </div>
              <div class="flex-shrink-0">
                <BLink href="javascript:void(0);" class="badge bg-warning-subtle text-warning badge-border me-1">BTC
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-info-subtle text-info badge-border me-1">ETH</BLink>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary badge-border me-1">USD
                </BLink>
                <BLink href="javascript:void(0);" class="badge bg-danger-subtle text-danger badge-border">EUR</BLink>
              </div>
            </div>
            <h3 class="mb-2">
              $<count-to :duration="5000" :startVal="0" :endVal="97685"></count-to><small
                class="text-muted fs-13">.22k</small>
            </h3>
            <h6 class="text-muted mb-0">Receive (Previous Month)</h6>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xxl="3" md="6">
        <swiper class="swiper-wrapper" :autoplay="{ delay: 2500, disableOnInteraction: false }" :modules="[Autoplay]">
          <swiper-slide>
            <BCard no-body class="card-animate">
              <BCardBody class="bg-primary-subtle">
                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions4" :height="55" :width="55"
                      class="me-auto m-0" />
                  </div>
                  <div class="flex-shrink-0">
                    <BLink href="javascript:void(0);" class="fw-medium">Bitcoin (BTC)</BLink>
                  </div>
                </div>
                <h3 class="mb-2">
                  $245<small class="text-muted fs-13">.65k</small>
                </h3>
                <h6 class="text-muted mb-0">Send - Receive (Previous Month)</h6>
              </BCardBody>
            </BCard>
          </swiper-slide>
          <swiper-slide>
            <BCard no-body class="card-animate">
              <BCardBody class="bg-primary-subtle">
                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions4" :height="55" :width="55"
                      class="me-auto m-0" />
                  </div>
                  <div class="flex-shrink-0">
                    <BLink href="javascript:void(0);" class="fw-medium">Ethereum (ETH)</BLink>
                  </div>
                </div>
                <h3 class="mb-2">
                  $24<small class="text-muted fs-13">.74k</small>
                </h3>
                <h6 class="text-muted mb-0">Send - Receive (Previous Month)</h6>
              </BCardBody>
            </BCard>
          </swiper-slide>
          <swiper-slide>
            <BCard no-body class="card-animate overflow-hidden">
              <BCardBody class="bg-primary-subtle">
                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions4" :height="55" :width="55"
                      class="me-auto m-0" />
                  </div>
                  <div class="flex-shrink-0">
                    <BLink href="javascript:void(0);" class="fw-medium">Monero (XMR)</BLink>
                  </div>
                </div>
                <h3 class="mb-2">
                  $124<small class="text-muted fs-13">.36k</small>
                </h3>
                <h6 class="text-muted mb-0">Send - Receive (Previous Month)</h6>
              </BCardBody>
            </BCard>
          </swiper-slide>
        </swiper>
      </BCol>
    </BRow>

    <BRow class="align-items-center mb-4 g-3">
      <BCol sm="3">
        <div class="d-flex align-items-center gap-2">
          <span class="text-muted flex-shrink-0">Sort by: </span>

          <Multiselect class="form-control" v-model="value2" :close-on-select="true" :searchable="true"
            :create-option="true" :options="[
              { value: 'All', label: 'All' },
              { value: 'USD', label: 'USD' },
              { value: 'ETH', label: 'ETH' },
              { value: 'BTC', label: 'BTC' },
              { value: 'EUR', label: 'EUR' },
              { value: 'JPY', label: 'JPY' }
            ]" />
        </div>
      </BCol>
      <BCol sm="auto" class="ms-auto">
        <div class="d-flex gap-2">
          <BLink href="javascript:void(0);" class="btn btn-primary">Deposite</BLink>
          <BLink href="javascript:void(0);" class="btn btn-danger">Withdraw</BLink>
        </div>
      </BCol>
    </BRow>

    <BCard no-body id="contactList">
      <BCardHeader>
        <BRow class="align-items-center g-3">
          <BCol md="3">
            <h5 class="card-title mb-0">All Transactions</h5>
          </BCol>
          <BCol md="auto" class="ms-auto">
            <div class="d-flex gap-2">
              <div class="search-box">
                <input type="text" class="form-control search" placeholder="Search for transactions..."
                  v-model="searchQuery" />
                <i class="ri-search-line search-icon"></i>
              </div>
              <BButton variant="primary">
                <i class="ri-equalizer-line align-bottom me-1"></i> Filters
              </BButton>
            </div>
          </BCol>
        </BRow>
      </BCardHeader>
      <BCardBody>
        <div class="table-responsive table-card">
          <table class="table align-middle table-nowrap" id="customerTable">
            <thead class="table-light text-muted">
              <tr>
                <th class="sort" data-sort="name" scope="col" style="width: 60px"></th>
                <th class="sort" data-sort="date" scope="col" @click="onSort('date')">Timestamp</th>
                <th class="sort" data-sort="currency_name" scope="col" @click="onSort('currency')">Currency</th>
                <th class="sort" data-sort="form_name" scope="col" @click="onSort('from')">Form</th>
                <th class="sort" data-sort="to_name" scope="col" @click="onSort('to')">To</th>
                <th class="sort" data-sort="details" scope="col" @click="onSort('details')">Details</th>
                <th class="sort" data-sort="transaction_id" scope="col" @click="onSort('id')">Transaction ID</th>
                <th class="sort" data-sort="type" scope="col" @click="onSort('type')">Type</th>
                <th class="sort" data-sort="amount" scope="col" @click="onSort('amount')">Amount</th>
                <th class="sort" data-sort="status" scope="col" @click="onSort('status')">Status</th>
              </tr>
            </thead>
            <tbody class="list form-check-all">
              <tr v-for="(data, index) of resultQuery" :key="index">
                <td class="id" style="display: none">
                  <BLink href="javascript:void(0);" class="fw-medium link-primary">#VZ001</BLink>
                </td>
                <td>
                  <div class="avatar-xs">
                    <div class="avatar-title rounded-circle fs-16" :class="{
                      'text-success bg-success-subtle':
                        data.icon == 'ri-arrow-left-down-fill',
                      'bg-danger-subtle text-danger':
                        data.icon == 'ri-arrow-right-up-fill',
                    }">
                      <i :class="data.icon"></i>
                    </div>
                  </div>
                </td>
                <td class="date">
                  {{ data.date }}
                  <small class="text-muted">{{ data.time }}</small>
                </td>
                <td class="currency_name">
                  <div class="d-flex align-items-center">
                    <img :src="data.image" alt="" class="avatar-xxs me-2" />
                    {{ data.currency }}
                  </div>
                </td>
                <td class="form_name">{{ data.from }}</td>
                <td class="to_name">{{ data.to }}</td>
                <td class="details">{{ data.details }}</td>
                <td class="transaction_id">{{ data.id }}</td>
                <td class="type">{{ data.type }}</td>
                <td>
                  <h6 class="mb-1 amount" :class="{
                    'text-success': data.icon == 'ri-arrow-left-down-fill',
                    'text-danger': data.icon == 'ri-arrow-right-up-fill',
                  }">
                    {{ data.amount }}
                  </h6>
                  <p class="text-muted mb-0">{{ data.amount1 }}</p>
                </td>
                <td class="status">
                  <span class="badge fs-11" :class="{
                    'bg-success-subtle text-success': data.status == 'Success',
                    'bg-danger-subtle text-danger': data.status == 'Failed',
                    'bg-warning-subtle text-warning': data.status == 'Processing',
                  }"><i class="ri-time-line align-bottom"></i>
                    {{ data.status }}</span>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="noresult" v-if="resultQuery.length < 1">
            <div class="text-center">
              <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions2" :height="75" :width="75" />
              <h5 class="mt-2">Sorry! No Result Found</h5>
              <p class="text-muted mb-0">
                We've searched more than 150+ transactions We did not find any
                transactions for you search.
              </p>
            </div>
          </div>
        </div>
        <div class="d-flex justify-content-end mt-3" v-if="resultQuery.length >= 1">
          <div class="pagination-wrap hstack gap-2">
            <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--"> Previous </BLink>
            <ul class="pagination listjs-pagination mb-0">
              <li :class="{ active: pageNumber == page, disabled: pageNumber == '...', }"
                v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber">
                <BLink class="page" href="#" data-i="1" data-page="8">{{ pageNumber }}</BLink>
              </li>
            </ul>
            <BLink class="page-item pagination-next" href="#" :disabled="page >= pages.length" @click="page++">
              Next
            </BLink>
          </div>
        </div>
      </BCardBody>
    </BCard>
  </Layout>
</template>
