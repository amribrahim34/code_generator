<script>
import Multiselect from "@vueform/multiselect";
import "@vueform/multiselect/themes/default.css";

import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import animationData from "@/components/widgets/msoeawqm.json";
import animationData1 from "@/components/widgets/gsqxdxog.json";
import Swal from "sweetalert2";
import axios from 'axios';
import Lottie from "@/components/widgets/lottie.vue";

export default {
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
    Multiselect,
  },
  data() {
    return {
      timeConfig: {
        enableTime: false,
        dateFormat: "d M, Y",
      },
      date2: null,
      defaultOptions: {
        animationData: animationData
      },
      defaultOptions1: {
        animationData: animationData1
      },
      searchQuery: null,
      addContactModal: false,
      page: 1,
      perPage: 8,
      pages: [],
      value: null,
      tagvalue: null,
      tagoption: [{
        value: 'Lead',
        label: 'Lead'
      },
      {
        value: 'Partner',
        label: 'Partner'
      },
      {
        value: 'Exiting',
        label: 'Exiting'
      },
      {
        value: 'Long-tern',
        label: 'Long-tern'
      },
      ],
      contactsList: [],

      //
      submitted: false,

      dataEdit: false,
      deleteModal: false,
      event: {
        _id: "",
        image_src: "",
        name: "",
        company: "",
        designation: "",
        email: "",
        last_contacted: "",
        lead_score: "",
        phone: "",
        tags: [],
        time: "",
      },
      //
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.contactsList);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.company.toLowerCase().includes(search) ||
            data.designation.toLowerCase().includes(search) ||
            data.email.toLowerCase().includes(search) ||
            data.image_src.toLowerCase().includes(search) ||
            data.last_contacted.toLowerCase().includes(search) ||
            data.lead_score.toString().toLowerCase().includes(search) ||
            data.name.toLowerCase().includes(search) ||
            data.phone.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    contactsList() {
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
    // 
    handleSubmit() {
      if (this.dataEdit) {
        this.submitted = true;
        if (this.submitted && (this.event.name && this.event.company && this.event.designation && this.event.email && this.event.phone && this.event.lead_score && this.event.tags)) {
          this.addContactModal = false;

          axios.patch(`https://api-node.themesbrand.website/apps/contact/${this.event._id}`, this.event)
            .then((response) => {
              const data = response.data.data;
              this.contactsList = this.contactsList.map(item => item._id.toString() == data._id.toString() ? { ...item, ...data } : item);
            }).catch((er) => {
              console.log(er);
            });
        }
      } else {
        this.submitted = true;
        if (this.submitted && (this.event.name && this.event.company && this.event.designation && this.event.email && this.event.phone && this.event.lead_score && this.event.tags)) {
          const data = {
            _id: (Math.floor(Math.random() * 100 + 20) - 20),
            image_src: require("@/assets/images/users/multi-user.jpg"),
            last_contacted: this.dateFormat(),
            ...this.event
          };
          this.addContactModal = false;

          axios.post(`https://api-node.themesbrand.website/apps/contact`, data)
            .then((response) => {
              this.contactsList.unshift(response.data.data);
            }).catch((er) => {
              console.log(er);
            });
        }
      }
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.contactsList];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.contactsList = sortedArray;
    },

    editDetails(data) {
      this.dataEdit = true;
      this.addContactModal = true;
      this.event = { ...data };

      this.submitted = false;
    },

    toggleModal() {
      this.addContactModal = true;
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
        axios.delete(`https://api-node.themesbrand.website/apps/contact/${this.event._id}`)
          .then((response) => {
            if (response.data.status === 'success') {
              this.contactsList = this.contactsList.filter((item) => item._id != this.event._id);
            }
          }).catch((er) => {
            console.log(er);
          });

        this.deleteModal = false;
      }
    },
    //

    dateFormat() {
      var d = new Date(),
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      return (d.getDate() + ' ' + months[d.getMonth()] + ', ' + d.getFullYear());
    },

    showdetail(data) {
      document.getElementById('image').setAttribute('src', data.image_src);
      document.getElementById('name').innerHTML = data.name;
      document.getElementById('company').innerHTML = data.company;
      document.getElementById('designation').innerHTML = data.designation;
      document.getElementById('email').innerHTML = data.email;
      document.getElementById('phoneno').innerHTML = data.phone;
      document.getElementById('leadscoreno').innerHTML = data.lead_score;
      document.getElementById('tags').innerHTML = '';
      data.tags.forEach((tag) => {
        document.getElementById('tags').innerHTML += '&nbsp;<span class="badge bg-primary-subtle text-primary">' + tag +
          '</span>';
      });
      document.getElementById('lastdate').innerHTML = data.last_contacted;
      document.getElementById('lasttime').innerHTML = data.time;
    },

    setPages() {
      let numberOfPages = Math.ceil(this.contactsList.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },
    paginate(contactsList) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return contactsList.slice(from, to);
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
          var cusList = this.contactsList;
          ids_array.forEach(function (id) {
            cusList = cusList.filter(function (customer) {
              return customer._id != id;
            });
          });
          this.contactsList = cusList;
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
  },
  beforeMount() {
    axios.get('https://api-node.themesbrand.website/apps/contact').then((data) => {
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"
      ];
      this.contactsList = [];
      data.data.data.forEach((row) => {
        var dd = new Date(row.last_contacted);
        row.last_contacted = dd.getDate() + " " + monthNames[dd.getMonth()] + ", " + dd.getFullYear();
        var hours = dd.getHours();
        var minutes = dd.getMinutes();
        var ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        hours = hours < 10 ? '0' + hours : hours;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        row.time = strTime;
        row.image_src = 'https://api-node.themesbrand.website/images/users/' + row.image_src;
        this.contactsList.push(row);
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

    var checkboxes = document.querySelectorAll('#contactList .form-check-input');
    Array.from(checkboxes).forEach(function (element) {
      element.addEventListener('change', function (event) {
        var checkedCount = document.querySelectorAll('#contactList .form-check-input:checked').length;

        if (event.target.closest("tr").classList.contains("table-active")) {
          (checkedCount > 0) ? document.getElementById("remove-actions").style.display = 'block' : document.getElementById("remove-actions").style.display = 'none';
        } else {
          (checkedCount > 0) ? document.getElementById("remove-actions").style.display = 'block' : document.getElementById("remove-actions").style.display = 'none';
        }
      });
    });
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Contacts" pageTitle="CRM" />
    <BRow>
      <BCol lg="12">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex align-items-center flex-wrap gap-2">
              <div class="flex-grow-1">
                <BButton variant="primary" class="add-btn me-1" @click="toggleModal">
                  <i class="ri-add-fill me-1 align-bottom"></i> Add Contacts
                </BButton>

              </div>
              <div class="flex-shrink-0">
                <div class="hstack text-nowrap gap-2">
                  <BButton variant="soft-secondary" id="remove-actions" @click="deleteMultiple">
                    <i class="ri-delete-bin-2-line"></i>
                  </BButton>
                  <BButton variant="secondary">
                    <i class="ri-filter-2-line me-1 align-bottom"></i> Filters
                  </BButton>
                  <BButton variant="soft-primary">Import</BButton>
                  <BDropdown variant="link" class="card-header-dropdown" toggle-class="btn btn-soft-secondary"
                    menu-class="dropdown-menu-end" :offset="{ alignmentAxis: -105, crossAxis: 0, mainAxis: 10 }">
                    <template #button-content><i class="ri-more-2-fill"></i></template>
                    <BDropdownItem>All</BDropdownItem>
                    <BDropdownItem>Last Week</BDropdownItem>
                    <BDropdownItem>Last Month</BDropdownItem>
                    <BDropdownItem>Last Year</BDropdownItem>
                  </BDropdown>
                </div>
              </div>
            </div>
          </BCardHeader>
        </BCard>
      </BCol>
      <BCol xxl="9">
        <BCard no-body id="contactList">
          <BCardHeader>
            <BRow class="g-3">
              <BCol md="4">
                <div class="search-box">
                  <input type="text" class="form-control search" placeholder="Search for contact..."
                    v-model="searchQuery" />
                  <i class="ri-search-line search-icon"></i>
                </div>
              </BCol>
              <BCol md="auto" class="ms-auto">
                <div class="d-flex align-items-center gap-2">
                  <span class="text-muted flex-shrink-0">Sort by: </span>
                  <Multiselect class="form-control" style="width:150px;" v-model="value" :close-on-select="true"
                    :searchable="true" :create-option="true" :options="[
                      { value: 'Name', label: 'Name' },
                      { value: 'Company', label: 'Company' },
                      { value: 'Lead', label: 'Lead' }
                    ]" />
                </div>
              </BCol>
            </BRow>
          </BCardHeader>
          <BCardBody>
            <div>
              <div class="table-responsive table-card mb-3">
                <table class="table align-middle table-nowrap mb-0" id="customerTable">
                  <thead class="table-light">
                    <tr>
                      <th scope="col" style="width: 50px">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" id="checkAll" value="option" />
                        </div>
                      </th>
                      <th class="sort" data-sort="name" scope="col" @click="onSort('name')">Name</th>
                      <th class="sort" data-sort="company_name" scope="col" @click="onSort('company')">
                        Company
                      </th>
                      <th class="sort" data-sort="email_id" scope="col" @click="onSort('email')">
                        Email ID
                      </th>
                      <th class="sort" data-sort="phone" scope="col" @click="onSort('phone')">
                        Phone No
                      </th>
                      <th class="sort" data-sort="lead_score" scope="col" @click="onSort('lead_score')">
                        Lead Score
                      </th>
                      <th class="sort" data-sort="Designation" scope="col" @click="onSort('tags')">
                        Tags
                      </th>
                      <th class="sort" data-sort="date" scope="col" @click="onSort('last_contacted')">
                        Last Contacted
                      </th>
                      <th scope="col">Action</th>
                    </tr>
                  </thead>
                  <tbody class="list form-check-all">
                    <tr v-for="(data, index) of resultQuery" :key="index">
                      <th scope="row">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="chk_child" value="option1" />
                        </div>
                      </th>
                      <td class="id" style="display: none">
                        <BLink href="javascript:void(0);" class="fw-medium link-primary">{{ data._id }}</BLink>
                      </td>
                      <td class="">
                        <div class="d-flex align-items-center">
                          <div class="flex-shrink-0"><img :src="data.image_src" alt=""
                              class="user_image avatar-xs rounded-circle">
                          </div>
                          <div class="flex-grow-1 ms-2 name">{{ data.name }}</div>
                        </div>
                      </td>
                      <td class="company_name">{{ data.company }}</td>
                      <td class="email_id">{{ data.email }}</td>
                      <td class="phone">{{ data.phone }}</td>
                      <td class="lead_score">{{ data.lead_score }}</td>
                      <td class="tags">
                        <span v-for="(tag, index) of data.tags" :key="index">
                          &nbsp;<BBadge variant="primary-subtle" class="bg-primary-subtle text-primary"> {{ tag
                          }}</BBadge>
                        </span>
                      </td>
                      <td> <span class="date">{{ data.last_contacted }}</span>&nbsp;<small class="text-muted time">{{
                        data.time
                      }}</small> </td>
                      <td>
                        <ul class="list-inline hstack gap-2 mb-0">
                          <li class="list-inline-item edit" v-b-tooltip.hover title="Call">
                            <BLink href="javascript:void(0);" class="text-muted d-inline-block">
                              <i class="ri-phone-line fs-16"></i>
                            </BLink>
                          </li>
                          <li class="list-inline-item edit" v-b-tooltip.hover title="Message">
                            <BLink href="javascript:void(0);" class="text-muted d-inline-block">
                              <i class="ri-question-answer-line fs-16"></i>
                            </BLink>
                          </li>
                          <li class="list-inline-item">
                            <BDropdown variant="link" toggle-class="btn btn-soft-primary btn-sm dropdown arrow-none"
                              menu-class="dropdown-menu-end"
                              :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                              <template #button-content><i class="ri-more-fill align-middle"></i></template>
                              <BDropdownItem @click="showdetail(data)"><i
                                  class="ri-eye-fill align-bottom me-2 text-muted"></i>
                                View</BDropdownItem>
                              <BDropdownItem @click="editDetails(data)"><i
                                  class="ri-pencil-fill align-bottom me-2 text-muted"></i>
                                Edit </BDropdownItem>
                              <BDropdownItem @click="deleteModalToggle(data)"> <i
                                  class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
                                Delete </BDropdownItem>
                            </BDropdown>
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="noresult" v-if="resultQuery.length < 1">
                  <div class="text-center">
                    <lottie class="avatar-xl" colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions"
                      :height="75" :width="75" />
                    <h5 class="mt-2">Sorry! No Result Found</h5>
                    <p class="text-muted mb-0">
                      We've searched more than 150+ Orders We did not find any
                      orders for you search.
                    </p>
                  </div>
                </div>
              </div>
              <div class="d-flex justify-content-end mt-3" v-if="resultQuery.length >= 1">
                <div class="pagination-wrap hstack gap-2">
                  <BLink class="page-item pagination-prev" href="#" :disabled="page <= 1" @click="page--">
                    Previous
                  </BLink>
                  <ul class="pagination listjs-pagination mb-0">
                    <li :class="{ active: pageNumber == page, disabled: pageNumber == '...', }"
                      v-for="(pageNumber, index) in pages" :key="index" @click="page = pageNumber">
                      <BLink class="page" href="#">{{ pageNumber }}</BLink>
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
      <BCol xxl="3">
        <BCard no-body id="contact-view-detail">
          <BCardBody class="text-center">
            <div class="position-relative d-inline-block">
              <img src="@/assets/images/users/avatar-10.jpg" id="image" alt=""
                class="avatar-lg rounded-circle img-thumbnail">
              <span class="contact-active position-absolute rounded-circle bg-success"><span
                  class="visually-hidden"></span></span>
            </div>
            <h5 class="mt-4 mb-1" id="name">Tonya Noble</h5>
            <p class="text-muted" id="company">Nesta Technologies</p>

            <ul class="list-inline mb-0">
              <li class="list-inline-item avatar-xs">
                <BLink href="javascript:void(0);" class="avatar-title bg-success-subtle text-success fs-15 rounded">
                  <i class="ri-phone-line"></i>
                </BLink>
              </li>
              <li class="list-inline-item avatar-xs">
                <BLink href="javascript:void(0);" class="avatar-title bg-danger-subtle text-danger fs-15 rounded">
                  <i class="ri-mail-line"></i>
                </BLink>
              </li>
              <li class="list-inline-item avatar-xs">
                <BLink href="javascript:void(0);" class="avatar-title bg-warning-subtle text-warning fs-15 rounded">
                  <i class="ri-question-answer-line"></i>
                </BLink>
              </li>
            </ul>
          </BCardBody>
          <BCardBody>
            <h6 class="text-muted text-uppercase fw-semibold mb-3">Personal Information</h6>
            <p class="text-muted mb-4">Hello, I'm Tonya Noble, The most effective objective is
              one that is tailored to the job you are applying for. It states what kind of
              career you are seeking, and what skills and experiences.</p>
            <div class="table-responsive table-card">
              <table class="table table-borderless mb-0">
                <tbody>
                  <tr>
                    <td class="fw-medium" scope="row">Designation</td>
                    <td id="designation">Lead Designer / Developer</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Email ID</td>
                    <td id="email">tonyanoble@velzon.com</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Phone No</td>
                    <td id="phoneno">414-453-5725</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Lead Score</td>
                    <td id="leadscoreno">154</td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Tags</td>
                    <td id="tags" class="hstack gap-1">
                      <BBadge variant="primary-subtle" class="bg-primary-subtle text-primary">Lead</BBadge>
                      <BBadge variant="primary-subtle" class="bg-primary-subtle text-primary">Partner</BBadge>
                    </td>
                  </tr>
                  <tr>
                    <td class="fw-medium" scope="row">Last Contacted</td>
                    <td><span id="lastdate">15 Dec, 2021 </span><small class="text-muted" id="lasttime">08:58AM</small>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <!-- add contact modal  -->
    <BModal v-model="addContactModal" id="showmodal" hide-footer title-class="exampleModalLabel"
      header-class="bg-primary-subtle p-3" class="v-modal-custom" centered
      :title="dataEdit ? 'Edit Contact' : 'Add Contact'">
      <b-form action="" id="addform" class="tablelist-form" autocomplete="off">
        <input type="hidden" id="id" />
        <BRow class="g-3">
          <BCol lg="12">
            <div class="text-center">
              <div class="position-relative d-inline-block">
                <div class="position-absolute  bottom-0 end-0">
                  <label for="customer-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="right"
                    aria-label="Select Image" data-bs-original-title="Select Image">
                    <div class="avatar-xs cursor-pointer">
                      <div class="avatar-title bg-light border rounded-circle text-muted">
                        <i class="ri-image-fill"></i>
                      </div>
                    </div>
                  </label>
                  <input class="form-control d-none" value="" id="customer-image-input" type="file"
                    accept="image/png, image/gif, image/jpeg">
                </div>
                <div class="avatar-lg p-1">
                  <div class="avatar-title bg-light rounded-circle">
                    <img :src="event.image_src || require('@/assets/images/users/user-dummy-img.jpg')" id="customer-img"
                      class="avatar-md rounded-circle object-fit-cover">
                  </div>
                </div>
              </div>
            </div>
            <div>
              <label for="name-field" class="form-label">Name</label>
              <input type="text" id="customername" class="form-control" placeholder="Enter name" v-model="event.name"
                :class="{ 'is-invalid': submitted && !event.name }" />
              <div class="invalid-feedback">Please enter a name.</div>
            </div>
          </BCol>
          <BCol lg="12">
            <div>
              <label for="company_name-field" class="form-label">Company Name</label>
              <input type="text" id="companyname" class="form-control" placeholder="Enter company name"
                v-model="event.company" :class="{ 'is-invalid': submitted && !event.company }" />
              <div class="invalid-feedback">Please enter a company name.</div>
            </div>
          </BCol>
          <BCol lg="12">
            <div>
              <label for="designation-field" class="form-label">Designation</label>
              <input type="text" id="designation-field" class="form-control" placeholder="Enter designation"
                v-model="event.designation" :class="{ 'is-invalid': submitted && !event.designation }" />
              <div class="invalid-feedback">Please enter a designation.</div>
            </div>
          </BCol>
          <BCol lg="12">
            <div>
              <label for="email_id-field" class="form-label">Email ID</label>
              <input type="text" id="emailid" class="form-control" placeholder="Enter email" v-model="event.email"
                :class="{ 'is-invalid': submitted && !event.email }" />
              <div class="invalid-feedback">Please enter a email.</div>
            </div>
          </BCol>
          <BCol lg="6">
            <div>
              <label for="phone-field" class="form-label">Phone</label>
              <input type="text" id="phone" class="form-control" placeholder="Enter phone no" v-model="event.phone"
                :class="{ 'is-invalid': submitted && !event.phone }" />
              <div class="invalid-feedback">Please enter a phone number.</div>
            </div>
          </BCol>
          <BCol lg="6">
            <div>
              <label for="lead_score-field" class="form-label">Lead Score</label>
              <input type="text" id="leadscore" class="form-control" placeholder="Enter value" v-model="event.lead_score"
                :class="{ 'is-invalid': submitted && !event.lead_score }" />
              <div class="invalid-feedback">Please enter a lead score.</div>
            </div>
          </BCol>
          <div>
            <label for="" class="form-label">Tags</label>
            <Multiselect mode="tags" :close-on-select="true" :searchable="true" :create-option="false"
              :options="tagoption" v-model="event.tags" :class="{ 'is-invalid': submitted && !event.tags }" />
            <div class="invalid-feedback">Please select a tags.</div>
          </div>
        </BRow>
        <div class="hstack gap-2 justify-content-end mt-3">
          <BButton type="button" variant="light" @click="addContactModal = false" id="edtclosemodal">Close</BButton>
          <BButton type="button" variant="success" id="add-btn" @click="handleSubmit">
            {{ dataEdit ? 'Update' : 'Add Contact' }}
          </BButton>
        </div>
      </b-form>
    </BModal>

    <!-- delete modal -->
    <BModal v-model="deleteModal" modal-class="zoomIn" hide-footer no-close-on-backdrop centered>
      <div class="mt-2 text-center">
        <lottie class="avatar-xl" colors="primary:#8c68cd,secondary:#f06548" :options="defaultOptions1" :height="100"
          :width="100" />
        <div class="mt-4 pt-2 fs-15 mx-4 mx-sm-5">
          <h4>You are about to delete a contact ?</h4>
          <p class="text-muted mx-4 mb-0">Deleting your contact will remove all of your information from our database.</p>
        </div>
      </div>
      <div class="d-flex gap-2 justify-content-center mt-4 mb-2">
        <button type="button" class="btn w-sm btn-light" @click="deleteModal = false">Close</button>
        <button type="button" class="btn w-sm btn-danger" id="delete-record" @click="deleteData">Yes, Delete It!</button>
      </div>
    </BModal>
  </Layout>
</template>