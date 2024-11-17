<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import Swal from "sweetalert2";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import axios from 'axios';
import animationData from "@/components/widgets/msoeawqm.json";
import animationData1 from "@/components/widgets/gsqxdxog.json";
import Lottie from "@/components/widgets/lottie.vue";

export default {
  data() {
    return {
      createModal: false,
      editOrderModal: false,
      page: 1,
      perPage: 8,
      pages: [],
      value: null,
      status: null,
      status1: null,
      statuscategory: 'All',
      value1: null,
      searchQuery: null,
      config: {
        wrap: true, // set wrap to true only when using 'input-group'
        altFormat: "M j, Y",
        altInput: true,
        dateFormat: "d M, Y",
        mode: "range",
      },
      timeConfig: {
        enableTime: false,
        dateFormat: "d M, Y",
      },
      date: null,
      date2: null,
      defaultOptions: {
        animationData: animationData
      },
      defaultOptions1: {
        animationData: animationData1
      },
      orders: [],
      isStatus: null,
      isPayment: null,

      //
      submitted: false,

      dataEdit: false,
      deleteModal: false,
      event: {
        _id: "",
        customer: "",
        orderId: "",
        orderDate: "",
        amount: "",
        payment: "",
        product: "",
        status: ""
      },
      //
    };
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Multiselect,
    flatPickr,
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.orders);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.orderId.toLowerCase().includes(search) ||
            data.customer.toLowerCase().includes(search) ||
            data.product.toLowerCase().includes(search) ||
            data.orderDate.toLowerCase().includes(search) ||
            data.amount.toString().toLowerCase().includes(search) ||
            data.payment.toLowerCase().includes(search) ||
            data.status.toLowerCase().includes(search)
          );
        });
      } else if (this.date !== null) {
        if (this.date !== null) {
          var date1 = this.date.split(" to ")[0];
          var date2 = this.date.split(" to ")[1];
        }
        return this.displayedPosts.filter((data) => {
          if (
            new Date(data.orderDate.slice(0, 12)) >= new Date(date1) &&
            new Date(data.orderDate.slice(0, 12)) <= new Date(date2)
          ) {
            return data;
          } else {
            return null;
          }
        });
      } else if (this.status !== null || this.value !== null) {
        return this.displayedPosts.filter((data) => {
          if (this.status != null && this.value != null) {
            if (this.status === data.status) {
              if (this.value === data.payment) {
                return data;
              } else if (this.value == 'All') {
                return data;
              }
            } else if (this.value == 'All' && this.status == 'All') {
              return data;
            } else if (this.status == 'All') {
              if (this.value === data.payment) {
                return data;
              }
            }
          } else if (this.status === data.status) {
            return data;
          } else if (this.value === data.payment) {
            return data;
          }
          else {
            return null;
          }
        });
      }
      // else if (this.date !== null && this.status !== null && this.value !== null) {
      //   return this.displayedPosts.filter((data) => {
      //     if (
      //       new Date(data.orderDate.slice(0, 12)) >= new Date(date1) &&
      //       new Date(data.orderDate.slice(0, 12)) <= new Date(date2) &&
      //       data.status === this.status &&
      //       data.payment === this.value
      //     ) {
      //       return data;
      //     } else {
      //       return null;
      //     }
      //   });
      // } 
      else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    orders() {
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
  beforeMount() {
    axios.get('https://api-node.themesbrand.website/apps/order').then((data) => {
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"
      ];
      this.orders = [];
      data.data.data.forEach((row) => {
        var dd = new Date(row.orderDate);
        row.orderDate = dd.getDate() + " " + monthNames[dd.getMonth()] + ", " + dd.getFullYear();
        this.orders.push(row);
      });
    }).catch((er) => {
      console.log(er);
    });

  },

  mounted() {
    var checkAll = document.getElementById("checkAll");
    if (checkAll) {
      checkAll.onclick = function () {
        var checkboxes = document.querySelectorAll(
          '.form-check-all input[type="checkbox"]'
        );

        if (checkAll.checked == true) {
          checkboxes.forEach(function (checkbox) {
            checkbox.checked = true;
            checkbox.closest("tr").classList.add("table-active");
            document.getElementById('remove-actions').style.display = 'block';
          });
        } else {
          checkboxes.forEach(function (checkbox) {
            checkbox.checked = false;
            checkbox.closest("tr").classList.remove("table-active");
            document.getElementById('remove-actions').style.display = 'none';
          });
        }
      };
    }

    var checkboxes = document.querySelectorAll('#orderTable .form-check-input');
    Array.from(checkboxes).forEach(function (element) {
      element.addEventListener('change', function (event) {
        var checkedCount = document.querySelectorAll('#orderTable .form-check-input:checked').length;

        if (event.target.closest("tr").classList.contains("table-active")) {
          (checkedCount > 0) ? document.getElementById("remove-actions").style.display = 'block' : document.getElementById("remove-actions").style.display = 'none';
        } else {
          (checkedCount > 0) ? document.getElementById("remove-actions").style.display = 'block' : document.getElementById("remove-actions").style.display = 'none';
        }
      });
    });

  },

  methods: {

    onChangeStatus(e) {
      this.isStatus = e;
    },
    onChangePayment(e) {
      this.isPayment = e;
    },
    setPages() {
      let numberOfPages = Math.ceil(this.orders.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(orders) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return orders.slice(from, to);
    },

    // 
    handleSubmit() {
      if (this.dataEdit) {
        this.submitted = true;
        if (this.submitted && (this.event.customer && this.event.payment && this.event.orderDate && this.event.amount && this.event.payment && this.event.status)) {
          this.createModal = false;

          axios.patch(`https://api-node.themesbrand.website/apps/order/${this.event._id}`, this.event)
            .then((response) => {
              const data = response.data.data;
              this.orders = this.orders.map(item => item._id.toString() == data._id.toString() ? { ...item, ...data } : item);
            }).catch((er) => {
              console.log(er);
            });
        }
      } else {
        this.submitted = true;
        if (this.submitted && (this.event.customer && this.event.payment && this.event.orderDate && this.event.amount && this.event.payment && this.event.status)) {
          const data = {
            _id: (Math.floor(Math.random() * 100 + 20) - 20),
            orderId: "#VZ2" + (Math.floor(Math.random() * 100 + 20) - 20),
            ...this.event
          };
          this.createModal = false;

          axios.post(`https://api-node.themesbrand.website/apps/order`, data)
            .then((response) => {
              this.orders.unshift(response.data.data);
            }).catch((er) => {
              console.log(er);
            });
        }
      }
    },

    editDetails(data) {
      this.dataEdit = true;
      this.createModal = true;
      this.event = { ...data };

      this.submitted = false;
    },

    toggleModal() {
      this.createModal = true;
      this.dataEdit = false;
      this.event = {};

      this.submitted = false;
    },

    deleteModalToggle(data) {
      this.deleteModal = true;
      this.event._id = data._id;
    },

    deleteData() {
      if (this.event._id) {
        axios.delete(`https://api-node.themesbrand.website/apps/order/${this.event._id}`)
          .then((response) => {
            if (response.data.status === 'success') {
              this.orders = this.orders.filter((item) => item._id != this.event._id);
            }
          }).catch((er) => {
            console.log(er);
          });

        this.deleteModal = false;
      }
    },
    //

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.orders];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.orders = sortedArray;
    },


    deleteMultiple() {
      let ids_array = [];
      var items = document.getElementsByName("chk_child");
      items.forEach(function (ele) {
        if (ele.checked == true) {
          var trNode = ele.parentNode.parentNode.parentNode;
          var id = trNode.querySelector(".id a").innerHTML;
          ids_array.push(id);
        }
      });
      if (typeof ids_array !== "undefined" && ids_array.length > 0) {
        if (confirm("Are you sure you want to delete this?")) {
          var cusList = this.orders;
          ids_array.forEach(function (id) {
            cusList = cusList.filter(function (orders) {
              return orders.orderId != id;
            });
          });
          this.orders = cusList;
          document.getElementById("checkAll").checked = false;
          var itemss = document.getElementsByName("chk_child");
          itemss.forEach(function (ele) {
            if (ele.checked == true) {
              ele.checked = false;
              ele.closest("tr").classList.remove("table-active");
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

    SearchData() {
      this.resultQuery;
      this.date = this.date2;
      this.status = this.status1;
      this.value = this.value1;
    },
    changecategory(data) {
      this.statuscategory = data;
    }
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Orders" pageTitle="Ecommerce" />
    <BRow>
      <BCol lg="12">
        <BCard no-body id="orderList">
          <BCardHeader class="border-0">
            <BRow class="align-items-center gy-3">
              <BCol cols="sm">
                <h5 class="card-title mb-0">Order History</h5>
              </BCol>
              <BCol sm="auto">
                <div class="d-flex gap-1 flex-wrap">
                  <BButton type="button" variant="primary" class="add-btn" id="create-btn" @click="toggleModal">
                    <i class="ri-add-line align-bottom me-1"></i> Create Order
                  </BButton>
                  <BButton type="button" variant="info" >
                    <i class="ri-file-download-line align-bottom me-1"></i> Import
                  </BButton>
                  <BButton variant="soft-danger" class="me-1" id="remove-actions" @click="deleteMultiple">
                    <i class="ri-delete-bin-2-line"></i>
                  </BButton>
                </div>
              </BCol>
            </BRow>
          </BCardHeader>
          <BCardBody class="border border-dashed border-end-0 border-start-0">
            <b-form>
              <BRow class="g-3">
                <BCol xxl="5" sm="6">
                  <div class="search-box">
                    <input type="text" class="form-control search" v-model="searchQuery"
                      placeholder="Search for order ID, customer, order status or something..." />
                    <i class="ri-search-line search-icon"></i>
                  </div>
                </BCol>
                <BCol xxl="2" sm="6">
                  <div>
                    <flat-pickr placeholder="Select date" v-model="date2" :config="config"
                      class="form-control flatpickr-input" id="demo-datepicker"></flat-pickr>
                  </div>
                </BCol>
                <BCol xxl="2" sm="4">
                  <div>
                    <Multiselect class="form-control" v-model="status1" :close-on-select="true" :searchable="true"
                      :create-option="true" @input="onChangePayment" :options="[
                        { value: '', label: 'Status' },
                        { value: 'All', label: 'All' },
                        { value: 'Pending', label: 'Pending' },
                        { value: 'Inprogress', label: 'Inprogress' },
                        { value: 'Cancelled', label: 'Cancelled' },
                        { value: 'Pickups', label: 'Pickups' },
                        { value: 'Returns', label: 'Returns' },
                        { value: 'Delivered', label: 'Delivered' },
                      ]" />
                  </div>
                </BCol>
                <BCol xxl="2" sm="4">
                  <div>
                    <Multiselect class="form-control" v-model="value1" :close-on-select="true" :searchable="true"
                      :create-option="true" @input="onChangeStatus" :options="[
                        { value: '', label: 'Select Payment' },
                        { value: 'All', label: 'All' },
                        { value: 'Mastercard', label: 'Mastercard' },
                        { value: 'Paypal', label: 'Paypal' },
                        { value: 'Visa', label: 'Visa' },
                        { value: 'COD', label: 'COD' },
                      ]" />
                  </div>
                </BCol>
                <BCol xxl="1" sm="4">
                  <div>
                    <BButton type="button" variant="primary" class="w-100" @click="SearchData">
                      <i class="ri-equalizer-fill me-1 align-bottom"></i>
                      Filters
                    </BButton>
                  </div>
                </BCol>
              </BRow>
            </b-form>
          </BCardBody>
          <BCardBody class="pt-0">
            <div>
              <ul class="nav nav-tabs nav-tabs-custom nav-primary mb-3" role="tablist">
                <li class="nav-item">
                  <BLink class="nav-link  All py-3" data-bs-toggle="tab" id="All" href="#home1" role="tab"
                    @click="changecategory('All')" aria-selected="true">
                    <i class="ri-store-2-fill me-1 align-bottom"></i> All Orders
                  </BLink>
                </li>
                <li class="nav-item">
                  <BLink class="nav-link py-3  Delivered" data-bs-toggle="tab" id="Delivered" href="#delivered" role="tab"
                    @click="changecategory('Delivered')" aria-selected="false">
                    <i class="ri-checkbox-circle-line me-1 align-bottom"></i>
                    Delivered
                  </BLink>
                </li>
                <li class="nav-item">
                  <BLink class="nav-link py-3 Pickups" data-bs-toggle="tab" id="Pickups" href="#pickups" role="tab"
                    @click="changecategory('Pickups')" aria-selected="false">
                    <i class="ri-truck-line me-1 align-bottom"></i> Pickups
                    <BBadge variant="danger" class="align-middle ms-1">2</BBadge>
                  </BLink>
                </li>
                <li class="nav-item">
                  <BLink class="nav-link py-3 Returns" data-bs-toggle="tab" id="Returns" href="#returns" role="tab"
                    @click="changecategory('Returns')" aria-selected="false">
                    <i class="ri-arrow-left-right-fill me-1 align-bottom"></i>
                    Returns
                  </BLink>
                </li>
                <li class="nav-item">
                  <BLink class="nav-link py-3 Cancelled" data-bs-toggle="tab" id="Cancelled" href="#cancelled" role="tab"
                    @click="changecategory('Cancelled')" aria-selected="false">
                    <i class="ri-close-circle-line me-1 align-bottom"></i>
                    Cancelled
                  </BLink>
                </li>
              </ul>

              <div class="table-responsive table-card mb-1">
                <table class="table table-nowrap align-middle" id="orderTable">
                  <thead class="text-muted table-light">
                    <tr class="text-uppercase">
                      <th scope="col" style="width: 25px">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" id="checkAll" value="option" />
                        </div>
                      </th>
                      <th class="sort" data-sort="id" @click="onSort('orderId')">Order ID</th>
                      <th class="sort" data-sort="customer_name" @click="onSort('customer')">Customer</th>
                      <th class="sort" data-sort="product_name" @click="onSort('orderDate')">Product</th>
                      <th class="sort" data-sort="date" @click="onSort('customer')">Order Date</th>
                      <th class="sort" data-sort="amount" @click="onSort('amount')">Amount</th>
                      <th class="sort" data-sort="payment" @click="onSort('payment')">Payment Method</th>
                      <th class="sort" data-sort="status" @click="onSort('status')">Delivery Status</th>
                      <th class="sort" data-sort="city">Action</th>
                    </tr>
                  </thead>
                  <tbody class="list form-check-all" v-for="(data, index) of resultQuery" :key="index">

                    <tr v-if="statuscategory == 'All' || statuscategory == data.status">
                      <th scope="row">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="chk_child" value="option1" />
                        </div>
                      </th>
                      <td class="id">
                        <router-link to="/ecommerce/order-details" class="fw-medium link-primary">{{ data.orderId }}
                        </router-link>
                      </td>
                      <td class="customer_name">{{ data.customer }}</td>
                      <td class="product_name">{{ data.product }}</td>
                      <td class="date">
                        {{ data.orderDate }}
                        <small class="text-muted">02:21 AM</small>
                      </td>
                      <td class="amount">${{ data.amount }}</td>
                      <td class="payment">{{ data.payment }}</td>
                      <td class="status">
                        <span class="badge text-uppercase" :class="{
                          'bg-secondary-subtle text-secondary': data.status == 'Inprogress',
                          'bg-info-subtle text-info': data.status == 'Pickups',
                          'bg-success-subtle text-success': data.status == 'Delivered',
                          'bg-danger-subtle text-danger': data.status == 'Cancelled',
                          'bg-primary-subtle text-primary': data.status == 'Returns',
                          'bg-warning-subtle text-warning': data.status == 'Pending',
                        }">{{ data.status }}</span>

                      </td>
                      <td>
                        <ul class="list-inline hstack gap-2 mb-0">
                          <li class="list-inline-item" v-b-tooltip.hover title="View">
                            <router-link to="/ecommerce/order-details" class="text-primary d-inline-block">
                              <i class="ri-eye-fill fs-16"></i>
                            </router-link>
                          </li>
                          <li class="list-inline-item edit" data-bs-toggle="tooltip" data-bs-trigger="hover"
                            data-bs-placement="top" title="Edit">
                            <BLink variant="text-primary" class="d-inline-block edit-item-btn" @click="editDetails(data)">
                              <i class="ri-pencil-fill fs-16"></i>
                            </BLink>
                          </li>
                          <li class="list-inline-item" data-bs-toggle="tooltip" data-bs-trigger="hover"
                            data-bs-placement="top" title="Remove">
                            <BLink class="text-danger d-inline-block remove-item-btn" @click="deleteModalToggle(data)">
                              <i class="ri-delete-bin-5-fill fs-16"></i>
                            </BLink>
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="noresult" v-if="resultQuery.length < 1">
                  <div class="text-center">
                    <lottie class="avatar-xl" colors="primary:#121331,secondary:#08a88a" :options="defaultOptions"
                      :height="75" :width="75" />
                    <h5 class="mt-2">Sorry! No Result Found</h5>
                    <p class="text-muted">
                      We've searched more than 150+ Orders We did not find any
                      orders for you search.
                    </p>
                  </div>
                </div>
              </div>

              <div class="d-flex justify-content-end" v-if="resultQuery.length >= 1">
                <div class="pagination-wrap hstack gap-2">
                  <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--"> Previous
                  </BLink>
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
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <!-- order modal -->
    <BModal v-model="createModal" hide-footer :title="dataEdit ? 'Edit Order' : 'Add Order'" header-class="p-3 bg-light"
      class="v-modal-custom" centered>
      <b-form action="#" id="addform" class="tablelist-form" autocomplete="off">
        <input type="hidden" id="id-field" />

        <div class="mb-3">
          <label for="customername-field" class="form-label">Customer Name</label>
          <input type="text" id="customername" class="form-control" placeholder="Enter Name" v-model="event.customer"
            :class="{ 'is-invalid': submitted && !event.customer }" />
          <div class="invalid-feedback">Please enter customer name.</div>
        </div>

        <div class="mb-3">
          <label for="productname" class="form-label">Product</label>
          <select class="form-control" data-trigger name="productname-field" id="productname" v-model="event.product"
            :class="{ 'is-invalid': submitted && !event.product }">
            <option value="">Product</option>
            <option value="Puma Tshirt">Puma Tshirt</option>
            <option value="Adidas Sneakers">
              Adidas Sneakers
            </option>
            <option value="350 ml Glass Grocery Container">
              350 ml Glass Grocery Container
            </option>
            <option value="American egale outfitters Shirt">
              American egale outfitters Shirt
            </option>
            <option value="Galaxy Watch4">Galaxy Watch4</option>
            <option value="Apple iPhone 12">
              Apple iPhone 12
            </option>
            <option value="Funky Prints T-shirt">
              Funky Prints T-shirt
            </option>
            <option value="USB Flash Drive Personalized with 3D Print">
              USB Flash Drive Personalized with 3D Print
            </option>
            <option value="Oxford Button-Down Shirt">
              Oxford Button-Down Shirt
            </option>
            <option value="Classic Short Sleeve Shirt">
              Classic Short Sleeve Shirt
            </option>
            <option value="Half Sleeve T-Shirts (Blue)">
              Half Sleeve T-Shirts (Blue)
            </option>
            <option value="Noise Evolve Smartwatch">
              Noise Evolve Smartwatch
            </option>
          </select>
          <div class="invalid-feedback">Please select product.</div>
        </div>

        <div class="mb-3">
          <label for="date-field" class="form-label">Order Date</label>
          <flat-pickr placeholder="Select date" :config="timeConfig" v-model="event.orderDate"
            :class="{ 'is-invalid': submitted && !event.orderDate }" class="form-control flatpickr-input"
            id="orderdate"></flat-pickr>
          <div class="invalid-feedback">Please enter date.</div>
        </div>

        <BRow class="gy-4 mb-3">
          <BCol md="6">
            <div>
              <label for="amount-field" class="form-label">Amount</label>
              <input type="text" id="amount" class="form-control" placeholder="Total amount" v-model="event.amount"
                :class="{ 'is-invalid': submitted && !event.amount }" />
              <div class="invalid-feedback">Please enter an amount.</div>
            </div>
          </BCol>
          <BCol md="6">
            <div>
              <label for="payment-field" class="form-label">Payment Method</label>
              <select class="form-control" data-trigger name="payment-method" id="payment" v-model="event.payment"
                :class="{ 'is-invalid': submitted && !event.payment }">
                <option value="">Payment Method</option>
                <option value="Mastercard">Mastercard</option>
                <option value="Visa">Visa</option>
                <option value="COD">COD</option>
                <option value="Paypal">Paypal</option>
              </select>
              <div class="invalid-feedback">Please select payment method.</div>
            </div>
          </BCol>
        </BRow>

        <div class="mb-3">
          <label for="delivered-status" class="form-label">Delivery Status</label>
          <select class="form-control" data-trigger name="delivered-status" id="delivered" v-model="event.status"
            :class="{ 'is-invalid': submitted && !event.status }">
            <option value="">Delivery Status</option>
            <option value="Pending">Pending</option>
            <option value="Inprogress">Inprogress</option>
            <option value="Cancelled">Cancelled</option>
            <option value="Pickups">Pickups</option>
            <option value="Delivered">Delivered</option>
            <option value="Returns">Returns</option>
          </select>
          <div class="invalid-feedback">Please select delivered status.</div>
        </div>

        <div class="hstack gap-2 justify-content-end">
          <BButton type="button" variant="light" @click="createModal = false" id="closemodal">
            Close
          </BButton>
          <BButton type="button" variant="success" id="add-btn" @click="handleSubmit">
            {{ dataEdit ? 'Update' : 'Add Order' }}
          </BButton>
        </div>
      </b-form>
    </BModal>

    <!-- delete modal -->
    <BModal v-model="deleteModal" modal-class="zoomIn" hide-footer no-close-on-backdrop centered>
      <div class="mt-2 text-center">
        <lottie class="avatar-xl" colors="primary:#f7b84b,secondary:#f06548" :options="defaultOptions1" :height="75"
          :width="75" />
        <div class="mt-4 pt-2 fs-15 mx-4 mx-sm-5">
          <h4>You are about to delete a order ?</h4>
          <p class="text-muted mx-4 mb-0">Deleting your order will remove all of your information from our database.</p>
        </div>
      </div>
      <div class="d-flex gap-2 justify-content-center mt-4 mb-2">
        <button variant="success" class="btn w-sm btn-light" @click="deleteModal = false">Close</button>
        <button type="button" class="btn w-sm btn-danger" id="delete-record" @click="deleteData">Yes, Delete It!</button>
      </div>
    </BModal>
  </Layout>
</template>