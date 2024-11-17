<script>
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

export default {
  data() {
    return {
      value: null,
      value1: null,
      date: null,
      rangeDateconfig: {
        mode: "range",
        dateFormat: "d M, Y",
      },
    };
  },
  components: {
    Layout,
    PageHeader,
    Multiselect,
    flatPickr,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="ICO List" pageTitle="Crypto" />
    <BRow class="row-cols-xxl-5 row-cols-lg-3 row-cols-sm-2 row-cols-1">
      <BCol>
        <BCard no-body>
          <BCardBody class="d-flex">
            <div class="flex-grow-1">
              <h4>4751</h4>
              <h6 class="text-muted fs-13 mb-0">ICOs Published</h6>
            </div>
            <div class="flex-shrink-0 avatar-sm">
              <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                <i class="ri-upload-2-line"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="d-flex">
            <div class="flex-grow-1">
              <h4>3423</h4>
              <h6 class="text-muted fs-13 mb-0">Active ICOs</h6>
            </div>
            <div class="flex-shrink-0 avatar-sm">
              <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                <i class="ri-remote-control-line"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="d-flex">
            <div class="flex-grow-1">
              <h4>354</h4>
              <h6 class="text-muted fs-13 mb-0">ICOs Trading</h6>
            </div>
            <div class="flex-shrink-0 avatar-sm">
              <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                <i class="ri-flashlight-fill"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="d-flex">
            <div class="flex-grow-1">
              <h4>2762</h4>
              <h6 class="text-muted fs-13 mb-0">Funded ICOs</h6>
            </div>
            <div class="flex-shrink-0 avatar-sm">
              <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                <i class="ri-hand-coin-line"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="d-flex">
            <div class="flex-grow-1">
              <h4>1585</h4>
              <h6 class="text-muted fs-13 mb-0">Upcoming ICO</h6>
            </div>
            <div class="flex-shrink-0 avatar-sm">
              <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                <i class="ri-donut-chart-line"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BCard no-body>
      <BCardBody>
        <BRow class="g-3">
          <BCol xxl="4" lg="6">
            <div class="search-box">
              <input type="text" class="form-control" placeholder="Search to ICOs..." />
              <i class="ri-search-line search-icon"></i>
            </div>
          </BCol>
          <BCol xxl="3" lg="6">
            <flat-pickr v-model="date" placeholder="Select date" :config="rangeDateconfig" class="form-control">
            </flat-pickr>
          </BCol>
          <BCol xxl="2" lg="4">
            <Multiselect class="form-control" v-model="value" :close-on-select="true" :searchable="true"
              :create-option="true" :options="[
                { value: 'Active', label: 'Active' },
                { value: 'Ended', label: 'Ended' },
                { value: 'Upcoming', label: 'Upcoming' },
              ]" />
          </BCol>
          <BCol xxl="2" lg="4">
            <Multiselect class="form-control" v-model="value1" :close-on-select="true" :searchable="true"
              :create-option="true" :options="[
                { value: '', label: 'Select Rating' },
                { value: '1', label: '1 star' },
                { value: '2', label: '2 star' },
                { value: '3', label: '3 star' },
                { value: '4', label: '4 star' },
                { value: '5', label: '5 star' },
              ]" />
          </BCol>
          <BCol xxl="1" lg="4">
            <BButton variant="primary" class="w-100">
              <i class="ri-equalizer-line align-bottom me-1"></i> Filters
            </BButton>
          </BCol>
        </BRow>
      </BCardBody>
    </BCard>

    <BRow>
      <BCol xxl="3" md="6">
        <BCard no-body class="overflow-hidden border-0">
          <BCardBody class="bg-success-subtle">
            <h5 class="fs-17 text-center mb-0">Active ICOs</h5>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/btc.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Data Wallet</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>  
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $15,00,000 / $13,75,954
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">89.97%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  4.8 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-danger mb-0">
                <i class="ri-time-line align-bottom"></i> 05 Days
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/companies/img-6.png" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">GreatRiver Technology</h5>
                <p class="text-muted mb-2">Information Technology</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-1">
              $39,00,000 / $31,57,654
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">84.57%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  4.4 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-danger mb-0">
                <i class="ri-time-line align-bottom"></i> 15 Days
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/vtc.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Manta Network Finance</h5>
                <p class="text-muted mb-2">Finance Services</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $42,50,000 / $30,84,214
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">70.24%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  2.7 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 25 Jan, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/xsg.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Goldfinch Network</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $28,00,000 / $8,74,986
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">24.57%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.2 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 04 Feb, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/companies/img-8.png" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Galaxy War</h5>
                <p class="text-muted mb-2">Gaming</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $40,00,000 / $24,12,741
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">62.04%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.9 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 05 March, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" md="6">
        <BCard no-body class="overflow-hidden border-0">
          <BCardBody class="bg-danger-subtle">
            <h5 class="fs-17 text-center mb-0">Ended ICOs</h5>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/bela.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Social Chain</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $14,00,000 / $13,20,471
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">97.62%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  2.8 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-muted mb-0">
                <i class="ri-time-line align-bottom"></i> 02 Jan, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/arn.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Angels Crypto</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $75,00,000 / $59,10,412
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">89.13%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  2.1 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-muted mb-0">
                <i class="ri-time-line align-bottom"></i> 23 Dec, 2021
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/cs.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Codex Exchange</h5>
                <p class="text-muted mb-2">Exchange</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $32,00,000 / $28,65,732
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">78.43%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.0 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-muted mb-0">
                <i class="ri-time-line align-bottom"></i> 04 Oct, 2021
              </h6>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" md="6">
        <BCard no-body class="overflow-hidden border-0">
          <BCardBody class="bg-primary-subtle">
            <h5 class="fs-17 text-center mb-0">Upcoming ICOs</h5>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2">
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/add.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">World Doin</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">$64,00,000</h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  4.7 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-primary mb-0">
                <i class="ri-time-line align-bottom"></i> 15 Jan, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/atm.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Bridge Plus</h5>
                <p class="text-muted mb-2">Platform</p>
              </div>
              <div>
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">$45,80,000</h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.5 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-muted mb-0">-</h6>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="3" md="6">
        <BCard no-body class="overflow-hidden border-0">
          <BCardBody class="bg-info-subtle">
            <h5 class="fs-17 text-center mb-0">Trading ICOs</h5>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2 ribbon-box ribbon-fill right">
          <div class="ribbon ribbon-primary shadow-none">
            <i class="ri-flashlight-fill me-1"></i> 1
          </div>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/bcbc.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">PowerCoin</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div class="me-4">
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $1,50,00,000 / $1,11,65,368
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">86.61%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  4.9 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 16 Feb, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2 ribbon-box ribbon-fill right">
          <div class="ribbon ribbon-primary shadow-none">
            <i class="ri-flashlight-fill me-1"></i> 2
          </div>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/bix.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Cyber Wonder</h5>
                <p class="text-muted mb-2">Platform</p>
              </div>
              <div class="me-4">
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $80,00,000 / $36,40,352
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">48.08%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  4.7 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 23 Jan, 2022
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="mb-2 ribbon-box ribbon-fill right">
          <div class="ribbon ribbon-primary shadow-none">
            <i class="ri-flashlight-fill me-1"></i> 3
          </div>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/rise.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">RootCoin</h5>
                <p class="text-muted mb-2">Blockchain Services</p>
              </div>
              <div class="me-4">
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $95,00,000 / $78,95,041
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">76.05%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.2 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 30 Dec, 2021
              </h6>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body class="ribbon-box ribbon-fill right">
          <div class="ribbon ribbon-primary shadow-none">
            <i class="ri-flashlight-fill me-1"></i> 4
          </div>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-light rounded">
                  <img src="@/assets/images/svg/crypto-icons/ark.svg" alt="" class="avatar-xxs" />
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="fs-15 mb-1">Arcana Finance</h5>
                <p class="text-muted mb-2">Finance Services</p>
              </div>
              <div class="me-4">
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary">Visit Website
                  <i class="ri-arrow-right-up-line align-bottom"></i>
                </BLink>
              </div>
            </div>
            <h6 class="text-muted mb-0">
              $68,00,000 / $45,85,367
              <BBadge variant="success-subtle" class="bg-success-subtle text-success">71.16%</BBadge>
            </h6>
          </BCardBody>
          <BCardBody class="border-top border-top-dashed">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="mb-0">
                  3.2 <i class="ri-star-fill align-bottom text-warning"></i>
                </h6>
              </div>
              <h6 class="flex-shrink-0 text-warning mb-0">
                <i class="ri-time-line align-bottom"></i> 02 Dec, 2021
              </h6>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
