<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { CheckCircleIcon, AlertOctagonIcon } from "@zhuowenli/vue-feather-icons";
import { CountTo } from "vue3-count-to";
import animationData from "@/components/widgets/msoeawqm.json";
import Lottie from "@/components/widgets/lottie.vue";
import Swal from "sweetalert2";

import { apiKeyList } from "@/common/data";

export default {
  data() {
    return {
      createApiModal: false,
      page: 1,
      perPage: 8,
      pages: [],
      apikeydata: apiKeyList,
      defaultOptions: {
        animationData: animationData
      },
    };
  },
  computed: {
    displayedPosts() {
      return this.paginate(this.apikeydata);
    },
    resultQuery() {
      if (this.searchQuery) {
        const search = this.searchQuery.toLowerCase();
        return this.displayedPosts.filter((data) => {
          return (
            data.name.toLowerCase().includes(search) ||
            data.designation.toLowerCase().includes(search) ||
            data.postDate.toLowerCase().includes(search) ||
            data.description.toLowerCase().includes(search) ||
            data.location.toLowerCase().includes(search)
          );
        });
      } else {
        return this.displayedPosts;
      }
    },
  },
  watch: {
    apikeydata() {
      this.setPages();
    },
  },
  created() {
    this.setPages();
  },
  methods: {
    setPages() {
      let numberOfPages = Math.ceil(this.apikeydata.length / this.perPage);
      this.pages = [];
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index);
      }
    },

    paginate(apikeydata) {
      let page = this.page;
      let perPage = this.perPage;
      let from = page * perPage - perPage;
      let to = page * perPage;
      return apikeydata.slice(from, to);
    },

    generateApiID() {
      var d = new Date().getTime();

      if (window.performance && typeof window.performance.now === "function") {
        d += performance.now();
      }

      var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : r & 0x3 | 0x8).toString(16);
      });

      return uuid;
    },

    onSort(column) {
      this.direction = this.direction === 'asc' ? 'desc' : 'asc';
      const sortedArray = [...this.apikeydata];
      sortedArray.sort((a, b) => {
        const res = a[column] < b[column] ? -1 : a[column] > b[column] ? 1 : 0;
        return this.direction === 'asc' ? res : -res;
      });
      this.apikeydata = sortedArray;
    },


    handleApikeydetails(e, item) {

      this.createApiModal = true;
      const modalHeader = document.querySelector('.exampleModalLabel');
      const createApibtn = document.getElementById('createApimodal-btn');
      const addbtn = document.getElementById('add-btn');
      const editbtn = document.getElementById('edit-btn');
      const apikeyelement = document.getElementById('apikey-element');

      const apikeyId = document.getElementById("apikeyId");
      const apikeyname = document.getElementById("api-key-name");
      const apikey = document.getElementById("api-key");
      if (e.target.id == "createApi-btn" || e.target.id == "addApi-btn") {
        document.getElementById("addform").reset();

        modalHeader.innerHTML = "Create API Key";
        createApibtn.style.display = 'block';
        apikeyelement.style.display = 'none';
        addbtn.style.display = 'none';
        editbtn.style.display = 'none';

      } else if (e.target.classList.contains("edit-item-btn")) {
        modalHeader.innerHTML = "Rename API name";
        createApibtn.style.display = 'none';
        addbtn.style.display = 'none';
        editbtn.style.display = 'block';
        apikeyelement.style.display = 'block';

        apikeyId.value = item.id;
        apikeyname.value = item.name;
        apikey.value = item.apikey;

      } else if (e.target.classList.contains("regenerate-api-btn")) {
        modalHeader.innerHTML = "Regenerate API";
        createApibtn.style.display = 'none';
        addbtn.style.display = 'none';
        editbtn.style.display = 'block';
        apikeyelement.style.display = 'block';

        apikeyId.value = item.id;
        apikeyname.value = item.name;
        apikey.value = this.generateApiID();

      } else {
        modalHeader.innerHTML = "Create API Key";
        if (apikeyname.value != (null || "")) {
          createApibtn.style.display = 'none';
          apikeyelement.style.display = 'block';
          addbtn.style.display = 'block';
          editbtn.style.display = 'none';
          apikey.value = this.generateApiID();
        } else {
          document.getElementById("api-key-error-msg").classList.remove("d-none");
          document.getElementById("api-key-error-msg").classList.add("d-block");

          setTimeout(() => {
            document.getElementById("api-key-error-msg").classList.add("d-none");
            document.getElementById("api-key-error-msg").classList.remove("d-block");
          }, "2000");

        }
      }
    },

    handleApiKeys() {
      var id = this.apikeydata.length + 1;
      var apikeyname = document.getElementById('api-key-name').value;
      var apikey = document.getElementById('api-key').value;

      if (document.querySelector('.exampleModalLabel').innerHTML == "Create API Key") {
        if (id != null && apikeyname != null && apikey != null) {
          const data = {
            id: id,
            name: apikeyname,
            createby: "Anna Adame",
            status: "Active",
            apikey: apikey,
            create_date: new Date().toUTCString().slice(5, 16),
            expiry_date: new Date().toUTCString().slice(5, 16)
          };
          document.getElementById("close-modal").click();
          this.apikeydata.unshift(data);
        }
        document.getElementById("addform").reset();
      } else if (document.querySelector('.exampleModalLabel').innerHTML == "Rename API name") {
        id = document.getElementById('apikeyId').value;

        this.apikeydata.forEach(element => {
          if (element.id.toString() == id.toString()) {
            element.name = apikeyname;
          }
        });
        document.getElementById("close-modal").click();
      } else {
        id = document.getElementById('apikeyId').value;

        this.apikeydata.forEach(element => {
          if (element.id.toString() == id.toString()) {
            element.apikey = apikey;
          }
        });
        document.getElementById("close-modal").click();
      }
    },

    deleteApikey(event) {
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
          this.apikeydata = this.apikeydata.filter((item) => {
            return item.id != event.id;
          });
          Swal.fire("Deleted!", "Your file has been deleted.", "success");
        }
      });
    },

    changestatus(data) { data.status == "Active" ? data.status = "Disable" : data.status = "Active"; }

  },
  components: {
    Layout,
    PageHeader,
    CountTo,
    CheckCircleIcon,
    AlertOctagonIcon,
    lottie: Lottie,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="API Key" pageTitle="Apps" />
    <BRow>
      <BCol lg="4">
        <BCard no-body class="card-height-100">
          <BCardBody>
            <h5 class="card-title mb-3">Developer Plan</h5>
            <div class="progress animated-progress custom-progress mb-1">
              <div class="progress-bar bg-secondary" role="progressbar" style="width: 38%" aria-valuenow="38" aria-valuemin="0"
                aria-valuemax="100"></div>
            </div>
            <p class="text-muted mb-2">You used 215 of 2000 of your API</p>
            <div class="text-end">
              <BLink class="btn btn-primary button create-btn btn-sm" type="button" id="createApi-btn"
                @click="(e) => handleApikeydetails(e)">Create API Key</BLink>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="4">
        <BCard no-body class="card-animate card-height-100">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-muted mb-0">Successful conversions</p>
                <h2 class="mt-4 ff-secondary fw-semibold">
                  <count-to :startVal='0' :endVal='50' :duration='5000'></count-to>
                </h2>
                <p class="mb-0 text-muted"><BBadge class="bg-light text-success mb-0"><i
                      class="ri-arrow-up-line align-middle"></i> 8.24 % </BBadge> 7 last week</p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-success-subtle rounded-circle fs-2">
                    <CheckCircleIcon width="24" height="24" class="text-success"></CheckCircleIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="4">
        <BCard no-body class="card-animate card-height-100">
          <BCardBody>
            <div class="d-flex justify-content-between">
              <div>
                <p class="fw-medium text-muted mb-0">Failed conversions</p>
                <h2 class="mt-4 ff-secondary fw-semibold">
                  <count-to :startVal='0' :endVal='8' :duration='5000'></count-to>
                </h2>
                <p class="mb-0 text-muted"><BBadge class="bg-light text-danger mb-0"><i
                      class="ri-arrow-down-line align-middle"></i> 25.87 % </BBadge> 7 last week</p>
              </div>
              <div>
                <div class="avatar-sm flex-shrink-0">
                  <span class="avatar-title bg-danger-subtle rounded-circle fs-2">
                    <AlertOctagonIcon width="24" height="24" class="text-danger"></AlertOctagonIcon>
                  </span>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="12">
        <BCard no-body id="apiKeyList">
          <BCardHeader class="d-flex align-items-center">
            <h5 class="card-title flex-grow-1 mb-0">API Keys</h5>
            <div class="d-flex gap-1 flex-wrap">
              <BButton variant="soft-danger" id="remove-actions" onClick="deleteMultiple()"><i
                  class="ri-delete-bin-2-line"></i>
              </BButton>
              <BLink class="btn btn-primary button create-btn" type="button" id="addApi-btn"
                @click="(e) => handleApikeydetails(e)"><i class="ri-add-line align-bottom me-1"></i>
                Add </BLink>
            </div>
          </BCardHeader>
          <BCardBody>
            <div>
              <div class="table-responsive table-card mb-3">
                <table class="table align-middle table-nowrap mb-0">
                  <thead class="table-light">
                    <tr>
                      <th scope="col" style="width: 50px;">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" id="checkAll" value="option">
                        </div>
                      </th>
                      <th class="sort d-none" data-sort="id" scope="col" @click="onSort('id')">Id</th>
                      <th class="sort" data-sort="name" scope="col" @click="onSort('name')">Name</th>
                      <th class="sort" data-sort="createBy" scope="col" @click="onSort('createby')">Created By</th>
                      <th class="sort" data-sort="apikey" scope="col" @click="onSort('apikey')">API Key</th>
                      <th class="sort" data-sort="status" scope="col" @click="onSort('status')">Status</th>
                      <th class="sort" data-sort="create_date" scope="col" @click="onSort('create_date')">Create Date</th>
                      <th class="sort" data-sort="expiry_date" scope="col" @click="onSort('expiry_date')">Expiry Date</th>
                      <th scope="col">Action</th>
                    </tr>
                  </thead>
                  <tbody class="list form-check-all">
                    <tr v-for="(data, index) of resultQuery" :key="index">
                      <th scope="row">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="chk_child" value="option1">
                        </div>
                      </th>
                      <td class="id" style="display:none;">
                        <BLink href="javascript:void(0);" class="fw-medium link-primary">{{ data.id }}</BLink>
                      </td>
                      <td class="name">{{ data.name }}</td>
                      <td class="createBy">{{ data.createby }}</td>
                      <td class="apikey">
                        <input type="text" class="form-control apikey-value" readonly="" :value="data.apikey">
                      </td>
                      <td class="status"><BBadge variant="bg-success-subtle text-success" :class="{
                        'bg-success-subtle text-success': data.status == 'Active',
                        'bg-danger-subtle text-danger': data.status == 'Disable',
                      }">{{ data.status }}</BBadge></td>
                      <td class="create_date">{{ data.create_date }}</td>
                      <td class="expiry_date">{{ data.expiry_date }}</td>
                      <td>
                        <BDropdown variant="soft-secondary" size="sm" toggle-class="arrow-none"
                          menu-class="dropdown-menu-end">
                          <template #button-content>
                            <i class="ri-more-fill align-middle"></i>
                          </template>
                          <BDropdownItem linkClass="edit-item-btn" id="edit-item-btn"
                            @click="(e) => handleApikeydetails(e, data)">
                            Rename
                          </BDropdownItem>
                          <BDropdownItem linkClass="regenerate-api-btn" id="regenerate-api-btn"
                            @click="(e) => handleApikeydetails(e, data)">
                            Regenerate Key
                          </BDropdownItem>
                          <BDropdownItem linkClass="disable-btn" id="disable-btn" href="javascript:void(0);"
                            @click="(e) => changestatus(data)">{{ data.status == "Active" ? "Disable" : "Active" }}
                          </BDropdownItem>
                          <BDropdownItem linkClass="remove-item-btn" href="#deleteApiKeyModal"
                            @click="deleteApikey(data)">
                            Delete
                          </BDropdownItem>
                        </BDropdown>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="noresult" v-if="resultQuery.length < 1">
                  <div class="text-center">
                    <lottie class="avatar-xl" colors="primary:#121331,secondary:#08a88a" :options="defaultOptions"
                      :height="75" :width="75" />
                    <h5 class="mt-2">Sorry! No Result Found</h5>
                    <p class="text-muted mb-0">We've searched more than 150+ API Keys We did not find any API for you
                      search.</p>
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
                  <BLink class="page-item pagination-next" href="#" @click="page++" :disabled="page >= pages.length">
                    Next
                  </BLink>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <!-- Modal -->
    <BModal v-model="createApiModal" id="showModal" title-class="exampleModalLabel" hide-footer class="v-modal-custom"
      centered no-close-on-backdrop>
      <BForm autocomplete="off" id="addform">
        <div id="api-key-error-msg" class="alert alert-danger py-2 d-none">Please enter api key name</div>
        <input type="hidden" id="apikeyId">
        <div class="mb-3">
          <label for="api-key-name" class="form-label">API Key Name <span class="text-danger">*</span></label>
          <input type="text" class="form-control" id="api-key-name" placeholder="Enter api key name">
        </div>
        <div class="mb-3" id="apikey-element" style="display: none;">
          <label for="api-key" class="form-label">API Key</label>
          <input type="text" class="form-control" id="api-key" disabled value="b5815DE8A7224438932eb296Z5">
        </div>
      </BForm>
      <div class="hstack gap-2 justify-content-end mt-3">
        <BButton type="button" variant="secondary" @click="createApiModal = false" id="close-modal">Close</BButton>
        <button type="button" class="btn btn-primary" id="createApimodal-btn"
          @click="(e) => handleApikeydetails(e)">Create API</button>
        <BButton type="button" variant="primary" id="add-btn" @click="handleApiKeys">Add</BButton>
        <BButton type="button" variant="primary" id="edit-btn" @click="handleApiKeys">Save Changes</BButton>
      </div>
    </BModal>
  </Layout>
</template>