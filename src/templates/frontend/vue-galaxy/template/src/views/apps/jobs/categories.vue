<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/xulniijg.json";
import animationData1 from "@/components/widgets/oclwxpmm.json";
import animationData2 from "@/components/widgets/dklbhvrt.json";
import animationData3 from "@/components/widgets/adwosptt.json";
import animationData4 from "@/components/widgets/kkcllwsu.json";
import animationData5 from "@/components/widgets/rahcoaeu.json";
import animationData6 from "@/components/widgets/smauprql.json";
import animationData7 from "@/components/widgets/itykargr.json";
import animationData8 from "@/components/widgets/cnyeuzxc.json";
import animationData9 from "@/components/widgets/sygggnra.json";
import animationData10 from "@/components/widgets/hfmdczge.json";
import animationData11 from "@/components/widgets/xhebrhsj.json";
import animationData12 from "@/components/widgets/ucvsemjq.json";
import animationData13 from "@/components/widgets/pvbjsfif.json";
import animationData14 from "@/components/widgets/auvicynv.json";

export default {
  data() {
    return {
      defaultOptions: {
        animationData: animationData
      },
      defaultOptions1: {
        animationData: animationData1
      },
      defaultOptions2: {
        animationData: animationData2
      },
      defaultOptions3: {
        animationData: animationData3
      },
      defaultOptions4: {
        animationData: animationData4
      },
      defaultOptions5: {
        animationData: animationData5
      },
      defaultOptions6: {
        animationData: animationData6
      },
      defaultOptions7: {
        animationData: animationData7
      },
      defaultOptions8: {
        animationData: animationData8
      },
      defaultOptions9: {
        animationData: animationData9
      },
      defaultOptions10: {
        animationData: animationData10
      },
      defaultOptions11: {
        animationData: animationData11
      },
      defaultOptions12: {
        animationData: animationData12
      },
      defaultOptions13: {
        animationData: animationData13
      },
      defaultOptions14: {
        animationData: animationData14
      },

    };
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Job Categories" pageTitle="Jobs" />
    <BRow>
      <BCol col lg="12">
        <BCard no-body>
          <BCardHeader>
            <BRow class="justify-content-between gy-3">
              <BCol lg="3">
                <div class="search-box">
                  <input type="text" class="form-control search" placeholder="Search for job categories...">
                  <i class="ri-search-line search-icon"></i>
                </div>
              </BCol>
              <BCol lg="auto">
                <div class="d-md-flex text-nowrap gap-2">
                  <BButton variant="info" class="add-btn"><i class="ri-add-fill me-1 align-bottom"></i> Add Categories
                  </BButton>
                  <BButton variant="danger"><i class="ri-filter-2-line me-1 align-bottom"></i> Filters</BButton>

                  <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0"
                    class="card-header-dropdown" no-caret>
                    <template #button-content> <span class="fs-18 btn btn-soft-info"><i class="ri-more-2-fill"></i></span>
                    </template>
                    <BDropdownItem href="#">All</BDropdownItem>
                    <BDropdownItem href="#">Last Week</BDropdownItem>
                    <BDropdownItem href="#">Last Month</BDropdownItem>
                    <BDropdownItem href="#">Last Year </BDropdownItem>
                  </BDropdown>

                </div>
              </BCol>
            </BRow>
          </BCardHeader>
        </BCard>
      </BCol>
    </BRow>

    <BRow class="row-cols-xxl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions" :height="50"
              :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Business Development</h5>
            </BLink>
            <p class="text-muted mb-0">102 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions1" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Automotive Jobs</h5>
            </BLink>
            <p class="text-muted mb-0">64 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions2" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Construction / Facilities</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions3" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Design, Art & Multimedia</h5>
            </BLink>
            <p class="text-muted mb-0">49 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions4" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Healthcare</h5>
            </BLink>
            <p class="text-muted mb-0">97 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions5" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Sales & Marketing</h5>
            </BLink>
            <p class="text-muted mb-0">312 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions6" :trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Accounting / Finance</h5>
            </BLink>
            <p class="text-muted mb-0">62 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions7" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Project Management</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions8" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Customer Services</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions9" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Content Writer</h5>
            </BLink>
            <p class="text-muted mb-0">746 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions10" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Government Jobs</h5>
            </BLink>
            <p class="text-muted mb-0">642 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions11" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Digital Marketing</h5>
            </BLink>
            <p class="text-muted mb-0">364 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions12" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Education & training</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions13" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">IT & Software</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol>
        <BCard no-body>
          <BCardBody class="text-center py-4">
            <lottie class="avatar-xl icon-primary" colors="primary:#405189" :options="defaultOptions14" trigger="hover"
              :height="50" :width="50" />
            <BLink href="#!" class="stretched-link">
              <h5 class="mt-4">Catering & Tourism</h5>
            </BLink>
            <p class="text-muted mb-0">35 Position</p>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="12">
        <div class="text-center mb-3">
          <BButton variant="link" class="text-secondary mt-2" id="loadmore"><i
              class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i> Load More </BButton>
        </div>
      </BCol>
    </BRow>
</Layout></template>