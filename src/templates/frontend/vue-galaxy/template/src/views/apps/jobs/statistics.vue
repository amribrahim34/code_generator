<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { UsersIcon } from "@zhuowenli/vue-feather-icons";

import getChartColorsArray from "@/common/getChartColorsArray";

export default {
  setup() {
    return {
      jobsummarychartseries: [{
        name: 'Application Sent  ',
        data: [33, 28, 30, 35, 40, 55, 70, 110, 150, 180, 210, 250]
      }, {
        name: ' Interviews',
        data: [20, 26, 45, 32, 42, 53, 59, 70, 78, 97, 110, 125]
      },
      {
        name: ' Hired',
        data: [12, 17, 45, 42, 24, 35, 42, 75, 102, 108, 156, 199]
      },
      {
        name: ' Rejected',
        data: [8, 13, 22, 27, 32, 34, 46, 59, 65, 97, 100, 110]
      }],
      jobsummarychartchartOptions: {
        chart: {
          height: 320,
          type: "area",
          toolbar: "false",
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
          width: 2,
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
        },
        colors: getChartColorsArray('["--vz-success","--vz-primary", "--vz-info", "--vz-danger"]'),
        fill: {
          opacity: 0.06,
          colors: getChartColorsArray('["--vz-success","--vz-primary", "--vz-info", "--vz-danger"]'),
          type: "solid",
        },
      },

      yournetworkchartseries: [{
        name: 'Following',
        data: [80, 50, 30, 40, 100, 20],
      },
      {
        name: 'Followers',
        data: [20, 30, 40, 80, 20, 80],
      }],
      yournetworkchartchartOptions: {
        chart: {
          height: 341,
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1,
          },
          toolbar: {
            show: false,
          },
        },
        stroke: {
          width: 2,
        },
        fill: {
          opacity: 0.2,
        },
        legend: {
          show: true,
          fontWeight: 500,
          offsetX: 0,
          offsetY: -8,
          markers: {
            width: 8,
            height: 8,
            radius: 6,
          },
          itemMargin: {
            horizontal: 10,
            vertical: 0,
          },
        },
        markers: {
          size: 0,
        },
        colors: getChartColorsArray('["--vz-primary", "--vz-info"]'),
        xaxis: {
          categories: ["2016", "2017", "2018", "2019", "2020", "2021"],
        },
      },

      userbydeviceseries: [78.56, 105.02, 42.89],
      userbydevicechartOptions: {
        labels: ["Desktop", "Mobile", "Tablet"],
        chart: {
          type: "donut",
          height: 219,
        },
        plotOptions: {
          pie: {
            size: 100,
            donut: {
              size: "76%",
            },
          },
        },
        dataLabels: {
          enabled: false,
        },
        legend: {
          show: false,
          position: "bottom",
          horizontalAlign: "center",
          offsetX: 0,
          offsetY: 0,
          markers: {
            width: 20,
            height: 6,
            radius: 2,
          },
          itemMargin: {
            horizontal: 12,
            vertical: 0,
          },
        },
        stroke: {
          width: 0,
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return value + "k" + " Users";
            },
          },
          tickAmount: 4,
          min: 0,
        },
        colors: getChartColorsArray('["--vz-primary", "--vz-warning", "--vz-info"]'),
      },

      visitorgraphseries: [{
        data: [{
          x: 'USA',
          y: 321
        },
        {
          x: 'Russia',
          y: 165
        },
        {
          x: 'India',
          y: 184
        },
        {
          x: 'China',
          y: 98
        },
        {
          x: 'Canada',
          y: 84
        },
        {
          x: 'Brazil',
          y: 31
        },
        {
          x: 'UK',
          y: 70
        },
        {
          x: 'Australia',
          y: 30
        },
        {
          x: 'Germany',
          y: 44
        },
        {
          x: 'Italy',
          y: 68
        },
        {
          x: 'Israel',
          y: 28
        },
        {
          x: 'Indonesia',
          y: 19
        },
        {
          x: 'Bangladesh',
          y: 29
        }
        ]
      }],
      visitorgraphchartOptions: {
        legend: {
          show: false,
        },
        chart: {
          height: 350,
          type: "treemap",
          toolbar: {
            show: false,
          },
        },
        title: {
          text: "Visitors Location",
          align: "center",
          style: {
            fontWeight: 500,
          },
        },
        colors: getChartColorsArray('["--vz-primary-rgb, 0.75", "--vz-secondary", "--vz-warning", "--vz-info","--vz-success", "--vz-danger"]'),
        plotOptions: {
          treemap: {
            distributed: true,
            enableShades: false,
          },
        },
      },

      chartcolors: { colors: ["#f06548"] },
      chartoptions: {
        chart: {
          width: 140,
          type: "area",
          sparkline: {
            enabled: true,
          },
          toolbar: {
            show: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
          width: 1.5,
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [50, 100, 100, 100],
          },
        },
        colors: ["#0ab39c"]
      }

    };
  },
  components: {
    Layout,
    PageHeader,
    UsersIcon
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Statistics" pageTitle="Jobs" />
    <BRow>
      <BCol xl="3" md="6">

        <BCard no-body class="card-height-100">
          <div class="d-flex">
            <div class="flex-grow-1 p-3">
              <h5 class="mb-3">Application</h5>
              <p class="mb-0 text-muted">
                <BBadge class="bg-light text-success mb-0"> <i class="ri-arrow-up-line align-middle"></i> 16.24 %
                </BBadge> vs. previous month
              </p>
            </div>
            <div>
              <apexchart class="apex-charts" width="140px" height="90px" dir="ltr" :series="[{
                name: 'Results',
                data: [0, 110, 95, 75, 120]
              }]" :options="{ ...chartoptions }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>

      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <div class="d-flex">
            <div class="flex-grow-1 p-3">
              <h5 class="mb-3">Interviewed</h5>
              <p class="mb-0 text-muted">
                <BBadge class="bg-light text-success mb-0"> <i class="ri-arrow-up-line align-middle"></i> 34.24 %
                </BBadge> vs. previous month
              </p>
            </div>
            <div>
              <apexchart class="apex-charts" width="140px" height="90px" dir="ltr" :series="[{
                name: 'Results',
                data: [0, 68, 35, 90, 99]
              }]" :options="{ ...chartoptions }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>

      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <div class="d-flex">
            <div class="flex-grow-1 p-3">
              <h5 class="mb-3">Hired</h5>
              <p class="mb-0 text-muted">
                <BBadge class="bg-light text-success mb-0"> <i class="ri-arrow-up-line align-middle"></i> 6.67 % </BBadge>
                vs. previous month
              </p>
            </div>
            <div>
              <apexchart class="apex-charts" width="140px" height="90px" dir="ltr" :series="[{
                name: 'Results',
                data: [0, 36, 110, 95, 130]
              }]" :options="{ ...chartoptions }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>

      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <div class="d-flex">
            <div class="flex-grow-1 p-3">
              <h5 class="mb-3">Rejected</h5>
              <p class="mb-0 text-muted">
                <BBadge class="bg-light text-danger mb-0"> <i class="ri-arrow-down-line align-middle"></i> 3.24 %
                </BBadge> vs. previous month
              </p>
            </div>
            <div>
              <apexchart class="apex-charts" width="140px" height="90px" dir="ltr" :series="[{
                name: 'Results',
                data: [0, 98, 85, 90, 67]
              }]" :options="{ ...chartoptions, ...chartcolors }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>

    </BRow>


    <BRow>
      <BCol xl="8">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex">
              <h5 class="card-title mb-0 flex-grow-1  ">Visitor Graph</h5>
              <div class="flex-shrink-0">
                <BDropdown variant="link" class="card-header-dropdown"
                  toggle-class="my-n3 text-reset dropdown-btn arrow-none" menu-class="dropdown-menu-end"
                  aria-haspopup="true" :offset="{ alignmentAxis: 2, crossAxis: 0, mainAxis: 0 }">
                  <template #button-content><span class="fw-semibold text-uppercase fs-12">Sort by: </span><span
                      class="text-muted">Current
                      Week<i class="mdi mdi-chevron-down ms-1"></i></span>
                  </template>
                  <BDropdownItem>Today</BDropdownItem>
                  <BDropdownItem>Last Week</BDropdownItem>
                  <BDropdownItem>Last Month</BDropdownItem>
                  <BDropdownItem>Current Year</BDropdownItem>
                </BDropdown>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" dir="ltr" height="350" :series="visitorgraphseries"
              :options="visitorgraphchartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xl="4">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Users by Device</BCardTitle>
            <div class="flex-shrink-0">
              <BDropdown variant="link" class="card-header-dropdown"
                toggle-class="my-n3 text-reset dropdown-btn arrow-none" menu-class="dropdown-menu-end"
                aria-haspopup="true" :offset="{ alignmentAxis: 2, crossAxis: 0, mainAxis: 0 }">
                <template #button-content><span class="text-muted fs-16"><i
                      class="mdi mdi-dots-vertical align-middle"></i></span>
                </template>
                <BDropdownItem>Today</BDropdownItem>
                <BDropdownItem>Last Week</BDropdownItem>
                <BDropdownItem>Last Month</BDropdownItem>
                <BDropdownItem>Current Year</BDropdownItem>
              </BDropdown>
            </div>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" dir="ltr" height="219" :series="userbydeviceseries"
              :options="userbydevicechartOptions"></apexchart>

            <div class="table-responsive mt-3">
              <table class="table table-borderless table-sm table-centered align-middle table-nowrap mb-0">
                <tbody class="border-0">
                  <tr>
                    <td>
                      <h4 class="text-truncate fs-14 fs-medium mb-0"><i
                          class="ri-stop-fill align-middle fs-18 text-primary me-2"></i>Desktop Users</h4>
                    </td>
                    <td>
                      <p class="text-muted mb-0">
                        <UsersIcon width="24" height="24" class="me-2 icon-sm" />78.56k
                      </p>
                    </td>
                    <td class="text-end">
                      <p class="text-success fw-medium fs-12 mb-0"><i
                          class="ri-arrow-up-s-fill fs-5 align-middle"></i>2.08% </p>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <h4 class="text-truncate fs-14 fs-medium mb-0"><i
                          class="ri-stop-fill align-middle fs-18 text-warning me-2"></i>Mobile Users</h4>
                    </td>
                    <td>
                      <p class="text-muted mb-0">
                        <UsersIcon width="24" height="24" class="me-2 icon-sm" />105.02k
                      </p>
                    </td>
                    <td class="text-end">
                      <p class="text-danger fw-medium fs-12 mb-0"><i
                          class="ri-arrow-down-s-fill fs-5 align-middle"></i>10.52%
                      </p>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <h4 class="text-truncate fs-14 fs-medium mb-0"><i
                          class="ri-stop-fill align-middle fs-18 text-info me-2"></i>Tablet Users</h4>
                    </td>
                    <td>
                      <p class="text-muted mb-0">
                        <UsersIcon width="24" height="24" class="me-2 icon-sm" />42.89k
                      </p>
                    </td>
                    <td class="text-end">
                      <p class="text-danger fw-medium fs-12 mb-0"><i
                          class="ri-arrow-down-s-fill fs-5 align-middle"></i>7.36%
                      </p>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="4" md="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Your Network Summary</BCardTitle>
            <div class="flex-shrink-0">
              <BDropdown variant="link" class="card-header-dropdown"
                toggle-class="my-n3 text-reset dropdown-btn arrow-none" menu-class="dropdown-menu-end"
                aria-haspopup="true" :offset="{ alignmentAxis: -45, crossAxis: 0, mainAxis: 0 }">
                <template #button-content><span class="fw-semibold text-uppercase fs-12">Sort by: </span><span
                    class="text-muted">Monthly<i class="mdi mdi-chevron-down ms-1"></i></span>
                </template>
                <BDropdownItem>Today</BDropdownItem>
                <BDropdownItem>Weekly</BDropdownItem>
                <BDropdownItem>Monthly</BDropdownItem>
                <BDropdownItem>Yearly</BDropdownItem>
              </BDropdown>
            </div>

          </BCardHeader>
          <BCardBody class="pb-0">
            <apexchart class="apex-charts" dir="ltr" height="341" :series="yournetworkchartseries"
              :options="yournetworkchartchartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xxl="8" md="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Jobs Summary</BCardTitle>
            <div class="flex-shrink-0">
              <BDropdown variant="link" class="card-header-dropdown"
                toggle-class="my-n3 text-reset dropdown-btn arrow-none" menu-class="dropdown-menu-end"
                aria-haspopup="true" :offset="{ alignmentAxis: -45, crossAxis: 0, mainAxis: 0 }">
                <template #button-content>
                  <span class="fw-semibold text-uppercase fs-12">Sort by: </span><span class="text-muted">Current Year<i
                      class="mdi mdi-chevron-down ms-1"></i></span>
                </template>
                <BDropdownItem>Today</BDropdownItem>
                <BDropdownItem>Last Week</BDropdownItem>
                <BDropdownItem>Last Month</BDropdownItem>
                <BDropdownItem>Current Year</BDropdownItem>
              </BDropdown>
            </div>
          </BCardHeader>
          <BCardBody class="px-0">
            <apexchart class="apex-charts" height="320" dir="ltr" :series="jobsummarychartseries"
              :options="jobsummarychartchartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>