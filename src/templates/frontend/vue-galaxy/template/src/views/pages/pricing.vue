<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

export default {
  methods: {
    monthly() {
      document.getElementById('month-tab').classList.add('active');
      document.getElementById('annual-tab').classList.remove('active');
      const highlightedItems = document.querySelectorAll(".month");

      highlightedItems.forEach(function (userItem) {
        userItem.style.display = "block";
      });
      const highlightedItems2 = document.querySelectorAll(".annual");

      highlightedItems2.forEach(function (userItem) {
        userItem.style.display = "none";
      });
    },
    anually() {
      document.getElementById('month-tab').classList.remove('active');
      document.getElementById('annual-tab').classList.add('active');
      const highlightedItems = document.querySelectorAll(".month");

      highlightedItems.forEach(function (userItem) {
        userItem.style.display = "none";
      });
      const highlightedItems2 = document.querySelectorAll(".annual");

      highlightedItems2.forEach(function (userItem) {
        userItem.style.display = "block";
      });
    },
  },
  mounted() {
    const highlightedItems2 = document.querySelectorAll(".annual");

    highlightedItems2.forEach(function (userItem) {
      userItem.style.display = "none";
    });
  },
  components: {
    Layout,
    PageHeader,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Pricing" pageTitle="Pages" />

    <BRow class="justify-content-center mt-4">
      <BCol lg="5">
        <div class="text-center mb-4">
          <h4 class="fw-semibold fs-22">Plans & Pricing</h4>
          <p class="text-muted mb-4 fs-15">
            Simple pricing. No hidden fees. Advanced features for you business.
          </p>

          <div class="d-inline-flex">
            <ul class="nav nav-pills arrow-navtabs plan-nav rounded mb-3 p-1" id="pills-tab" role="tablist">
              <li class="nav-item" role="presentation">
                <BButton variant="link" class="nav-link fw-semibold active" id="month-tab" data-bs-toggle="pill"
                  data-bs-target="#month" type="button" role="tab" aria-selected="true" @click="monthly">
                  Monthly
                </BButton>
              </li>
              <li class="nav-item" role="presentation">
                <BButton variant="link" class="nav-link fw-semibold" id="annual-tab" data-bs-toggle="pill"
                  data-bs-target="#annual" type="button" role="tab" aria-selected="false" @click="anually">
                  Annually <BBadge variant="success">25% Off</BBadge>
                </BButton>
              </li>
            </ul>
          </div>
        </div>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="3" lg="6">
        <BCard no-body class="pricing-box">
          <BCardBody class="bg-light m-2 p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="flex-grow-1">
                <h5 class="mb-0 fw-semibold">Starter</h5>
              </div>
              <div class="ms-auto">
                <h2 class="month mb-0">
                  $19 <small class="fs-13 text-muted">/Month</small>
                </h2>
                <h2 class="annual mb-0">
                  <small class="fs-16"><del>$228</del></small> $171
                  <small class="fs-13 text-muted">/Year</small>
                </h2>
              </div>
            </div>

            <p class="text-muted">
              The perfect way to get started and get used to our tools.
            </p>
            <ul class="list-unstyled vstack gap-3">
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>3</b> Projects</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>299</b> Customers</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Scalable Bandwidth</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>5</b> FTP Login</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>24/7</b> Support</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Domain</div>
                </div>
              </li>
            </ul>
            <div class="mt-3 pt-2">
              <BLink href="javascript:void(0);" class="btn btn-danger disabled w-100">Your Current Plan</BLink>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" lg="6">
        <BCard no-body class="pricing-box">
          <BCardBody class="bg-light m-2 p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="flex-grow-1">
                <h5 class="mb-0 fw-semibold">Professional</h5>
              </div>
              <div class="ms-auto">
                <h2 class="month mb-0">
                  $29 <small class="fs-13 text-muted">/Month</small>
                </h2>
                <h2 class="annual mb-0">
                  <small class="fs-16"><del>$348</del></small> $261
                  <small class="fs-13 text-muted">/Year</small>
                </h2>
              </div>
            </div>
            <p class="text-muted">
              Excellent for scalling teams to build culture. Special plan for
              professional business.
            </p>
            <ul class="list-unstyled vstack gap-3">
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>8</b> Projects</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>449</b> Customers</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Scalable Bandwidth</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>7</b> FTP Login</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>24/7</b> Support</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Domain</div>
                </div>
              </li>
            </ul>
            <div class="mt-3 pt-2">
              <BLink href="javascript:void(0);" class="btn btn-primary w-100">Change Plan</BLink>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" lg="6">
        <BCard no-body class="pricing-box ribbon-box right">
          <BCardBody class="bg-light m-2 p-4">
            <div class="ribbon-two ribbon-two-danger"><span>Popular</span></div>
            <div class="d-flex align-items-center mb-3">
              <div class="flex-grow-1">
                <h5 class="mb-0 fw-semibold">Enterprise</h5>
              </div>
              <div class="ms-auto">
                <h2 class="month mb-0">
                  $39 <small class="fs-13 text-muted">/Month</small>
                </h2>
                <h2 class="annual mb-0">
                  <small class="fs-16"><del>$468</del></small> $351
                  <small class="fs-13 text-muted">/Year</small>
                </h2>
              </div>
            </div>
            <p class="text-muted">
              This plan is for those who have a team already and running a large
              business.
            </p>
            <ul class="list-unstyled vstack gap-3">
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>15</b> Projects</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Customers</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Scalable Bandwidth</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>12</b> FTP Login</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>24/7</b> Support</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>35GB</b> Storage</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-danger me-1">
                    <i class="ri-close-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Domain</div>
                </div>
              </li>
            </ul>
            <div class="mt-3 pt-2">
              <BLink href="javascript:void(0);" class="btn btn-primary w-100">Change Plan</BLink>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" lg="6">
        <BCard no-body class="pricing-box">
          <BCardBody class="bg-light m-2 p-4">
            <div class="d-flex align-items-center mb-3">
              <div class="flex-grow-1">
                <h5 class="mb-0 fw-semibold">Unlimited</h5>
              </div>
              <div class="ms-auto">
                <h2 class="month mb-0">
                  $49 <small class="fs-13 text-muted">/Month</small>
                </h2>
                <h2 class="annual mb-0">
                  <small class="fs-16"><del>$588</del></small> $441
                  <small class="fs-13 text-muted">/Year</small>
                </h2>
              </div>
            </div>
            <p class="text-muted">
              For most businesses that want to optimize web queries.
            </p>
            <ul class="list-unstyled vstack gap-3">
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Projects</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Customers</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Scalable Bandwidth</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> FTP Login</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>24/7</b> Support</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                </div>
              </li>
              <li>
                <div class="d-flex">
                  <div class="flex-shrink-0 text-success me-1">
                    <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                  </div>
                  <div class="flex-grow-1">Domain</div>
                </div>
              </li>
            </ul>
            <div class="mt-3 pt-2">
              <BLink href="javascript:void(0);" class="btn btn-primary w-100">Change Plan</BLink>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow class="justify-content-center mt-5">
      <BCol lg="5">
        <div class="text-center mb-4 pb-2">
          <h4 class="fw-semibold fs-22">
            Choose the plan that's right for you
          </h4>
          <p class="text-muted mb-4 fs-15">
            Simple pricing. No hidden fees. Advanced features for you business.
          </p>
        </div>
      </BCol>
    </BRow>

    <BRow class="justify-content-center">
      <BCol xl="9">
        <BRow>
          <BCol lg="4">
            <BCard no-body class="pricing-box">
              <BCardBody class="p-4 m-2">
                <div class="d-flex align-items-center">
                  <div class="flex-grow-1">
                    <h5 class="mb-1 fw-semibold">Basic Plan</h5>
                    <p class="text-muted mb-0">For Startup</p>
                  </div>
                  <div class="avatar-sm">
                    <div class="avatar-title bg-light rounded-circle text-primary">
                      <i class="ri-book-mark-line fs-20"></i>
                    </div>
                  </div>
                </div>
                <div class="pt-4">
                  <h2>
                    <sup><small>$</small></sup>19 <span class="fs-13 text-muted">/Month</span>
                  </h2>
                </div>
                <hr class="my-4 text-muted" />
                <div>
                  <ul class="list-unstyled text-muted vstack gap-3">
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Upto <b>3</b> Projects</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Upto <b>299</b> Customers</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Scalable Bandwidth</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>5</b> FTP Login</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-danger me-1">
                          <i class="ri-close-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>24/7</b> Support</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-danger me-1">
                          <i class="ri-close-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-danger me-1">
                          <i class="ri-close-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Domain</div>
                      </div>
                    </li>
                  </ul>
                  <div class="mt-4">
                    <BLink href="javascript:void(0);" class="
                        btn btn-soft-primary
                        w-100
                        waves-effect waves-light
                      ">Sign up free</BLink>
                  </div>
                </div>
              </BCardBody>
            </BCard>
          </BCol>
          <BCol lg="4">
            <BCard no-body class="pricing-box ribbon-box right">
              <BCardBody class="p-4 m-2">
                <div class="ribbon-two ribbon-two-danger">
                  <span>Popular</span>
                </div>
                <div>
                  <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                      <h5 class="mb-1 fw-semibold">Pro Business</h5>
                      <p class="text-muted mb-0">Professional plans</p>
                    </div>
                    <div class="avatar-sm">
                      <div class="
                          avatar-title
                          bg-light
                          rounded-circle
                          text-primary
                        ">
                        <i class="ri-medal-line fs-20"></i>
                      </div>
                    </div>
                  </div>

                  <div class="pt-4">
                    <h2>
                      <sup><small>$</small></sup> 29<span class="fs-13 text-muted">/Month</span>
                    </h2>
                  </div>
                </div>
                <hr class="my-4 text-muted" />
                <div>
                  <ul class="list-unstyled vstack gap-3 text-muted">
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Upto <b>15</b> Projects</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">
                          <b>Unlimited</b> Customers
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Scalable Bandwidth</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>12</b> FTP Login</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>24/7</b> Support</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-danger me-1">
                          <i class="ri-close-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-danger me-1">
                          <i class="ri-close-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Domain</div>
                      </div>
                    </li>
                  </ul>
                  <div class="mt-4">
                    <BLink href="javascript:void(0);" class="btn btn-primary w-100 waves-effect waves-light">Get
                      started</BLink>
                  </div>
                </div>
              </BCardBody>
            </BCard>
          </BCol>
          <BCol lg="4">
            <BCard no-body class="pricing-box">
              <BCardBody class="p-4 m-2">
                <div>
                  <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                      <h5 class="mb-1 fw-semibold">Platinum Plan</h5>
                      <p class="text-muted mb-0">Enterprise Businesses</p>
                    </div>
                    <div class="avatar-sm">
                      <div class="
                          avatar-title
                          bg-light
                          rounded-circle
                          text-primary
                        ">
                        <i class="ri-stack-line fs-20"></i>
                      </div>
                    </div>
                  </div>

                  <div class="pt-4">
                    <h2>
                      <sup><small>$</small></sup> 39<span class="fs-13 text-muted">/Month</span>
                    </h2>
                  </div>
                </div>
                <hr class="my-4 text-muted" />
                <div>
                  <ul class="list-unstyled vstack gap-3 text-muted">
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>Unlimited</b> Projects</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">
                          <b>Unlimited</b> Customers
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Scalable Bandwidth</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">
                          <b>Unlimited</b> FTP Login
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>24/7</b> Support</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1"><b>Unlimited</b> Storage</div>
                      </div>
                    </li>
                    <li>
                      <div class="d-flex">
                        <div class="flex-shrink-0 text-success me-1">
                          <i class="ri-checkbox-circle-fill fs-15 align-middle"></i>
                        </div>
                        <div class="flex-grow-1">Domain</div>
                      </div>
                    </li>
                  </ul>
                  <div class="mt-4">
                    <BLink href="javascript:void(0);" class="
                        btn btn-soft-primary
                        w-100
                        waves-effect waves-light
                      ">Get started</BLink>
                  </div>
                </div>
              </BCardBody>
            </BCard>
          </BCol>
        </BRow>
      </BCol>
    </BRow>

    <BRow class="justify-content-center mt-5">
      <BCol lg="4">
        <div class="text-center mb-4 pb-2">
          <h4 class="fw-semibold fs-22">Simple Pricing Plan</h4>
          <p class="text-muted mb-4 fs-15">
            Simple pricing. No hidden fees. Advanced features for you business.
          </p>
        </div>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="6">
        <BCard no-body class="pricing-box text-center">
          <BRow class="g-0">
            <BCol lg="6">
              <BCardBody class="h-100">
                <div>
                  <h5 class="mb-1">Starter</h5>
                  <p class="text-muted">Starter plans</p>
                </div>

                <div class="py-4">
                  <h2>
                    <sup><small>$</small></sup>22 <span class="fs-13 text-muted"> /Per month</span>
                  </h2>
                </div>

                <div class="text-center plan-btn mt-2">
                  <BLink href="javascript:void(0);" class="btn btn-primary w-sm waves-effect waves-light">Sign up
                  </BLink>
                </div>
              </BCardBody>
            </BCol>
            <BCol lg="6">
              <BCardBody class="border-start mt-4 mt-lg-0">
                <BCardHeader class="bg-light">
                  <h5 class="fs-15 mb-0">Plan Features:</h5>
                </BCardHeader>
                <BCardBody class="pb-0">
                  <ul class="list-unstyled vstack gap-3 mb-0">
                    <li>
                      Users: <span class="text-success fw-semibold">1</span>
                    </li>
                    <li>
                      Storage:
                      <span class="text-success fw-semibold">01 GB</span>
                    </li>
                    <li>
                      Domain: <span class="text-success fw-semibold">No</span>
                    </li>
                    <li>
                      Support: <span class="text-success fw-semibold">No</span>
                    </li>
                  </ul>
                </BCardBody>
              </BCardBody>
            </BCol>
          </BRow>
        </BCard>
      </BCol>

      <BCol lg="6">
        <BCard no-body class="pricing-box ribbon-box ribbon-fill text-center">
          <div class="ribbon ribbon-primary">New</div>
          <BRow class="g-0">
            <BCol lg="6">
              <BCardBody class="h-100">
                <div>
                  <h5 class="mb-1">Professional</h5>
                  <p class="text-muted">Professional plans</p>
                </div>

                <div class="py-4">
                  <h2>
                    <sup><small>$</small></sup>29 <span class="fs-13 text-muted">/Per month</span>
                  </h2>
                </div>

                <div class="text-center plan-btn mt-2">
                  <BLink href="javascript:void(0);" class="btn btn-primary w-sm waves-effect waves-light">Sign up
                  </BLink>
                </div>
              </BCardBody>
            </BCol>
            <BCol lg="6">
              <BCardBody class="border-start mt-4 mt-lg-0">
                <BCardHeader class="bg-light">
                  <h5 class="fs-15 mb-0">Plan Features:</h5>
                </BCardHeader>
                <BCardBody class="pb-0">
                  <ul class="list-unstyled vstack gap-3 mb-0">
                    <li>
                      Users: <span class="text-success fw-semibold">3</span>
                    </li>
                    <li>
                      Storage:
                      <span class="text-success fw-semibold">10 GB</span>
                    </li>
                    <li>
                      Domain: <span class="text-success fw-semibold">Yes</span>
                    </li>
                    <li>
                      Support: <span class="text-success fw-semibold">No</span>
                    </li>
                  </ul>
                </BCardBody>
              </BCardBody>
            </BCol>
          </BRow>
        </BCard>
      </BCol>

      <BCol lg="6">
        <BCard no-body class="pricing-box ribbon-box ribbon-fill text-center">
          <div class="ribbon ribbon-primary">New</div>
          <BRow class="g-0">
            <BCol lg="6">
              <BCardBody class="h-100">
                <div>
                  <h5 class="mb-1">Enterprise</h5>
                  <p class="text-muted">Enterprise plans</p>
                </div>

                <div class="py-4">
                  <h2>
                    <sup><small>$</small></sup>39 <span class="fs-13 text-muted">/Per month</span>
                  </h2>
                </div>

                <div class="text-center plan-btn mt-2">
                  <BLink href="javascript:void(0);" class="btn btn-primary w-sm waves-effect waves-light">Sign up
                  </BLink>
                </div>
              </BCardBody>
            </BCol>
            <BCol lg="6">
              <BCardBody class="border-start mt-4 mt-lg-0">
                <BCardHeader class="bg-light">
                  <h5 class="fs-15 mb-0">Plan Features:</h5>
                </BCardHeader>
                <BCardBody class="pb-0">
                  <ul class="list-unstyled vstack gap-3 mb-0">
                    <li>
                      Users: <span class="text-success fw-semibold">3</span>
                    </li>
                    <li>
                      Storage:
                      <span class="text-success fw-semibold">20 GB</span>
                    </li>
                    <li>
                      Domain: <span class="text-success fw-semibold">Yes</span>
                    </li>
                    <li>
                      Support: <span class="text-success fw-semibold">Yes</span>
                    </li>
                  </ul>
                </BCardBody>
              </BCardBody>
            </BCol>
          </BRow>
        </BCard>
      </BCol>

      <BCol lg="6">
        <BCard no-body class="pricing-box text-center">
          <BRow class="g-0">
            <BCol lg="6">
              <BCardBody class="h-100">
                <div>
                  <h5 class="mb-1">Unlimited</h5>
                  <p class="text-muted">Unlimited plans</p>
                </div>
                <div class="py-4">
                  <h2>
                    <sup><small>$</small></sup>49 <span class="fs-13 text-muted">/Per month</span>
                  </h2>
                </div>

                <div class="text-center plan-btn mt-2">
                  <BLink href="javascript:void(0);" class="btn btn-primary w-sm waves-effect waves-light">Sign up
                  </BLink>
                </div>
              </BCardBody>
            </BCol>
            <BCol lg="6">
              <BCardBody class="border-start mt-4 mt-lg-0">
                <BCardHeader class="bg-light">
                  <h5 class="fs-15 mb-0">Plan Features:</h5>
                </BCardHeader>
                <BCardBody class="pb-0">
                  <ul class="list-unstyled vstack gap-3 mb-0">
                    <li>
                      Users: <span class="text-success fw-semibold">5</span>
                    </li>
                    <li>
                      Storage:
                      <span class="text-success fw-semibold">40 GB</span>
                    </li>
                    <li>
                      Domain: <span class="text-success fw-semibold">Yes</span>
                    </li>
                    <li>
                      Support: <span class="text-success fw-semibold">Yes</span>
                    </li>
                  </ul>
                </BCardBody>
              </BCardBody>
            </BCol>
          </BRow>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
