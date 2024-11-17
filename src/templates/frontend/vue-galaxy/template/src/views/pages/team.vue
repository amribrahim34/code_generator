<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import Swal from "sweetalert2";

export default {
  data() {
    return {
      modalShow: false,
      teammember: [
        {
          "id": 12,
          "coverImg": require("@/assets/images/small/img-9.jpg"),
          "bookmark": false,
          "memberImg": require("@/assets/images/users/avatar-2.jpg"),
          "memberName": "Nancy Martino",
          "position": "Team Leader & HR",
          "projects": "225",
          "tasks": "197"
        }, {
          "id": 11,
          "coverImg": require("@/assets/images/small/img-12.jpg"),
          "bookmark": true,
          "memberImg": "",
          "nickname": "HB",
          "memberName": "Henry Baird",
          "position": "Full Stack Developer",
          "projects": "352",
          "tasks": "376"
        }, {
          "id": 10,
          "coverImg": require("@/assets/images/small/img-11.jpg"),
          "bookmark": false,
          "memberImg": require("@/assets/images/users/avatar-3.jpg"),
          "memberName": "Frank Hook",
          "position": "Project Manager",
          "projects": "164",
          "tasks": "182"
        }, {
          "id": 9,
          "coverImg": require("@/assets/images/small/img-1.jpg"),
          "bookmark": true,
          "memberImg": require("@/assets/images/users/avatar-8.jpg"),
          "memberName": "Jennifer Carter",
          "position": "UI/UX Designer",
          "projects": "241",
          "tasks": "204"
        }, {
          "id": 8,
          "coverImg": require("@/assets/images/small/img-10.jpg"),
          "bookmark": false,
          "memberImg": "",
          "nickname": "ME",
          "memberName": "Megan Elmore",
          "position": "Team Leader & Web Developer",
          "projects": "201",
          "tasks": "263"
        }, {
          "id": 7,
          "coverImg": require("@/assets/images/small/img-2.jpg"),
          "bookmark": false,
          "memberImg": require("@/assets/images/users/avatar-4.jpg"),
          "memberName": "Alexis Clarke",
          "position": "Backend Developer",
          "projects": "132",
          "tasks": "147"
        }, {
          "id": 6,
          "coverImg": require("@/assets/images/small/img-4.jpg"),
          "bookmark": true,
          "memberImg": "",
          "nickname": "NC",
          "memberName": "Nathan Cole",
          "position": "Front-End Developer",
          "projects": "352",
          "tasks": "376"
        }, {
          "id": 5,
          "coverImg": require("@/assets/images/small/img-7.jpg"),
          "bookmark": true,
          "memberImg": require("@/assets/images/users/avatar-6.jpg"),
          "memberName": "Joseph Parker",
          "position": "Full Stack Developer",
          "projects": "64",
          "tasks": "93"
        }, {
          "id": 4,
          "coverImg": require("@/assets/images/small/img-3.jpg"),
          "bookmark": false,
          "memberImg": require("@/assets/images/users/avatar-5.jpg"),
          "memberName": "Erica Kernan",
          "position": "Web Designer",
          "projects": "345",
          "tasks": "298"
        }, {
          "id": 3,
          "coverImg": require("@/assets/images/small/img-5.jpg"),
          "bookmark": true,
          "memberImg": "",
          "nickname": "DP",
          "memberName": "Donald Palmer",
          "position": "Wed Developer",
          "projects": "97",
          "tasks": "135"
        }, {
          "id": 2,
          "coverImg": require("@/assets/images/small/img-8.jpg"),
          "bookmark": false,
          "memberImg": require("@/assets/images/users/avatar-7.jpg"),
          "memberName": "Jack Gough",
          "position": "React Js Developer",
          "projects": "87",
          "tasks": "121"
        }, {
          "id": 1,
          "coverImg": require("@/assets/images/small/img-6.jpg"),
          "bookmark": false,
          "memberImg": "",
          "nickname": "MW",
          "memberName": "Marie Ward",
          "position": "Backend Developer",
          "projects": "145",
          "tasks": "210"
        }
      ]
    };
  },
  methods: {
    deletefolder(event) {
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
          this.teammember.splice(this.teammember.indexOf(event), 1);
          Swal.fire("Deleted!", "Your file has been deleted.", "success");
        }
      });
    },
    toggleFavourite(ele) {
      ele.target.closest('.favourite-btn').classList.toggle("active");
    }
  },
  mounted() {

    var list = document.querySelectorAll(".team-list");
    function onButtonGroupClick(event) {
      if (event.target.id === 'list-view-button' || event.target.parentElement.id === 'list-view-button') {
        document.getElementById("list-view-button").classList.add("active");
        document.getElementById("grid-view-button").classList.remove("active");
        Array.from(list).forEach(function (el) {
          el.classList.add("list-view-filter");
          el.classList.remove("grid-view-filter");
        });

      } else {
        document.getElementById("grid-view-button").classList.add("active");
        document.getElementById("list-view-button").classList.remove("active");
        Array.from(list).forEach(function (el) {
          el.classList.remove("list-view-filter");
          el.classList.add("grid-view-filter");
        });
      }
    }
    if (list) {
      var buttonGroups = document.querySelectorAll('.filter-button');
      if (buttonGroups) {
        Array.from(buttonGroups).forEach(function (btnGroup) {
          btnGroup.addEventListener('click', onButtonGroupClick);
        });
      }
    }


  },
  components: {
    Layout,
    PageHeader,
  },
};
</script>
    
<template>
  <Layout>
    <PageHeader title="Team" pageTitle="Pages" />
    <BCard no-body>
      <BCardBody>
        <BRow class="g-2">
          <BCol sm="4">
            <div class="search-box">
              <input type="text" class="form-control" id="searchMemberList"
                placeholder="Search for name or designation...">
              <i class="ri-search-line search-icon"></i>
            </div>
          </BCol>
          <BCol sm="auto" class="ms-auto">
            <div class="list-grid-nav hstack gap-1">
              <BButton type="button" id="grid-view-button"
                class="btn btn-soft-secondary nav-link btn-icon fs-14 active filter-button"><i class="ri-grid-fill"></i>
              </BButton>
              <BButton type="button" id="list-view-button"
                class="btn btn-soft-secondary nav-link  btn-icon fs-14 filter-button"><i class="ri-list-unordered"></i>
              </BButton>
              <BDropdown variant="soft-primary" right toggle-class="arrow-none" class="btn-icon fs-14" no-caret>
                <template #button-content><i class="ri-more-2-fill"></i>
                </template>
                <BDropdownItem href="#">
                  All
                </BDropdownItem>
                <BDropdownItem href="#">
                  Last Week
                </BDropdownItem>
                <BDropdownItem href="#">
                  Last Month
                </BDropdownItem>
                <BDropdownItem href="#">
                  Last Year
                </BDropdownItem>
              </BDropdown>
              <BButton variant="primary" class="addMembers-modal" @click="modalShow = !modalShow"><i
                  class="ri-add-fill me-1 align-bottom"></i> Add Members</BButton>
            </div>
          </BCol>
        </BRow>
      </BCardBody>
    </Bcard>

    <BRow>
      <BCol lg="12">
        <div>
          <div id="teamlist">
            <BRow class="team-list grid-view-filter" id="team-member-list">

              <BCol v-for="(teamData, index) of this.teammember" :key="index">
                <BCard no-body class="team-box">
                  <div class="team-cover">
                    <img :src="teamData.coverImg" alt="" class="img-fluid" />
                  </div>
                  <BCardBody class="p-4">
                    <BRow class="align-items-center team-row">
                      <BCol class="team-settings">
                        <BRow>
                          <BCol>
                            <div class="flex-shrink-0 me-2">
                              <BButton type="button" variant="light" class="btn-icon rounded-circle btn-sm favourite-btn"
                                :class="{
                                  'active': teamData.bookmark == true
                                }" @click="toggleFavourite">
                                <i class="ri-star-fill fs-14"></i>
                              </BButton>
                            </div>
                          </BCol>

                          <div class="dropdown col text-end">
                            <BDropdown variant="link" toggle-class="m-n3 arrow-none text-light" menu-class="dropdown-menu-end">
                              <template #button-content>
                                <i class="ri-more-fill fs-17"></i>
                              </template>
                              <BDropdownItem class="edit-list" @click="modalShow = !modalShow">
                                <i class="ri-pencil-line me-2 align-bottom text-muted"></i>
                                Edit
                              </BDropdownItem>
                              <BDropdownItem class="remove-list" @click="deletefolder(teamData)">
                                <i class="ri-delete-bin-5-line me-2 align-bottom text-muted"></i>Remove
                              </BDropdownItem>
                            </BDropdown>
                          </div>

                        </BRow>
                      </BCol>
                      <BCol lg="4" col>
                        <div class="team-profile-img">
                          <div class="avatar-lg img-thumbnail rounded-circle flex-shrink-0">

                            <img :src="teamData.memberImg" alt="" class="member-img img-fluid d-block rounded-circle"
                              v-if="teamData.memberImg" />
                            <div class="avatar-title border bg-light text-primary rounded-circle text-uppercase"
                              v-if="!teamData.memberImg">{{ teamData.nickname }}</div>
                          </div>
                          <div class="team-content">
                            <BLink class="member-name" data-bs-toggle="offcanvas" href="#member-overview"
                              aria-controls="member-overview">
                              <h5 class="fs-16 mb-1">{{ teamData.memberName }}</h5>
                            </BLink>
                            <p class="text-muted member-designation mb-0">{{ teamData.position }}</p>
                          </div>
                        </div>
                      </BCol>
                      <BCol lg="4" col>
                        <BRow class="text-muted text-center">
                          <BCol cols="6" class="border-end border-end-dashed">
                            <h5 class="mb-1 projects-num">{{ teamData.projects }}</h5>
                            <p class="text-muted mb-0">Projects</p>
                          </BCol>
                          <BCol cols="6">
                            <h5 class="mb-1 tasks-num">{{ teamData.tasks }}</h5>
                            <p class="text-muted mb-0">Tasks</p>
                          </BCol>
                        </BRow>
                      </BCol>
                      <BCol col lg="2">
                        <div class="text-end">
                          <router-link to="/pages/profile" class="btn btn-light view-btn">View Profile</router-link>
                        </div>
                      </BCol>
                    </BRow>
                  </BCardBody>
                </BCard>
              </BCol>
            </BRow>
            <div class="text-center mb-3">
              <BLink href="javascript:void(0);" class="text-success"><i
                  class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i> Load More </BLink>
            </div>
          </div>
          <div class="py-4 mt-4 text-center" id="noresult" style="display: none;">
            <lord-icon src="https://cdn.lordicon.com/msoeawqm.json" trigger="loop"
              colors="primary:#405189,secondary:#0ab39c" style="width:72px;height:72px"></lord-icon>
            <h5 class="mt-4">Sorry! No Result Found</h5>
          </div>
          <!-- Modal -->

          <BModal v-model="modalShow" hide-footer hide-header hide-header-close content-class="border-0"
            class="v-modal-custom" centered>
            <form autocomplete="off" id="memberlist-form" class="needs-validation" novalidate>
              <BRow>
                <BCol lg="12">
                  <input type="hidden" id="memberid-input" class="form-control" value="">
                  <div class="px-1 pt-1">
                    <div class="modal-team-cover position-relative mb-0 mt-n4 mx-n4 rounded-top overflow-hidden">
                      <img src="@/assets/images/small/img-9.jpg" alt="" id="cover-img" class="img-fluid" />
                      <div class="d-flex position-absolute start-0 end-0 top-0 p-3">
                        <div class="flex-grow-1">
                          <h5 class="modal-title text-white" id="createMemberLabel">Add New Members</h5>
                        </div>
                        <div class="flex-shrink-0">
                          <div class="d-flex gap-3 align-items-center">
                            <div>
                              <label for="cover-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="top"
                                title="Select Cover Image">
                                <div class="avatar-xs">
                                  <div class="avatar-title bg-light border rounded-circle text-muted cursor-pointer">
                                    <i class="ri-image-fill"></i>
                                  </div>
                                </div>
                              </label>
                              <input class="form-control d-none" value="" id="cover-image-input" type="file"
                                accept="image/png, image/gif, image/jpeg">
                            </div>
                            <BButton type="button" class="btn-close btn-close-white" id="createMemberBtn-close"
                              @click="modalShow = !modalShow"></BButton>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="text-center mb-4 mt-n5 pt-2">
                    <div class="position-relative d-inline-block">
                      <div class="position-absolute bottom-0 end-0">
                        <label for="member-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="right"
                          title="Select Member Image">
                          <div class="avatar-xs">
                            <div class="avatar-title bg-light border rounded-circle text-muted cursor-pointer">
                              <i class="ri-image-fill"></i>
                            </div>
                          </div>
                        </label>
                        <input class="form-control d-none" value="" id="member-image-input" type="file"
                          accept="image/png, image/gif, image/jpeg">
                      </div>
                      <div class="avatar-lg">
                        <div class="avatar-title bg-light rounded-circle">
                          <img src="@/assets/images/users/user-dummy-img.jpg" id="member-img"
                            class="avatar-md rounded-circle h-auto" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="mb-3">
                    <label for="teammembersName" class="form-label">Name</label>
                    <input type="text" class="form-control" id="teammembersName" placeholder="Enter name" required>
                    <div class="invalid-feedback">Please Enter a member name.</div>
                  </div>

                  <div class="mb-4">
                    <label for="designation" class="form-label">Designation</label>
                    <input type="text" class="form-control" id="designation" placeholder="Enter designation" required>
                    <div class="invalid-feedback">Please Enter a designation.</div>
                  </div>
                  <input type="hidden" id="project-input" class="form-control" value="">
                  <input type="hidden" id="task-input" class="form-control" value="">

                  <div class="hstack gap-2 justify-content-end">
                    <BButton type="button" variant="light" @click="modalShow = false">Close</BButton>
                    <BButton type="submit" variant="success" id="addNewMember">Add Member</BButton>
                  </div>
                </BCol>
              </BRow>
            </form>
          </BModal>

          <div class="offcanvas offcanvas-end border-0" tabindex="-1" id="member-overview">
            <div class="offcanvas-body profile-offcanvas p-0">
              <div class="team-cover">
                <img src="@/assets/images/small/img-9.jpg" alt="" class="img-fluid" />
              </div>
              <div class="p-3">
                <div class="team-settings">
                  <BRow>
                    <BCol>
                      <button type="button" class="btn btn-light btn-icon rounded-circle btn-sm favourite-btn "> <i
                          class="ri-star-fill fs-14"></i> </button>
                    </BCol>
                    <BCol class="text-end dropdown">
                      <BLink href="javascript:void(0);" id="dropdownMenuLink14" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <i class="ri-more-fill fs-17"></i>
                      </BLink>
                      <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuLink14">
                        <li><BLink class="dropdown-item" href="javascript:void(0);"><i
                              class="ri-star-line me-2 align-middle"></i>Favorites</BLink></li>
                        <li><BLink class="dropdown-item" href="javascript:void(0);"><i
                              class="ri-delete-bin-5-line me-2 align-middle"></i>Delete</BLink></li>
                      </ul>
                    </BCol>
                  </BRow>
                </div>
              </div>
              <div class="p-3 text-center">
                <img src="@/assets/images/users/avatar-2.jpg" alt=""
                  class="avatar-lg img-thumbnail rounded-circle mx-auto profile-img">
                <div class="mt-3">
                  <h5 class="fs-15 profile-name">Nancy Martino</h5>
                  <p class="text-muted profile-designation">Team Leader & HR</p>
                </div>
                <div class="hstack gap-2 justify-content-center mt-4">
                  <div class="avatar-xs">
                    <BLink href="javascript:void(0);" class="avatar-title bg-secondary-subtle text-secondary rounded fs-16">
                      <i class="ri-slack-fill"></i>
                    </BLink>
                  </div>
                  <div class="avatar-xs">
                    <BLink href="javascript:void(0);" class="avatar-title bg-info-subtle text-info rounded fs-16">
                      <i class="ri-linkedin-fill"></i>
                    </BLink>
                  </div>
                  <div class="avatar-xs">
                    <BLink href="javascript:void(0);" class="avatar-title bg-danger-subtle text-danger rounded fs-16">
                      <i class="ri-dribbble-fill"></i>
                    </BLink>
                  </div>
                </div>
              </div>
              <BRow class="g-0 text-center">
                <BCol cols="6">
                  <div class="p-3 border border-dashed border-start-0">
                    <h5 class="mb-1 profile-project">124</h5>
                    <p class="text-muted mb-0">Projects</p>
                  </div>
                </BCol>
                <BCol cols="6">
                  <div class="p-3 border border-dashed border-start-0">
                    <h5 class="mb-1 profile-task">81</h5>
                    <p class="text-muted mb-0">Tasks</p>
                  </div>
                </BCol>
              </BRow>
              <div class="p-3">
                <h5 class="fs-15 mb-3">Personal Details</h5>
                <div class="mb-3">
                  <p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Number</p>
                  <h6>+(256) 2451 8974</h6>
                </div>
                <div class="mb-3">
                  <p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Email</p>
                  <h6>nancymartino@email.com</h6>
                </div>
                <div>
                  <p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Location</p>
                  <h6 class="mb-0">Carson City - USA</h6>
                </div>
              </div>
              <div class="p-3 border-top">
                <h5 class="fs-15 mb-4">File Manager</h5>
                <div class="d-flex mb-3">
                  <div class="flex-shrink-0 avatar-xs">
                    <div class="avatar-title bg-danger-subtle text-danger rounded fs-16">
                      <i class="ri-image-2-line"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="mb-1"><BLink href="javascript:void(0);">Images</BLink></h6>
                    <p class="text-muted mb-0">4469 Files</p>
                  </div>
                  <div class="text-muted">
                    12 GB
                  </div>
                </div>
                <div class="d-flex mb-3">
                  <div class="flex-shrink-0 avatar-xs">
                    <div class="avatar-title bg-secondary-subtle text-secondary rounded fs-16">
                      <i class="ri-file-zip-line"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="mb-1"><BLink href="javascript:void(0);">Documents</BLink></h6>
                    <p class="text-muted mb-0">46 Files</p>
                  </div>
                  <div class="text-muted">
                    3.46 GB
                  </div>
                </div>
                <div class="d-flex mb-3">
                  <div class="flex-shrink-0 avatar-xs">
                    <div class="avatar-title bg-success-subtle text-success rounded fs-16">
                      <i class="ri-live-line"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="mb-1"><BLink href="javascript:void(0);">Media</BLink></h6>
                    <p class="text-muted mb-0">124 Files</p>
                  </div>
                  <div class="text-muted">
                    4.3 GB
                  </div>
                </div>
                <div class="d-flex">
                  <div class="flex-shrink-0 avatar-xs">
                    <div class="avatar-title bg-primary-subtle text-primary rounded fs-16">
                      <i class="ri-error-warning-line"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="mb-1"><BLink href="javascript:void(0);">Others</BLink></h6>
                    <p class="text-muted mb-0">18 Files</p>
                  </div>
                  <div class="text-muted">
                    846 MB
                  </div>
                </div>
              </div>
            </div>
            <div class="offcanvas-foorter border p-3 hstack gap-3 text-center position-relative">
              <BButton variant="light" class="w-100"><i class="ri-question-answer-fill align-bottom ms-1"></i> Send
                Message</BButton>
              <router-link to="/pages/profile" class="btn btn-primary w-100"><i class="ri-user-3-fill align-bottom ms-1"></i>
                View Profile</router-link>
            </div>
          </div>
        </div>
      </BCol>
    </BRow>
  </Layout>
</template>
    