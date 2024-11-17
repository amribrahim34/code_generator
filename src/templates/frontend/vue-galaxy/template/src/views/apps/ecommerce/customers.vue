<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import Swal from "sweetalert2";
import axios from "axios";
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/msoeawqm.json";
import animationData1 from "@/components/widgets/gsqxdxog.json";

export default {
  data() {
    return {
      date1: null,
      date: null,
      addCustomerModal: false,
      editCustomerModal: false,
      rangeDateconfig: {
        wrap: true, // set wrap to true only when using 'input-group'
        altFormat: "M j, Y",
        altInput: true,
        dateFormat: "d M, Y",
        mode: "range",
      },
      config: {
        enableTime: false,
        dateFormat: "d M, Y",
      },
      searchQuery: null,
      defaultOptions: {
        animationData: animationData,
      },
      defaultOptions2: {
        animationData: animationData1,
      },
      page: 1,
      perPage: 8,
      value: "All",
      value1: null,
      pages: [],
      customerList: [],

      //
      submitted: false,

      dataEdit: false,
      deleteModal: false,
      event: {
        _id: "",
        customer: "",
        customerId: "",
        date: "",
        email: "",
        phone: "",
        status: "",
      },

      //
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.customerList);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.customer.toLowerCase().includes(search) ||
            data.email.toLowerCase().includes(search) ||
            data.phone.includes(search) ||
            data.date.toLowerCase().includes(search) ||
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
            new Date(data.date.slice(0, 12)) >= new Date(date1) &&
            new Date(data.date.slice(0, 12)) <= new Date(date2)
          ) {
            return data;
          } else {
            return null;
          }
        });
      } else if (this.value !== null) {
        return this.displayedPosts.filter((data) => {
          if (data.status === this.value || this.value == "All") {
            return data;
          } else {
            return null;
          }
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  created() {
    this.setPages();
  },
  watch: {
    customerList() {
      this.setPages();
    },
  },
  filters: {
    trimWords(value) {
      return value.split(" ").splice(0, 20).join(" ") + "...";
    },
  },
  beforeMount() {
    axios
      .get("https://api-node.themesbrand.website/apps/customer")
      .then((data) => {
        this.customerList = [];
        data.data.data.forEach((row) => {
          const monthNames = [
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
          ];
          var dd = new Date(row.date);
          row.date =
            dd.getDate() +
            " " +
            monthNames[dd.getMonth()] +
            ", " +
            dd.getFullYear();
          this.customerList.push(row);
        });
      })
      .catch((er) => {
        console.log(er);
      });
  },

  methods: {
    //
    handleSubmit() {
      if (this.dataEdit) {
        this.submitted = true;
        if (
          this.submitted &&
          this.event.customer &&
          this.event.email &&
          this.event.phone &&
          this.event.date &&
          this.event.status
        ) {
          this.addCustomerModal = false;

          axios
            .patch(
              `https://api-node.themesbrand.website/apps/customer/${this.event._id}`,
              this.event
            )
            .then((response) => {
              const data = response.data.data;
              this.customerList = this.customerList.map((item) =>
                item._id.toString() == data._id.toString()
                  ? { ...item, ...data }
                  : item
              );
            })
            .catch((er) => {
              console.log(er);
            });
        }
      } else {
        this.submitted = true;
        if (
          this.submitted &&
          this.event.customer &&
          this.event.email &&
          this.event.phone &&
          this.event.date &&
          this.event.status
        ) {
          const data = {
            _id: Math.floor(Math.random() * 100 + 20) - 20,
            customerId: "#VZ2" + (Math.floor(Math.random() * 100 + 20) - 20),
            ...this.event,
          };
          this.addCustomerModal = false;

          axios
            .post(`https://api-node.themesbrand.website/apps/customer`, data)
            .then((response) => {
              this.customerList.unshift(response.data.data);
            })
            .catch((er) => {
              console.log(er);
            });
        }
      }
    },

    onSort(column) {
      this.direction = this.direction === "asc" ? "desc" : "asc";
      const sortedArray = [...this.customerList];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === "asc" ? res : -res;
      });
      this.customerList = sortedArray;
    },

    editDetails(data) {
      this.dataEdit = true;
      this.addCustomerModal = true;
      this.event = { ...data };

      this.submitted = false;
    },

    toggleModal() {
      this.addCustomerModal = true;
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
        axios
          .delete(
            `https://api-node.themesbrand.website/apps/customer/${this.event._id}`
          )
          .then((response) => {
            if (response.data.status === "success") {
              this.customerList = this.customerList.filter(
                (item) => item._id != this.event._id
              );
            }
          })
          .catch((er) => {
            console.log(er);
          });

        this.deleteModal = false;
      }
    },
    //

    setPages() {
      let numberOfPages = Math.ceil(this.customerList.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },

    paginate(customerList) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return customerList.slice(from, to);
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
          var cusList = this.customerList;
          ids_array.forEach(function (id) {
            cusList = cusList.filter(function (customer) {
              return customer.customerId != id;
            });
          });
          this.customerList = cusList;
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
      this.value = this.value1;
    },
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
            document.getElementById("remove-actions").style.display = "block";
          });
        } else {
          checkboxes.forEach(function (checkbox) {
            checkbox.checked = false;
            checkbox.closest("tr").classList.remove("table-active");
            document.getElementById("remove-actions").style.display = "none";
          });
        }
      };
    }

    var checkboxes = document.querySelectorAll(
      "#customerTable .form-check-input"
    );
    Array.from(checkboxes).forEach(function (element) {
      element.addEventListener("change", function (event) {
        var checkedCount = document.querySelectorAll(
          "#customerTable .form-check-input:checked"
        ).length;

        if (event.target.closest("tr").classList.contains("table-active")) {
          checkedCount > 0
            ? (document.getElementById("remove-actions").style.display =
                "block")
            : (document.getElementById("remove-actions").style.display =
                "none");
        } else {
          checkedCount > 0
            ? (document.getElementById("remove-actions").style.display =
                "block")
            : (document.getElementById("remove-actions").style.display =
                "none");
        }
      });
    });
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Multiselect,
    flatPickr,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Customers" pageTitle="Ecommerce" />
    <BRow>
      <BCol lg="12">
        <BCard no-body id="customerList">
          <BCardHeader class="border-bottom-dashed">
            <BRow class="g-4 align-items-center">
              <BCol sm>
                <div>
                  <h5 class="card-title mb-0">Customer List</h5>
                </div>
              </BCol>
              <BCol sm="auto">
                <div class="d-flex flex-wrap align-items-start gap-2">
                  <BButton
                    variant="soft-danger"
                    class="me-1"
                    id="remove-actions"
                    @click="deleteMultiple"
                  >
                    <i class="ri-delete-bin-2-line"></i>
                  </BButton>
                  <BButton
                    type="button"
                    variant="primary"
                    class="add-btn"
                    id="create-btn"
                    @click="toggleModal"
                  >
                    <i class="ri-add-line align-bottom me-1"></i> Add Customer
                  </BButton>
                  <BButton type="button" variant="secondary">
                    <i class="ri-file-download-line align-bottom me-1"></i>
                    Import
                  </BButton>
                </div>
              </BCol>
            </BRow>
          </BCardHeader>
          <BCardBody class="border-bottom-dashed border-bottom">
            <b-form>
              <BRow class="g-3">
                <BCol xl="6">
                  <div class="search-box">
                    <input
                      type="text"
                      class="form-control search"
                      placeholder="Search for customer, email, phone, status or something..."
                      v-model="searchQuery"
                    />
                    <i class="ri-search-line search-icon"></i>
                  </div>
                </BCol>
                <BCol xl="6">
                  <BRow class="g-3">
                    <BCol sm="4">
                      <div class="">
                        <flat-pickr
                          v-model="date"
                          placeholder="Select date"
                          :config="rangeDateconfig"
                          class="form-control"
                        ></flat-pickr>
                      </div>
                    </BCol>
                    <BCol sm="4">
                      <div>
                        <Multiselect
                          class="form-control"
                          v-model="value1"
                          :close-on-select="true"
                          :searchable="true"
                          :create-option="true"
                          :options="[
                            { value: '', label: 'Status', disabled: true },
                            { value: 'All', label: 'All' },
                            { value: 'Active', label: 'Active' },
                            { value: 'Block', label: 'Block' },
                          ]"
                        />
                      </div>
                    </BCol>

                    <BCol sm="4">
                      <div>
                        <BButton
                          type="button"
                          variant="primary"
                          class="w-100"
                          @click="SearchData"
                        >
                          <i class="ri-equalizer-fill me-2 align-bottom"></i
                          >Filters
                        </BButton>
                      </div>
                    </BCol>
                  </BRow>
                </BCol>
              </BRow>
            </b-form>
          </BCardBody>
          <BCardBody>
            <div>
              <div class="table-responsive table-card mb-1">
                <table class="table align-middle" id="customerTable">
                  <thead class="table-light text-muted">
                    <tr>
                      <th scope="col" style="width: 50px">
                        <div class="form-check">
                          <input
                            class="form-check-input"
                            type="checkbox"
                            id="checkAll"
                            value="option"
                          />
                        </div>
                      </th>
                      <th
                        class="sort"
                        data-sort="customer_name"
                        @click="onSort('customer')"
                      >
                        Customer
                      </th>
                      <th
                        class="sort"
                        data-sort="email"
                        @click="onSort('email')"
                      >
                        Email
                      </th>
                      <th
                        class="sort"
                        data-sort="phone"
                        @click="onSort('phone')"
                      >
                        Phone
                      </th>
                      <th class="sort" data-sort="date" @click="onSort('date')">
                        Joining Date
                      </th>
                      <th
                        class="sort"
                        data-sort="status"
                        @click="onSort('status')"
                      >
                        Status
                      </th>
                      <th class="sort" data-sort="action">Action</th>
                    </tr>
                  </thead>
                  <tbody class="list form-check-all">
                    <tr v-for="(item, index) of resultQuery" :key="index">
                      <th scope="row">
                        <div class="form-check">
                          <input
                            class="form-check-input"
                            type="checkbox"
                            name="chk_child"
                            value="option1"
                          />
                        </div>
                      </th>
                      <td class="id" style="display: none">
                        <BLink
                          href="javascript:void(0);"
                          class="fw-medium link-primary"
                          >{{ item.customerId }}</BLink
                        >
                      </td>
                      <td class="customer_name">{{ item.customer }}</td>
                      <td class="email">{{ item.email }}</td>
                      <td class="phone">{{ item.phone }}</td>
                      <td class="date">{{ item.date }}</td>
                      <td class="status">
                        <span
                          class="badge text-uppercase"
                          :class="{
                            'bg-success-subtle text-success':
                              item.status == 'Active',
                            'bg-danger-subtle text-danger':
                              item.status == 'Block',
                          }"
                        >
                          {{ item.status }}
                        </span>
                      </td>
                      <td>
                        <ul class="list-inline hstack gap-2 mb-0">
                          <li
                            class="list-inline-item edit"
                            data-bs-toggle="tooltip"
                            data-bs-trigger="hover"
                            data-bs-placement="top"
                            title="Edit"
                          >
                            <BLink
                              variant="text-primary"
                              class="d-inline-block edit-item-btn"
                              @click="editDetails(item)"
                            >
                              <i class="ri-pencil-fill fs-16"></i>
                            </BLink>
                          </li>
                          <li
                            class="list-inline-item"
                            data-bs-toggle="tooltip"
                            data-bs-trigger="hover"
                            data-bs-placement="top"
                            title="Remove"
                          >
                            <BLink
                              class="text-danger d-inline-block remove-item-btn"
                              @click="deleteModalToggle(item)"
                            >
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
                    <lottie
                      class="avatar-xl"
                      colors="primary:#121331,secondary:#08a88a"
                      :options="defaultOptions"
                      :height="75"
                      :width="75"
                    />
                    <h5 class="mt-2">Sorry! No Result Found</h5>
                    <p class="text-muted mb-0">
                      We've searched more than 150+ customer We did not find any
                      customer for you search.
                    </p>
                  </div>
                </div>
              </div>
              <div
                class="d-flex justify-content-end"
                v-if="resultQuery.length >= 1"
              >
                <div class="pagination-wrap hstack gap-2">
                  <BLink
                    class="page-item pagination-prev"
                    href="#"
                    :disabled="page <= 1"
                    @click="page--"
                  >
                    Previous
                  </BLink>
                  <ul class="pagination listjs-pagination mb-0">
                    <li
                      :class="{
                        active: pageNumber == page,
                        disabled: pageNumber == '...',
                      }"
                      v-for="(pageNumber, index) in pages"
                      :key="index"
                      @click="page = pageNumber"
                    >
                      <BLink class="page" href="#">{{ pageNumber }}</BLink>
                    </li>
                  </ul>
                  <BLink
                    class="page-item pagination-next"
                    href="#"
                    @click="page++"
                    :disabled="page >= pages.length"
                  >
                    Next
                  </BLink>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <!-- customer modal  -->
    <BModal
      v-model="addCustomerModal"
      id="showModal"
      hide-footer
      :title="dataEdit ? 'Edit Customer' : 'Add Customer'"
      header-class="p-3 bg-light"
      class="v-modal-custom"
      centered
    >
      <b-form action="#" id="addform" class="tablelist-form" autocomplete="off">
        <input type="hidden" id="id-field" />

        <div class="mb-3" id="modal-id" style="display: none">
          <label for="id-field1" class="form-label">ID</label>
          <input
            type="text"
            id="idfield1"
            class="form-control"
            placeholder="ID"
            readonly
          />
        </div>

        <div class="mb-3">
          <label for="customername-field" class="form-label"
            >Customer Name</label
          >
          <input
            type="text"
            id="customername"
            class="form-control"
            placeholder="Enter Name"
            v-model="event.customer"
            :class="{ 'is-invalid': submitted && !event.customer }"
          />
          <div class="invalid-feedback">Please enter a customer name.</div>
        </div>

        <div class="mb-3">
          <label for="email-field" class="form-label">Email</label>
          <input
            type="email"
            id="email"
            class="form-control"
            placeholder="Enter Email"
            v-model="event.email"
            :class="{ 'is-invalid': submitted && !event.email }"
          />
          <div class="invalid-feedback">Please enter an email.</div>
        </div>

        <div class="mb-3">
          <label for="phone-field" class="form-label">Phone</label>
          <input
            type="text"
            id="phone"
            class="form-control"
            placeholder="Enter Phone no."
            v-model="event.phone"
            :class="{ 'is-invalid': submitted && !event.phone }"
          />
          <div class="invalid-feedback">Please enter a phone.</div>
        </div>

        <div class="mb-3">
          <label for="date-field" class="form-label">Joining Date</label>
          <flat-pickr
            :config="config"
            class="form-control"
            id="joindate"
            v-model="event.date"
            :class="{ 'is-invalid': submitted && !event.date }"
          ></flat-pickr>
          <div class="invalid-feedback">Please select a date.</div>
        </div>
        <div class="mb-3">
          <label for="status-field" class="form-label">Status</label>
          <select
            class="form-control"
            data-trigger
            id="statusfield"
            v-model="event.status"
            :class="{ 'is-invalid': submitted && !event.status }"
          >
            <option value="">Status</option>
            <option value="Active">Active</option>
            <option value="Block">Block</option>
          </select>
          <div class="invalid-feedback">Please select a status.</div>
        </div>

        <div class="hstack gap-2 justify-content-end">
          <BButton
            type="button"
            id="closemodal"
            variant="light"
            @click="addCustomerModal = false"
          >
            Close
          </BButton>
          <BButton type="button" variant="success" @click="handleSubmit">
            {{ dataEdit ? "Update" : "Add Customer" }}
          </BButton>
        </div>
      </b-form>
    </BModal>

    <!-- delete modal -->
    <BModal
      v-model="deleteModal"
      modal-class="zoomIn"
      hide-footer
      no-close-on-backdrop
      centered
    >
      <div class="mt-2 text-center">
        <lottie
          class="avatar-xl"
          colors="primary:#f7b84b,secondary:#f06548"
          :options="defaultOptions2"
          :height="100"
          :width="100"
        />
        <div class="mt-4 pt-2 fs-15 mx-4 mx-sm-5">
          <h4>Are you sure ?</h4>
          <p class="text-muted mx-4 mb-0">
            Are you sure you want to remove this record ?
          </p>
        </div>
      </div>
      <div class="d-flex gap-2 justify-content-center mt-4 mb-2">
        <button
          type="button"
          class="btn w-sm btn-light"
          @click="deleteModal = false"
        >
          Close
        </button>
        <button
          type="button"
          class="btn w-sm btn-danger"
          id="delete-record"
          @click="deleteData"
        >
          Yes, Delete It!
        </button>
      </div>
    </BModal>
  </Layout>
</template>
