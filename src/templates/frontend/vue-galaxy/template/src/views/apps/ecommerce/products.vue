<script>
import Slider from "@vueform/slider";
import Multiselect from "@vueform/multiselect";
import Swal from "sweetalert2";
import Layout from "@/layouts/main.vue";
import "@vueform/multiselect/themes/default.css";
import PageHeader from "@/components/page-header";
import axios from 'axios';
import animationData from "@/components/widgets/msoeawqm.json";
import Lottie from "@/components/widgets/lottie.vue";

export default {
  data() {
    return {
      searchQuery: null,
      defaultOptions: {
        animationData: animationData
      },
      sliderCustomzie: [1000, 3000],
      productsData: [],
      pages: [],
      page: 1,
      perPage: 10,
      value: ["Watches", "Headset"],
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
            data.name.toLowerCase().includes(search) ||
            data.category.toLowerCase().includes(search) ||
            data.stock.toString().toLowerCase().includes(search) ||
            data.price.toString().toLowerCase().includes(search) ||
            data.orders.toString().toLowerCase().includes(search) ||
            data.rating.toString().toLowerCase().includes(search) ||
            data.publishedDate[0].toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    productsData(newValue) {
      this.setPages(newValue);
    },
    resultQuery() {
      if (this.searchQuery) this.setPages(this.displayedPosts);
      else this.setPages(this.productsData);
    },
  },
  created() {
    this.setPages(this.productsData);

  },
  filters: {
    trimWords(value) {
      return value.split(" ").splice(0, 20).join(" ") + "...";
    },
  },
  beforeMount() {
    axios.get('https://api-node.themesbrand.website/apps/product').then((data) => {
      this.productsData = [];
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"
      ];
      data.data.data.forEach(row => {
        var dd = new Date(row.publishedDate);
        row.publishedDate = dd.getDate() + " " + monthNames[dd.getMonth()] + ", " + dd.getFullYear();
        var hours = dd.getHours();
        var minutes = dd.getMinutes();
        var ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        hours = hours < 10 ? '0' + hours : hours;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        row.publishedtime = strTime;
        row.image_src = 'https://api-node.themesbrand.website/images/products/' + row.image;
        // row.image_src = `@/assets/images/products/img-8.png`;
        this.productsData.push(row);
      });
    }).catch((er) => {
      console.log(er);
    });

  },

  methods: {
    deleteMultiple() {
      let ids_array = [];
      var items = document.getElementsByName("chk_child");
      items.forEach(function (ele) {
        if (ele.checked == true) {
          var trNode = ele.parentNode.parentNode;
          var id = trNode.querySelector(".id a").innerHTML;
          ids_array.push(id);
        }
      });
      if (typeof ids_array !== "undefined" && ids_array.length > 0) {
        if (confirm("Are you sure you want to delete this?")) {
          var cusList = this.productsData;
          ids_array.forEach(function (id) {
            cusList = cusList.filter(function (orders) {
              return orders._id != id;
            });
          });
          this.productsData = cusList;
          document.getElementById("checkAll").checked = false;
          var itemss = document.getElementsByName("chk_child");
          itemss.forEach(function (ele) {
            if (ele.checked == true) {
              ele.checked = false;
              ele.closest("tr").classList.remove("table-active");
              document.getElementById('selection-element').style.display = 'none';
            }
          });
        } else {
          return false;
        }
      } else {
        Swal.fire({
          title: "Please select at least one checkbox",
          confirmButtonClass: "btn btn-info",
          buttonsStyling: false,
          showCloseButton: true,
        });
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
    setPages(data) {
      let numberOfPages = Math.ceil(data.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    deletedata(event) {
      Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        cancelButtonColor: "#f46a6a",
        confirmButtonColor: "#34c38f",
        confirmButtonText: "Yes, delete it!",
      }).then((result) => {
        if (result.value) {
          this.productsData.splice(this.productsData.indexOf(event), 1);
          axios.delete(`https://api-node.themesbrand.website/apps/product/${event._id}`)
            .then(() => {

            }).catch((er) => {
              console.log(er);
            });
          Swal.fire("Deleted!", "Your file has been deleted.", "success");
        }
      });

    },
    paginate(productsData) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return productsData.slice(from, to);
    },
  },
  mounted() {
    var total = 0;
    var checkchild = document.querySelectorAll('.form-check-all input[type="checkbox"]');
    checkchild.forEach(function (checkbox) {
      checkbox.onclick = function () {
        total = 0;
        checkchild.forEach(function (box) {
          if (box.checked == true) {
            total++;
          }
        });
        if (checkbox.checked == true) {
          checkbox.closest("tr").classList.add("table-active");
          document.getElementById('selection-element').style.display = 'block';
          document.getElementById('select-content').innerHTML = total;
        } else {
          if (total <= 0) {
            document.getElementById('selection-element').style.display = 'none';
          }
          checkbox.closest("tr").classList.remove("table-active");
          document.getElementById('select-content').innerHTML = total;
        }
      };
    });
    var checkAll = document.getElementById("checkAll");
    if (checkAll) {
      checkAll.onclick = function () {
        var checkboxes = document.querySelectorAll(
          '.form-check-all input[type="checkbox"]'
        );
        if (checkAll.checked == true) {
          checkboxes.forEach(function (checkbox) {
            checkbox.checked = true;
            document.getElementById('selection-element').style.display = 'block';
            document.getElementById('select-content').innerHTML = checkboxes.length;
            checkbox.closest("tr").classList.add("table-active");
          });
        } else {
          checkboxes.forEach(function (checkbox) {
            checkbox.checked = false;
            document.getElementById('selection-element').style.display = 'none';
            checkbox.closest("tr").classList.remove("table-active");
          });
        }
      };
    }
  },

  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Slider,
    Multiselect,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Products" pageTitle="Ecommerce" />
    <BRow>
      <BCol xl="3" lg="4">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex mb-3">
              <div class="flex-grow-1">
                <h5 class="fs-16">Filters</h5>
              </div>
              <div class="flex-shrink-0">
                <BLink href="#" class="text-decoration-underline">Clear All</BLink>
              </div>
            </div>

            <div class="filter-choices-input">
              <Multiselect v-model="value" mode="tags" :close-on-select="true" :searchable="true" :create-option="true"
                :options="[
                  { value: 'Watches', label: 'Watches' },
                  { value: 'Headset', label: 'Headset' },
                  { value: 'Sweatshirt', label: 'Sweatshirt' },
                  { value: '20% Off', label: '20% Off' },
                  { value: '4 Star', label: '4 Star' },
                ]" />
            </div>
          </BCardHeader>

          <div class="accordion accordion-flush">
            <BCardBody class="border-bottom">
              <div>
                <p class="text-muted text-uppercase fs-12 fw-medium mb-2">
                  Products
                </p>
                <ul class="list-unstyled mb-0 filter-list">
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Grocery</h5>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Fashion</h5>
                      </div>
                      <div class="flex-shrink-0 ms-2">
                        <BBadge class="bg-light text-muted">5</BBadge>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Watches</h5>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Electronics</h5>
                      </div>
                      <div class="flex-shrink-0 ms-2">
                        <BBadge class="bg-light text-muted">5</BBadge>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Furniture</h5>
                      </div>
                      <div class="flex-shrink-0 ms-2">
                        <BBadge class="bg-light text-muted">6</BBadge>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Automotive Accessories</h5>
                      </div>
                    </BLink>
                  </li>
                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Appliances</h5>
                      </div>
                      <div class="flex-shrink-0 ms-2">
                        <BBadge class="bg-light text-muted">7</BBadge>
                      </div>
                    </BLink>
                  </li>

                  <li>
                    <BLink href="#" class="d-flex py-1 align-items-center">
                      <div class="flex-grow-1">
                        <h5 class="fs-13 mb-0 listname">Kids</h5>
                      </div>
                    </BLink>
                  </li>
                </ul>
              </div>
            </BCardBody>

            <BCardBody class="border-bottom">
              <p class="text-muted text-uppercase fs-12 fw-medium mb-5">
                Price
              </p>

              <div id="product-price-range"></div>
              <Slider v-model="sliderCustomzie" :min="0" :max="5000"  />
            </BCardBody>

            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingBrands">
                <button class="accordion-button bg-transparent shadow-none" type="button" v-b-toggle.flush-collapseBrands>
                  <span class="text-muted text-uppercase fs-12 fw-medium">Brands</span>
                  <BBadge variant="success" class="rounded-pill align-middle ms-1">2</BBadge>
                </button>
              </h2>

              <BCollapse id="flush-collapseBrands" visible>
                <div class="accordion-body text-body pt-0">
                  <div class="search-box search-box-sm">
                    <input type="text" class="form-control bg-light border-0" placeholder="Search Brands..." />
                    <i class="ri-search-line search-icon"></i>
                  </div>
                  <div class="d-flex flex-column gap-2 mt-3">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productBrandRadio5" checked />
                      <label class="form-check-label" for="productBrandRadio5">Boat</label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productBrandRadio4" />
                      <label class="form-check-label" for="productBrandRadio4">OnePlus</label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productBrandRadio3" />
                      <label class="form-check-label" for="productBrandRadio3">Realme</label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productBrandRadio2" />
                      <label class="form-check-label" for="productBrandRadio2">Sony</label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productBrandRadio1" checked />
                      <label class="form-check-label" for="productBrandRadio1">JBL</label>
                    </div>

                    <div>
                      <BButton type="button" variant="link" class="text-decoration-none text-uppercase fw-medium p-0">
                        1,235 More
                      </BButton>
                    </div>
                  </div>
                </div>
              </BCollapse>
            </div>

            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingDiscount">
                <button class="accordion-button bg-transparent shadow-none collapsed" type="button"
                  v-b-toggle.flush-collapseDiscount>
                  <span class="text-muted text-uppercase fs-12 fw-medium">Discount</span>
                  <BBadge variant="success" class="rounded-pill align-middle ms-1">1</BBadge>
                </button>
              </h2>
              <BCollapse id="flush-collapseDiscount">
                <div class="accordion-body text-body pt-1">
                  <div class="d-flex flex-column gap-2">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio6" />
                      <label class="form-check-label" for="productdiscountRadio6">
                        50% or more
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio5" />
                      <label class="form-check-label" for="productdiscountRadio5">
                        40% or more
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio4" />
                      <label class="form-check-label" for="productdiscountRadio4">
                        30% or more
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio3" checked />
                      <label class="form-check-label" for="productdiscountRadio3">
                        20% or more
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio2" />
                      <label class="form-check-label" for="productdiscountRadio2">
                        10% or more
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productdiscountRadio1" />
                      <label class="form-check-label" for="productdiscountRadio1">
                        Less than 10%
                      </label>
                    </div>
                  </div>
                </div>
              </BCollapse>
            </div>

            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingRating">
                <button class="accordion-button bg-transparent shadow-none collapsed" type="button"
                  v-b-toggle.flush-collapseRating>
                  <span class="text-muted text-uppercase fs-12 fw-medium">Rating</span>
                  <BBadge variant="success" class="rounded-pill align-middle ms-1">1</BBadge>
                </button>
              </h2>

              <BCollapse id="flush-collapseRating">
                <div class="accordion-body text-body">
                  <div class="d-flex flex-column gap-2">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productratingRadio4" checked />
                      <label class="form-check-label" for="productratingRadio4">
                        <span class="text-muted">
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star"></i>
                        </span>
                        4 & Above
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productratingRadio3" />
                      <label class="form-check-label" for="productratingRadio3">
                        <span class="text-muted">
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                        </span>
                        3 & Above
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productratingRadio2" />
                      <label class="form-check-label" for="productratingRadio2">
                        <span class="text-muted">
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                        </span>
                        2 & Above
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="productratingRadio1" />
                      <label class="form-check-label" for="productratingRadio1">
                        <span class="text-muted">
                          <i class="mdi mdi-star text-warning"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                          <i class="mdi mdi-star"></i>
                        </span>
                        1
                      </label>
                    </div>
                  </div>
                </div>
              </BCollapse>
            </div>
          </div>
        </BCard>
      </BCol>

      <BCol xl="9" lg="8">
        <div>
          <BCard no-body>
            <BCardHeader class="border-0">
              <BRow class="g-4">
                <BCol sm="auto">
                  <div>
                    <router-link to="/ecommerce/add-product" class="btn btn-primary"><i
                        class="ri-add-line align-bottom me-1"></i> Add
                      Product</router-link>
                  </div>
                </BCol>
                <BCol sm>
                  <div class="d-flex justify-content-sm-end">
                    <div class="search-box ms-2">
                      <input type="text" class="form-control" v-model="searchQuery" placeholder="Search Products..." />
                      <i class="ri-search-line search-icon"></i>
                    </div>
                  </div>
                </BCol>
              </BRow>
            </BCardHeader>

            <BCardHeader>
              <BRow class="align-items-center">
                <BCol>
                  <ul class="nav nav-tabs-custom card-header-tabs border-bottom-0" role="tablist">
                    <li class="nav-item">
                      <BLink class="nav-link active fw-semibold" data-bs-toggle="tab" href="#productnav-all" role="tab">
                        All
                        <BBadge variant="danger-subtle"
                          class="bg-danger-subtle text-danger align-middle rounded-pill ms-1">12</BBadge>
                      </BLink>
                    </li>
                  </ul>
                </BCol>
                <div class="col-auto">
                  <div id="selection-element">
                    <div class="my-n1 d-flex align-items-center text-muted">
                      Select
                      <div id="select-content" class="text-body fw-semibold px-1"></div>
                      Result
                      <BButton type="button" variant="link" class="link-danger p-0 ms-3" @click="deleteMultiple">
                        Remove
                      </BButton>
                    </div>
                  </div>
                </div>
              </BRow>
            </BCardHeader>
            <BCardBody>
              <div class="tab-content text-muted">
                <div class="tab-pane active" id="productnav-all" role="tabpanel">
                  <div id="table-product-list-all" class="table-card gridjs-border-none table-responsive">
                    <table class="table align-middle table-nowrap mb-0" id="customerTable">
                      <thead class="table-light">
                        <tr class="text-muted">
                          <th scope="col" style="width: 50px">
                            <input class="form-check-input" type="checkbox" id="checkAll" value="option" />
                          </th>
                          <th class="sort" data-sort="product" @click="onSort('id')">Product</th>
                          <th class="sort" data-sort="stock" @click="onSort('stock')">Stock</th>
                          <th class="sort" data-sort="price" @click="onSort('price')">Price</th>
                          <th class="sort" data-sort="orders" @click="onSort('orders')">Orders</th>
                          <th class="sort" data-sort="rating" @click="onSort('rating')">Rating</th>
                          <th class="sort" data-sort="published" @click="onSort('published')">Published</th>
                          <th scope="col">Action</th>
                        </tr>
                      </thead>
                      <tbody class="list form-check-all">
                        <tr class="gridjs-tr" v-for="(data, index) of resultQuery" :key="index">
                          <td data-column-id="productListAllCheckbox" class="gridjs-td">
                            <input type="checkbox" name="chk_child" class="form-check-input" />
                          </td>
                          <td class="id" hidden>
                            <BLink href="">{{ data._id }}</BLink>
                          </td>
                          <td data-column-id="product" class="gridjs-td">
                            <span>
                              <div class="d-flex align-items-center">
                                <div class="flex-shrink-0 me-3">
                                  <div class="avatar-sm bg-light rounded p-1">
                                    <img :src="data.image_src" alt="" class="img-fluid d-block" />
                                  </div>
                                </div>
                                <div class="flex-grow-1">
                                  <h5 class="fs-14 mb-1">
                                    <router-link to="/ecommerce/product-details" class="text-body">{{ data.name }}
                                    </router-link>
                                  </h5>
                                  <p class="text-muted mb-0">
                                    Category :
                                    <span class="fw-medium">{{
                                      data.category
                                    }}</span>
                                  </p>
                                </div>
                              </div>
                            </span>
                          </td>
                          <td data-column-id="stock" class="gridjs-td">
                            {{ data.stock }}
                          </td>
                          <td data-column-id="price" class="gridjs-td">
                            $ {{ data.price }}.00
                          </td>
                          <td data-column-id="orders" class="gridjs-td">
                            {{ data.orders }}
                          </td>
                          <td data-column-id="rating" class="gridjs-td">
                            <span>
                              <BBadge class="bg-light text-body fs-12 fw-medium"><i
                                  class="mdi mdi-star text-warning me-1"></i>{{ data.rating }}</BBadge>
                            </span>
                          </td>
                          <td data-column-id="published" class="gridjs-td">
                            <span>{{ data.publishedDate
                            }}<small class="text-muted ms-1">{{
  data.publishedtime
}}</small></span>
                          </td>
                          <td data-column-id="action" class="gridjs-td">
                            <span>
                              <div class="dropdown">
                                <BDropdown variant="link" toggle-class="btn btn-soft-secondary btn-sm dropdown arrow-none"
                                  menu-class="dropdown-menu-end"
                                  :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                  <template #button-content> <i class="ri-more-fill"></i>
                                  </template>
                                  <BDropdownItem to="/ecommerce/product-details"><i
                                        class="ri-eye-fill align-bottom me-2 text-muted"></i>
                                      View</BDropdownItem>
                                  <BDropdownItem to="/ecommerce/add-product"> <i
                                        class="ri-pencil-fill align-bottom me-2 text-muted"></i>
                                      Edit
                                  </BDropdownItem >
                                  <li class="dropdown-divider"></li>
                                  <BDropdownItem @click="deletedata(data)"><i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
                                    Delete
                                  </BDropdownItem>
                                </BDropdown>
                              </div>
                            </span>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <div class="d-flex justify-content-end m-3">
                      <div class="pagination-wrap hstack gap-2">
                        <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--">
                          Previous
                        </BLink>
                        <ul class="pagination listjs-pagination mb-0">
                          <li v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber"
                            :class="{ active: pageNumber == page, disabled: pageNumber == '...', }">
                            <BLink class="page" href="#">{{ pageNumber }}</BLink>
                          </li>
                        </ul>
                        <BLink class="page-item pagination-next" href="#" :disabled="page >= pages.length"
                          @click="page++">
                          Next
                        </BLink>
                      </div>
                    </div>
                  </div>
                </div>

                 <div class="tab-pane" id="productnav-published" role="tabpanel">
                  <div id="table-product-list-published" class="table-card gridjs-border-none"></div>
                </div>

                <div class="tab-pane" id="productnav-draft" role="tabpanel">
                  <div class="py-4 text-center">
                    <div>
                      <lottie class="avatar-xl" colors="primary:#121331,secondary:#08a88a" :options="defaultOptions"
                        :height="75" :width="75" />
                    </div>

                    <div class="mt-4">
                      <h5>Sorry! No Result Found</h5>
                    </div>
                  </div>
                </div>
              </div>
            </BCardBody>
          </BCard>
        </div>
      </BCol>
    </BRow>
  </Layout>
</template>
<style lang="scss">
@import '@vueform/slider/themes/default.css';
</style>