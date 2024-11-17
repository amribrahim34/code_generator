<script>
import { CountTo } from "vue3-count-to";

var echarts = require("echarts");
import {
  UsersIcon,
  ActivityIcon,
  ClockIcon,
  ExternalLinkIcon,
  AlertTriangleIcon,
} from "@zhuowenli/vue-feather-icons";

import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/autoplay";

import usaJson from "../../components/widgets/USA.json";
import worldJson from "../../components/widgets/world.json";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import SessionsCounties from "../dashboard/analytics/sessions-countries.vue";
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/lupuorrc.json";

import getChartColorsArray from "@/common/getChartColorsArray";
import simplebar from "simplebar-vue"
function generateData(count, yrange) {
  var i = 0;
  var series = [];
  while (i < count) {
    var x = "w" + (i + 1).toString();
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

    series.push({
      x: x,
      y: y,
    });
    i++;
  }
  return series;
}

export default {
  data() {
    return {
      searchQuery: null,

      candidateList: [{ id: "1", name: "Anna Adame", img: require("@/assets/images/users/avatar-1.jpg"), username: "@Anna", designation: "Web Developer" },
      { id: "2", name: "Patricia Cavin", img: require("@/assets/images/users/avatar-2.jpg"), username: "@Patricia", designation: "Web Developer" },
      { id: "3", name: "Jason Tran", img: require("@/assets/images/users/avatar-3.jpg"), username: "@Jason", designation: "Magento Developer" },
      { id: "4", name: "Cheryl Moore", img: require("@/assets/images/users/avatar-4.jpg"), username: "@Cheryl", designation: "Product Designer" },
      { id: "5", name: "Jennifer Bailey", img: require("@/assets/images/users/avatar-5.jpg"), username: "@Jennifer", designation: "Marketing Director" },
      ],
      audienceChartOptions: {
        series: [{
          name: "Last Year",
          data: [
            25.3, 12.5, 20.2, 18.5, 40.4, 25.4, 15.8, 22.3, 19.2, 25.3, 12.5,
            20.2,
          ],
        },
        {
          name: "Current Year",
          data: [
            36.2, 22.4, 38.2, 30.5, 26.4, 30.4, 20.2, 29.6, 10.9, 36.2, 22.4,
            38.2,
          ],
        },
        ],
        chartOptions: {
          chart: {
            type: "bar",
            height: 306,
            stacked: true,
            toolbar: {
              show: false,
            },
          },
          plotOptions: {
            bar: {
              horizontal: false,
              columnWidth: "30%",
              borderRadius: 6,
            },
          },
          dataLabels: {
            enabled: false,
          },
          legend: {
            show: true,
            position: "bottom",
            horizontalAlign: "center",
            fontWeight: 400,
            fontSize: "8px",
            offsetX: 0,
            offsetY: 0,
            markers: {
              width: 9,
              height: 9,
              radius: 4,
            },
          },
          stroke: {
            show: true,
            width: 2,
            colors: ["transparent"],
          },
          grid: {
            show: false,
          },
          colors: getChartColorsArray('["--vz-primary", "--vz-light"]'),
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
              show: true,
              strokeDashArray: 1,
              height: 1,
              width: "100%",
              offsetX: 0,
              offsetY: 0,
            },
          },
          yaxis: {
            show: false,
          },
          fill: {
            opacity: 1,
          },
        },
      },
      portfolioChart: {
        series: [19405, 40552, 15824, 30635],
        chartOptions: {
          labels: ["Bitcoin", "Ethereum", "Litecoin", "Dash"],
          chart: {
            type: "donut",
            height: 210,
          },
          plotOptions: {
            pie: {
              size: 100,
              offsetX: 0,
              offsetY: 0,
              donut: {
                size: "70%",
                labels: {
                  show: true,
                  name: {
                    show: true,
                    fontSize: "18px",
                    offsetY: -5,
                  },
                  value: {
                    show: true,
                    fontSize: "20px",
                    color: "#343a40",
                    fontWeight: 500,
                    offsetY: 5,
                    formatter: function (val) {
                      return "$" + val;
                    },
                  },
                  total: {
                    show: true,
                    fontSize: "13px",
                    label: "Total value",
                    color: "#9599ad",
                    fontWeight: 500,
                    formatter: function (w) {
                      return (
                        "$" +
                        w.globals.seriesTotals.reduce(function (a, b) {
                          return a + b;
                        }, 0)
                      );
                    },
                  },
                },
              },
            },
          },
          dataLabels: {
            enabled: false,
          },
          legend: {
            show: false,
          },
          yaxis: {
            labels: {
              formatter: function (value) {
                return "$" + value;
              },
            },
          },
          stroke: {
            lineCap: "round",
            width: 2,
          },
          colors: getChartColorsArray('["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.65", "--vz-primary-rgb, 0.50"]'),
        },
      },
      topReferralsChart: {
        series: [{
          name: "Jan",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Feb",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Mar",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Apr",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "May",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Jun",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Jul",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Aug",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        {
          name: "Sep",
          data: generateData(20, {
            min: -30,
            max: 55,
          }),
        },
        ],
        chartOptions: {
          chart: {
            height: 310,
            type: "heatmap",
            toolbar: {
              show: false,
            },
          },
          legend: {
            show: false,
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            width: 1,
          },
          title: {
            style: {
              fontWeight: 500,
            },
          },
          colors: getChartColorsArray(
            '["--vz-success", "--vz-info", "--vz-primary", "--vz-warning", "--vz-secondary"]'),
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
      },
      defaultOptions: { animationData: animationData },
      Autoplay
    };
  },
  computed: {
    displayedPosts() {
      return this.candidateList;
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.name.toLowerCase().includes(search) ||
            data.username.toLowerCase().includes(search) ||
            data.designation.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  methods: {

    selectBank() {
      if (document.querySelector('input[name=listGroupRadioGrid]:checked')) {
        document.getElementById("notification-overlay").style.visibility = "visible";
        document.getElementById("notification-overlay").style.opacity = "1";

        var checkedElem = document.querySelector('input[name=listGroupRadioGrid]:checked').parentElement;
        var payamount = checkedElem.querySelector(".pay-amount").innerHTML;
        document.querySelector("#notification-overlay .success-pay").innerHTML = payamount;
      } else {
        document.getElementById("notification-warn").classList.remove("d-none");
        setTimeout(() => document.getElementById("notification-warn").classList.add("d-none"), 2000);
      }
    },

    selectBankback() {
      document.getElementById("notification-overlay").style.visibility = "hidden";
      document.getElementById("notification-overlay").style.opacity = "0";
    },

    updateQuantity(productQty, itemAmount, priceselection) {
      // Calculate the total price based on the quantity and item amount
      const totalPrice = parseInt(productQty) * parseFloat(itemAmount);

      // Update the displayed total price
      if (priceselection) {
        priceselection.textContent = totalPrice.toFixed(2);
      }

      // You can also update any other properties or perform additional logic here
    },

    plusamount() {
      event.target.previousElementSibling.value++;
      var itemAmount = event.target.parentElement?.parentElement?.previousElementSibling?.querySelector(".product-price")?.value;

      var priceselection = event.target?.parentElement?.parentElement?.nextElementSibling?.querySelector(".product-line-price");
      var productQty = event.target.parentElement.querySelector(".product-quantity").value;

      this.updateQuantity(productQty, itemAmount, priceselection);
    },

    minusamount() {
      event.target.nextElementSibling.value--;
      var itemAmount = event.target.parentElement?.parentElement?.nextElementSibling?.querySelector(".product-price")?.value;
      var priceselection = event.target?.parentElement?.parentElement?.nextElementSibling?.querySelector(".product-line-price");
      var productQty = event.target.parentElement.querySelector(".product-quantity").value;

      this.updateQuantity(productQty, itemAmount, priceselection);
    },

    showdetail(data) {
      document.getElementById('candidate-img').setAttribute('src', data.img);
      document.querySelector('#candidate-name').innerHTML = data.name;
      document.querySelector('#candidate-position').innerHTML = data.username;
    },

    customcreditcard() {
      var cardNumInput = document.getElementById("card-num-input");
      var cardNumElem = document.getElementById("card-num-elem");

      var cardHolderInput = document.getElementById("card-holder-input"),
        cardHolderElem = document.getElementById("card-holder-elem");

      var expiryMonthInput = document.getElementById("expiry-month-input"),
        expiryMonthElem = document.getElementById("expiry-month-elem");

      var expiryYearInput = document.getElementById("expiry-year-input"),
        expiryYearElem = document.getElementById("expiry-year-elem");

      var cvcInput = document.getElementById("cvc-input"),
        cvcElem = document.getElementById("cvc-elem");

      var cardForm = document.getElementById("custom-card-form");

      cardNumInput.onkeydown = function (e) {
        var key = e.keyCode || e.charCode;

        var is_digit = key >= 48 && key <= 57 || key >= 96 && key <= 105;
        var is_delete = key == 8 || key == 46;

        if (is_digit || is_delete) {
          var text = e.target.value;
          var len = text.length;

          if (is_digit && (len == 4 || len == 9 || len == 14)) cardNumInput.value = text + " ";
        } else return false;
      };


      cardNumInput.onkeyup = function (e) {
        var key = e.keyCode || e.charCode;

        var is_digit = key >= 48 && key <= 57 || key >= 96 && key <= 105;
        var is_delete = key == 8 || key == 46;

        if (is_digit || is_delete) {
          var text = e.target.value;
          var len = text.length;
          var digits = "XXXX XXXX XXXX XXXX".split('');

          if (is_digit && (len == 4 || len == 9 || len == 14)) digits[len] = " ";

          for (var i = 0; i < len; i++) {
            digits[i] = text.charAt(i);
          } cardNumElem.innerText = digits.join('');

        } else return false;
      };

      cardHolderInput.onkeyup = function (e) {
        cardHolderElem.innerText = e.target.value;
      };

      expiryMonthInput.onchange = function (e) {
        if (!e.target.value) expiryMonthElem.innerText = "00";

        expiryMonthElem.innerText = e.target.value;
      };

      expiryYearInput.onchange = function (e) {
        if (!e.target.value) expiryYearElem.innerText = "0000";
        expiryYearElem.innerText = e.target.value;
      };

      cvcInput.onkeyup = function (e) {
        var text = e.target.value;
        var digits = ['_', '_', '_'];

        for (var i = 0; i < text.length; i++) {
          digits[i] = text.charAt(i);
        } cvcElem.innerText = digits.join('');
      };

      cardForm.onsubmit = function (e) {
        e.preventDefault();
      };
    },
  },
  components: {
    Layout,
    PageHeader,
    UsersIcon,
    ActivityIcon,
    ClockIcon,
    ExternalLinkIcon,
    AlertTriangleIcon,
    CountTo,
    SessionsCounties,
    Swiper,
    SwiperSlide,
    lottie: Lottie,
    simplebar
  },
  mounted() {
    let chartuser = document.getElementById("users-by-country");
    let chartDom = document.getElementById("sales-by-locations");

    let userChart = echarts.init(chartuser);
    let myChart = echarts.init(chartDom);
    let option;
    let useroption;

    echarts.registerMap("USA", usaJson, {
      Alaska: {
        left: -131,
        top: 25,
        width: 15,
      },
      Hawaii: {
        left: -110,
        top: 28,
        width: 5,
      },
      "Puerto Rico": {
        left: -76,
        top: 26,
        width: 2,
      },
    });
    option = {
      tooltip: {
        trigger: "item",
        showDelay: 0,
        transitionDuration: 0.2,
      },
      series: [{
        name: "USA PopEstimates",
        type: "map",
        roam: true,
        map: "USA",
        emphasis: {
          label: {
            show: true,
          },
        },
        data: [{
          name: "Alabama",
          value: 4822023
        },
        {
          name: "Alaska",
          value: 731449
        },
        {
          name: "Arizona",
          value: 6553255
        },
        {
          name: "Arkansas",
          value: 2949131
        },
        {
          name: "California",
          value: 38041430
        },
        {
          name: "Colorado",
          value: 5187582
        },
        {
          name: "Connecticut",
          value: 3590347
        },
        {
          name: "Delaware",
          value: 917092
        },
        {
          name: "District of Columbia",
          value: 632323
        },
        {
          name: "Florida",
          value: 19317568
        },
        {
          name: "Georgia",
          value: 9919945
        },
        {
          name: "Hawaii",
          value: 1392313
        },
        {
          name: "Idaho",
          value: 1595728
        },
        {
          name: "Illinois",
          value: 12875255
        },
        {
          name: "Indiana",
          value: 6537334
        },
        {
          name: "Iowa",
          value: 3074186
        },
        {
          name: "Kansas",
          value: 2885905
        },
        {
          name: "Kentucky",
          value: 4380415
        },
        {
          name: "Louisiana",
          value: 4601893
        },
        {
          name: "Maine",
          value: 1329192
        },
        {
          name: "Maryland",
          value: 5884563
        },
        {
          name: "Massachusetts",
          value: 6646144
        },
        {
          name: "Michigan",
          value: 9883360
        },
        {
          name: "Minnesota",
          value: 5379139
        },
        {
          name: "Mississippi",
          value: 2984926
        },
        {
          name: "Missouri",
          value: 6021988
        },
        {
          name: "Montana",
          value: 1005141
        },
        {
          name: "Nebraska",
          value: 1855525
        },
        {
          name: "Nevada",
          value: 2758931
        },
        {
          name: "New Hampshire",
          value: 1320718
        },
        {
          name: "New Jersey",
          value: 8864590
        },
        {
          name: "New Mexico",
          value: 2085538
        },
        {
          name: "New York",
          value: 19570261
        },
        {
          name: "North Carolina",
          value: 9752073
        },
        {
          name: "North Dakota",
          value: 699628
        },
        {
          name: "Ohio",
          value: 11544225
        },
        {
          name: "Oklahoma",
          value: 3814820
        },
        {
          name: "Oregon",
          value: 3899353
        },
        {
          name: "Pennsylvania",
          value: 12763536
        },
        {
          name: "Rhode Island",
          value: 1050292
        },
        {
          name: "South Carolina",
          value: 4723723
        },
        {
          name: "South Dakota",
          value: 833354
        },
        {
          name: "Tennessee",
          value: 6456243
        },
        {
          name: "Texas",
          value: 26059203
        },
        {
          name: "Utah",
          value: 2855287
        },
        {
          name: "Vermont",
          value: 626011
        },
        {
          name: "Virginia",
          value: 8185867
        },
        {
          name: "Washington",
          value: 6897012
        },
        {
          name: "West Virginia",
          value: 1855413
        },
        {
          name: "Wisconsin",
          value: 5726398
        },
        {
          name: "Wyoming",
          value: 576412
        },
        {
          name: "Puerto Rico",
          value: 3667084
        },
        ],
      },],
    };
    myChart.setOption(option);
    option && myChart.setOption(option);

    echarts.registerMap("world", worldJson, {
      Alaska: {
        left: -131,
        top: 25,
        width: 15,
      },
      Hawaii: {
        left: -110,
        top: 28,
        width: 5,
      },
      "Puerto Rico": {
        left: -76,
        top: 26,
        width: 2,
      },
    });
    useroption = {
      tooltip: {
        trigger: "item",
        showDelay: 0,
        transitionDuration: 0.2,
      },
      series: [{
        name: "World",
        type: "map",
        map: "world",
        label: {
          show: false,
        },
      },],
    };

    userChart.setOption(useroption);
    useroption && userChart.setOption(useroption);
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Widgets" pageTitle="Velzon" />
    <BRow>
      <BCol cols="12">
        <h5 class="text-decoration-underline mb-3 pb-1">Tile Boxs</h5>
      </BCol>
    </BRow>

    <BRow>
      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="flex-grow-1">
                <p class="text-uppercase fw-medium text-muted mb-0">
                  Total Earnings
                </p>
              </div>
              <div class="flex-shrink-0">
                <h5 class="text-success fs-14 mb-0">
                  <i class="ri-arrow-right-up-line fs-13 align-middle"></i>
                  +16.24 %
                </h5>
              </div>
            </div>
            <div class="d-flex align-items-end justify-content-between mt-4">
              <div>
                <h4 class="fs-22 fw-semibold ff-secondary mb-4">
                  $<count-to :startVal="0" :endVal="559" :duration="5000"></count-to>k
                </h4>
                <BLink href="" class="text-decoration-underline">View net earnings</BLink>
              </div>
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-success-subtle rounded fs-3">
                  <i class="bx bx-dollar-circle text-success"></i>
                </span>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate bg-info">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="flex-grow-1">
                <p class="text-uppercase fw-medium text-white-50 mb-0">
                  Orders
                </p>
              </div>
              <div class="flex-shrink-0">
                <h5 class="text-warning fs-14 mb-0">
                  <i class="ri-arrow-right-down-line fs-13 align-middle"></i>
                  -3.57 %
                </h5>
              </div>
            </div>
            <div class="d-flex align-items-end justify-content-between mt-4">
              <div>
                <h4 class="fs-22 fw-semibold ff-secondary mb-4 text-white">
                  <count-to class="counter-value" :startVal="0" :endVal="36894" :duration="5000"></count-to>
                </h4>
                <BLink href="" class="text-decoration-underline text-white-50">View all orders</BLink>
              </div>
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-white bg-opacity-25 rounded fs-3">
                  <i class="bx bx-shopping-bag text-white"></i>
                </span>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="flex-grow-1">
                <p class="text-uppercase fw-medium text-muted mb-0">
                  Customers
                </p>
              </div>
              <div class="flex-shrink-0">
                <h5 class="text-success fs-14 mb-0">
                  <i class="ri-arrow-right-up-line fs-13 align-middle"></i>
                  +29.08 %
                </h5>
              </div>
            </div>
            <div class="d-flex align-items-end justify-content-between mt-4">
              <div>
                <h4 class="fs-22 fw-semibold ff-secondary mb-4">
                  <count-to :startVal="0" :endVal="183" :duration="5000"></count-to>M
                </h4>
                <BLink href="" class="text-decoration-underline">See details</BLink>
              </div>
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-warning-subtle rounded fs-3">
                  <i class="bx bx-user-circle text-warning"></i>
                </span>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="flex-grow-1">
                <p class="text-uppercase fw-medium text-muted mb-0">
                  My Balance
                </p>
              </div>
              <div class="flex-shrink-0">
                <h5 class="text-muted fs-14 mb-0">+0.00 %</h5>
              </div>
            </div>
            <div class="d-flex align-items-end justify-content-between mt-4">
              <div>
                <h4 class="fs-22 fw-semibold ff-secondary mb-4">
                  $<count-to :startVal="0" :endVal="165" :duration="5000"></count-to>k
                </h4>
                <BLink href="" class="text-decoration-underline">Withdraw money</BLink>
              </div>
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-primary-subtle rounded fs-3">
                  <i class="bx bx-wallet text-primary"></i>
                </span>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>

    </BRow>

    <BRow>
      <BCol xl="12">
        <BCard no-body class="crm-widget">
          <BCardBody class="p-0">
            <BRow class="row-cols-md-3 row-cols-1">
              <BCol lg class="border-end">
                <div class="py-4 px-3">
                  <h5 class="text-muted text-uppercase fs-13">
                    Campaign Sent
                    <i class="
                        ri-arrow-up-circle-line
                        text-success
                        fs-18
                        float-end
                        align-middle
                      "></i>
                  </h5>
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <i class="ri-space-ship-line display-6 text-muted"></i>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h2 class="mb-0">
                        <count-to :startVal="0" :endVal="197" :duration="5000"></count-to>
                      </h2>
                    </div>
                  </div>
                </div>
              </BCol>

              <BCol lg class="border-end">
                <div class="mt-3 mt-md-0 py-4 px-3">
                  <h5 class="text-muted text-uppercase fs-13">
                    Annual Profit
                    <i class="
                        ri-arrow-up-circle-line
                        text-success
                        fs-18
                        float-end
                        align-middle
                      "></i>
                  </h5>
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <i class="ri-exchange-dollar-line display-6 text-muted"></i>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h2 class="mb-0">
                        $<count-to :startVal="0" :endVal="489" :duration="5000"></count-to>k
                      </h2>
                    </div>
                  </div>
                </div>
              </BCol>

              <BCol lg class="border-end">
                <div class="mt-3 mt-md-0 py-4 px-3">
                  <h5 class="text-muted text-uppercase fs-13">
                    Lead Conversation
                    <i class="
                        ri-arrow-down-circle-line
                        text-danger
                        fs-18
                        float-end
                        align-middle
                      "></i>
                  </h5>
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <i class="ri-pulse-line display-6 text-muted"></i>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h2 class="mb-0">
                        <count-to :startVal="0" :endVal="32" :duration="5000"></count-to>%
                      </h2>
                    </div>
                  </div>
                </div>
              </BCol>

              <BCol lg class="border-end">
                <div class="mt-3 mt-lg-0 py-4 px-3">
                  <h5 class="text-muted text-uppercase fs-13">
                    Daily Average Income
                    <i class="
                        ri-arrow-up-circle-line
                        text-success
                        fs-18
                        float-end
                        align-middle
                      "></i>
                  </h5>
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <i class="ri-trophy-line display-6 text-muted"></i>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h2 class="mb-0">
                        $<count-to :startVal="0" :endVal="1596" :duration="5000"></count-to>0
                      </h2>
                    </div>
                  </div>
                </div>
              </BCol>

              <BCol lg>
                <div class="mt-3 mt-lg-0 py-4 px-3">
                  <h5 class="text-muted text-uppercase fs-13">
                    Annual Deals
                    <i class="
                        ri-arrow-down-circle-line
                        text-danger
                        fs-18
                        float-end
                        align-middle
                      "></i>
                  </h5>
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <i class="ri-service-line display-6 text-muted"></i>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h2 class="mb-0">
                        <count-to :startVal="0" :endVal="2659" :duration="5000"></count-to>
                      </h2>
                    </div>
                  </div>
                </div>
              </BCol>

            </BRow>

          </BCardBody>

        </BCard>

      </BCol>

    </BRow>

    <BRow>
      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-muted mb-0">Users</p>
                <h2 class="mt-4 ff-secondary fw-semibold">
                  <count-to :startVal="0" :endVal="28" :duration="5000"></count-to>k
                </h2>
                <p class="mb-0 text-muted">
                  <BBadge class="bg-light text-success mb-0">
                    <i class="ri-arrow-up-line align-middle"></i> 16.24 %
                  </BBadge>
                  vs. previous month
                </p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-info-subtle rounded-circle fs-2">
                    <UsersIcon class="text-info"></UsersIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-muted mb-0">Sessions</p>
                <h2 class="mt-4 ff-secondary fw-semibold">
                  <count-to :startVal="0" :endVal="97" :duration="5000"></count-to>k
                </h2>
                <p class="mb-0 text-muted">
                  <BBadge class="bg-light text-danger mb-0">
                    <i class="ri-arrow-down-line align-middle"></i> 3.96 %
                  </BBadge>
                  vs. previous month
                </p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-info-subtle rounded-circle fs-2">
                    <ActivityIcon class="text-info"></ActivityIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate bg-primary">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-white-50 mb-0">Avg. Visit Duration</p>
                <h2 class="mt-4 ff-secondary fw-semibold text-white">
                  <count-to :startVal="0" :endVal="3" :duration="5000"></count-to>m
                  <count-to :startVal="0" :endVal="40" :duration="5000"></count-to>sec
                </h2>
                <p class="mb-0 text-white-50">
                  <BBadge variant="white" class="bg-white bg-opacity-25 text-white mb-0">
                    <i class="ri-arrow-down-line align-middle"></i> 0.24 %
                  </BBadge>
                  vs. previous month
                </p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-white bg-opacity-25 rounded-circle fs-2">
                    <ClockIcon class="text-white"></ClockIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-muted mb-0">Bounce Rate</p>
                <h2 class="mt-4 ff-secondary fw-semibold">
                  <count-to :startVal="0" :endVal="33" :duration="5000"></count-to>%
                </h2>
                <p class="mb-0 text-muted">
                  <BBadge class="bg-light text-success mb-0">
                    <i class="ri-arrow-up-line align-middle"></i> 7.05 %
                  </BBadge>
                  vs. previous month
                </p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-info-subtle rounded-circle fs-2">
                    <ExternalLinkIcon class="text-info"></ExternalLinkIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>

    </BRow>

    <BRow>
      <BCol xl="3" md="6">
        <BCard no-body class="bg-success card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-white bg-opacity-25 text-white rounded-2 fs-2">
                  <i class="bx bx-shopping-bag"></i>
                </span>
              </div>
              <div class="flex-grow-1 ms-3">
                <p class="text-uppercase fw-medium text-white-50 mb-3">
                  Total Sales
                </p>
                <h4 class="fs-4 mb-3 text-white">
                  <count-to :startVal="0" :endVal="2045" :duration="5000"></count-to>
                </h4>
                <p class="text-white-50 mb-0">From 1930 last year</p>
              </div>
              <div class="flex-shrink-0 align-self-center">
                <BBadge variant="white" class="bg-white bg-opacity-25 text-white fs-12"><i
                    class="ri-arrow-up-s-line fs-13 align-middle me-1"></i>6.11 %<span> </span>
                </BBadge>
              </div>
            </div>
          </BCardBody>

        </BCard>
      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="avatar-sm flex-shrink-0">
                <span class="
                    avatar-title
                    bg-warning-subtle
                    text-warning
                    rounded-2
                    fs-2
                  ">
                  <i class="bx bxs-user-account"></i>
                </span>
              </div>
              <div class="flex-grow-1 ms-3">
                <p class="text-uppercase fw-medium text-muted mb-3">
                  Number of Users
                </p>
                <h4 class="fs-4 mb-3">
                  <count-to :startVal="0" :endVal="7522" :duration="5000"></count-to>
                </h4>
                <p class="text-muted mb-0">From 9530 last year</p>
              </div>
              <div class="flex-shrink-0 align-self-center">
                <BBadge variant="danger-subtle" class="bg-danger-subtle text-danger fs-12"><i
                    class="ri-arrow-down-s-line fs-13 align-middle me-1"></i>10.35 %<span> </span>
                </BBadge>
              </div>
            </div>
          </BCardBody>

        </BCard>
      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-danger-subtle text-danger rounded-2 fs-2">
                  <i class="bx bxs-badge-dollar"></i>
                </span>
              </div>
              <div class="flex-grow-1 ms-3">
                <p class="text-uppercase fw-medium text-muted mb-3">
                  Total Revenue
                </p>
                <h4 class="fs-4 mb-3">
                  $<count-to :startVal="0" :endVal="2845" :duration="5000"></count-to>
                </h4>
                <p class="text-muted mb-0">From $1,750.04 last year</p>
              </div>
              <div class="flex-shrink-0 align-self-center">
                <BBadge variant="success-subtle" class="bg-success-subtle text-success fs-12"><i
                    class="ri-arrow-up-s-line fs-13 align-middle me-1"></i>22.96 %<span> </span>
                </BBadge>
              </div>
            </div>
          </BCardBody>

        </BCard>
      </BCol>


      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center">
              <div class="avatar-sm flex-shrink-0">
                <span class="avatar-title bg-info-subtle text-info rounded-2 fs-2">
                  <i class="bx bx-store-alt"></i>
                </span>
              </div>
              <div class="flex-grow-1 ms-3">
                <p class="text-uppercase fw-medium text-muted mb-3">
                  Number of Stores
                </p>
                <h4 class="fs-4 mb-3">
                  $<count-to :startVal="0" :endVal="405" :duration="5000"></count-to>k
                </h4>
                <p class="text-muted mb-0">From 308 last year</p>
              </div>
              <div class="flex-shrink-0 align-self-center">
                <BBadge variant="success-subtle" class="bg-success-subtle text-success fs-12"><i
                    class="ri-arrow-up-s-line fs-13 align-middle me-1"></i>16.31 %<span> </span>
                </BBadge>
              </div>
            </div>
          </BCardBody>

        </BCard>
      </BCol>

    </BRow>

    <BRow>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0" class="float-end" no-caret>
              <template #button-content> <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical"></i></span>
              </template>
              <BDropdownItem href="#">Favorite</BDropdownItem>
              <BDropdownItem href="#">Apply Now</BDropdownItem>
            </BDropdown>

            <div class="mb-4 pb-2">
              <img src="@/assets/images/companies/img-3.png" alt="" class="avatar-sm">
            </div>
            <BLink href="#!">
              <h6 class="fs-15 fw-semibold">Marketing Director <span class="text-muted fs-13">(2-4 Yrs Exp.)</span></h6>
            </BLink>
            <p class="text-muted mb-0"><i class="ri-building-line align-bottom"></i> Themesbrand <span class="ms-2"><i
                  class="ri-map-pin-2-line align-bottom"></i> California</span></p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0" class="float-end" no-caret>
              <template #button-content> <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical"></i></span>
              </template>
              <BDropdownItem href="#">Favorite</BDropdownItem>
              <BDropdownItem href="#">Apply Now</BDropdownItem>
            </BDropdown>
            <div class="mb-4 pb-2">
              <img src="@/assets/images/companies/img-4.png" alt="" class="avatar-sm">
            </div>
            <BLink href="#!">
              <h6 class="fs-15 fw-semibold">Sr. Web Designer <span class="text-muted fs-13">(2+ Yrs Exp.)</span></h6>
            </BLink>
            <p class="text-muted mb-0"><i class="ri-building-line align-bottom"></i> Themesbrand <span class="ms-2"><i
                  class="ri-map-pin-2-line align-bottom"></i> California</span></p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100 bg-primary-subtle shadow-none bg-opacity-10">
          <BCardBody>
            <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0" class="float-end" no-caret>
              <template #button-content> <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical"></i></span>
              </template>
              <BDropdownItem href="#">Favorite</BDropdownItem>
              <BDropdownItem href="#">Apply Now</BDropdownItem>
            </BDropdown>
            <div class="mb-4 pb-2">
              <img src="@/assets/images/companies/img-6.png" alt="" class="avatar-sm">
            </div>
            <BLink href="#!">
              <h6 class="fs-15 fw-semibold">Sr. Web Designer <span class="text-muted fs-13">(2+ Yrs Exp.)</span></h6>
            </BLink>
            <p class="text-muted mb-0"><i class="ri-building-line align-bottom"></i> Themesbrand <span class="ms-2"><i
                  class="ri-map-pin-2-line align-bottom"></i> California</span></p>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100 bg-info-subtle shadow-none bg-opacity-10">
          <BCardBody>
            <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0" class="float-end" no-caret>
              <template #button-content> <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical"></i></span>
              </template>
              <BDropdownItem href="#">Favorite</BDropdownItem>
              <BDropdownItem href="#">Apply Now</BDropdownItem>
            </BDropdown>
            <div class="mb-4 pb-2">
              <img src="@/assets/images/companies/img-8.png" alt="" class="avatar-sm">
            </div>
            <BLink href="#!">
              <h6 class="fs-15 fw-semibold">Sr. Web Designer <span class="text-muted fs-13">(2+ Yrs Exp.)</span></h6>
            </BLink>
            <p class="text-muted mb-0"><i class="ri-building-line align-bottom"></i> Themesbrand <span class="ms-2"><i
                  class="ri-map-pin-2-line align-bottom"></i> California</span></p>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol cols="12">
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Other Widgets</h5>
      </BCol>
    </BRow>

    <BRow>
      <BCol xl="4">
        <BCard no-body>
          <BCardBody class="p-0">
            <BAlert variant="warning" class="border-0 rounded-top rounded-0 m-0 d-flex align-items-center" show>
              <alert-triangle-icon class="text-warning me-2 icon-sm"></alert-triangle-icon>
              <div class="flex-grow-1 text-truncate">
                Your free trial expired in <b>17</b> days.
              </div>
              <div class="flex-shrink-0">
                <router-link to="/pages/profile" class="text-reset text-decoration-underline"><b>Upgrade</b>
                </router-link>
              </div>
            </BAlert>

            <BRow class="align-items-end">
              <BCol sm="8">
                <div class="p-3">
                  <p class="fs-16 lh-base">
                    Upgrade your plan from a
                    <span class="fw-semibold">Free trial</span>, to ‘Premium
                    Plan’ <i class="mdi mdi-arrow-right"></i>
                  </p>
                  <div class="mt-3">
                    <router-link to="/pages/profile" class="btn btn-success">Upgrade Account!</router-link>
                  </div>
                </div>
              </BCol>
              <BCol sm="4">
                <div class="px-3">
                  <img src="@/assets/images/user-illustarator-2.png" class="img-fluid" alt="" />
                </div>
              </BCol>
            </BRow>
          </BCardBody>

        </BCard>
      </BCol>

      <BCol xl="4">
        <BCard no-body class="bg-primary">
          <BCardBody class="p-0">
            <BAlert variant="danger"
              class="rounded-top alert-solid alert-label-icon border-0 rounded-0 m-0 d-flex align-items-center" show>
              <i class="ri-error-warning-line label-icon"></i>
              <div class="flex-grow-1 text-truncate">
                Your free trial expired in <b>17</b> days.
              </div>
              <div class="flex-shrink-0">
                <router-link to="/pages/profile" class="text-reset text-decoration-underline"><b>Upgrade</b>
                </router-link>
              </div>
            </BAlert>

            <BRow class="align-items-end">
              <BCol sm="8">
                <div class="p-3">
                  <p class="fs-16 lh-base text-white">
                    Upgrade your plan from a
                    <span class="fw-semibold">Free trial</span>, to ‘Premium
                    Plan’ <i class="mdi mdi-arrow-right"></i>
                  </p>
                  <div class="mt-3">
                    <router-link to="/pages/profile" class="btn btn-info">Upgrade Account!</router-link>
                  </div>
                </div>
              </BCol>
              <BCol sm="4">
                <div class="px-3">
                  <img src="@/assets/images/user-illustarator-1.png" class="img-fluid" alt="" />
                </div>
              </BCol>
            </BRow>
          </BCardBody>

        </BCard>
      </BCol>

      <BCol xl="4">
        <BCard no-body>
          <BCardBody class="p-0">
            <BAlert variant="warning" class="border-0 rounded-top rounded-0 m-0 d-flex align-items-center" show>
              <div class="flex-grow-1 text-truncate">
                We will choose a gift for you in <b>5</b> days.
              </div>
              <div class="flex-shrink-0">
                <router-link to="/pages/profile" class="text-reset text-decoration-underline"><b>Get Free Gift</b>
                </router-link>
              </div>
            </BAlert>
            <div class="d-flex p-3">
              <div class="flex-shrink-0">
                <div class="avatar-md me-3">
                  <span class="avatar-title bg-danger-subtle rounded-circle fs-1">
                    <i class="ri-gift-2-line text-danger"></i>
                  </span>
                </div>
              </div>
              <div>
                <p class="fs-16 lh-base">
                  Personalized <span class="fw-semibold">Gift Boxes</span>, with
                  attitude, Let's collect your Xmas box
                  <i class="mdi mdi-arrow-right"></i>
                </p>
                <div class="mt-3">
                  <router-link to="/pages/profile" class="btn btn-secondary">Get a Free Gift</router-link>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>
      </BCol>

    </BRow>

    <BRow>
      <BCol lg="4">
        <BCard no-body>
          <BCardBody>
            <h5 class="fs-15 fw-semibold">Brand Logo Design - MD</h5>
            <p class="text-muted">Graphics Work</p>
            <div class="d-flex flex-wrap justify-content-evenly">
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-1-circle
                    text-success
                    fs-18
                    align-middle
                    me-2
                  "></i>Completed
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-3-circle
                    text-info
                    fs-18
                    align-middle
                    me-2
                  "></i>In Progress
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-2-circle
                    text-primary
                    fs-18
                    align-middle
                    me-2
                  "></i>To Do
              </p>
            </div>
          </BCardBody>
          <BProgress class="animated-progress rounded-bottom rounded-0" style="height: 6px">
            <BProgressBar :value="30" variant="success" class="rounded-0" />
            <BProgressBar :value="50" variant="info" class="rounded-0" />
            <BProgressBar :value="20" variant="primary" class="rounded-0" />
          </BProgress>
        </BCard>
      </BCol>

      <BCol lg="4">
        <BCard no-body>
          <BCardBody>
            <h5 class="fs-15 fw-semibold">Redesign - Landing Page</h5>
            <p class="text-muted">UI/UX Design</p>
            <div class="d-flex flex-wrap justify-content-evenly">
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-3-circle
                    text-success
                    fs-18
                    align-middle
                    me-2
                  "></i>Completed
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-0-circle
                    text-info
                    fs-18
                    align-middle
                    me-2
                  "></i>In Progress
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-8-circle
                    text-primary
                    fs-18
                    align-middle
                    me-2
                  "></i>To Do
              </p>
            </div>
          </BCardBody>
          <BProgress class="animated-progress rounded-bottom rounded-0" style="height: 6px">
            <BProgressBar :value="30" variant="success" class="rounded-0" />
            <BProgressBar :value="0" variant="info" class="rounded-0" />
            <BProgressBar :value="70" variant="primary" class="rounded-0" />
          </BProgress>
        </BCard>
      </BCol>

      <BCol lg="4">
        <BCard no-body>
          <BCardBody>
            <h5 class="fs-15 fw-semibold">Ecommerce App for Web</h5>
            <p class="text-muted">CRM Project</p>
            <div class="d-flex flex-wrap justify-content-evenly">
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-10-circle
                    text-success
                    fs-18
                    align-middle
                    me-2
                  "></i>Completed
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-3-circle
                    text-info
                    fs-18
                    align-middle
                    me-2
                  "></i>In Progress
              </p>
              <p class="text-muted mb-0">
                <i class="
                    mdi mdi-numeric-2-circle
                    text-primary
                    fs-18
                    align-middle
                    me-2
                  "></i>To Do
              </p>
            </div>
          </BCardBody>
          <BProgress class="animated-progress rounded-bottom rounded-0" style="height: 6px">
            <BProgressBar :value="60" variant="success" class="rounded-0" />
            <BProgressBar :value="25" variant="info" class="rounded-0" />
            <BProgressBar :value="15" variant="primary" class="rounded-0" />
          </BProgress>
        </BCard>
      </BCol>

    </BRow>

    <BRow>
      <BCol xxl="5">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Upcoming Activities</BCardTitle>
            <div class="flex-shrink-0">
              <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0"
                class="card-header-dropdown" no-caret>
                <template #button-content> <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical"></i></span>
                </template>
                <BDropdownItem href="#">Edit</BDropdownItem>
                <BDropdownItem href="#">Remove</BDropdownItem>
              </BDropdown>
            </div>
          </BCardHeader>

          <BCardBody class="pt-0">
            <ul class="list-group list-group-flush border-dashed">
              <li class="list-group-item ps-0">
                <BRow class="align-items-center g-3">
                  <BCol sm="auto">
                    <div class="avatar-sm p-1 py-2 h-auto bg-light rounded-3">
                      <div class="text-center">
                        <h5 class="mb-0">25</h5>
                        <div class="text-muted">Tue</div>
                      </div>
                    </div>
                  </BCol>
                  <BCol>
                    <h5 class="text-muted mt-0 mb-1 fs-13">
                      12:00am - 03:30pm
                    </h5>
                    <BLink href="#" class="text-reset fs-14 mb-0">Meeting for campaign with sales team</BLink>
                  </BCol>
                  <BCol sm="auto">
                    <div class="avatar-group">
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Stine Nielsen">
                          <img src="@/assets/images/users/avatar-1.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Jansh Brown">
                          <img src="@/assets/images/users/avatar-2.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Dan Gibson">
                          <img src="@/assets/images/users/avatar-3.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);">
                          <div class="avatar-xxs">
                            <span class="
                                avatar-title
                                rounded-circle
                                bg-info
                                text-white
                              ">
                              5
                            </span>
                          </div>
                        </BLink>
                      </div>
                    </div>
                  </BCol>
                </BRow>

              </li>

              <li class="list-group-item ps-0">
                <BRow class="align-items-center g-3">
                  <BCol cols="auto">
                    <div class="avatar-sm p-1 py-2 h-auto bg-light rounded-3">
                      <div class="text-center">
                        <h5 class="mb-0">20</h5>
                        <div class="text-muted">Wed</div>
                      </div>
                    </div>
                  </BCol>
                  <BCol>
                    <h5 class="text-muted mt-0 mb-1 fs-13">
                      02:00pm - 03:45pm
                    </h5>
                    <BLink href="#" class="text-reset fs-14 mb-0">Adding a new event with attachments</BLink>
                  </BCol>
                  <BCol sm="auto">
                    <div class="avatar-group">
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Frida Bang">
                          <img src="@/assets/images/users/avatar-4.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Malou Silva">
                          <img src="@/assets/images/users/avatar-5.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Simon Schmidt">
                          <img src="@/assets/images/users/avatar-6.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Tosh Jessen">
                          <img src="@/assets/images/users/avatar-7.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);">
                          <div class="avatar-xxs">
                            <span class="
                                avatar-title
                                rounded-circle
                                bg-success
                                text-white
                              ">
                              3
                            </span>
                          </div>
                        </BLink>
                      </div>
                    </div>
                  </BCol>
                </BRow>

              </li>

              <li class="list-group-item ps-0">
                <BRow class="align-items-center g-3">
                  <BCol cols="auto">
                    <div class="avatar-sm p-1 py-2 h-auto bg-light rounded-3">
                      <div class="text-center">
                        <h5 class="mb-0">17</h5>
                        <div class="text-muted">Wed</div>
                      </div>
                    </div>
                  </BCol>
                  <BCol>
                    <h5 class="text-muted mt-0 mb-1 fs-13">
                      04:30pm - 07:15pm
                    </h5>
                    <BLink href="#" class="text-reset fs-14 mb-0">Create new project Bundling Product</BLink>
                  </BCol>
                  <BCol sm="auto">
                    <div class="avatar-group">
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Nina Schmidt">
                          <img src="@/assets/images/users/avatar-8.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Stine Nielsen">
                          <img src="@/assets/images/users/avatar-1.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Jansh Brown">
                          <img src="@/assets/images/users/avatar-2.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);">
                          <div class="avatar-xxs">
                            <span class="
                                avatar-title
                                rounded-circle
                                bg-primary
                                text-white
                              ">
                              4
                            </span>
                          </div>
                        </BLink>
                      </div>
                    </div>
                  </BCol>
                </BRow>

              </li>

              <li class="list-group-item ps-0">
                <BRow class="align-items-center g-3">
                  <BCol cols="auto">
                    <div class="avatar-sm p-1 py-2 h-auto bg-light rounded-3">
                      <div class="text-center">
                        <h5 class="mb-0">12</h5>
                        <div class="text-muted">Tue</div>
                      </div>
                    </div>
                  </BCol>
                  <BCol>
                    <h5 class="text-muted mt-0 mb-1 fs-13">
                      10:30am - 01:15pm
                    </h5>
                    <BLink href="#" class="text-reset fs-14 mb-0">Weekly closed sales won checking with sales team
                    </BLink>
                  </BCol>
                  <BCol sm="auto">
                    <div class="avatar-group">
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Stine Nielsen">
                          <img src="@/assets/images/users/avatar-1.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Jansh Brown">
                          <img src="@/assets/images/users/avatar-5.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);" class="d-inline-block" data-bs-toggle="tooltip"
                          data-bs-placement="top" title="" data-bs-original-title="Dan Gibson">
                          <img src="@/assets/images/users/avatar-2.jpg" alt="" class="rounded-circle avatar-xxs" />
                        </BLink>
                      </div>
                      <div class="avatar-group-item">
                        <BLink href="javascript: void(0);">
                          <div class="avatar-xxs">
                            <span class="
                                avatar-title
                                rounded-circle
                                bg-warning
                                text-white
                              ">
                              9
                            </span>
                          </div>
                        </BLink>
                      </div>
                    </div>
                  </BCol>
                </BRow>

              </li>

            </ul>

            <BRow class="align-items-center mt-2 text-center text-sm-start">
              <BCol sm>
                <div class="text-muted">
                  Showing<span class="fw-semibold">4</span> of
                  <span class="fw-semibold">125</span> Results
                </div>
              </BCol>
              <BCol sm="auto">
                <ul class="
                    pagination pagination-separated pagination-sm
                    justify-content-center justify-content-sm-start
                    mb-0
                  ">
                  <li class="page-item disabled">
                    <BLink href="#" class="page-link">←</BLink>
                  </li>
                  <li class="page-item">
                    <BLink href="#" class="page-link">1</BLink>
                  </li>
                  <li class="page-item active">
                    <BLink href="#" class="page-link">2</BLink>
                  </li>
                  <li class="page-item">
                    <BLink href="#" class="page-link">3</BLink>
                  </li>
                  <li class="page-item">
                    <BLink href="#" class="page-link">→</BLink>
                  </li>
                </ul>
              </BCol>
            </BRow>
          </BCardBody>

        </BCard>

      </BCol>

      <BCol xxl="7">
        <BRow>
          <BCol xl="6">
            <BCard no-body class="card-height-100">
              <BCardHeader class="align-items-center d-flex">
                <BCardTitle class="mb-0 flex-grow-1">My Tasks</BCardTitle>
                <div class="flex-shrink-0">
                  <BDropdown variant="link" right toggle-class="text-decoration-none arrow-none p-0"
                    class="card-header-dropdown" no-caret>
                    <template #button-content> <span class="text-muted"><i
                          class="ri-settings-4-line align-middle me-1 fs-15"></i>Settings</span>
                    </template>
                    <BDropdownItem href="#">Edit</BDropdownItem>
                    <BDropdownItem href="#">Remove</BDropdownItem>
                  </BDropdown>
                </div>
              </BCardHeader>


              <BCardBody class="p-0">
                <div class="align-items-center p-3 justify-content-between d-flex">
                  <div class="flex-shrink-0">
                    <div class="text-muted">
                      <span class="fw-semibold">4</span> of
                      <span class="fw-semibold">10</span> remaining
                    </div>
                  </div>
                  <BButton variant="primary" size="sm">
                    <i class="ri-add-line align-middle me-1"></i> Add Task
                  </BButton>
                </div>


                <simplebar data-simplebar style="max-height: 257px">
                  <ul class="list-group list-group-flush border-dashed px-3">
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check ps-0 flex-sharink-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_one" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_one">Review and make sure nothing slips
                            through
                            cracks</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">15 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check ps-0 flex-sharink-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_two" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_two">Send meeting invites for sales
                            upcampaign</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">20 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check flex-sharink-0 ps-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_three" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_three">Weekly closed sales won checking
                            with sales
                            team</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">24 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check ps-0 flex-sharink-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_four" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_four">Add notes that can be viewed from
                            the individual
                            view</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">27 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check ps-0 flex-sharink-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_five" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_five">Move stuff to another page</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">27 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                    <li class="list-group-item ps-0">
                      <div class="d-flex align-items-start">
                        <div class="form-check ps-0 flex-sharink-0">
                          <input type="checkbox" class="form-check-input ms-0" id="task_six" />
                        </div>
                        <div class="flex-grow-1">
                          <label class="form-check-label mb-0 ps-2" for="task_six">Styling wireframe design and
                            documentation for
                            velzon admin</label>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                          <p class="text-muted fs-12 mb-0">27 Sep, 2021</p>
                        </div>
                      </div>
                    </li>
                  </ul>

                </simplebar>
                <div class="p-3">
                  <BLink href="javascript:void(0);" class="text-muted text-decoration-underline">Show more...</BLink>
                </div>
              </BCardBody>

            </BCard>

          </BCol>

          <BCol xl="6">
            <BCard no-body class="card-height-100">
              <BCardHeader class="
                  border-bottom-dashed
                  align-items-center
                  d-flex
                ">
                <BCardTitle class="mb-0 flex-grow-1">Recent Activity</BCardTitle>
                <div class="flex-shrink-0">
                  <BButton variant="soft-primary" size="sm">
                    View All Activity
                  </BButton>
                </div>
              </BCardHeader>

              <BCardBody class="p-0">
                <simplebar data-simplebar style="max-height: 364px;" class="p-3">
                  <div class="acitivity-timeline acitivity-main">
                    <div class="acitivity-item d-flex">
                      <div class="flex-shrink-0 avatar-xs acitivity-avatar">
                        <div class="avatar-title bg-success-subtle text-success rounded-circle">
                          <i class="ri-shopping-cart-2-line"></i>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Purchase by James Price</h6>
                        <p class="text-muted mb-1">Product noise evolve smartwatch</p>
                        <small class="mb-0 text-muted">02:14 PM Today</small>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0 avatar-xs acitivity-avatar">
                        <div class="avatar-title bg-primary-subtle text-primary rounded-circle">
                          <i class="ri-stack-fill"></i>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Added new <span class="fw-semibold">style collection</span></h6>
                        <p class="text-muted mb-1">By Nesta Technologies</p>
                        <div class="d-inline-flex gap-2 border border-dashed p-2 mb-2 w-75">
                          <router-link to="/ecommerce/product-details" class="bg-light rounded p-1">
                            <img src="@/assets/images/products/img-8.png" alt="" class="img-fluid d-block" />
                          </router-link>
                          <router-link to="/ecommerce/product-details" class="bg-light rounded p-1">
                            <img src="@/assets/images/products/img-2.png" alt="" class="img-fluid d-block" />
                          </router-link>
                          <router-link to="/ecommerce/product-details" class="bg-light rounded p-1">
                            <img src="@/assets/images/products/img-10.png" alt="" class="img-fluid d-block" />
                          </router-link>
                        </div>
                        <p class="mb-0 text-muted"><small>9:47 PM Yesterday</small>
                        </p>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0">
                        <img src="@/assets/images/users/avatar-2.jpg" alt=""
                          class="avatar-xs rounded-circle acitivity-avatar">
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Natasha Carey have liked the products</h6>
                        <p class="text-muted mb-1">Allow users to like products in your WooCommerce store.</p>
                        <small class="mb-0 text-muted">25 Dec, 2021</small>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0">
                        <div class="avatar-xs acitivity-avatar">
                          <div class="avatar-title rounded-circle bg-secondary">
                            <i class="mdi mdi-sale fs-14"></i>
                          </div>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Today offers by <router-link to="/ecommerce/seller-details" class="link-secondary">
                            Digitech Galaxy</router-link>
                        </h6>
                        <p class="text-muted mb-2">Offer is valid on orders of Rs.500 Or above for selected products
                          only.</p>
                        <small class="mb-0 text-muted">12 Dec, 2021</small>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0">
                        <div class="avatar-xs acitivity-avatar">
                          <div class="avatar-title rounded-circle bg-danger-subtle text-danger">
                            <i class="ri-bookmark-fill"></i>
                          </div>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Favorite Product</h6>
                        <p class="text-muted mb-2">Esther James have Favorite product.</p>
                        <small class="mb-0 text-muted">25 Nov, 2021</small>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0">
                        <div class="avatar-xs acitivity-avatar">
                          <div class="avatar-title rounded-circle bg-secondary">
                            <i class="mdi mdi-sale fs-14"></i>
                          </div>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Flash sale starting <span class="text-primary">Tomorrow.</span></h6>
                        <p class="text-muted mb-0">Flash sale by <BLink href="javascript:void(0);"
                            class="link-secondary fw-medium">Zoetic Fashion</BLink>
                        </p>
                        <small class="mb-0 text-muted">22 Oct, 2021</small>
                      </div>
                    </div>
                    <div class="acitivity-item py-3 d-flex">
                      <div class="flex-shrink-0">
                        <div class="avatar-xs acitivity-avatar">
                          <div class="avatar-title rounded-circle bg-info-subtle text-info">
                            <i class="ri-line-chart-line"></i>
                          </div>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Monthly sales report</h6>
                        <p class="text-muted mb-2"><span class="text-danger">
                            2 days left</span> notification to submit the monthly sales report. <BLink
                            href="javascript:void(0);" class="link-warning text-decoration-underline">Reports
                            Builder</BLink>
                        </p>
                        <small class="mb-0 text-muted">15 Oct</small>
                      </div>
                    </div>
                    <div class="acitivity-item d-flex">
                      <div class="flex-shrink-0">
                        <img src="@/assets/images/users/avatar-3.jpg" alt=""
                          class="avatar-xs rounded-circle acitivity-avatar" />
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h6 class="mb-1">Frank Hook Commented</h6>
                        <p class="text-muted mb-2 fst-italic">" A product that has reviews is more likable to be sold
                          than a product. "</p>
                        <small class="mb-0 text-muted">26 Aug, 2021</small>
                      </div>
                    </div>
                  </div>
                </simplebar>
              </BCardBody>

            </BCard>

          </BCol>

        </BRow>

      </BCol>

    </BRow>

    <BRow>
      <BCol xl="4" md="6">
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
                data: [0, 36, 110, 95, 130]
              }]" :options="{ ...chartoptions }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>
      <BCol xl="4" md="6">
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
                data: [0, 98, 85, 90, 67]
              }]" :options="{ ...chartoptions, ...chartcolors }"></apexchart>
            </div>
          </div>
        </BCard>
      </BCol>
      <BCol xl="4" md="6">
        <BCard no-body class="card-height-100">
          <div class="d-flex">
            <div class="flex-grow-1 p-3">
              <h5 class="mb-3">Hired</h5>
              <p class="mb-0 text-muted">
                <BBadge class="bg-light text-success mb-0"> <i class="ri-arrow-up-line align-middle"></i> 6.67 %
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
    </BRow>

    <BRow>
      <BCol cols="12">
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">
          Chart & Map Widgets
        </h5>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="4" xl="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Live Users By Country</BCardTitle>
            <div class="flex-shrink-0">
              <BButton variant="soft-primary" size="sm">
                Export Report
              </BButton>
            </div>
          </BCardHeader>


          <BCardBody>
            <div id="users-by-country" style="height: 269px"></div>

            <div class="table-responsive table-card mt-3">
              <table class="
                  table table-borderless table-sm table-centered
                  align-middle
                  table-nowrap
                  mb-1
                ">
                <thead class="
                    text-muted
                    border-dashed border border-start-0 border-end-0
                    bg-light-subtle
                  ">
                  <tr>
                    <th>Duration (Secs)</th>
                    <th style="width: 30%">Sessions</th>
                    <th style="width: 30%">Views</th>
                  </tr>
                </thead>
                <tbody class="border-0">
                  <tr>
                    <td>0-30</td>
                    <td>2,250</td>
                    <td>4,250</td>
                  </tr>
                  <tr>
                    <td>31-60</td>
                    <td>1,501</td>
                    <td>2,050</td>
                  </tr>
                  <tr>
                    <td>61-120</td>
                    <td>750</td>
                    <td>1,600</td>
                  </tr>
                  <tr>
                    <td>121-240</td>
                    <td>540</td>
                    <td>1,040</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xxl="4" xl="6">
        <SessionsCounties />

      </BCol>


      <BCol xxl="4">
        <BCard no-body class="card-height-100">
          <BCardHeader class="border-0 align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Audiences Metrics</BCardTitle>
            <div class="hstack gap-1 justify-content-end">
              <BButton variant="soft-secondary" size="sm">
                ALL
              </BButton>
              <BButton variant="soft-secondary" size="sm">
                1M
              </BButton>
              <BButton variant="soft-secondary" size="sm">
                6M
              </BButton>
              <BButton variant="soft-primary" size="sm">
                1Y
              </BButton>
            </div>
          </BCardHeader>

          <!-- <BAlert >Default Alert</BAlert> -->
          <BCardHeader class="p-0">
            <BAlert variant="primary" :model-value="true"
              class="alert-label-icon border-0 rounded-0 m-0 d-flex align-items-center" show>
              <i class="ri-error-warning-line label-icon"></i>
              <div class="flex-grow-1 text-truncate">
                Your free trial expired in <b>17</b> days.
              </div>
              <div class="flex-shrink-0">
                <router-link to="/pages/pricing" class="text-reset text-decoration-underline"><b>Upgrade</b></router-link>
              </div>
            </BAlert>
          </BCardHeader>
          <BCardHeader class="p-0 border-0 bg-light-subtle">
            <BRow class="g-0 text-center">
              <BCol cols="6" sm="4">
                <div class="p-3 border border-dashed border-start-0">
                  <h5 class="mb-1">
                    <count-to :startVal="0" :endVal="854" :duration="5000"></count-to>
                    <span class="text-success ms-1 fs-12">49%<i
                        class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                  </h5>
                  <p class="text-muted mb-0">Avg. Session</p>
                </div>
              </BCol>

              <BCol cols="6" sm="4">
                <div class="p-3 border border-dashed border-start-0">
                  <h5 class="mb-1">
                    <count-to :startVal="0" :endVal="1278" :duration="5000"></count-to>
                    <span class="text-success ms-1 fs-12">60%<i
                        class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                  </h5>
                  <p class="text-muted mb-0">Conversion Rate</p>
                </div>
              </BCol>

              <BCol cols="6" sm="4">
                <div class="p-3 border border-dashed border-start-0 border-end-0">
                  <h5 class="mb-1">
                    <count-to :startVal="0" :endVal="3" :duration="5000"></count-to>m
                    <count-to :startVal="0" :endVal="3" :duration="40"></count-to>sec
                  </h5>
                  <p class="text-muted mb-0">Avg. Ses. Duration</p>
                </div>
              </BCol>

            </BRow>
          </BCardHeader>


          <BCardBody class="p-0 pb-2">
            <div>
              <apexchart class="apex-charts" dir="ltr" height="306" :series="audienceChartOptions.series"
                :options="audienceChartOptions.chartOptions"></apexchart>
            </div>
          </BCardBody>

        </BCard>

      </BCol>

    </BRow>

    <BRow>
      <BCol xxl="4" xl="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Sales by Locations</BCardTitle>
            <div class="flex-shrink-0">
              <BButton variant="soft-primary" size="sm">
                Export Report
              </BButton>
            </div>
          </BCardHeader>


          <BCardBody>
            <div id="sales-by-locations" style="height: 269px"></div>

            <div class="px-2 py-2 mt-1">
              <p class="mb-1">New Maxico <span class="float-end">75%</span></p>

              <BProgress striped class="mt-2" :value="75" variant="primary" style="height: 6px" />

              <p class="mt-3 mb-1">
                California <span class="float-end">47%</span>
              </p>

              <BProgress striped class="mt-2" :value="47" variant="primary" style="height: 6px" />

              <p class="mt-3 mb-1">Texas <span class="float-end">82%</span></p>

              <BProgress striped class="mt-2" :value="82" variant="primary" style="height: 6px" />
            </div>
          </BCardBody>

        </BCard>

      </BCol>


      <BCol xxl="4" xl="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="border-bottom-dashed align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">My Portfolio</BCardTitle>
            <div>
              <BDropdown text="BTC" variant="primary-subtle" size="sm" right>
                <BDropdownItem href="#">BTC</BDropdownItem>
                <BDropdownItem href="#">USD</BDropdownItem>
                <BDropdownItem href="#">Euro</BDropdownItem>
              </BDropdown>
            </div>
          </BCardHeader>

          <BCardBody>
            <apexchart class="apex-charts" dir="ltr" height="210" :series="portfolioChart.series"
              :options="portfolioChart.chartOptions"></apexchart>

            <ul class="list-group list-group-flush border-dashed mb-0">
              <li class="list-group-item px-0">
                <div class="d-flex">
                  <div class="flex-shrink-0 avatar-xs">
                    <span class="avatar-title bg-light p-1 rounded-circle">
                      <img src="@/assets/images/svg/crypto-icons/btc.svg" class="img-fluid" alt="" />
                    </span>
                  </div>
                  <div class="flex-grow-1 ms-2">
                    <h6 class="mb-1">Bitcoin</h6>
                    <p class="fs-12 mb-0 text-muted">
                      <i class="
                          mdi mdi-circle
                          fs-10
                          align-middle
                          text-primary
                          me-1
                        "></i>BTC
                    </p>
                  </div>
                  <div class="flex-shrink-0 text-end">
                    <h6 class="mb-1">BTC 0.00584875</h6>
                    <p class="text-success fs-12 mb-0">$19,405.12</p>
                  </div>
                </div>
              </li>

              <li class="list-group-item px-0">
                <div class="d-flex">
                  <div class="flex-shrink-0 avatar-xs">
                    <span class="avatar-title bg-light p-1 rounded-circle">
                      <img src="@/assets/images/svg/crypto-icons/eth.svg" class="img-fluid" alt="" />
                    </span>
                  </div>
                  <div class="flex-grow-1 ms-2">
                    <h6 class="mb-1">Ethereum</h6>
                    <p class="fs-12 mb-0 text-muted">
                      <i class="mdi mdi-circle fs-10 align-middle text-info me-1"></i>ETH
                    </p>
                  </div>
                  <div class="flex-shrink-0 text-end">
                    <h6 class="mb-1">ETH 2.25842108</h6>
                    <p class="text-danger fs-12 mb-0">$40552.18</p>
                  </div>
                </div>
              </li>

              <li class="list-group-item px-0">
                <div class="d-flex">
                  <div class="flex-shrink-0 avatar-xs">
                    <span class="avatar-title bg-light p-1 rounded-circle">
                      <img src="@/assets/images/svg/crypto-icons/ltc.svg" class="img-fluid" alt="" />
                    </span>
                  </div>
                  <div class="flex-grow-1 ms-2">
                    <h6 class="mb-1">Litecoin</h6>
                    <p class="fs-12 mb-0 text-muted">
                      <i class="
                          mdi mdi-circle
                          fs-10
                          align-middle
                          text-warning
                          me-1
                        "></i>LTC
                    </p>
                  </div>
                  <div class="flex-shrink-0 text-end">
                    <h6 class="mb-1">LTC 10.58963217</h6>
                    <p class="text-success fs-12 mb-0">$15824.58</p>
                  </div>
                </div>
              </li>

              <li class="list-group-item px-0 pb-0">
                <div class="d-flex">
                  <div class="flex-shrink-0 avatar-xs">
                    <span class="avatar-title bg-light p-1 rounded-circle">
                      <img src="@/assets/images/svg/crypto-icons/dash.svg" class="img-fluid" alt="" />
                    </span>
                  </div>
                  <div class="flex-grow-1 ms-2">
                    <h6 class="mb-1">Dash</h6>
                    <p class="fs-12 mb-0 text-muted">
                      <i class="
                          mdi mdi-circle
                          fs-10
                          align-middle
                          text-success
                          me-1
                        "></i>DASH
                    </p>
                  </div>
                  <div class="flex-shrink-0 text-end">
                    <h6 class="mb-1">DASH 204.28565885</h6>
                    <p class="text-success fs-12 mb-0">$30635.84</p>
                  </div>
                </div>
              </li>
            </ul>

          </BCardBody>

        </BCard>

      </BCol>


      <BCol xxl="4">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Top Referrals Pages</BCardTitle>
            <div class="flex-shrink-0">
              <BButton variant="soft-primary" size="sm">
                Export Report
              </BButton>
            </div>
          </BCardHeader>

          <BCardBody>
            <apexchart class="apex-charts" dir="ltr" height="310" :series="topReferralsChart.series"
              :options="topReferralsChart.chartOptions"></apexchart>

            <BRow class="g-3">
              <BCol md="6">
                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0">
                      <i class="mdi mdi-circle align-middle text-primary me-2"></i>www.google.com
                    </p>
                  </div>
                  <div class="flex-shrink-0">
                    <p class="mb-0">24.58%</p>
                  </div>
                </div>

                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0">
                      <i class="mdi mdi-circle align-middle text-warning me-2"></i>www.medium.com
                    </p>
                  </div>
                  <div class="flex-shrink-0">
                    <p class="mb-0">12.22%</p>
                  </div>
                </div>

                <div class="d-flex">
                  <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0">
                      <i class="mdi mdi-circle align-middle text-secondary me-2"></i>Other
                    </p>
                  </div>
                  <div class="flex-shrink-0">
                    <p class="mb-0">17.58%</p>
                  </div>
                </div>

              </BCol>
              <BCol md="6">
                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0">
                      <i class="mdi mdi-circle align-middle text-info me-2"></i>www.youtube.com
                    </p>
                  </div>
                  <div class="flex-shrink-0">
                    <p class="mb-0">17.51%</p>
                  </div>
                </div>

                <div class="d-flex mb-3">
                  <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0">
                      <i class="mdi mdi-circle align-middle text-success me-2"></i>www.meta.com
                    </p>
                  </div>
                  <div class="flex-shrink-0">
                    <p class="mb-0">23.05%</p>
                  </div>
                </div>

              </BCol>
            </BRow>

            <div class="mt-2 text-center">
              <BLink href="javascript:void(0);" class="text-muted text-decoration-underline">Show All</BLink>
            </div>
          </BCardBody>

        </BCard>
      </BCol>

    </BRow>

    <BRow>
      <BCol cols="12">
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Ecommerce Widgets</h5>
      </BCol>
    </BRow>

    <BRow>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardHeader class="align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Hot Products</BCardTitle>
            <div class="flex-shrink-0">
              <BLink class="text-muted" href="#" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                View All
              </BLink>
            </div>
          </BCardHeader>
          <BCardBody>
            <swiper class="swiper mySwiper" :autoplay="true" :slidesPerView="2" :spaceBetween="30" :modules="[Autoplay]">
              <swiper-slide style="max-width: 200px;">
                <div>
                  <div class="bg-info-subtle rounded">
                    <img src="@/assets/images/products/img-3.png" alt="" style="max-height: 210px;max-width: auto" />
                  </div>
                  <div class="pt-3">
                    <h5 class="text-secondary">$99.94</h5>
                    <BLink href="#!">
                      <h6 class="fs-15 lh-base text-truncate mb-0">350 ml Glass Grocery Container</h6>
                    </BLink>
                  </div>
                </div>
              </swiper-slide>
              <swiper-slide style="max-width: 200px;">
                <div>
                  <div class="bg-success-subtle rounded">
                    <img src="@/assets/images/products/img-4.png" alt="" style="max-height: 210px;max-width: auto;" />
                  </div>
                  <div class="pt-3">
                    <h5 class="text-secondary">$99.94</h5>
                    <BLink href="#!">
                      <h6 class="fs-15 lh-base text-truncate mb-0">Fabric Dual Tone Living Room Chair</h6>
                    </BLink>
                  </div>
                </div>
              </swiper-slide>
              <swiper-slide style="max-width: 200px;">
                <div>
                  <div class="bg-warning-subtle rounded">
                    <img src="@/assets/images/products/img-5.png" alt="" style="max-height: 210px;max-width: auto;" />
                  </div>
                  <div class="pt-3">
                    <h5 class="text-secondary">$99.94</h5>
                    <BLink href="#!">
                      <h6 class="fs-15 lh-base text-truncate mb-0">Crux Motorsports Helmet</h6>
                    </BLink>
                  </div>
                </div>
              </swiper-slide>
              <swiper-slide style="max-width: 200px;">
                <div>
                  <div class="bg-secondary-subtle rounded">
                    <img src="@/assets/images/products/img-6.png" alt="" style="max-height: 210px;max-width: auto;" />
                  </div>
                  <div class="pt-3">
                    <h5 class="text-secondary">$99.94</h5>
                    <BLink href="#!">
                      <h6 class="fs-15 lh-base text-truncate mb-0">Half Sleeve T-Shirts (Blue)</h6>
                    </BLink>
                  </div>
                </div>
              </swiper-slide>
              <swiper-slide style="max-width: 200px;">
                <div>
                  <div class="bg-success-subtle rounded">
                    <img src="@/assets/images/products/img-7.png" alt="" style="max-height: 210px;max-width: auto;" />
                  </div>
                  <div class="pt-3">
                    <h5 class="text-secondary">$99.94</h5>
                    <BLink href="#!">
                      <h6 class="fs-15 lh-base text-truncate mb-0">Fabric Dual Tone Living Room Chair</h6>
                    </BLink>
                  </div>
                </div>
              </swiper-slide>
            </swiper>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center mb-3">
              <div class="avatar-sm me-3 flex-shrink-0">
                <div class="avatar-title bg-info-subtle rounded">
                  <img src="@/assets/images/products/img-6.png" alt="" class="avatar-xs">
                </div>
              </div>
              <div class="flex-grow-1">
                <p class="text-muted mb-2">Adidas</p>
                <h5 class="fs-15 mb-0">Half Sleeve T-Shirts (Blue)</h5>
              </div>
            </div>
            <p class="text-muted pb-1">If you couldn't relate to the information in the previous point, you might be
              looking for the singlet T-shirt, which is also known as the half T-shirt.</p>

            <BRow class="mb-4">
              <BCol xl="6">
                <h6 class="fs-14 mb-2">Sizes</h6>
                <ul class="clothes-size list-unstyled hstack gap-2 mb-0">
                  <li>
                    <input type="radio" name="sizes" id="color-1" disabled />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-1">S</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-2" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-2">M</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-3" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-3">L</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-4" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-4">XL</label>
                  </li>
                </ul>
              </BCol>


              <BCol xl="6">
                <div>
                  <h6 class="fs-14 mb-2">Colors</h6>
                  <div class="d-flex flex-wrap gap-2 select-color">
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="Out of Stock">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-primary"
                        disabled>
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="03 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-secondary">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="03 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-success">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="02 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-info">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </BCol>

            </BRow>


            <div class="d-flex mb-4 align-items-center">
              <div class="flex-grow-1">
                <h5 class="text-primary fs-18 mb-0 product-price"><span>$22.45</span> <small
                    class="text-decoration-line-through text-muted fs-13 product-price-line">$37.45</small></h5>
              </div>

              <div class="input-step flex-shrink-0">
                <button type="button" class="minus" @click="minusamount()">–</button>
                <input type="number" class="product-quantity" value="2" min="0" max="100" readonly>
                <button type="button" class="plus" @click="plusamount()">+</button>
              </div>
            </div>

            <BLink href="#!" class="btn btn-soft-danger d-block">Add to Cart</BLink>

          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody class="position-relative">
            <h5 class="mb-3">Select Bank</h5>
            <div class="vstack gap-3">
              <div class="form-check card-radio">
                <input id="listGroupRadioGrid1" name="listGroupRadioGrid" type="radio" class="form-check-input">
                <label class="form-check-label" for="listGroupRadioGrid1">
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <div class="avatar-xs">
                        <div class="avatar-title bg-success-subtle text-success fs-18 rounded">
                          <i class="ri-visa-fill"></i>
                        </div>
                      </div>
                    </div>
                    <div class="flex-grow-1 mt-3 ms-3">
                      <h6 class="mb-1">Visa Card</h6>
                      <b class="pay-amount">$8,500</b>
                    </div>
                  </div>
                </label>
              </div>

              <div class="form-check card-radio">
                <input id="listGroupRadioGrid2" name="listGroupRadioGrid" type="radio" class="form-check-input">
                <label class="form-check-label" for="listGroupRadioGrid2">
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <div class="avatar-xs">
                        <div class="avatar-title bg-info-subtle text-info fs-18 rounded">
                          <i class="ri-bank-card-2-line"></i>
                        </div>
                      </div>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h6 class="mb-1">Credit Card</h6>
                      <b class="pay-amount">$8,326</b>
                    </div>
                  </div>
                </label>
              </div>

              <div class="form-check card-radio">
                <input id="listGroupRadioGrid3" name="listGroupRadioGrid" type="radio" class="form-check-input">
                <label class="form-check-label" for="listGroupRadioGrid3">
                  <div class="d-flex align-items-center">
                    <div class="flex-shrink-0">
                      <div class="avatar-xs">
                        <div class="avatar-title bg-danger-subtle text-danger fs-18 rounded">
                          <i class="ri-mastercard-line"></i>
                        </div>
                      </div>
                    </div>
                    <div class="flex-grow-1 ms-3">
                      <h6 class="mb-1">Mastercard Card</h6>
                      <b class="pay-amount">$8,400</b>
                    </div>
                  </div>
                </label>
              </div>

            </div>

            <BButton variant="success" type="button" class="w-100 mt-3" id="confirm-btn" @click="selectBank">Confirm
            </BButton>

            <div id="notification-warn" class="position-absolute top-0 start-0 end-0 d-none">
              <div class="alert alert-warning" role="alert">
                Select at list one item
              </div>
            </div>

            <div class="notification-elem" id="notification-overlay">
              <div class="text-center">
                <lottie colors="primary:#0ab39c,secondary:#405189" :options="defaultOptions" :height="120" :width="120" />
                <div class="mt-4 pt-2">
                  <h5 class="mb-1 success-pay">$6,201 Payment Successfully</h5>
                  <p class="text-muted mx-4">Aww yeah, you successfully read this important message.</p>

                  <div>
                    <BButton variant="success" type="button" size="sm" class="w-sm" id="back-btn" @click="selectBankback">
                      Back to Home</BButton>
                  </div>
                </div>
              </div>
            </div>
          </BCardBody>

        </BCard>

      </BCol>

      <BCol xl="3" md="6">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <div class="d-flex align-items-center mb-3">
              <div class="avatar-sm me-3 flex-shrink-0">
                <div class="avatar-title bg-danger-subtle rounded">
                  <img src="@/assets/images/products/img-8.png" alt="" class="avatar-xs">
                </div>
              </div>
              <div class="flex-grow-1">
                <p class="text-muted mb-2">Adidas</p>
                <h5 class="fs-15 mb-0">Half Sleeve T-Shirts (Pink)</h5>
              </div>
            </div>
            <p class="text-muted pb-1">If you couldn't relate to the information in the previous point, you might be
              looking for the singlet T-shirt, which is also known as the half T-shirt.</p>

            <BRow class="mb-4">
              <BCol xl="6">
                <h6 class="fs-14 mb-2">Sizes</h6>
                <ul class="clothes-size list-unstyled hstack gap-2 mb-0">
                  <li>
                    <input type="radio" name="sizes" id="color-1" disabled />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-1">S</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-2" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-2">M</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-3" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-3">L</label>
                  </li>
                  <li>
                    <input type="radio" name="sizes" id="color-4" />
                    <label
                      class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle"
                      for="color-4">XL</label>
                  </li>
                </ul>
              </BCol>


              <BCol xl="6">
                <div>
                  <h6 class="fs-14 mb-2">Colors</h6>
                  <div class="d-flex flex-wrap gap-2 select-color">
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="Out of Stock">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-primary"
                        disabled>
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="03 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-secondary">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="03 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-success">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                    <div data-bs-toggle="tooltip" v-b-tooltip.hover title="02 Items Available">
                      <button type="button"
                        class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-info">
                        <i class="ri-checkbox-blank-circle-fill"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </BCol>

            </BRow>


            <div class="d-flex mb-4 align-items-center">
              <div class="flex-grow-1">
                <h5 class="text-primary fs-18 mb-0 product-price"><span>$48.20</span> <small
                    class="text-decoration-line-through text-muted fs-13 product-price-line">$124.10</small></h5>
              </div>

              <div class="input-step flex-shrink-0">
                <button type="button" class="minus" @click="minusamount()">–</button>
                <input type="number" class="product-quantity" value="2" min="0" max="100" readonly>
                <button type="button" class="plus" @click="plusamount()">+</button>
              </div>
            </div>

            <BLink href="#!" class="btn btn-soft-danger d-block">Add to Cart</BLink>

          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="5">
        <BCard no-body>
          <BRow class="g-0">
            <BCol lg="6">
              <BCardBody class="border-end">
                <div class="search-box">
                  <input type="text" class="form-control bg-light border-light" autocomplete="off" id="searchList"
                    placeholder="Search candidate..." v-model="searchQuery">
                  <i class="ri-search-line search-icon"></i>
                </div>
                <simplebar data-simplebar style="max-height: 190px" class="px-3 mx-n3">
                  <ul class="list-unstyled mb-0 pt-2" id="candidate-list">

                    <li v-for="(data, index) of resultQuery" :key="index" @click="showdetail(data)">
                      <BLink href="javascript:void(0);" class="d-flex align-items-center py-2">
                        <div class="flex-shrink-0 me-2">
                          <div class="avatar-xs">
                            <img :src="data.img" alt="" class="img-fluid rounded-circle candidate-img">
                          </div>
                        </div>
                        <div class="flex-grow-1">
                          <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">{{ data.name }}</span> <span
                              class="text-muted fw-normal">{{ data.username }}</span></h5>
                          <div class="d-none candidate-position">{{ data.designation }}</div>
                        </div>
                      </BLink>
                    </li>
                  </ul>
                </simplebar>
              </BCardBody>
            </BCol>
            <BCol lg="6">
              <BCardBody class="text-center">
                <div class="avatar-md mb-3 mx-auto">
                  <img src="@/assets/images/users/avatar-1.jpg" alt="" id="candidate-img"
                    class="img-thumbnail rounded-circle shadow-none">
                </div>

                <h5 id="candidate-name" class="mb-0">Anna Adame</h5>
                <p id="candidate-position" class="text-muted">Web Developer</p>

                <div class="d-flex gap-2 justify-content-center mb-3">
                  <button type="button" class="btn avatar-xs p-0" v-b-tooltip.hover title="Google">
                    <span class="avatar-title rounded-circle bg-light text-body">
                      <i class="ri-google-line"></i>
                    </span>
                  </button>

                  <button type="button" class="btn avatar-xs p-0" v-b-tooltip.hover title="Linkedin">
                    <span class="avatar-title rounded-circle bg-light text-body">
                      <i class="ri-linkedin-line"></i>
                    </span>
                  </button>
                  <button type="button" class="btn avatar-xs p-0" v-b-tooltip.hover title="Dribbble">
                    <span class="avatar-title rounded-circle bg-light text-body">
                      <i class="ri-dribbble-fill"></i>
                    </span>
                  </button>
                </div>

                <div>
                  <BButton type="button" variant="success" class="rounded-pill w-sm"><i
                      class="ri-add-fill me-1 align-bottom"></i> Follow</BButton>
                </div>
              </BCardBody>
            </BCol>
          </BRow>
        </BCard>

      </BCol>

    </BRow>

    <BRow>
      <BCol cols="12">
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Credit Card</h5>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="4">
        <BCard no-body class="card-height-100 ">
          <BCardHeader>
            <h5 class="card-title mb-0">Credit Card - Custom</h5>
          </BCardHeader>
          <BCardBody>
            <div class="mx-auto" style="max-width: 350px">
              <div class="text-bg-info bg-gradient p-4 rounded-3 mb-3">
                <div class="d-flex">
                  <div class="flex-grow-1">
                    <i class="bx bx-chip h1 text-warning"></i>
                  </div>
                  <div class="flex-shrink-0">
                    <i class="bx bxl-visa display-2 mt-n3"></i>
                  </div>
                </div>
                <div class="card-number fs-20" id="card-num-elem">
                  XXXX XXXX XXXX XXXX
                </div>

                <BRow class="mt-4">
                  <BCol cols="4">
                    <div>
                      <div class="text-white-50">Card Holder</div>
                      <div id="card-holder-elem" class="fw-medium fs-14">Full Name</div>
                    </div>
                  </BCol>
                  <BCol cols="4">
                    <div class="expiry">
                      <div class="text-white-50">Expires</div>
                      <div class="fw-medium fs-14">
                        <span id="expiry-month-elem">00</span>
                        /
                        <span id="expiry-year-elem">0000</span>
                      </div>
                    </div>
                  </BCol>
                  <BCol cols="4">
                    <div>
                      <div class="text-white-50">CVC</div>
                      <div id="cvc-elem" class="fw-medium fs-14">---</div>
                    </div>
                  </BCol>
                </BRow>
              </div>

            </div>


            <form id="custom-card-form" autocomplete="off">
              <div class="mb-3">
                <label for="card-num-input" class="form-label">Card Number</label>
                <input id="card-num-input" class="form-control" maxlength="19" placeholder="0000 0000 0000 0000"
                  @keypress="(e) => customcreditcard(e)" />
              </div>

              <div class="mb-3">
                <label for="card-holder-input" class="form-label">Card Holder</label>
                <input type="text" class="form-control" id="card-holder-input" placeholder="Enter holder name"
                  @keypress="(e) => customcreditcard(e)" />
              </div>

              <BRow>
                <BCol lg="4">
                  <div>
                    <label for="expiry-month-input" class="form-label">Expiry Month</label>
                    <select class="form-select" id="expiry-month-input" @change="(e) => customcreditcard(e)">
                      <option></option>
                      <option value="01">01</option>
                      <option value="02">02</option>
                      <option value="03">03</option>
                      <option value="04">04</option>
                      <option value="05">05</option>
                      <option value="06">06</option>
                      <option value="07">07</option>
                      <option value="08">08</option>
                      <option value="09">09</option>
                      <option value="10">10</option>
                      <option value="11">11</option>
                      <option value="12">12</option>
                    </select>
                  </div>
                </BCol>


                <BCol lg="4">
                  <div>
                    <label for="expiry-year-input" class="form-label">Expiry Year</label>
                    <select class="form-select" id="expiry-year-input" @change="(e) => customcreditcard(e)">
                      <option></option>
                      <option value="2020">2020</option>
                      <option value="2021">2021</option>
                      <option value="2022">2022</option>
                      <option value="2023">2023</option>
                      <option value="2024">2024</option>
                      <option value="2025">2025</option>
                      <option value="2026">2026</option>
                      <option value="2027">2027</option>
                      <option value="2028">2028</option>
                      <option value="2029">2029</option>
                      <option value="2030">2030</option>
                    </select>
                  </div>
                </BCol>
                <BCol lg="4">
                  <div class="cvc">
                    <label for="cvc-input" class="form-label">CVC</label>
                    <input type="text" id="cvc-input" class="form-control" maxlength="3"
                      @keypress="(e) => customcreditcard(e)" />
                  </div>
                </BCol>
              </BRow>
              <BButton variant="danger" class="w-100 mt-3" type="submit">Pay Now</BButton>
            </form>
          </BCardBody>
        </BCard>
      </BCol>


      <BCol xl="4">
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Credit Card - card js plugin</h5>
          </BCardHeader>
          <BCardBody>
            <div class="card-wrapper mb-3">
              <div class="mx-auto" style="max-width: 350px">
                <div class="text-bg-success bg-gradient p-4 rounded-3 mb-3 credit-card">
                  <div class="d-flex">
                    <div class="flex-grow-1">
                      <i class='bx bxs-wallet-alt h1'></i>
                    </div>
                  </div>
                  <div class="card-number fs-20" id="card-num-elem">
                    •••• •••• •••• ••••
                  </div>
                  <div class="mt-4 d-flex justify-content-between">
                    <div class="cols-4">
                      <div>
                        <div id="card-holder-elem" class="fw-medium fs-14">FULL NAME</div>
                      </div>
                    </div>
                    <div class="cols-4 ex-date">
                      <div>
                        <div class="text-white-50">Expires</div>
                        <div class="fw-medium fs-14">
                          <span id="expiry-month-elem">00</span>
                          /
                          <span id="expiry-year-elem">0000</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="form-container active">
              <form action="" id="card-form-elem" autocomplete="off">
                <div class="mb-3">
                  <label for="card-number-input" class="form-label">Card Number</label>
                  <input class="form-control" placeholder="Card number" type="tel" id="card-number-input">
                </div>
                <div class="mb-3">
                  <label for="card-name-input" class="form-label">Card Holder</label>
                  <input class="form-control" placeholder="Full name" type="text" id="card-name-input">
                </div>
                <BRow>
                  <BCol sm="6">
                    <div class="mb-3">
                      <label for="card-expiry-input" class="form-label">Expiry</label>
                      <input class="form-control" placeholder="MM/YY" type="tel" id="card-expiry-input">
                    </div>
                  </BCol>
                  <BCol sm="6">
                    <div class="mb-3">
                      <label for="card-cvc-input" class="form-label">CVC</label>
                      <input class="form-control" placeholder="CVC" type="number" id="card-cvc-input">
                    </div>
                  </BCol>
                </BRow>
                <BButton variant="danger" class="w-100" type="submit">Pay Now</BButton>
              </form>
            </div>
          </BCardBody>

        </BCard>

      </BCol>

    </BRow>

  </Layout>
</template>