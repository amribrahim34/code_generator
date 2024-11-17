<script>
import { CountTo } from "vue3-count-to";
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { buySellList } from "@/common/data";

export default {
  components: {
    Layout,
    PageHeader,
    CountTo,
  },
  data() {
    return {
      posts: buySellList,
      page: 1,
      perPage: 8,
      pages: [],
      searchQuery: null,
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.posts);
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
    posts() {
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
      let numberOfPages = Math.ceil(this.posts.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(posts) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return posts.slice(from, to);
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.posts];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.posts = sortedArray;
    },
  },
  setup() {
    const options = {
      series: [
        {
          data: [
            {
              x: new Date(1538778600000),
              y: [6629.81, 6650.5, 6623.04, 6633.33],
            },
            {
              x: new Date(1538780400000),
              y: [6632.01, 6643.59, 6620, 6630.11],
            },
            {
              x: new Date(1538782200000),
              y: [6630.71, 6648.95, 6623.34, 6635.65],
            },
            {
              x: new Date(1538784000000),
              y: [6635.65, 6651, 6629.67, 6638.24],
            },
            {
              x: new Date(1538785800000),
              y: [6638.24, 6640, 6620, 6624.47],
            },
            {
              x: new Date(1538787600000),
              y: [6624.53, 6636.03, 6621.68, 6624.31],
            },
            {
              x: new Date(1538789400000),
              y: [6624.61, 6632.2, 6617, 6626.02],
            },
            {
              x: new Date(1538791200000),
              y: [6627, 6627.62, 6584.22, 6603.02],
            },
            {
              x: new Date(1538793000000),
              y: [6605, 6608.03, 6598.95, 6604.01],
            },
            {
              x: new Date(1538794800000),
              y: [6604.5, 6614.4, 6602.26, 6608.02],
            },
            {
              x: new Date(1538796600000),
              y: [6608.02, 6610.68, 6601.99, 6608.91],
            },
            {
              x: new Date(1538798400000),
              y: [6608.91, 6618.99, 6608.01, 6612],
            },
            {
              x: new Date(1538800200000),
              y: [6612, 6615.13, 6605.09, 6612],
            },
            {
              x: new Date(1538802000000),
              y: [6612, 6624.12, 6608.43, 6622.95],
            },
            {
              x: new Date(1538803800000),
              y: [6623.91, 6623.91, 6615, 6615.67],
            },
            {
              x: new Date(1538805600000),
              y: [6618.69, 6618.74, 6610, 6610.4],
            },
            {
              x: new Date(1538807400000),
              y: [6611, 6622.78, 6610.4, 6614.9],
            },
            {
              x: new Date(1538809200000),
              y: [6614.9, 6626.2, 6613.33, 6623.45],
            },
            {
              x: new Date(1538811000000),
              y: [6623.48, 6627, 6618.38, 6620.35],
            },
            {
              x: new Date(1538812800000),
              y: [6619.43, 6620.35, 6610.05, 6615.53],
            },
            {
              x: new Date(1538814600000),
              y: [6615.53, 6617.93, 6610, 6615.19],
            },
            {
              x: new Date(1538816400000),
              y: [6615.19, 6621.6, 6608.2, 6620],
            },
            {
              x: new Date(1538818200000),
              y: [6619.54, 6625.17, 6614.15, 6620],
            },
            {
              x: new Date(1538820000000),
              y: [6620.33, 6634.15, 6617.24, 6624.61],
            },
            {
              x: new Date(1538821800000),
              y: [6625.95, 6626, 6611.66, 6617.58],
            },
            {
              x: new Date(1538823600000),
              y: [6619, 6625.97, 6595.27, 6598.86],
            },
            {
              x: new Date(1538825400000),
              y: [6598.86, 6598.88, 6570, 6587.16],
            },
            {
              x: new Date(1538827200000),
              y: [6588.86, 6600, 6580, 6593.4],
            },
            {
              x: new Date(1538829000000),
              y: [6593.99, 6598.89, 6585, 6587.81],
            },
            {
              x: new Date(1538830800000),
              y: [6587.81, 6592.73, 6567.14, 6578],
            },
            {
              x: new Date(1538832600000),
              y: [6578.35, 6581.72, 6567.39, 6579],
            },
            {
              x: new Date(1538834400000),
              y: [6579.38, 6580.92, 6566.77, 6575.96],
            },
            {
              x: new Date(1538836200000),
              y: [6575.96, 6589, 6571.77, 6588.92],
            },
            {
              x: new Date(1538838000000),
              y: [6588.92, 6594, 6577.55, 6589.22],
            },
            {
              x: new Date(1538839800000),
              y: [6589.3, 6598.89, 6589.1, 6596.08],
            },
            {
              x: new Date(1538841600000),
              y: [6597.5, 6600, 6588.39, 6596.25],
            },
            {
              x: new Date(1538843400000),
              y: [6598.03, 6600, 6588.73, 6595.97],
            },
            {
              x: new Date(1538845200000),
              y: [6595.97, 6602.01, 6588.17, 6602],
            },
            {
              x: new Date(1538847000000),
              y: [6602, 6607, 6596.51, 6599.95],
            },
            {
              x: new Date(1538848800000),
              y: [6600.63, 6601.21, 6590.39, 6591.02],
            },
            {
              x: new Date(1538850600000),
              y: [6591.02, 6603.08, 6591, 6591],
            },
            {
              x: new Date(1538852400000),
              y: [6591, 6601.32, 6585, 6592],
            },
            {
              x: new Date(1538854200000),
              y: [6593.13, 6596.01, 6590, 6593.34],
            },
            {
              x: new Date(1538856000000),
              y: [6593.34, 6604.76, 6582.63, 6593.86],
            },
            {
              x: new Date(1538857800000),
              y: [6593.86, 6604.28, 6586.57, 6600.01],
            },
            {
              x: new Date(1538859600000),
              y: [6601.81, 6603.21, 6592.78, 6596.25],
            },
            {
              x: new Date(1538861400000),
              y: [6596.25, 6604.2, 6590, 6602.99],
            },
            {
              x: new Date(1538863200000),
              y: [6602.99, 6606, 6584.99, 6587.81],
            },
            {
              x: new Date(1538865000000),
              y: [6587.81, 6595, 6583.27, 6591.96],
            },
            {
              x: new Date(1538866800000),
              y: [6591.97, 6596.07, 6585, 6588.39],
            },
            {
              x: new Date(1538868600000),
              y: [6587.6, 6598.21, 6587.6, 6594.27],
            },
            {
              x: new Date(1538870400000),
              y: [6596.44, 6601, 6590, 6596.55],
            },
            {
              x: new Date(1538872200000),
              y: [6598.91, 6605, 6596.61, 6600.02],
            },
            {
              x: new Date(1538874000000),
              y: [6600.55, 6605, 6589.14, 6593.01],
            },
            {
              x: new Date(1538875800000),
              y: [6593.15, 6605, 6592, 6603.06],
            },
            {
              x: new Date(1538877600000),
              y: [6603.07, 6604.5, 6599.09, 6603.89],
            },
            {
              x: new Date(1538879400000),
              y: [6604.44, 6604.44, 6600, 6603.5],
            },
            {
              x: new Date(1538881200000),
              y: [6603.5, 6603.99, 6597.5, 6603.86],
            },
            {
              x: new Date(1538883000000),
              y: [6603.85, 6605, 6600, 6604.07],
            },
            {
              x: new Date(1538884800000),
              y: [6604.98, 6606, 6604.07, 6606],
            },
          ],
        },
      ],
      chartOptions: {
        chart: {
          type: "candlestick",
          height: 360,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          candlestick: {
            colors: {
              upward: "#0AB39C",
              downward: "#F06548",
            },
          },
        },
        xaxis: {
          type: "datetime",
        },
        yaxis: {
          tooltip: {
            enabled: true,
          },
          labels: {
            formatter: function (value) {
              return "$" + value;
            },
          },
        },
        tooltip: {
          shared: true,
          y: [
            {
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
    };
    const data = [
      {
        image: require("@/assets/images/svg/crypto-icons/btc.svg"),
        currency_name: "Bitcoin (BTC)",
        price: "$47,071.60",
        pairs: "BTC/USD",
        high: "$28,722.76",
        low: "$68,789.63",
        market: "$888,411,910",
        volume: 1.5,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/eth.svg"),
        currency_name: "Ethereum (ETH)",
        price: "$3,813.14",
        pairs: "ETH/USDT",
        high: "$4,036.24",
        low: "$3,588.14",
        market: "$314,520,675",
        volume: 0.42,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/ltc.svg"),
        currency_name: "Litecoin (LTC)",
        price: "$149.65",
        pairs: "LTC/USDT",
        high: "$412.96",
        low: "$104.33",
        market: "$314,520,675",
        volume: 0.89,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/fil.svg"),
        currency_name: "Filecoin (FIL)",
        price: "$35.21",
        pairs: "FIL/USD",
        high: "$36.41",
        low: "$35.03",
        market: "$374,618,945.51",
        volume: 0.84,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/eth.svg"),
        currency_name: "Ethereum (ETH)",
        price: "$3,813.14",
        pairs: "ETH/USDT",
        high: "$4,036.24",
        low: "$3,588.14",
        market: "$314,520,675",
        volume: 0.42,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/btc.svg"),
        currency_name: "Bitcoin (BTC)",
        price: "$47,071.60",
        pairs: "BTC/USD",
        high: "$28,722.76",
        low: "$68,789.63",
        market: "$888,411,910",
        volume: 1.5,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/aave.svg"),
        currency_name: "Aave (AAVE)",
        price: "$275.47",
        pairs: "AAVE/USDT",
        high: "$277.11",
        low: "$255.01",
        market: "$156,209,195.18",
        volume: 8.2,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/dot.svg"),
        currency_name: "Polkadot (DOT)",
        price: "$28.88",
        pairs: "DOT/USD",
        high: "$30.56",
        low: "$28.66",
        market: "$880,387,980.14",
        volume: 1.03,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/ant.svg"),
        currency_name: "Aragon (ANT)",
        price: "$13.31",
        pairs: "ANT/USD",
        high: "$13.85",
        low: "$12.53",
        market: "$156,209,195.18",
        volume: 3.96,
      },
      {
        image: require("@/assets/images/svg/crypto-icons/ada.svg"),
        currency_name: "Cardano (ADA)",
        price: "$1.35",
        pairs: "ADA/USD",
        high: "$1.39",
        low: "$1.32",
        market: "$880,387,980.14",
        volume: 0.42,
      },
    ];
    return {
      options,
      data,
    };
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Buy & Sell" pageTitle="Crypto" />

    <BRow>
      <BCol xl="3" sm="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="text-muted mb-3">Total Buy</h6>
                <h2 class="mb-0">
                  $<count-to :startVal="0" :duration="5000" :endVal="243"></count-to><small
                    class="text-muted fs-13">.10k</small>
                </h2>
              </div>
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                  <i class="ri-shopping-bag-line"></i>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" sm="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="text-muted mb-3">Total Sell</h6>
                <h2 class="mb-0">
                  $<count-to :startVal="0" :duration="5000" :endVal="658"></count-to><small
                    class="text-muted fs-13">.00k</small>
                </h2>
              </div>
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                  <i class="ri-funds-line"></i>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" sm="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="text-muted mb-3">Today's Buy</h6>
                <h2 class="mb-0">
                  $<count-to :startVal="0" :duration="5000" :endVal="104"></count-to><small
                    class="text-muted fs-13">.85k</small>
                </h2>
              </div>
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                  <i class="ri-arrow-left-down-fill"></i>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3" sm="6">
        <BCard no-body class="card-animate">
          <BCardBody>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h6 class="text-muted mb-3">Today's Sell</h6>
                <h2 class="mb-0">
                  $<count-to :startVal="0" :duration="5000" :endVal="87"></count-to><small
                    class="text-muted fs-13">.35k</small>
                </h2>
              </div>
              <div class="flex-shrink-0 avatar-sm">
                <div class="avatar-title bg-primary-subtle text-primary fs-22 rounded">
                  <i class="ri-arrow-right-up-fill"></i>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol xxl="9">
        <BCard no-body class="card-height-100">
          <BCardHeader class="border-0 align-items-center d-flex">
            <BCardTitle class="mb-0 flex-grow-1">Market Graph</BCardTitle>
            <div class="hstack gap-1">
              <BButton type="button" variant="soft-secondary" size="sm">
                1H
              </BButton>
              <BButton type="button" variant="soft-secondary" size="sm">
                7D
              </BButton>
              <BButton type="button" variant="soft-secondary" size="sm">
                1M
              </BButton>
              <BButton type="button" variant="soft-secondary" size="sm">
                1Y
              </BButton>
              <BButton type="button" variant="soft-primary" size="sm">
                ALL
              </BButton>
            </div>
          </BCardHeader>
          <BCardBody class="p-0">
            <div
              class="bg-light-subtle border-top-dashed border border-start-0 border-end-0 border-bottom-dashed py-3 px-4">
              <BRow class="align-items-center">
                <BCol cols="6">
                  <div class="d-flex flex-wrap gap-4 align-items-center">
                    <div>
                      <h3 class="fs-19">
                        $46,959.<small class="fs-14 text-muted">00</small>
                      </h3>
                      <p class="text-muted text-uppercase fw-medium mb-0">
                        Bitcoin (BTC)
                        <BBadge variant="success-subtle" class="bg-success-subtle text-success"><i
                            class="ri-arrow-right-up-line align-bottom"></i>
                          2.15%</BBadge>
                      </p>
                    </div>
                  </div>
                </BCol>
                <BCol cols="6">
                  <div class="d-flex">
                    <div class="d-flex justify-content-end text-end flex-wrap gap-4 ms-auto">
                      <div class="pe-3">
                        <h6 class="mb-2 text-muted">High</h6>
                        <h5 class="text-success mb-0">$28,722.76</h5>
                      </div>
                      <div class="pe-3">
                        <h6 class="mb-2 text-muted">Low</h6>
                        <h5 class="text-danger mb-0">$68,789.63</h5>
                      </div>
                      <div>
                        <h6 class="mb-2 text-muted">Market Volume</h6>
                        <h5 class="text-primary mb-0">$888,411,910</h5>
                      </div>
                    </div>
                  </div>
                </BCol>
              </BRow>
            </div>
          </BCardBody>
          <BCardBody class="p-0 pb-3">
            <apexchart class="apex-charts" height="350" dir="ltr" :series="options.series"
              :options="options.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xxl="3">
        <BCard no-body class="card-height-100">
          <BCardBody class="p-0">
            <BTabs nav-class="nav-tabs-custom rounded  border-bottom-0 mx-n3 text-muted" style="overflow: hidden;" justified>
              <BTab title="Buy" class="nav-item ">
                <div class="p-3 bg-primary-subtle">
                  <div class="float-end ms-2">
                    <h6 class="text-primary mb-0">
                      USD Balance : <span class="text-body">$12,426.07</span>
                    </h6>
                  </div>
                  <h6 class="mb-0 text-primary">Buy Coin</h6>
                </div>
                <div class="p-3">
                  <BRow>
                    <BCol cols="6">
                      <div class="mb-3">
                        <label>Currency :</label>
                        <select class="form-select">
                          <option>BTC</option>
                          <option>ETH</option>
                          <option>LTC</option>
                        </select>
                      </div>
                    </BCol>
                    <BCol cols="6">
                      <div class="mb-3">
                        <label>Payment Method :</label>
                        <select class="form-select">
                          <option>Wallet Balance</option>
                          <option>Credit / Debit Card</option>
                          <option>PayPal</option>
                          <option>Payoneer</option>
                        </select>
                      </div>
                    </BCol>
                  </BRow>
                  <div>
                    <div class="input-group mb-3">
                      <label class="input-group-text">Amount</label>
                      <input type="text" class="form-control" placeholder="0" />
                    </div>

                    <div class="input-group mb-3">
                      <label class="input-group-text">Price</label>
                      <input type="text" class="form-control" placeholder="2.045585" />
                      <label class="input-group-text">$</label>
                    </div>

                    <div class="input-group mb-0">
                      <label class="input-group-text">Total</label>
                      <input type="text" class="form-control" placeholder="2700.16" />
                    </div>
                  </div>
                  <div class="mt-3 pt-2">
                    <div class="d-flex mb-2">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">
                          Transaction Fees<span class="text-muted ms-1 fs-11">(0.05%)</span>
                        </p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">$1.08</h6>
                      </div>
                    </div>
                    <div class="d-flex mb-2">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">
                          Minimum Received<span class="text-muted ms-1 fs-11">(2%)</span>
                        </p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">$7.85</h6>
                      </div>
                    </div>
                    <div class="d-flex">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">Estimated Rate</p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">1 BTC ~ $46982.70</h6>
                      </div>
                    </div>
                  </div>
                  <div class="mt-3 pt-2">
                    <BButton type="button" variant="soft-success" class="w-100">
                      Buy Coin
                    </BButton>
                  </div>
                </div>
              </BTab>
              <BTab title="sell" class="nav-item">
                <div class="p-3 bg-primary-subtle">
                  <div class="float-end ms-2">
                    <h6 class="text-primary mb-0">
                      USD Balance : <span class="text-body">$12,426.07</span>
                    </h6>
                  </div>
                  <h6 class="mb-0 text-danger">Sell Coin</h6>
                </div>
                <div class="p-3">
                  <BRow>
                    <BCol cols="6">
                      <div class="mb-3">
                        <label for="currencySelect">Currency :</label>
                        <select class="form-select" id="currencySelect">
                          <option value="BTC" selected>BTC</option>
                          <option value="ETH">ETH</option>
                          <option value="EUR">EUR</option>
                          <option value="JPY">JPY</option>
                          <option value="LTC">LTC</option>
                        </select>
                      </div>
                    </BCol>
                    <BCol cols="6">
                      <div class="mb-3">
                        <div class="mb-3">
                          <label for="paymentMethod">Payment Method :</label>
                          <select class="form-select" id="paymentMethod">
                            <option>Wallet Balance</option>
                            <option>Credit / Debit Card</option>
                            <option>PayPal</option>
                            <option>Payoneer</option>
                          </select>
                        </div>
                      </div>
                    </BCol>
                  </BRow>
                  <div>
                    <div class="input-group mb-3">
                      <label class="input-group-text">Amount</label>
                      <input type="text" class="form-control" placeholder="0" />
                    </div>
                    <div class="input-group mb-3">
                      <label class="input-group-text">Price</label>
                      <input type="text" class="form-control" placeholder="2.045585" />
                      <label class="input-group-text">$</label>
                    </div>
                    <div class="input-group mb-0">
                      <label class="input-group-text">Total</label>
                      <input type="text" class="form-control" placeholder="2700.16" />
                    </div>
                  </div>
                  <div class="mt-3 pt-2">
                    <div class="d-flex mb-2">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">
                          Transaction Fees<span class="text-muted ms-1 fs-11">(0.05%)</span>
                        </p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">$1.08</h6>
                      </div>
                    </div>
                    <div class="d-flex mb-2">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">
                          Minimum Received<span class="text-muted ms-1 fs-11">(2%)</span>
                        </p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">$7.85</h6>
                      </div>
                    </div>
                    <div class="d-flex">
                      <div class="flex-grow-1">
                        <p class="fs-13 mb-0">Estimated Rate</p>
                      </div>
                      <div class="flex-shrink-0">
                        <h6 class="mb-0">1 BTC ~ $46982.70</h6>
                      </div>
                    </div>
                  </div>
                  <div class="mt-3 pt-2">
                    <BButton type="button" variant="danger" class="w-100">
                      Sell Coin
                    </BButton>
                  </div>
                </div>
              </BTab>
            </BTabs>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BCard no-body>
      <BCardHeader class="border-bottom-dashed">
        <BRow class="align-items-center">
          <BCol cols="3">
            <h5 class="card-title mb-0">Markets</h5>
          </BCol>
          <div class="col-auto ms-auto">
            <div class="d-flex gap-2">
              <BButton variant="primary">
                <i class="ri-equalizer-line align-bottom me-1"></i> Filters
              </BButton>
            </div>
          </div>
        </BRow>
      </BCardHeader>
      <BCardBody class="p-0 border-bottom border-bottom-dashed">
        <div class="search-box">
          <input type="text" class="form-control search border-0 py-3" placeholder="Search to currency..." />
          <i class="ri-search-line search-icon"></i>
        </div>
      </BCardBody>
      <BCardBody>
        <div class="table-responsive table-card">
          <table class="table align-middle table-nowrap" id="customerTable">
            <thead class="table-light text-muted">
              <tr>
                <th class="sort" data-sort="currency_name" scope="col" @click="onSort('currency_name')">Currency</th>
                <th class="sort" data-sort="current_value" scope="col" @click="onSort('price')">Price</th>
                <th class="sort" data-sort="pairs" scope="col" @click="onSort('pairs')">Pairs</th>
                <th class="sort" data-sort="high" scope="col" @click="onSort('high')">24 High</th>
                <th class="sort" data-sort="low" scope="col" @click="onSort('low')">24 Low</th>
                <th class="sort" data-sort="market_cap" scope="col" @click="onSort('market')">Market Volume</th>
                <th class="sort" data-sort="valume" scope="col" @click="onSort('volume')">Volume %</th>
                <th scope="col">Action</th>
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
                    <BLink href="javascript:void(0);" class="currency_name">{{
                      data.currency_name
                    }}</BLink>
                  </div>
                </td>
                <td class="current_value">{{ data.price }}</td>
                <td class="pairs">{{ data.pairs }}</td>
                <td class="high">{{ data.high }}</td>
                <td class="low">{{ data.low }}</td>
                <td class="market_cap">{{ data.market }}</td>
                <td class="valume">
                  <h6 class="fs-13 mb-0" :class="{
                    'text-danger': data.volume > 1,
                    'text-success': data.volume < 1,
                  }">
                    <i class="mdi mdi-trending-up align-middle me-1"></i>{{ data.volume }}%
                  </h6>
                </td>
                <td>
                  <BButton variant="soft-primary" size="sm">Trade Now</BButton>
                </td>
              </tr>
            </tbody>
          </table>
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
