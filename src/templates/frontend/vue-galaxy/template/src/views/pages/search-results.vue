<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";

export default {
  components: {
    Layout,
    PageHeader,
    Swiper,
    SwiperSlide,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Search Results" pageTitle="Pages" />

    <BRow>
      <BCol lg="12">
        <BCard no-body>
          <BCardHeader class="border-0">
            <BRow class="justify-content-center mb-4">
              <BCol lg="6">
                <BRow class="g-2">
                  <BCol>
                    <div class="position-relative mb-3">
                      <input type="text" class="
                          form-control form-control-lg
                          bg-light
                          border-light
                        " placeholder="Search here.." value="Admin Dashboard" />
                      <BLink class="
                          btn btn-link
                          link-success
                          btn-lg
                          position-absolute
                          end-0
                          top-0
                        " data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample"
                        aria-controls="offcanvasExample"><i class="ri-mic-fill"></i></BLink>
                    </div>
                  </BCol>
                  <div class="col-auto">
                    <BButton type="submit" variant="primary" size="lg">
                      <i class="mdi mdi-magnify me-1"></i> Search
                    </BButton>
                  </div>
                </BRow>
              </BCol>
              <BCol lg="12">
                <h5 class="fs-16 fw-semibold text-center mb-0">
                  Showing results for "<span class="text-primary fw-medium fst-italic">Admin Dashboard</span>
                  "
                </h5>
              </BCol>
            </BRow>

            <div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvasExample"
              aria-labelledby="offcanvasExampleLabel">
              <div class="offcanvas-body">
                <BButton class="btn-close text-reset float-end" data-bs-dismiss="offcanvas" aria-label="Close"></BButton>
                <div class="
                    d-flex
                    flex-column
                    h-100
                    justify-content-center
                    align-items-center
                  ">
                  <div class="search-voice">
                    <i class="ri-mic-fill align-middle"></i>
                    <span class="voice-wave"></span>
                    <span class="voice-wave"></span>
                    <span class="voice-wave"></span>
                  </div>
                  <h4>Talk to me, what can I do for you?</h4>
                </div>
              </div>
            </div>
          </BCardHeader>
          <BCardBody class="p-4">
            <BDropdown variant="transparent" right toggle-class="arrow-none" class="fw-medium text-reset mb-n1"
              no-caret style="position: absolute; right: 2px;">
              <template #button-content> <i class="ri-settings-4-line align-middle me-1"></i> Settings
              </template>
              <BDropdownItem href="#">
                Search Settings
              </BDropdownItem>
              <BDropdownItem href="#">
                Advanced Search
              </BDropdownItem>
              <BDropdownItem href="#">
                Search History
              </BDropdownItem>
              <BDropdownItem href="#">
                Search Help
              </BDropdownItem>
              <BDropdownDivider></BDropdownDivider>
              <BDropdownItem href="#">
                Dark Mode:Off
              </BDropdownItem>
            </BDropdown>
            <BTabs nav-class=" nav-tabs-custom text-muted">
              <BTab class="nav-item">
                <template #title>
                  <i class="ri-search-2-line text-muted align-bottom me-1"></i>
                  All Results
                </template>
                <div class="pb-3 pt-4">
                  <h5 class="mb-1">
                    <BLink href="javascript:void(0);">Velzon - Responsive Bootstrap 5 Admin Dashboard</BLink>
                  </h5>
                  <p class="text-success mb-2">
                    https://themesbrand.com/velzon/index.html
                  </p>
                  <p class="text-muted mb-2">
                    Velzon admin is super flexible, powerful, clean, modern &
                    responsive admin template based on
                    <span class="fw-semibold">bootstrap 5</span> stable with
                    unlimited possibilities. You can simply change to any layout
                    or mode by changing a couple of lines of code. You can start
                    small and large projects or update design in your existing
                    project using Velzon it is very quick and easy as it is
                    beautiful, adroit, and delivers the ultimate user
                    experience.
                  </p>
                  <ul class="
                      list-inline
                      d-flex
                      align-items-center
                      g-3
                      text-muted
                      fs-14
                      mb-0
                    ">
                    <li class="list-inline-item me-3">
                      <i class="ri-thumb-up-line align-middle me-1"></i>10
                    </li>
                    <li class="list-inline-item me-3">
                      <i class="ri-question-answer-line align-middle me-1"></i>8
                    </li>
                    <li class="list-inline-item">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                          <i class="ri-user-line"></i>
                        </div>
                        <div class="flex-grow-1 fs-13 ms-1">
                          <span class="fw-medium">Themesbrand</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>

                <div class="border border-dashed"></div>

                <div class="py-3">
                  <h5 class="fs-13 mb-3 text-muted fst-italic">
                    Showing results Images
                  </h5>
                  <BRow>
                    <BCol xl="4" lg="10">
                      <BRow class="g-2">
                        <BCol md="3" sm="6">
                          <div>
                            <BLink class="image-popup d-block">
                              <img src="@/assets/images/small/img-1.jpg" alt="" class="img-fluid d-block rounded" />
                            </BLink>
                          </div>
                        </BCol>
                        <BCol md="3" sm="6">
                          <div>
                            <BLink class="image-popup d-block">
                              <img src="@/assets/images/small/img-3.jpg" alt="" class="img-fluid d-block rounded" />
                            </BLink>
                          </div>
                        </BCol>
                        <BCol md="3" sm="6">
                          <div>
                            <BLink class="image-popup d-block">
                              <img src="@/assets/images/small/img-4.jpg" alt="" class="img-fluid d-block rounded" />
                            </BLink>
                          </div>
                        </BCol>
                        <BCol md="3" sm="6">
                          <div class="search-more-results rounded">
                            <BLink href="javascript:void(0);" onclick="myFunction()" class="d-block">
                              <img src="@/assets/images/small/img-5.jpg" alt="" class="img-fluid d-block rounded" />

                              <div class="bg-overlay"></div>
                              <div class="nav-icon">
                                <i class="ri-image-fill align-middle me-1"></i>
                                99+
                              </div>
                            </BLink>
                          </div>
                        </BCol>
                      </BRow>
                    </BCol>
                  </BRow>
                </div>

                <div class="border border-dashed"></div>

                <div class="py-3">
                  <h5 class="mb-1">
                    <BLink href="javascript:void(0);">Skote - Admin & Dashboard Template by Themesbrand</BLink>
                  </h5>
                  <p class="text-success mb-2">
                    https://themesbrand.com/skote/
                  </p>
                  <p class="text-muted mb-2">
                    Skote is an admin dashboard template that is a beautifully
                    crafted, clean & minimal designed admin template with Dark,
                    Light Layouts with RTL options. You can build any type of
                    web application like Saas based interface, eCommerce,
                    Crypto, CRM, CMS, Project management apps, Admin Panels,
                    etc.
                  </p>
                  <ul class="
                      list-inline
                      d-flex
                      align-items-center
                      g-3
                      text-muted
                      fs-14
                      mb-0
                    ">
                    <li class="list-inline-item me-3">
                      <i class="ri-thumb-up-line align-middle me-1"></i>485
                    </li>
                    <li class="list-inline-item me-3">
                      <i class="ri-question-answer-line align-middle me-1"></i>167
                    </li>
                    <li class="list-inline-item">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                          <i class="ri-user-line"></i>
                        </div>
                        <div class="flex-grow-1 fs-13 ms-1">
                          <span class="fw-medium">Themesbrand</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>

                <div class="border border-dashed"></div>

                <div class="py-3">
                  <h5 class="mb-1">
                    <BLink href="javascript:void(0);">Minia - React Js Admin & Dashboard Template</BLink>
                  </h5>
                  <p class="text-success mb-2">
                    https://themesbrand.com/minia/react/
                  </p>
                  <p class="text-muted mb-2">
                    Minia react is a simple and beautiful admin template built
                    with Bootstrap ^5.1.3. It has
                    <span class="fw-semibold">5+ different layouts and 3 modes</span>
                    ( Dark, Light & RTL ) which are managed by SCSS only. You
                    can simply change to any layouts or mode by changing a
                    couple of lines code.
                  </p>
                  <ul class="
                      list-inline
                      d-flex
                      align-items-center
                      g-3
                      text-muted
                      fs-14
                      mb-0
                    ">
                    <li class="list-inline-item me-3">
                      <i class="ri-thumb-up-line align-middle me-1"></i>69
                    </li>
                    <li class="list-inline-item me-3">
                      <i class="ri-question-answer-line align-middle me-1"></i>43
                    </li>
                    <li class="list-inline-item">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                          <i class="ri-user-line"></i>
                        </div>
                        <div class="flex-grow-1 fs-13 ms-1">
                          <span class="fw-medium">Themesbrand</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>

                <div class="border border-dashed"></div>

                <div class="py-3">
                  <h5 class="mb-1">
                    <BLink href="javascript:void(0);">Doson - Angular Admin & Dashboard Template by
                      Themesbrand</BLink>
                  </h5>
                  <p class="text-success mb-2">
                    https://themesbrand.com/dason/angular/
                  </p>
                  <p class="text-muted mb-2">
                    Dason is a simple and beautiful admin template built with
                    Bootstrap ^5.1.3. It has 5+ different layouts and 3 modes (
                    Dark, Light & RTL ) which are managed by SCSS only. You can
                    simply change to any layouts or mode by changing a couple of
                    lines code.
                  </p>
                  <ul class="
                      list-inline
                      d-flex
                      align-items-center
                      g-3
                      text-muted
                      fs-14
                      mb-0
                    ">
                    <li class="list-inline-item me-3">
                      <i class="ri-thumb-up-line align-middle me-1"></i>102
                    </li>
                    <li class="list-inline-item me-3">
                      <i class="ri-question-answer-line align-middle me-1"></i>36
                    </li>
                    <li class="list-inline-item">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                          <i class="ri-user-line"></i>
                        </div>
                        <div class="flex-grow-1 fs-13 ms-1">
                          <span class="fw-medium">Themesbrand</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>

                <div>
                  <ul class="
                      pagination pagination-separated
                      justify-content-center
                      mb-0
                    ">
                    <li class="page-item disabled">
                      <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-left"></i></BLink>
                    </li>
                    <li class="page-item active">
                      <BLink href="javascript:void(0);" class="page-link">1</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">2</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">3</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">4</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">5</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-right"></i>
                      </BLink>
                    </li>
                  </ul>
                </div>
              </BTab>
              <BTab>
                <template #title>
                  <i class="ri-image-fill text-muted align-bottom me-1"></i>
                  Images
                </template>
                <BRow class="pt-4">
                  <BCol lg="12">
                    <div class="images-menu mb-3">
                      <swiper class="swiper responsive-swiper rounded gallery-light pb-4" :loop="true" :slidesPerView="8"
                        :spaceBetween="5">
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-12.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Bootstrap</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-11.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Website</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-10.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Responsive</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-9.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Design</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-8.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">eCommerce</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-7.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Templates</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-6.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Admin Panel</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-5.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Simple</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                        <swiper-slide>
                          <div class="swiper-slide">
                            <div class="
                                d-flex
                                align-items-center
                                border border-dashed
                                rounded
                                p-2
                              ">
                              <div class="flex-shrink-0">
                                <img src="@/assets/images/small/img-3.jpg" alt="" width="65" class="rounded" />
                              </div>
                              <div class="flex-grow-1 ms-2">
                                <BLink href="javascript:void(0);" class="stretched-link fw-medium">Dark</BLink>
                              </div>
                            </div>
                          </div>
                        </swiper-slide>
                      </swiper>
                    </div>
                  </BCol>
                </BRow>
                <div class="gallery-light">
                  <BRow>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-1.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-1.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Glasses and laptop from above
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Ron Mackie</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-2.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-2.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Working at a coffee shop
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Nancy Martino</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-3.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-3.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Photo was taken in Beach
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Elwood Arter</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-4.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-4.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">Drawing a sketch</h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Jason McQuaid</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-5.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-5.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Working from home little spot
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Henry Baird</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-6.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-6.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Project discussion with team
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Erica Kernan</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-7.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-7.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Sunrise above a beach
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">James Ballard</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-8.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-8.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Glasses and laptop from above
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Ruby Griffin</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-9.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-9.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Dramatic clouds at the Golden Gate Bridge
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Ron Mackie</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-10.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-10.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Fun day at the Hill Station
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Henry Baird</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-11.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-11.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                Cycling in the countryside
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Nancy Martino</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                    <BCol xl="3" lg="4" sm="6">
                      <BCard no-body class="gallery-box">
                        <div class="gallery-container">
                          <BLink class="image-popup" href="assets/images/small/img-12.jpg" title="">
                            <img class="gallery-img img-fluid mx-auto" src="@/assets/images/small/img-12.jpg" alt="" />
                            <div class="gallery-overlay">
                              <h5 class="overlay-caption">
                                A mix of friends and strangers heading off to
                                find an adventure.
                              </h5>
                            </div>
                          </BLink>
                        </div>
                        <div class="box-content">
                          <div class="d-flex align-items-center mt-2">
                            <div class="flex-grow-1 text-muted">
                              by
                              <BLink href="" class="text-body text-truncate">Erica Kernan</BLink>
                            </div>
                            <div class="flex-shrink-0">
                              <div class="d-flex gap-3">
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-thumb-up-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  2.2K
                                </BButton>
                                <BButton type="button" variant="link" size="sm" class="
                                    
                                    fs-12
                                    text-body text-decoration-none
                                    px-0
                                  ">
                                  <i class="
                                      ri-question-answer-fill
                                      text-muted
                                      align-bottom
                                      me-1
                                    "></i>
                                  1.3K
                                </BButton>
                              </div>
                            </div>
                          </div>
                        </div>
                      </BCard>
                    </BCol>
                  </BRow>
                  <div class="mt-4">
                    <ul class="
                        pagination pagination-separated
                        justify-content-center
                        mb-0
                      ">
                      <li class="page-item disabled">
                        <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-left"></i>
                        </BLink>
                      </li>
                      <li class="page-item active">
                        <BLink href="javascript:void(0);" class="page-link">1</BLink>
                      </li>
                      <li class="page-item">
                        <BLink href="javascript:void(0);" class="page-link">2</BLink>
                      </li>
                      <li class="page-item">
                        <BLink href="javascript:void(0);" class="page-link">3</BLink>
                      </li>
                      <li class="page-item">
                        <BLink href="javascript:void(0);" class="page-link">4</BLink>
                      </li>
                      <li class="page-item">
                        <BLink href="javascript:void(0);" class="page-link">5</BLink>
                      </li>
                      <li class="page-item">
                        <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-right"></i>
                        </BLink>
                      </li>
                    </ul>
                  </div>
                </div>
              </BTab>
              <BTab>
                <template #title>
                  <i class="ri-list-unordered text-muted align-bottom me-1"></i>
                  News
                </template>
                <BRow class="pt-4">
                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-1.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="success-subtle" class="bg-success-subtle text-success fs-11">Business
                                </BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">A mix of friends and strangers heading off to
                                find an adventure</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                James Ballard
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                23 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-2.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="warning-subtle" class="bg-warning-subtle text-warning fs-11">Development
                                </BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">How to get creative in your work ?</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Ruby Griffin
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                23 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-3.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="info-subtle" class="bg-info-subtle text-info fs-11">Fashion</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">How to become a best sale marketer in a
                                year!</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Elwood Arter
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                23 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-4.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="primary-subtle"
                                  class="bg-primary-subtle text-primary fs-11">Product</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">Manage white space in responsive layouts ?</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Nancy Martino
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                23 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-5.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="success-subtle"
                                  class="bg-success-subtle text-success fs-11">Business</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">Stack designer Olivia Murphy offers freelancing
                                advice</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Erica Kernan
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                11 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-6.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="danger-subtle"
                                  class="bg-danger-subtle text-danger fs-11">Design</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">A day in the of a professional fashion
                                designer</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Jason McQuaid
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                14 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-7.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="danger-subtle"
                                  class="bg-danger-subtle text-danger fs-11">Design</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">Design your apps in your own way</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Henry Baird
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                19 Nov, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>

                  <BCol lg="6">
                    <BCard no-body class="border">
                      <BCardBody>
                        <div class="d-sm-flex">
                          <div class="flex-shrink-0">
                            <img src="@/assets/images/small/img-8.jpg" alt="" width="115" class="rounded-1" />
                          </div>
                          <div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
                            <ul class="list-inline mb-2">
                              <li class="list-inline-item">
                                <BBadge variant="warning-subtle"
                                  class="bg-warning-subtle text-warning fs-11">Development</BBadge>
                              </li>
                            </ul>
                            <h5>
                              <BLink href="javascript:void(0);">How apps is changing the IT world</BLink>
                            </h5>
                            <ul class="list-inline mb-0">
                              <li class="list-inline-item">
                                <i class="
                                    ri-user-3-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                Elwood Arter
                              </li>
                              <li class="list-inline-item">
                                <i class="
                                    ri-calendar-2-fill
                                    text-success
                                    align-middle
                                    me-1
                                  "></i>
                                10 Aug, 2021
                              </li>
                            </ul>
                          </div>
                        </div>
                      </BCardBody>
                    </BCard>
                  </BCol>
                </BRow>

                <div class="mt-4">
                  <ul class="
                      pagination pagination-separated
                      justify-content-center
                      mb-0
                    ">
                    <li class="page-item disabled">
                      <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-left"></i></BLink>
                    </li>
                    <li class="page-item active">
                      <BLink href="javascript:void(0);" class="page-link">1</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">2</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">3</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">4</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link">5</BLink>
                    </li>
                    <li class="page-item">
                      <BLink href="javascript:void(0);" class="page-link"><i class="mdi mdi-chevron-right"></i>
                      </BLink>
                    </li>
                  </ul>
                </div>
              </BTab>
              <BTab>
                <template #title>
                  <i class="ri-video-line text-muted align-bottom me-1"></i>
                  Videos
                </template>
                <BRow class="pt-4">
                  <BCol lg="12" class="video-list">
                    <div class="list-element">
                      <h5 class="mb-1">
                        <BLink href="javascript:void(0);">Admin dashboard templates - Material Design for
                          Velzon</BLink>
                      </h5>
                      <p class="text-success">
                        https://themesbrand.com/velzon/index.html
                      </p>
                      <div class="d-flex flex-column flex-sm-row">
                        <div class="flex-shrink-0">
                          <iframe src="https://www.youtube.com/embed/GfSZtaoc5bw" title="YouTube video" allowfullscreen
                            class="rounded"></iframe>
                        </div>
                        <div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
                          <p class="text-muted mb-0">
                            Velzon admin is super flexible, powerful, clean,
                            modern & responsive admin template based on
                            <b>bootstrap 5</b> stable with unlimited
                            possibilities. You can simply change to any layout
                            or mode by changing a couple of lines of code. You
                            can start small and large projects or update design
                            in your existing project using Velzon it is very
                            quick and easy as it is beautiful, adroit, and
                            delivers the ultimate user experience.
                          </p>
                          <div class="border border-dashed mb-1 mt-3"></div>
                          <ul class="
                              list-inline
                              d-flex
                              align-items-center
                              g-3
                              text-muted
                              fs-14
                              mb-0
                            ">
                            <li class="list-inline-item me-3">
                              <i class="ri-thumb-up-line align-middle me-1"></i>335
                            </li>
                            <li class="list-inline-item me-3">
                              <i class="
                                  ri-question-answer-line
                                  align-middle
                                  me-1
                                "></i>102
                            </li>
                            <li class="list-inline-item">
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                  <i class="ri-user-line"></i>
                                </div>
                                <div class="flex-grow-1 fs-13 ms-1">
                                  <span class="fw-medium">Themesbrand</span>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>

                    <div class="list-element mt-4">
                      <h5 class="mb-1">
                        <BLink href="javascript:void(0);">Create Responsive Admin Dashboard using Html CSS</BLink>
                      </h5>
                      <p class="text-success">
                        https://themesbrand.com/velzon/index.html
                      </p>
                      <div class="d-flex flex-column flex-sm-row">
                        <div class="flex-shrink-0">
                          <iframe src="https://www.youtube.com/embed/Z-fV2lGKnnU" title="YouTube video" allowfullscreen
                            class="rounded"></iframe>
                        </div>
                        <div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
                          <p class="text-muted mb-0">
                            Velzon admin is super flexible, powerful, clean,
                            modern & responsive admin template based on
                            <b>bootstrap 5</b> stable with unlimited
                            possibilities. You can simply change to any layout
                            or mode by changing a couple of lines of code. You
                            can start small and large projects or update design
                            in your existing project using Velzon it is very
                            quick and easy as it is beautiful, adroit, and
                            delivers the ultimate user experience.
                          </p>
                          <div class="border border-dashed mb-1 mt-3"></div>
                          <ul class="
                              list-inline
                              d-flex
                              align-items-center
                              g-3
                              text-muted
                              fs-14
                              mb-0
                            ">
                            <li class="list-inline-item me-3">
                              <i class="ri-thumb-up-line align-middle me-1"></i>485
                            </li>
                            <li class="list-inline-item me-3">
                              <i class="
                                  ri-question-answer-line
                                  align-middle
                                  me-1
                                "></i>167
                            </li>
                            <li class="list-inline-item">
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                  <i class="ri-user-line"></i>
                                </div>
                                <div class="flex-grow-1 fs-13 ms-1">
                                  <span class="fw-medium">Themesbrand</span>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>

                    <div class="list-element mt-4">
                      <h5 class="mb-1">
                        <BLink href="javascript:void(0);">Velzon - The Most Popular Bootstrap 5 HTML, Angular &
                          React Js Admin</BLink>
                      </h5>
                      <p class="text-success">
                        https://themesbrand.com/velzon/index.html
                      </p>
                      <div class="d-flex flex-column flex-sm-row">
                        <div class="flex-shrink-0">
                          <iframe src="https://www.youtube.com/embed/2RZQN_ko0iU" title="YouTube video" allowfullscreen
                            class="rounded"></iframe>
                        </div>
                        <div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
                          <p class="text-muted mb-0">
                            Velzon admin is super flexible, powerful, clean,
                            modern & responsive admin template based on
                            <b>bootstrap 5</b> stable with unlimited
                            possibilities. You can simply change to any layout
                            or mode by changing a couple of lines of code. You
                            can start small and large projects or update design
                            in your existing project using Velzon it is very
                            quick and easy as it is beautiful, adroit, and
                            delivers the ultimate user experience.
                          </p>
                          <div class="border border-dashed mb-1 mt-3"></div>
                          <ul class="
                              list-inline
                              d-flex
                              align-items-center
                              g-3
                              text-muted
                              fs-14
                              mb-0
                            ">
                            <li class="list-inline-item me-3">
                              <i class="ri-thumb-up-line align-middle me-1"></i>122
                            </li>
                            <li class="list-inline-item me-3">
                              <i class="
                                  ri-question-answer-line
                                  align-middle
                                  me-1
                                "></i>51
                            </li>
                            <li class="list-inline-item">
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                  <i class="ri-user-line"></i>
                                </div>
                                <div class="flex-grow-1 fs-13 ms-1">
                                  <span class="fw-medium">Themesbrand</span>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>

                    <div class="list-element mt-4">
                      <h5 class="mb-1">
                        <BLink href="javascript:void(0);">Velzon Admin Dashboard (website analytics) with
                          Bootstrap 5</BLink>
                      </h5>
                      <p class="text-success">
                        https://themesbrand.com/velzon/index.html
                      </p>
                      <div class="d-flex flex-column flex-sm-row">
                        <div class="flex-shrink-0">
                          <iframe src="https://www.youtube.com/embed/Z-fV2lGKnnU" title="YouTube video" allowfullscreen
                            class="rounded"></iframe>
                        </div>
                        <div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
                          <p class="text-muted mb-0">
                            Velzon admin is super flexible, powerful, clean,
                            modern & responsive admin template based on
                            <b>bootstrap 5</b> stable with unlimited
                            possibilities. You can simply change to any layout
                            or mode by changing a couple of lines of code. You
                            can start small and large projects or update design
                            in your existing project using Velzon it is very
                            quick and easy as it is beautiful, adroit, and
                            delivers the ultimate user experience.
                          </p>
                          <div class="border border-dashed mb-1 mt-3"></div>
                          <ul class="
                              list-inline
                              d-flex
                              align-items-center
                              g-3
                              text-muted
                              fs-14
                              mb-0
                            ">
                            <li class="list-inline-item me-3">
                              <i class="ri-thumb-up-line align-middle me-1"></i>485
                            </li>
                            <li class="list-inline-item me-3">
                              <i class="
                                  ri-question-answer-line
                                  align-middle
                                  me-1
                                "></i>69
                            </li>
                            <li class="list-inline-item">
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                  <i class="ri-user-line"></i>
                                </div>
                                <div class="flex-grow-1 fs-13 ms-1">
                                  <span class="fw-medium">Themesbrand</span>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>

                    <div class="list-element mt-4">
                      <h5 class="mb-1">
                        <BLink href="javascript:void(0);">Dashboard Admin Basics - YouTube</BLink>
                      </h5>
                      <p class="text-success">
                        https://themesbrand.com/velzon/index.html
                      </p>
                      <div class="d-flex flex-column flex-sm-row">
                        <div class="flex-shrink-0">
                          <iframe src="https://www.youtube.com/embed/1y_kfWUCFDQ" title="YouTube video" allowfullscreen
                            class="rounded"></iframe>
                        </div>
                        <div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
                          <p class="text-muted mb-0">
                            Velzon admin is super flexible, powerful, clean,
                            modern & responsive admin template based on
                            <b>bootstrap 5</b> stable with unlimited
                            possibilities. You can simply change to any layout
                            or mode by changing a couple of lines of code. You
                            can start small and large projects or update design
                            in your existing project using Velzon it is very
                            quick and easy as it is beautiful, adroit, and
                            delivers the ultimate user experience.
                          </p>
                          <div class="border border-dashed mb-1 mt-3"></div>
                          <ul class="
                              list-inline
                              d-flex
                              align-items-center
                              g-3
                              text-muted
                              fs-14
                              mb-0
                            ">
                            <li class="list-inline-item me-3">
                              <i class="ri-thumb-up-line align-middle me-1"></i>58
                            </li>
                            <li class="list-inline-item me-3">
                              <i class="
                                  ri-question-answer-line
                                  align-middle
                                  me-1
                                "></i>24
                            </li>
                            <li class="list-inline-item">
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                  <i class="ri-user-line"></i>
                                </div>
                                <div class="flex-grow-1 fs-13 ms-1">
                                  <span class="fw-medium">Themesbrand</span>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </BCol>
                  <div class="text-center">
                    <BButton id="loadmore" variant="link" class="text-success mt-2">
                      <i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i>
                      Load more
                    </BButton>
                  </div>
                </BRow>
              </BTab>
            </BTabs>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>