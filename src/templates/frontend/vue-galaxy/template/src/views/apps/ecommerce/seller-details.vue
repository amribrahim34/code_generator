<script>
import { CountTo } from "vue3-count-to";

import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay, Mousewheel } from "swiper/modules";

import "swiper/css";
import "swiper/css/autoplay";
import 'swiper/css/mousewheel';

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import { productsData } from "@/common/data";
import getChartColorsArray from "@/common/getChartColorsArray";

export default {
  components: {
    CountTo,
    Layout,
    PageHeader,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      page: 1,
      perPage: 10,
      pages: [],
      searchQuery: null,
      series: [{
        name: "Orders",
        type: "area",
        data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67],
      },
      {
        name: "Earnings",
        type: "bar",
        data: [
          89.25, 98.58, 68.74, 108.87, 77.54, 84.03, 51.24, 28.57, 92.57,
          42.36, 88.51, 36.57,
        ],
      },
      {
        name: "Refunds",
        type: "line",
        data: [8, 12, 7, 17, 21, 11, 5, 9, 7, 29, 12, 35],
      },
      ],
      chartOptions: {
        chart: {
          height: 370,
          type: "line",
          toolbar: {
            show: false,
          },
        },
        stroke: {
          curve: "straight",
          dashArray: [0, 0, 8],
          width: [2, 0, 2.2],
        },
        fill: {
          opacity: [0.1, 0.9, 1],
        },
        markers: {
          size: [0, 0, 0],
          strokeWidth: 2,
          hover: {
            size: 4,
          },
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
          axisTicks: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
        },
        grid: {
          show: true,
          xaxis: {
            lines: {
              show: true,
            },
          },
          yaxis: {
            lines: {
              show: false,
            },
          },
          padding: {
            top: 0,
            right: -2,
            bottom: 15,
            left: 10,
          },
        },
        legend: {
          show: true,
          horizontalAlign: "center",
          offsetX: 0,
          offsetY: -5,
          markers: {
            width: 9,
            height: 9,
            radius: 6,
          },
          itemMargin: {
            horizontal: 10,
            vertical: 0,
          },
        },
        plotOptions: {
          bar: {
            columnWidth: "30%",
            barHeight: "70%",
          },
        },
        colors: getChartColorsArray('["--vz-secondary", "--vz-primary", "--vz-primary-rgb, 0.60"]'),
        tooltip: {
          shared: true,
          y: [{
            formatter: function (y) {
              if (typeof y !== "undefined") {
                return y.toFixed(0);
              }
              return y;
            },
          },
          {
            formatter: function (y) {
              if (typeof y !== "undefined") {
                return "$" + y.toFixed(2) + "k";
              }
              return y;
            },
          },
          {
            formatter: function (y) {
              if (typeof y !== "undefined") {
                return y.toFixed(0) + " Sales";
              }
              return y;
            },
          },
          ],
        },
      },
      productsData: productsData,
      Autoplay, Mousewheel
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.productsData);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.currency_name.toLowerCase().includes(search) ||
            data.price.includes(search) ||
            data.pairs.toLowerCase().includes(search) ||
            data.high.toLowerCase().includes(search) ||
            data.low.toLowerCase().includes(search) ||
            data.market.toLowerCase().includes(search) ||
            data.volume.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    productsData() {
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
      let numberOfPages = Math.ceil(this.productsData.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.productsData];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.productsData = sortedArray;
    },
    paginate(productsData) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return productsData.slice(from, to);
    },
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Sellers Details" pageTitle="Ecommerce" />
    <BRow>
      <BCol xxl="3">
        <BCard no-body>
          <BCardBody class="p-4">
            <div>
              <div class="flex-shrink-0 avatar-md mx-auto">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/companies/img-2.png" alt="" height="50" />
                </div>
              </div>
              <div class="mt-4 text-center">
                <h5 class="mb-1">Force Medicines</h5>
                <p class="text-muted">Since 1987</p>
              </div>
              <div class="table-responsive">
                <table class="table mb-0 table-borderless">
                  <tbody>
                    <tr>
                      <th><span class="fw-medium">Owner Name</span></th>
                      <td>David Marshall</td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Company Type</span></th>
                      <td>Partnership</td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Email</span></th>
                      <td>forcemedicines@gamil.com</td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Website</span></th>
                      <td>
                        <BLink href="javascript:void(0);" class="link-primary">www.forcemedicines.com</BLink>
                      </td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Contact No.</span></th>
                      <td>+(123) 9876 654 321</td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Fax</span></th>
                      <td>+1 999 876 5432</td>
                    </tr>
                    <tr>
                      <th><span class="fw-medium">Location</span></th>
                      <td>United Kingdom</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed p-4">
            <div>
              <h6 class="text-muted text-uppercase fw-semibold mb-4">
                Customer Reviews
              </h6>
              <div>
                <div>
                  <div class="bg-light px-3 py-2 rounded-2 mb-2">
                    <div class="d-flex align-items-center">
                      <div class="flex-grow-1">
                        <div class="fs-16 align-middle text-warning">
                          <i class="ri-star-fill"></i>
                          <i class="ri-star-fill"></i>
                          <i class="ri-star-fill"></i>
                          <i class="ri-star-fill"></i>
                          <i class="ri-star-half-fill"></i>
                        </div>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">4.5 out of 5</h6>
                      </div>
                    </div>
                  </div>
                  <div class="text-center">
                    <div class="text-muted">
                      Total <span class="fw-medium">5.50k</span> reviews
                    </div>
                  </div>
                </div>

                <div class="mt-3">
                  <BRow class="align-items-center g-2">
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0">5 star</h6>
                      </div>
                    </div>
                    <BCol>
                      <div class="p-1">
                        <BProgress variant="success" class="animated-progess progress-sm" :value="50.16" />
                      </div>
                    </BCol>
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0 text-muted">2758</h6>
                      </div>
                    </div>
                  </BRow>

                  <BRow class="align-items-center g-2">
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0">4 star</h6>
                      </div>
                    </div>
                    <BCol>
                      <div class="p-1">
                        <BProgress variant="success" class="animated-progess progress-sm" :value="29.32" />
                      </div>
                    </BCol>
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0 text-muted">1063</h6>
                      </div>
                    </div>
                  </BRow>

                  <BRow class="align-items-center g-2">
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0">3 star</h6>
                      </div>
                    </div>
                    <BCol>
                      <div class="p-1">
                        <BProgress variant="warning" class="animated-progess progress-sm" :value="18.12" />
                      </div>
                    </BCol>
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0 text-muted">997</h6>
                      </div>
                    </div>
                  </BRow>

                  <BRow class="align-items-center g-2">
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0">2 star</h6>
                      </div>
                    </div>
                    <BCol>
                      <div class="p-1">
                        <BProgress variant="success" class="animated-progess progress-sm" :value="4.98" />
                      </div>
                    </BCol>

                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0 text-muted">227</h6>
                      </div>
                    </div>
                  </BRow>

                  <BRow class="align-items-center g-2">
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0">1 star</h6>
                      </div>
                    </div>
                    <BCol>
                      <div class="p-1">
                        <BProgress variant="danger" class="animated-progess progress-sm" :value="7.42" />
                      </div>
                    </BCol>
                    <div class="col-auto">
                      <div class="p-1">
                        <h6 class="mb-0 text-muted">408</h6>
                      </div>
                    </div>
                  </BRow>
                </div>
              </div>
            </div>
          </BCardBody>
          <BCardBody class="p-4 border-top border-top-dashed">
            <h6 class="text-muted text-uppercase fw-semibold mb-4">
              Products Reviews
            </h6>
            <swiper class="vertical-swiper" :direction="'vertical'" :modules="[Autoplay, Mousewheel]" :slidesPerView="2"
              :spaceBetween="10" :mousewheel="true" :loop="true" :autoplay="{ delay: 2500, disableOnInteraction: false }"
              style="height: 250px">
              <swiper-slide>
                <div class="swiper-slide">
                  <BCard no-body class="border border-dashed shadow-none">
                    <BCardBody>
                      <div class="d-flex">
                        <div class="flex-shrink-0 avatar-sm">
                          <div class="avatar-title bg-light rounded">
                            <img src="@/assets/images/companies/img-1.png" alt="" height="30" />
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <div>
                            <p class="text-muted mb-1 fst-italic text-truncate-two-lines">
                              " Great product and looks great, lots of features.
                              "
                            </p>
                            <div class="fs-11 align-middle text-warning">
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                            </div>
                          </div>
                          <div class="text-end mb-0 text-muted">
                            - by
                            <cite title="Source Title">Force Medicines</cite>
                          </div>
                        </div>
                      </div>
                    </BCardBody>
                  </BCard>
                </div>
              </swiper-slide>
              <swiper-slide>
                <div class="swiper-slide">
                  <BCard no-body class="border border-dashed shadow-none">
                    <BCardBody>
                      <div class="d-flex">
                        <div class="flex-shrink-0">
                          <img src="@/assets/images/users/avatar-3.jpg" alt="" class="avatar-sm rounded" />
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <div>
                            <p class="text-muted mb-1 fst-italic text-truncate-two-lines">
                              " Amazing template, very easy to understand and
                              manipulate. "
                            </p>
                            <div class="fs-11 align-middle text-warning">
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-half-fill"></i>
                            </div>
                          </div>
                          <div class="text-end mb-0 text-muted">
                            - by
                            <cite title="Source Title">Henry Baird</cite>
                          </div>
                        </div>
                      </div>
                    </BCardBody>
                  </BCard>
                </div>
              </swiper-slide>
              <swiper-slide>
                <div class="swiper-slide">
                  <BCard no-body class="border border-dashed shadow-none">
                    <BCardBody>
                      <div class="d-flex">
                        <div class="flex-shrink-0 avatar-sm">
                          <div class="avatar-title bg-light rounded">
                            <img src="@/assets/images/companies/img-8.png" alt="" height="30" />
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <div>
                            <p class="text-muted mb-1 fst-italic text-truncate-two-lines">
                              "Very beautiful product and Very helpful customer
                              service."
                            </p>
                            <div class="fs-11 align-middle text-warning">
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-line"></i>
                              <i class="ri-star-line"></i>
                            </div>
                          </div>
                          <div class="text-end mb-0 text-muted">
                            - by
                            <cite title="Source Title">Zoetic Fashion</cite>
                          </div>
                        </div>
                      </div>
                    </BCardBody>
                  </BCard>
                </div>
              </swiper-slide>
              <swiper-slide>
                <div class="swiper-slide">
                  <BCard no-body class="border border-dashed shadow-none">
                    <BCardBody>
                      <div class="d-flex">
                        <div class="flex-shrink-0">
                          <img src="@/assets/images/users/avatar-2.jpg" alt="" class="avatar-sm rounded" />
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <div>
                            <p class="text-muted mb-1 fst-italic text-truncate-two-lines">
                              " The product is very beautiful. I like it. "
                            </p>
                            <div class="fs-11 align-middle text-warning">
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-fill"></i>
                              <i class="ri-star-half-fill"></i>
                              <i class="ri-star-line"></i>
                            </div>
                          </div>
                          <div class="text-end mb-0 text-muted">
                            - by
                            <cite title="Source Title">Nancy Martino</cite>
                          </div>
                        </div>
                      </div>
                    </BCardBody>
                  </BCard>
                </div>
              </swiper-slide>
            </swiper>

            <div class="text-center mt-3">
              <BLink href="javascript:void(0)" class="link-primary">View All Reviews
                <i class="ri-arrow-right-line align-bottom ms-1"></i>
              </BLink>
            </div>
          </BCardBody>
          <BCardBody class="p-4 border-top border-top-dashed">
            <h6 class="text-muted text-uppercase fw-semibold mb-4">
              Contact Support
            </h6>
            <form action="#">
              <div class="mb-3">
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="4"
                  placeholder="Enter your messages..."></textarea>
              </div>
              <div class="text-end">
                <BButton type="submit" variant="primary">
                  <i class="ri-mail-send-line align-bottom me-1"></i> Send
                  Messages
                </BButton>
              </div>
            </form>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="9">
        <BCard no-body>
          <BCardHeader class="border-0 align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Revenue</BCardTitle>
            <div>
              <BButton type="button" variant="soft-secondary" size="sm" class="me-1">
                ALL
              </BButton>
              <BButton type="button" variant="soft-secondary" size="sm" class="me-1">
                1M
              </BButton>
              <BButton type="button" variant="soft-secondary" size="sm" class="me-1">
                6M
              </BButton>
              <BButton type="button" variant="soft-primary" size="sm">
                1Y
              </BButton>
            </div>
          </BCardHeader>

          <BCardHeader class="p-0 border-0 bg-light-subtle">
            <BRow class="g-0 text-center">
              <BCol cols="6" sm="3">
                <div class="p-3 border border-dashed border-start-0">
                  <h5 class="mb-1">
                    <count-to :duration="5000" :startVal="0" :endVal="7585"></count-to>
                  </h5>
                  <p class="text-muted mb-0">Orders</p>
                </div>
              </BCol>
              <BCol cols="6" sm="3">
                <div class="p-3 border border-dashed border-start-0">
                  <h5 class="mb-1">
                    $<count-to :duration="5000" :startVal="0" :endVal="22.89"></count-to>k
                  </h5>
                  <p class="text-muted mb-0">Earnings</p>
                </div>
              </BCol>
              <BCol cols="6" sm="3">
                <div class="p-3 border border-dashed border-start-0">
                  <h5 class="mb-1">
                    <count-to :duration="5000" :startVal="0" :endVal="367"></count-to>
                  </h5>
                  <p class="text-muted mb-0">Refunds</p>
                </div>
              </BCol>
              <BCol cols="6" sm="3">
                <div class="p-3 border border-dashed border-start-0 border-end-0">
                  <h5 class="mb-1 text-success">
                    <count-to :duration="5000" :startVal="0" :endVal="18.92"></count-to>%
                  </h5>
                  <p class="text-muted mb-0">Conversation Ratio</p>
                </div>
              </BCol>
            </BRow>
          </BCardHeader>

          <BCardBody class="p-0 pb-2">
            <div>
              <apexchart class="apex-charts" dir="ltr" :series="series" :options="chartOptions" height="370">
              </apexchart>
            </div>
          </BCardBody>
        </BCard>

        <BRow class="g-4 mb-3">
          <BCol sm="auto">
            <div>
              <router-link to="/ecommerce/add-product" class="btn btn-primary"><i
                  class="ri-add-line align-bottom me-1"></i> Add New</router-link>
            </div>
          </BCol>
          <BCol sm>
            <div class="d-flex justify-content-sm-end">
              <div class="search-box ms-2">
                <input type="text" class="form-control" placeholder="Search Products..." />
                <i class="ri-search-line search-icon"></i>
              </div>
            </div>
          </BCol>
        </BRow>
        <BCard no-body>
          <BCardBody>
            <div class="table-card gridjs-border-none table-responsive">
              <table class="table align-middle table-nowrap mb-0" id="customerTable">
                <thead class="table-light">
                  <tr>
                    <th scope="col" style="width: 50px">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="checkAll" value="option" />
                      </div>
                    </th>
                    <th class="sort" data-sort="product" @click="onSort('')">Product</th>
                    <th class="sort" data-sort="stock" @click="onSort('stock')">Stock</th>
                    <th class="sort" data-sort="price" @click="onSort('price')">Price</th>
                    <th class="sort" data-sort="orders" @click="onSort('orders')">Orders</th>
                    <th class="sort" data-sort="rating" @click="onSort('rating')">Rating</th>
                    <th class="sort" data-sort="published" @click="onSort('publishedDate')">Published</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody class="list form-check-all">
                  <tr class="gridjs-tr" v-for="(data, index) of resultQuery" :key="index">
                    <td data-column-id="productListAllCheckbox" class="gridjs-td">
                      <input type="checkbox" class="gridjs-checkbox" />
                    </td>
                    <td data-column-id="product" class="gridjs-td">
                      <span>
                        <div class="d-flex align-items-center">
                          <div class="flex-shrink-0 me-3">
                            <div class="avatar-sm bg-light rounded p-1">
                              <img :src="data.image" alt="" class="img-fluid d-block" />
                            </div>
                          </div>
                          <div class="flex-grow-1">
                            <h5 class="fs-14 mb-1">
                              <router-link to="/ecommerce/product-details" class="text-body">{{ data.name }}
                              </router-link>
                            </h5>
                            <p class="text-muted mb-0">
                              Category : <span class="fw-medium">{{ data.category }}</span>
                            </p>
                          </div>
                        </div>
                      </span>
                    </td>
                    <td data-column-id="stock" class="gridjs-td">{{ data.stock }}</td>
                    <td data-column-id="price" class="gridjs-td">{{ data.price }}</td>
                    <td data-column-id="orders" class="gridjs-td">{{ data.orders }}</td>
                    <td data-column-id="rating" class="gridjs-td">
                      <span><span class="badge bg-light text-body fs-12 fw-medium"><i
                            class="mdi mdi-star text-warning me-1"></i>{{ data.rating }}</span></span>
                    </td>
                    <td data-column-id="published" class="gridjs-td">
                      <span>{{ data.publishedDate[0] }}<small class="text-muted ms-1">{{ data.publishedDate[1]
                      }}</small></span>
                    </td>
                    <td data-column-id="action" class="gridjs-td">
                      <span>
                        <BDropdown variant="link" toggle-class="btn btn-soft-secondary btn-sm dropdown arrow-none"
                          menu-class="dropdown-menu-end" :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                          <template #button-content><i class="ri-more-fill align-middle"></i></template>
                          <BDropdownItem to="/ecommerce/product-details"> <i
                              class="ri-eye-fill align-bottom me-2 text-muted"></i>
                            View</BDropdownItem>
                          <BDropdownItem to="/ecommerce/add-product"><i
                              class="ri-pencil-fill align-bottom me-2 text-muted"></i>
                            Edit </BDropdownItem>
                          <li class="dropdown-divider"></li>
                          <BDropdownItem> <i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
                            Delete </BDropdownItem>
                        </BDropdown>
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="d-flex justify-content-end m-3 pt-3">
              <div class="pagination-wrap hstack gap-2">
                <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--"> Previous
                </BLink>
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
      </BCol>
    </BRow>
  </Layout>
</template>