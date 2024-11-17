<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import { Navigation, Thumbs } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import simplebar from 'simplebar-vue';
import { layoutComputed } from "@/state/helpers";

import "swiper/css";
import 'swiper/css/navigation';

export default {
  data() {
    return {
      productDetailsWidgets: [
        {
          id: 1,
          icon: "ri-money-dollar-circle-fill",
          label: "Price",
          labelDetail: "$120.40",
        },
        {
          id: 2,
          icon: "ri-file-copy-2-fill",
          label: "No. of Orders",
          labelDetail: "2,234",
        },
        {
          id: 3,
          icon: "ri-stack-fill",
          label: "Available Stocks",
          labelDetail: "1,230",
        },
        {
          id: 4,
          icon: "ri-inbox-archive-fill",
          label: "Total Revenue",
          labelDetail: "$60,645",
        },
      ],
      thumbsSwiper: null,
      Navigation: Navigation,
      Thumbs: Thumbs
    };
  },
  methods: {
    setThumbsSwiper(swiper) {
      this.thumbsSwiper = swiper;
    }
  },
  computed: {
    ...layoutComputed,
  },
  watch: {
    layoutType: {
      immediate: true,
      deep: true,
      handler(newVal, oldVal) {
        if (newVal !== oldVal) {
          this.setThumbsSwiper();
        }
      },
    },
  },
  mounted() {
    this.setThumbsSwiper();
  },
  components: {
    Layout,
    PageHeader,
    Swiper,
    SwiperSlide,
    simplebar
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Product Details" pageTitle="Ecommerce" />
    <BRow>
      <BCol lg="12">
        <BCard no-body>
          <BCardBody>
            <BRow class="gx-lg-5">
              <BCol xl="4" md="8" class="mx-auto">
                <div class="product-img-slider sticky-side-div">


                  <swiper :modules="[Navigation, Thumbs]" class="product-thumbnail-slider p-2 rounded bg-light"
                    :navigation="{ nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev', }"
                    :thumbs="{ swiper: thumbsSwiper }">
                    <swiper-slide>
                      <img src="@/assets/images/products/img-8.png" alt class="img-fluid d-block" />
                    </swiper-slide>
                    <swiper-slide>
                      <img src="@/assets/images/products/img-6.png" alt class="img-fluid d-block" />
                    </swiper-slide>
                    <swiper-slide>
                      <img src="@/assets/images/products/img-1.png" alt class="img-fluid d-block" />
                    </swiper-slide>
                    <swiper-slide>
                      <img src="@/assets/images/products/img-8.png" alt class="img-fluid d-block" />
                    </swiper-slide>
                  </swiper>

                  <div class="swiper-button-next"></div>
                  <div class="swiper-button-prev"></div>

                  <swiper :modules="[Thumbs]" class="product-nav-slider mt-2" :loop="false" :spaceBetween="10"
                    :slidesPerView="4" :freeMode="true" watch-slides-progress @swiper="setThumbsSwiper">
                    <swiper-slide>
                      <div class="nav-slide-item">
                        <img src="@/assets/images/products/img-8.png" alt class="img-fluid d-block" />
                      </div>
                    </swiper-slide>
                    <swiper-slide>
                      <div class="nav-slide-item">
                        <img src="@/assets/images/products/img-6.png" alt class="img-fluid d-block" />
                      </div>
                    </swiper-slide>
                    <swiper-slide>
                      <div class="nav-slide-item">
                        <img src="@/assets/images/products/img-1.png" alt class="img-fluid d-block" />
                      </div>
                    </swiper-slide>
                    <swiper-slide>
                      <div class="nav-slide-item">
                        <img src="@/assets/images/products/img-8.png" alt class="img-fluid d-block" />
                      </div>
                    </swiper-slide>
                  </swiper>


                </div>
              </BCol>

              <BCol xl="8">
                <div class="mt-xl-0 mt-5">
                  <div class="d-flex">
                    <div class="flex-grow-1">
                      <h4>Full Sleeve Sweatshirt for Men (Pink)</h4>
                      <div class="hstack gap-3 flex-wrap">
                        <div>
                          <BLink href="#" class="text-primary d-block">Tommy Hilfiger</BLink>
                        </div>
                        <div class="vr"></div>
                        <div class="text-muted">
                          Seller :
                          <span class="text-body fw-medium">Zoetic Fashion</span>
                        </div>
                        <div class="vr"></div>
                        <div class="text-muted">
                          Published :
                          <span class="text-body fw-medium">26 Mar, 2021</span>
                        </div>
                      </div>
                    </div>
                    <div class="flex-shrink-0">
                      <div>
                        <router-link to="/ecommerce/add-product" class="btn btn-light" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="Edit">
                          <i class="ri-pencil-fill align-bottom"></i>
                        </router-link>
                      </div>
                    </div>
                  </div>

                  <div class="d-flex flex-wrap gap-2 align-items-center mt-3">
                    <div class="text-muted fs-16">
                      <span class="mdi mdi-star text-warning"></span>
                      <span class="mdi mdi-star text-warning"></span>
                      <span class="mdi mdi-star text-warning"></span>
                      <span class="mdi mdi-star text-warning"></span>
                      <span class="mdi mdi-star text-warning"></span>
                    </div>
                    <div class="text-muted">( 5.50k Customer Review )</div>
                  </div>

                  <BRow class="mt-4">
                    <BCol lg="3" sm="6" v-for="(item, index) of productDetailsWidgets" :key="index">
                      <div class="p-2 border border-dashed rounded">
                        <div class="d-flex align-items-center">
                          <div class="avatar-sm me-2">
                            <div class="avatar-title rounded bg-transparent text-primary fs-24">
                              <i :class="`${item.icon}`"></i>
                            </div>
                          </div>
                          <div class="flex-grow-1">
                            <p class="text-muted mb-1">{{ item.label }} :</p>
                            <h5 class="mb-0">{{ item.labelDetail }}</h5>
                          </div>
                        </div>
                      </div>
                    </BCol>
                  </BRow>

                  <BRow>
                    <BCol xl="6">
                      <div class="mt-4">
                        <h5 class="fs-14">Sizes :</h5>
                        <div class="d-flex flex-wrap gap-2">
                          <div v-b-tooltip.hover title="Out of Stock">
                            <input type="radio" class="btn-check" name="productsize-radio" id="productsize-radio1"
                              disabled />
                            <label
                              class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
                              for="productsize-radio1">S</label>
                          </div>

                          <div v-b-tooltip.hover title="04 Items Available">
                            <input type="radio" class="btn-check" name="productsize-radio" id="productsize-radio2" />
                            <label
                              class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
                              for="productsize-radio2">M</label>
                          </div>
                          <div v-b-tooltip.hover title="06 Items Available">
                            <input type="radio" class="btn-check" name="productsize-radio" id="productsize-radio3" />
                            <label
                              class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
                              for="productsize-radio3">L</label>
                          </div>

                          <div v-b-tooltip.hover title="Out of Stock">
                            <input type="radio" class="btn-check" name="productsize-radio" id="productsize-radio4"
                              disabled />
                            <label
                              class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
                              for="productsize-radio4">XL</label>
                          </div>
                        </div>
                      </div>
                    </BCol>

                    <BCol xl="6">
                      <div class="mt-4">
                        <h5 class="fs-14">Colors :</h5>
                        <div class="d-flex flex-wrap gap-2">
                          <div v-b-tooltip.hover title="Out of Stock">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-primary"
                              disabled>
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="03 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-secondary">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="03 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-success">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="02 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-info">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="01 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-warning">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="04 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-danger">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="03 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-light">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                          <div v-b-tooltip.hover title="04 Items Available">
                            <button type="button"
                              class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-body">
                              <i class="ri-checkbox-blank-circle-fill"></i>
                            </button>
                          </div>
                        </div>
                      </div>
                    </BCol>
                  </BRow>

                  <div class="mt-4 text-muted">
                    <h5 class="fs-14">Description :</h5>
                    <p>
                      Tommy Hilfiger men striped pink sweatshirt. Crafted with
                      cotton. Material composition is 100% organic cotton. This
                      is one of the world’s leading designer lifestyle brands
                      and is internationally recognized for celebrating the
                      essence of classic American cool style, featuring preppy
                      with a twist designs.
                    </p>
                  </div>

                  <BRow>
                    <BCol sm="6">
                      <div class="mt-3">
                        <h5 class="fs-14">Features :</h5>
                        <ul class="list-unstyled">
                          <li class="py-1">
                            <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                            Full Sleeve
                          </li>
                          <li class="py-1">
                            <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                            Cotton
                          </li>
                          <li class="py-1">
                            <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                            All Sizes available
                          </li>
                          <li class="py-1">
                            <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                            4 Different Color
                          </li>
                        </ul>
                      </div>
                    </BCol>
                    <BCol sm="6">
                      <div class="mt-3">
                        <h5 class="fs-14">Services :</h5>
                        <ul class="list-unstyled product-desc-list">
                          <li class="py-1">10 Days Replacement</li>
                          <li class="py-1">Cash on Delivery available</li>
                        </ul>
                      </div>
                    </BCol>
                  </BRow>

                  <div class="product-content mt-5">
                    <h5 class="fs-14 mb-3">Product Description :</h5>
                    <BTabs nav-class="nav-tabs-custom nav-primary">
                      <BTab title="Specification" active>
                        <div class="border border-top-0 p-4 table-responsive">
                          <table class="table mb-0">
                            <tbody>
                              <tr>
                                <th scope="row" style="width: 200px">
                                  Category
                                </th>
                                <td>T-Shirt</td>
                              </tr>
                              <tr>
                                <th scope="row">Brand</th>
                                <td>Tommy Hilfiger</td>
                              </tr>
                              <tr>
                                <th scope="row">Color</th>
                                <td>Blue</td>
                              </tr>
                              <tr>
                                <th scope="row">Material</th>
                                <td>Cotton</td>
                              </tr>
                              <tr>
                                <th scope="row">Weight</th>
                                <td>140 Gram</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </BTab>
                      <BTab class="border border-top-0 p-4" title="Details">
                        <div>
                          <h5 class="font-size-16 mb-3">
                            Tommy Hilfiger Sweatshirt for Men (Pink)
                          </h5>
                          <p>
                            Tommy Hilfiger men striped pink sweatshirt. Crafted
                            with cotton. Material composition is 100% organic
                            cotton. This is one of the world’s leading designer
                            lifestyle brands and is internationally recognized
                            for celebrating the essence of classic American cool
                            style, featuring preppy with a twist designs.
                          </p>
                          <div>
                            <p class="mb-2">
                              <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                              Machine Wash
                            </p>
                            <p class="mb-2">
                              <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                              Fit Type: Regular
                            </p>
                            <p class="mb-2">
                              <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                              100% Cotton
                            </p>
                            <p class="mb-0">
                              <i class="mdi mdi-circle-medium me-1 text-muted align-middle"></i>
                              Long sleeve
                            </p>
                          </div>
                        </div>
                      </BTab>
                    </BTabs>
                  </div>

                  <div class="mt-5">
                    <div>
                      <h5 class="fs-14 mb-3">Ratings & Reviews</h5>
                    </div>
                    <BRow class="gy-4 gx-0">
                      <BCol lg="4">
                        <div>
                          <div class="pb-3">
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
                                Total
                                <span class="fw-medium">5.50k</span> reviews
                              </div>
                            </div>
                          </div>

                          <div class="mt-3">
                            <BRow class="align-items-center g-2">
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0">5 star</h6>
                                </div>
                              </div>
                              <BCol>
                                <div class="p-2">
                                  <BProgress variant="primary" class="animated-progess progress-sm" :value="50.16" />
                                </div>
                              </BCol>
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0 text-muted">2758</h6>
                                </div>
                              </div>
                            </BRow>

                            <BRow class="align-items-center g-2">
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0">4 star</h6>
                                </div>
                              </div>
                              <BCol>
                                <div class="p-2">
                                  <BProgress variant="secondary" class="animated-progess progress-sm" :value="19.32" />
                                </div>
                              </BCol>
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0 text-muted">1063</h6>
                                </div>
                              </div>
                            </BRow>

                            <BRow class="align-items-center g-2">
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0">3 star</h6>
                                </div>
                              </div>
                              <BCol>
                                <div class="p-2">
                                  <BProgress variant="success" class="animated-progess progress-sm" :value="18.12" />
                                </div>
                              </BCol>
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0 text-muted">997</h6>
                                </div>
                              </div>
                            </BRow>

                            <BRow class="align-items-center g-2">
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0">2 star</h6>
                                </div>
                              </div>
                              <BCol>
                                <div class="p-2">
                                  <BProgress variant="warning" class="animated-progess progress-sm" :value="7.42" />
                                </div>
                              </BCol>

                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0 text-muted">408</h6>
                                </div>
                              </div>
                            </BRow>

                            <BRow class="align-items-center g-2">
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0">1 star</h6>
                                </div>
                              </div>
                              <BCol>
                                <div class="p-2">
                                  <BProgress variant="danger" class="animated-progess progress-sm" :value="4.98" />
                                </div>
                              </BCol>
                              <div class="col-auto">
                                <div class="p-2">
                                  <h6 class="mb-0 text-muted">274</h6>
                                </div>
                              </div>
                            </BRow>
                          </div>
                        </div>
                      </BCol>

                      <BCol lg="8">
                        <div class="ps-lg-4">
                          <div class="d-flex flex-wrap align-items-start gap-3">
                            <h5 class="fs-14">Reviews:</h5>
                          </div>

                          <simplebar class="me-lg-n3 pe-lg-4" data-simplebar style="max-height: 225px">
                            <ul class="list-unstyled mb-0">
                              <li class="py-2">
                                <div class="border border-dashed rounded p-3">
                                  <div class="d-flex align-items-start mb-3">
                                    <div class="hstack gap-3">
                                      <BBadge tag="div" variant="primary" class="rounded-pill mb-0 text-bg-primary">
                                        <i class="mdi mdi-star"></i> 4.2
                                      </BBadge>
                                      <div class="vr"></div>
                                      <div class="flex-grow-1">
                                        <p class="text-muted mb-0">
                                          Superb sweatshirt. I loved it. It is
                                          for winter.
                                        </p>
                                      </div>
                                    </div>
                                  </div>

                                  <div class="d-flex flex-grow-1 gap-2 mb-3">
                                    <BLink href="#" class="d-block">
                                      <img src="@/assets/images/small/img-12.jpg" alt
                                        class="avatar-sm rounded object-fit-cover" />
                                    </BLink>
                                    <BLink href="#" class="d-block">
                                      <img src="@/assets/images/small/img-11.jpg" alt
                                        class="avatar-sm rounded object-fit-cover" />
                                    </BLink>
                                    <BLink href="#" class="d-block">
                                      <img src="@/assets/images/small/img-10.jpg" alt
                                        class="avatar-sm rounded object-fit-cover" />
                                    </BLink>
                                  </div>

                                  <div class="d-flex align-items-end">
                                    <div class="flex-grow-1">
                                      <h5 class="fs-14 mb-0">Henry</h5>
                                    </div>

                                    <div class="flex-shrink-0">
                                      <p class="text-muted fs-13 mb-0">
                                        12 Jul, 21
                                      </p>
                                    </div>
                                  </div>
                                </div>
                              </li>
                              <li class="py-2">
                                <div class="border border-dashed rounded p-3">
                                  <div class="d-flex align-items-start mb-3">
                                    <div class="hstack gap-3">
                                      <BBadge tag="div" variant="primary" class="rounded-pill mb-0 text-bg-primary">
                                        <i class="mdi mdi-star"></i> 4.0
                                      </BBadge>
                                      <div class="vr"></div>
                                      <div class="flex-grow-1">
                                        <p class="text-muted mb-0">
                                          Great at this price, Product quality
                                          and look is awesome.
                                        </p>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="d-flex align-items-end">
                                    <div class="flex-grow-1">
                                      <h5 class="fs-14 mb-0">Nancy</h5>
                                    </div>

                                    <div class="flex-shrink-0">
                                      <p class="text-muted fs-13 mb-0">
                                        06 Jul, 21
                                      </p>
                                    </div>
                                  </div>
                                </div>
                              </li>

                              <li class="py-2">
                                <div class="border border-dashed rounded p-3">
                                  <div class="d-flex align-items-start mb-3">
                                    <div class="hstack gap-3">
                                      <BBadge tag="div" variant="primary" class="rounded-pill mb-0 text-bg-primary">
                                        <i class="mdi mdi-star"></i> 4.2
                                      </BBadge>
                                      <div class="vr"></div>
                                      <div class="flex-grow-1">
                                        <p class="text-muted mb-0">
                                          Good product. I am so happy.
                                        </p>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="d-flex align-items-end">
                                    <div class="flex-grow-1">
                                      <h5 class="fs-14 mb-0">Joseph</h5>
                                    </div>

                                    <div class="flex-shrink-0">
                                      <p class="text-muted fs-13 mb-0">
                                        06 Jul, 21
                                      </p>
                                    </div>
                                  </div>
                                </div>
                              </li>

                              <li class="py-2">
                                <div class="border border-dashed rounded p-3">
                                  <div class="d-flex align-items-start mb-3">
                                    <div class="hstack gap-3">
                                      <BBadge tag="div" variant="primary" class="rounded-pill mb-0 text-bg-primary">
                                        <i class="mdi mdi-star"></i> 4.1
                                      </BBadge>
                                      <div class="vr"></div>
                                      <div class="flex-grow-1">
                                        <p class="text-muted mb-0">
                                          Nice Product, Good Quality.
                                        </p>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="d-flex align-items-end">
                                    <div class="flex-grow-1">
                                      <h5 class="fs-14 mb-0">Jimmy</h5>
                                    </div>

                                    <div class="flex-shrink-0">
                                      <p class="text-muted fs-13 mb-0">
                                        24 Jun, 21
                                      </p>
                                    </div>
                                  </div>
                                </div>
                              </li>
                            </ul>
                          </simplebar>
                        </div>
                      </BCol>
                    </BRow>
                  </div>
                </div>
              </BCol>
            </BRow>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>

<!-- <template>
  <swiper :modules="[Thumbs]" :thumbs="{ swiper: thumbsSwiper }" ...>
    ...
  </swiper>

  <swiper
    :modules="[Thumbs]"
    watch-slides-progress
    @swiper="setThumbsSwiper"
    ...
  >
    ...
  </swiper>
</template>
<script>
  import { ref } from 'vue';
  import { Thumbs } from 'swiper/modules';
  import { Swiper, SwiperSlide } from 'swiper/vue';

  export default {
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      const thumbsSwiper = ref(null);
      const setThumbsSwiper = (swiper) => {
        thumbsSwiper.value = swiper;
      };
      return {
        Thumbs,
        thumbsSwiper,
        setThumbsSwiper,
      };
    },
  };
</script> -->
