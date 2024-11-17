<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/autoplay";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import animationData from "@/components/widgets/msoeawqm.json";
import Lottie from "@/components/widgets/lottie.vue";
import { market } from "@/common/data";

export default {
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      series: [
        {
          name: "Balance",
          data: [
            [1327359600000, 30.95],
            [1327446000000, 31.34],
            [1327532400000, 31.18],
            [1327618800000, 31.05],
            [1327878000000, 31.0],
            [1327964400000, 30.95],
            [1328050800000, 31.24],
            [1328137200000, 31.29],
            [1328223600000, 31.85],
            [1328482800000, 31.86],
            [1328569200000, 32.28],
            [1328655600000, 32.1],
            [1328742000000, 32.65],
            [1328828400000, 32.21],
            [1329087600000, 32.35],
            [1329174000000, 32.44],
            [1329260400000, 32.46],
            [1329346800000, 32.86],
            [1329433200000, 32.75],
            [1329778800000, 32.54],
            [1329865200000, 32.33],
            [1329951600000, 32.97],
            [1330038000000, 33.41],
            [1330297200000, 33.27],
            [1330383600000, 33.27],
            [1330470000000, 32.89],
            [1330556400000, 33.1],
            [1330642800000, 33.73],
            [1330902000000, 33.22],
            [1330988400000, 31.99],
            [1331074800000, 32.41],
            [1331161200000, 33.05],
            [1331247600000, 33.64],
            [1331506800000, 33.56],
            [1331593200000, 34.22],
            [1331679600000, 33.77],
            [1331766000000, 34.17],
            [1331852400000, 33.82],
            [1332111600000, 34.51],
            [1332198000000, 33.16],
            [1332284400000, 33.56],
            [1332370800000, 33.71],
            [1332457200000, 33.81],
            [1332712800000, 34.4],
            [1332799200000, 34.63],
            [1332885600000, 34.46],
            [1332972000000, 34.48],
            [1333058400000, 34.31],
            [1333317600000, 34.7],
            [1333404000000, 34.31],
            [1333490400000, 33.46],
            [1333576800000, 33.59],
            [1333922400000, 33.22],
            [1334008800000, 32.61],
            [1334095200000, 33.01],
            [1334181600000, 33.55],
            [1334268000000, 33.18],
            [1334527200000, 32.84],
            [1334613600000, 33.84],
            [1334700000000, 33.39],
            [1334786400000, 32.91],
            [1334872800000, 33.06],
            [1335132000000, 32.62],
            [1335218400000, 32.4],
            [1335304800000, 33.13],
            [1335391200000, 33.26],
            [1335477600000, 33.58],
            [1335736800000, 33.55],
            [1335823200000, 33.77],
            [1335909600000, 33.76],
            [1335996000000, 33.32],
            [1336082400000, 32.61],
            [1336341600000, 32.52],
            [1336428000000, 32.67],
            [1336514400000, 32.52],
            [1336600800000, 31.92],
            [1336687200000, 32.2],
            [1336946400000, 32.23],
            [1337032800000, 32.33],
            [1337119200000, 32.36],
            [1337205600000, 32.01],
            [1337292000000, 31.31],
            [1337551200000, 32.01],
            [1337637600000, 32.01],
            [1337724000000, 32.18],
            [1337810400000, 31.54],
            [1337896800000, 31.6],
            [1338242400000, 32.05],
            [1338328800000, 31.29],
            [1338415200000, 31.05],
            [1338501600000, 29.82],
            [1338760800000, 30.31],
            [1338847200000, 30.7],
            [1338933600000, 31.69],
            [1339020000000, 31.32],
            [1339106400000, 31.65],
            [1339365600000, 31.13],
            [1339452000000, 31.77],
            [1339538400000, 31.79],
            [1339624800000, 31.67],
            [1339711200000, 32.39],
            [1339970400000, 32.63],
            [1340056800000, 32.89],
            [1340143200000, 31.99],
            [1340229600000, 31.23],
            [1340316000000, 31.57],
            [1340575200000, 30.84],
            [1340661600000, 31.07],
            [1340748000000, 31.41],
            [1340834400000, 31.17],
            [1340920800000, 32.37],
            [1341180000000, 32.19],
            [1341266400000, 32.51],
            [1341439200000, 32.53],
            [1341525600000, 31.37],
            [1341784800000, 30.43],
            [1341871200000, 30.44],
            [1341957600000, 30.2],
            [1342044000000, 30.14],
            [1342130400000, 30.65],
            [1342389600000, 30.4],
            [1342476000000, 30.65],
            [1342562400000, 31.43],
            [1342648800000, 31.89],
            [1342735200000, 31.38],
            [1342994400000, 30.64],
            [1343080800000, 30.02],
            [1343167200000, 30.33],
            [1343253600000, 30.95],
            [1343340000000, 31.89],
            [1343599200000, 31.01],
            [1343685600000, 30.88],
            [1343772000000, 30.69],
            [1343858400000, 30.58],
            [1343944800000, 32.02],
            [1344204000000, 32.14],
            [1344290400000, 32.37],
            [1344376800000, 32.51],
            [1344463200000, 32.65],
            [1344549600000, 32.64],
            [1344808800000, 32.27],
            [1344895200000, 32.1],
            [1344981600000, 32.91],
            [1345068000000, 33.65],
            [1345154400000, 33.8],
            [1345413600000, 33.92],
            [1345500000000, 33.75],
            [1345586400000, 33.84],
            [1345672800000, 33.5],
            [1345759200000, 32.26],
            [1346018400000, 32.32],
            [1346104800000, 32.06],
            [1346191200000, 31.96],
            [1346277600000, 31.46],
            [1346364000000, 31.27],
            [1346709600000, 31.43],
            [1346796000000, 32.26],
            [1346882400000, 32.79],
            [1346968800000, 32.46],
            [1347228000000, 32.13],
            [1347314400000, 32.43],
            [1347400800000, 32.42],
            [1347487200000, 32.81],
            [1347573600000, 33.34],
            [1347832800000, 33.41],
            [1347919200000, 32.57],
            [1348005600000, 33.12],
            [1348092000000, 34.53],
            [1348178400000, 33.83],
            [1348437600000, 33.41],
            [1348524000000, 32.9],
            [1348610400000, 32.53],
            [1348696800000, 32.8],
            [1348783200000, 32.44],
            [1349042400000, 32.62],
            [1349128800000, 32.57],
            [1349215200000, 32.6],
            [1349301600000, 32.68],
            [1349388000000, 32.47],
            [1349647200000, 32.23],
            [1349733600000, 31.68],
            [1349820000000, 31.51],
            [1349906400000, 31.78],
            [1349992800000, 31.94],
            [1350252000000, 32.33],
            [1350338400000, 33.24],
            [1350424800000, 33.44],
            [1350511200000, 33.48],
            [1350597600000, 33.24],
            [1350856800000, 33.49],
            [1350943200000, 33.31],
            [1351029600000, 33.36],
            [1351116000000, 33.4],
            [1351202400000, 34.01],
            [1351638000000, 34.02],
            [1351724400000, 34.36],
            [1351810800000, 34.39],
            [1352070000000, 34.24],
            [1352156400000, 34.39],
            [1352242800000, 33.47],
            [1352329200000, 32.98],
            [1352415600000, 32.9],
            [1352674800000, 32.7],
            [1352761200000, 32.54],
            [1352847600000, 32.23],
            [1352934000000, 32.64],
            [1353020400000, 32.65],
            [1353279600000, 32.92],
            [1353366000000, 32.64],
            [1353452400000, 32.84],
            [1353625200000, 33.4],
            [1353884400000, 33.3],
            [1353970800000, 33.18],
            [1354057200000, 33.88],
            [1354143600000, 34.09],
            [1354230000000, 34.61],
            [1354489200000, 34.7],
            [1354575600000, 35.3],
            [1354662000000, 35.4],
            [1354748400000, 35.14],
            [1354834800000, 35.48],
            [1355094000000, 35.75],
            [1355180400000, 35.54],
            [1355266800000, 35.96],
            [1355353200000, 35.53],
            [1355439600000, 37.56],
            [1355698800000, 37.42],
            [1355785200000, 37.49],
            [1355871600000, 38.09],
            [1355958000000, 37.87],
            [1356044400000, 37.71],
            [1356303600000, 37.53],
            [1356476400000, 37.55],
            [1356562800000, 37.3],
            [1356649200000, 36.9],
            [1356908400000, 37.68],
            [1357081200000, 38.34],
            [1357167600000, 37.75],
            [1357254000000, 38.13],
            [1357513200000, 37.94],
            [1357599600000, 38.14],
            [1357686000000, 38.66],
            [1357772400000, 38.62],
            [1357858800000, 38.09],
            [1358118000000, 38.16],
            [1358204400000, 38.15],
            [1358290800000, 37.88],
            [1358377200000, 37.73],
            [1358463600000, 37.98],
            [1358809200000, 37.95],
            [1358895600000, 38.25],
            [1358982000000, 38.1],
            [1359068400000, 38.32],
            [1359327600000, 38.24],
            [1359414000000, 38.52],
            [1359500400000, 37.94],
            [1359586800000, 37.83],
            [1359673200000, 38.34],
            [1359932400000, 38.1],
            [1360018800000, 38.51],
            [1360105200000, 38.4],
            [1360191600000, 38.07],
            [1360278000000, 39.12],
            [1360537200000, 38.64],
            [1360623600000, 38.89],
            [1360710000000, 38.81],
            [1360796400000, 38.61],
            [1360882800000, 38.63],
            [1361228400000, 38.99],
            [1361314800000, 38.77],
            [1361401200000, 38.34],
            [1361487600000, 38.55],
            [1361746800000, 38.11],
            [1361833200000, 38.59],
            [1361919600000, 39.6],
          ],
        },
      ],
      chartOptions: {
        colors: ["#BD83F4"],
        chart: {
          width: "100%",
          height: 46,
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
          width: 4.0,
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
      },
      market: market,
      cryptoSlider: [
        {
          id: 1,
          img: require("@/assets/images/svg/crypto-icons/btc.svg"),
          label: "Bitcoin",
          price: "$1,523,647",
          change: "+13.11%",
          changeClass: "success",
          coinName: "btc",
          chartsColor: "#0ab39c",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#0ab39c"],
          },
          series: [
            {
              name: "Bitcoin",
              data: [85, 68, 35, 90, 8, 11, 26, 54],
            },
          ],
        },
        {
          id: 2,
          img: require("@/assets/images/svg/crypto-icons/ltc.svg"),
          label: "Litecoin",
          price: "$2,145,687",
          change: "+15.08%",
          changeClass: "success",
          coinName: "ltc",
          chartsColor: "#f17171",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#f17171"],
          },
          series: [
            {
              name: "Litecoin",
              data: [25, 50, 41, 87, 12, 36, 9, 54],
            },
          ],
        },
        {
          id: 3,
          img: require("@/assets/images/svg/crypto-icons/eth.svg"),
          label: "Ethereum",
          price: "$3,312,870",
          change: "+08.57%",
          changeClass: "success",
          coinName: "etc",
          chartsColor: "#f17171",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#f17171"],
          },
          series: [
            {
              name: "Ethereum",
              data: [36, 21, 65, 22, 35, 50, 29, 44],
            },
          ],
        },
        {
          id: 4,
          img: require("@/assets/images/svg/crypto-icons/bnb.svg"),
          label: "Binance",
          price: "$1,820,045",
          change: "-09.21%",
          changeClass: "danger",
          coinName: "bnb",
          chartsColor: "#f17171",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#f17171"],
          },
          series: [
            {
              name: "Binance",
              data: [30, 58, 29, 89, 12, 36, 9, 54],
            },
          ],
        },
        {
          id: 5,
          img: require("@/assets/images/svg/crypto-icons/dash.svg"),
          label: "Dash",
          price: "$9,458,153",
          change: "+12.07%",
          changeClass: "success",
          coinName: "dash",
          chartsColor: "#0ab39c",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#0ab39c"],
          },
          series: [
            {
              name: "Dash",
              data: [24, 68, 39, 86, 29, 42, 11, 58],
            },
          ],
        },
        {
          id: 6,
          img: require("@/assets/images/svg/crypto-icons/usdt.svg"),
          label: "Tether",
          price: "$5,201,458",
          change: "+14.99%",
          changeClass: "success",
          coinName: "usdt",
          chartsColor: "#0ab39c",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#0ab39c"],
          },
          series: [
            {
              name: "Dash",
              data: [13, 76, 12, 85, 25, 60, 9, 54],
            },
          ],
        },
        {
          id: 7,
          img: require("@/assets/images/svg/crypto-icons/neo.svg"),
          label: "NEO",
          price: "$6,147,957",
          change: "-05.07%",
          changeClass: "danger",
          coinName: "neo",
          chartsColor: "#0ab39c",
          chartOptions: {
            chart: {
              width: "100%",
              height: 46,
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
            colors: ["#0ab39c"],
          },
          series: [
            {
              name: "Neo",
              data: [9, 66, 41, 89, 12, 36, 25, 54],
            },
          ],
        },
      ],
      page: 1,
      perPage: 6,
      pages: [],
      searchQuery: null,
      defaultOptions: { animationData: animationData },
      Autoplay
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.market);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.currency_name.toLowerCase().includes(search) ||
            data.quantity.toLowerCase().includes(search) ||
            data.price.toLowerCase().includes(search) ||
            data.value.toLowerCase().includes(search) ||
            data.returns.toLowerCase().includes(search) ||
            data.volume.includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    market() {
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
      let numberOfPages = Math.ceil(this.market.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(market) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;

      return market.slice(from, to);
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.market];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.market = sortedArray;
    },
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="My Wallet" pageTitle="Crypto" />
    <BRow>
      <BCol xxl="9">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex align-items-center">
              <div class="flex-grow-1">
                <h5 class="card-title mb-0">My Portfolio Statistics</h5>
              </div>
              <div class="toolbar d-flex align-items-start justify-content-center flex-wrap gap-2">
                <BButton type="button" variant="soft-primary" size="sm" class="timeline-btn" id="one_month">
                  1M
                </BButton>
                <BButton type="button" variant="soft-primary" size="sm" class="timeline-btn" id="six_months">
                  6M
                </BButton>
                <BButton type="button" variant="soft-primary" size="sm" class="timeline-btn" id="one_year">
                  1Y
                </BButton>
                <BButton type="button" variant="soft-primary" size="sm" class="timeline-btn active" id="all">
                  ALL
                </BButton>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <div>
              <apexchart class="apex-charts" dir="ltr" height="320" :series="series" :options="chartOptions">
              </apexchart>
            </div>
          </BCardBody>
        </BCard>

        <div class="d-flex align-items-center mb-3">
          <div class="flex-grow-1">
            <h5 class="mb-0">Watchlist</h5>
          </div>
          <div class="flexshrink-0">
            <BButton variant="primary" size="sm">
              <i class="ri-star-line align-bottom"></i> Add Watchlist
            </BButton>
          </div>
        </div>

        <swiper class="cryptoSlider" :slidesPerView="1" :loop="false" :spaceBetween="24" :modules="[Autoplay]"
          :autoplay="{ delay: 2500, disableOnInteraction: false, }"
          :breakpoints="{ 640: { slidesPerView: 2, }, 1024: { slidesPerView: 3, }, 1600: { slidesPerView: 4, }, }">
          <template v-for="(item, index) of cryptoSlider" :key="index">
            <swiper-slide>
              <BCard no-body>
                <BCardBody>
                  <div class="float-end">
                    <BDropdown variant="link" toggle-class="fs-18 arrow-none" menu-class="dropdown-menu-end"
                      :offset="{ alignmentAxis: -105, crossAxis: 0, mainAxis: 10 }">
                      <template #button-content><i class="mdi mdi-dots-horizontal"></i></template>
                      <BDropdownItem>View Details</BDropdownItem>
                      <BDropdownItem>Remove Watchlist</BDropdownItem>
                    </BDropdown>
                  </div>
                  <div class="d-flex align-items-center">
                    <img :src="item.img" class="bg-light rounded-circle p-1 avatar-xs img-fluid" alt />
                    <h6 class="ms-2 mb-0 fs-14">{{ item.label }}</h6>
                  </div>
                  <BRow class="align-items-end g-0">
                    <BCol cols="6">
                      <h5 class="mb-1 mt-4">{{ item.price }}</h5>
                      <p class="text-success fs-13 fw-medium mb-0">
                        {{ item.change }}
                        <span class="text-muted ms-2 fs-10 text-uppercase">({{ item.coinName }})</span>
                      </p>
                    </BCol>
                    <BCol cols="6">
                      <apexchart class="apex-charts" :options="item.chartOptions" height="50" dir="ltr"
                        :series="item.series.length > 0 ? item.series : []" :key="item.id"></apexchart>
                    </BCol>
                  </BRow>
                </BCardBody>
              </BCard>
            </swiper-slide>
          </template>
        </swiper>

        <BCard no-body id="marketList">
          <BCardHeader class="border-bottom-dashed d-flex align-items-center">
            <BCardTitle class="mb-0 flex-grow-1">Market Status</BCardTitle>
            <div class="flex-shrink-0">
              <b-btn-group class="btn-group">
                <BButton type="button" variant="primary" size="sm">
                  Today
                </BButton>
                <BButton type="button" variant="outline-primary" size="sm">
                  Overall
                </BButton>
              </b-btn-group>
            </div>
          </BCardHeader>
          <BCardBody>
            <div class="table-responsive table-card">
              <table class="table align-middle table-nowrap" id="customerTable">
                <thead class="table-light text-muted">
                  <tr>
                    <th class="sort" data-sort="currency_name" scope="col" @click="onSort('currency_name')">
                      Name
                    </th>
                    <th class="sort" data-sort="quantity_value" scope="col" @click="onSort('quantity')">
                      Quantity
                    </th>
                    <th class="sort" data-sort="avg_price" scope="col" @click="onSort('price')">
                      Avg. Price
                    </th>
                    <th class="sort" data-sort="current_value" scope="col" @click="onSort('value')">
                      Current Value
                    </th>
                    <th class="sort" data-sort="returns" scope="col" @click="onSort('returns')">
                      Returns
                    </th>
                    <th class="sort" data-sort="returns_per" scope="col" @click="onSort('volume')">
                      Returns %
                    </th>
                  </tr>
                </thead>
                <tbody class="list form-check-all">
                  <tr v-for="(data, index) of resultQuery" :key="index">
                    <td class="id" style="display: none">
                      <BLink href="javascript:void(0);" class="fw-medium link-primary">#VZ001</BLink>
                    </td>
                    <td>
                      <div class="d-flex align-items-center fw-medium">
                        <img :src="data.image" alt="" class="avatar-xxs me-2" />
                        <BLink href="javascript:void(0)" class="currency_name">{{
                          data.currency_name
                        }}</BLink>
                      </div>
                    </td>
                    <td class="quantity_value">{{ data.quantity }}</td>
                    <td class="avg_price">{{ data.price }}</td>
                    <td class="current_value">{{ data.value }}</td>
                    <td class="returns">{{ data.returns }}</td>
                    <td class="returns_per">
                      <h6 class="fs-13 mb-0" :class="{
                        'text-danger': data.volume > 1,
                        'text-success': data.volume < 1,
                      }">
                        <i
                          :class="{ 'mdi mdi-trending-up align-middle me-1': data.volume < 1, 'mdi mdi-trending-down align-middle me-1': data.volume > 1 }"></i>{{
                            data.volume }}%
                      </h6>
                    </td>
                  </tr>
                </tbody>
              </table>
              <div class="noresult" v-if="resultQuery.length < 1">
                <div class="text-center">
                  <lottie class="avatar-xl" colors="primary:#121331,secondary:#08a88a" :options="defaultOptions"
                    :height="75" :width="75" />
                  <h5 class="mt-2">Sorry! No Result Found</h5>
                  <p class="text-muted mb-0">
                    We've searched more than 150+ Currencies We did not find any
                    Currencies for you search.
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
      </BCol>

      <BCol xxl="3">
        <BCard no-body>
          <BCardBody class="bg-primary-subtle">
            <div class="d-flex">
              <div class="flex-grow-1">
                <h5 class="fs-13 mb-3">My Portfolio</h5>
                <h2>$61,91,967<small class="text-muted fs-14">.29</small></h2>
                <p class="text-muted mb-0">
                  $25,10,974
                  <BBadge tag="small" variant="success-subtle" class="bg-success-subtle text-success"><i
                      class="ri-arrow-right-up-line fs-13 align-bottom"></i>4.37%</BBadge>
                </p>
              </div>
              <div class="flex-shrink-0">
                <i class="mdi mdi-wallet-outline text-primary h1"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h5 class="fs-13 mb-3">Today's Profit</h5>
                <h2>$2,74,365<small class="text-muted fs-14">.84</small></h2>
                <p class="text-muted mb-0">
                  $9,10,564
                  <BBadge tag="small" variant="success-subtle" class="bg-success-subtle text-success"><i
                      class="ri-arrow-right-up-line fs-13 align-bottom"></i>1.25%</BBadge>
                </p>
              </div>
              <div class="flex-shrink-0">
                <i class="ri-hand-coin-line text-primary h1"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h5 class="fs-13 mb-3">Overall Profit</h5>
                <h2>$32,67,120<small class="text-muted fs-14">.42</small></h2>
                <p class="text-muted mb-0">
                  $18,22,730
                  <BBadge tag="small" variant="success-subtle" class="bg-success-subtle text-success"><i
                      class="ri-arrow-right-up-line fs-13 align-bottom"></i>8.34%</BBadge>
                </p>
              </div>
              <div class="flex-shrink-0">
                <i class="ri-line-chart-line text-primary h1"></i>
              </div>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">Recent Transaction</h5>
          </BCardHeader>
          <BCardBody>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0">
                <img src="@/assets/images/svg/crypto-icons/btc.svg" alt="" class="avatar-xxs" />
              </div>
              <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Bitcoin (BTC)</h6>
                <p class="text-muted mb-0">Today</p>
              </div>
              <div>
                <h6 class="text-danger mb-0">- $422.89</h6>
              </div>
            </div>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0">
                <img src="@/assets/images/svg/crypto-icons/ltc.svg" alt="" class="avatar-xxs" />
              </div>
              <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Litecoin (LTC)</h6>
                <p class="text-muted mb-0">Yesterday</p>
              </div>
              <div>
                <h6 class="text-success mb-0">+ $784.20</h6>
              </div>
            </div>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0">
                <img src="@/assets/images/svg/crypto-icons/xmr.svg" alt="" class="avatar-xxs" />
              </div>
              <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Monero (XMR)</h6>
                <p class="text-muted mb-0">01 Jan, 2022</p>
              </div>
              <div>
                <h6 class="text-danger mb-0">- $356.74</h6>
              </div>
            </div>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0">
                <img src="@/assets/images/svg/crypto-icons/fil.svg" alt="" class="avatar-xxs" />
              </div>
              <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Filecoin (FIL)</h6>
                <p class="text-muted mb-0">30 Dec, 2021</p>
              </div>
              <div>
                <h6 class="text-success mb-0">+ $1,247.00</h6>
              </div>
            </div>
            <div class="d-flex mb-3">
              <div class="flex-shrink-0">
                <img src="@/assets/images/svg/crypto-icons/dot.svg" alt="" class="avatar-xxs" />
              </div>
              <div class="flex-grow-1 ms-3">
                <h6 class="mb-1">Polkadot (DOT)</h6>
                <p class="text-muted mb-0">27 Dec, 2021</p>
              </div>
              <div>
                <h6 class="text-success btn mb-0">+ $7,365.80</h6>
              </div>
            </div>
            <div>
              <router-link to="/crypto/transactions" class="btn btn-soft-primary w-100">View All Transactions
                <i class="ri-arrow-right-line align-bottom"></i>
              </router-link>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
