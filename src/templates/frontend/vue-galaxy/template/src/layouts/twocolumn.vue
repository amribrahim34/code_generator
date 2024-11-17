<script>
import router from "@/router";
import simplebar from "simplebar-vue";

import {
  layoutComputed
} from "@/state/helpers";
import Menu from "@/components/menu.vue";
import NavBar from "@/components/nav-bar";
import RightBar from "@/components/right-bar";
import Footer from "@/components/footer";

/**
 * Vertical layout
 */
export default {
  components: {
    NavBar,
    RightBar,
    Footer,
    Menu,
    simplebar
  },
  data() {
    return {
      isMenuCondensed: false,
      rmenu: localStorage.getItem('rmenu') ? localStorage.getItem('rmenu') : 'twocolumn',
    };
  },

  computed: {
    ...layoutComputed,
  },
  created: () => {
    document.body.removeAttribute("data-layout", "horizontal");
    document.body.removeAttribute("data-topbar", "dark");
    document.body.removeAttribute("data-layout-size", "boxed");
  },
  methods: {
    initActiveMenu() {
      const pathName = window.location.pathname;
      const ul = document.getElementById("navbar-nav");
      if (ul) {
        const items = Array.from(ul.querySelectorAll("a.nav-link"));
        let activeItems = items.filter((x) => x.classList.contains("active"));
        this.removeActivation(activeItems);
        let matchingMenuItem = items.find((x) => {
          return x.getAttribute("href") === pathName;
        });
        if (matchingMenuItem) {
          this.activateParentDropdown(matchingMenuItem);
        } else {
          var id = pathName.replace("/", "");
          if (id) document.body.classList.add("twocolumn-panel");
          this.activateIconSidebarActive(pathName);
        }
      }
    },

    updateMenu(e, event) {
      document.body.classList.remove("twocolumn-panel");
      const ul = document.getElementById("navbar-nav");
      if (ul) {
        const items = Array.from(ul.querySelectorAll(".show"));
        items.forEach((item) => {
          item.classList.remove("show");
        });
      }
      const icons = document.getElementById("two-column-menu");
      if (icons) {
        const activeIcons = Array.from(
          icons.querySelectorAll(".nav-icon.active")
        );
        activeIcons.forEach((item) => {
          item.classList.remove("active");
        });
      }
      document.getElementById(e).classList.add("show");
      event.target.classList.add("active")
      this.activateIconSidebarActive("#" + e);
    },

    removeActivation(items) {
      items.forEach((item) => {
        if (item.classList.contains("menu-link")) {
          if (!item.classList.contains("active")) {
            item.setAttribute("aria-expanded", false);
          }
          item.nextElementSibling.classList.remove("show");
        }
        if (item.classList.contains("nav-link")) {
          if (item.nextElementSibling) {
            item.nextElementSibling.classList.remove("show");
          }
          item.setAttribute("aria-expanded", false);
        }
        item.classList.remove("active");
      });
    },

    activateIconSidebarActive(id) {
      var menu = document.querySelector(
        "#two-column-menu .simplebar-content-wrapper a[href='" +
        id +
        "'].nav-icon"
      );
      if (menu !== null) {
        menu.classList.add("active");
      }
    },

    activateParentDropdown(item) {
      // navbar-nav menu add active
      item.classList.add("active");
      let parentCollapseDiv = item.closest(".collapse.menu-dropdown");
      if (parentCollapseDiv) {
        // to set aria expand true remaining
        parentCollapseDiv.classList.add("show");
        parentCollapseDiv.parentElement.children[0].classList.add("active");
        parentCollapseDiv.parentElement.children[0].setAttribute("aria-expanded", "true");
        if (parentCollapseDiv.parentElement.closest(".collapse.menu-dropdown")) {
          if (parentCollapseDiv.parentElement.closest(".collapse.menu-dropdown").previousElementSibling) {
            if (parentCollapseDiv.parentElement.closest(".collapse.menu-dropdown").previousElementSibling.parentElement.closest(".collapse.menu-dropdown")) {
              const grandparent = parentCollapseDiv.parentElement.closest(".collapse.menu-dropdown").previousElementSibling.parentElement.closest(".collapse.menu-dropdown");
              this.activateIconSidebarActive("#" + grandparent.getAttribute("id"));
              grandparent.classList.add("show");
            }
          }
          this.activateIconSidebarActive("#" + parentCollapseDiv.parentElement.closest(".collapse.menu-dropdown")
            .getAttribute("id"));

          parentCollapseDiv.parentElement.closest(".collapse").classList.add("show");
          if (parentCollapseDiv.parentElement.closest(".collapse").previousElementSibling)
            parentCollapseDiv.parentElement.closest(".collapse").previousElementSibling.classList.add("active");
          return false;
        }
        this.activateIconSidebarActive("#" + parentCollapseDiv.getAttribute("id"));
        return false;
      }
      return false;
    },

    toggleMenu() {
      document.body.classList.toggle("sidebar-enable");

      if (window.screen.width >= 992) {
        // eslint-disable-next-line no-unused-vars
        router.afterEach((routeTo, routeFrom) => {
          document.body.classList.remove("sidebar-enable");
          document.body.classList.remove("vertical-collpsed");
        });
        document.body.classList.toggle("vertical-collpsed");
      } else {
        // eslint-disable-next-line no-unused-vars
        router.afterEach((routeTo, routeFrom) => {
          document.body.classList.remove("sidebar-enable");
        });
        document.body.classList.remove("vertical-collpsed");
      }
      this.isMenuCondensed = !this.isMenuCondensed;
    },

    toggleRightSidebar() {
      document.body.classList.toggle("right-bar-enabled");
    },

    hideRightSidebar() {
      document.body.classList.remove("right-bar-enabled");
    },
  },

  mounted() {
    this.initActiveMenu();
    if (this.rmenu == 'vertical' && this.layoutType == 'twocolumn') {
      document.documentElement.setAttribute("data-layout", "vertical");
    }
    document.getElementById('overlay').addEventListener('click', () => {
      document.body.classList.remove('vertical-sidebar-enable');
    });

    window.addEventListener("resize", () => {
      if (this.layoutType == 'twocolumn') {
        var windowSize = document.documentElement.clientWidth;
        if (windowSize < 767) {
          document.documentElement.setAttribute("data-layout", "vertical");
          this.rmenu = 'vertical';
          localStorage.setItem('rmenu', 'vertical');
        } else {
          document.documentElement.setAttribute("data-layout", "twocolumn");
          this.rmenu = 'twocolumn';
          localStorage.setItem('rmenu', 'twocolumn');
          setTimeout(() => {
            this.initActiveMenu();
          }, 50);

        }
      }
    });
    if (document.querySelectorAll(".navbar-nav .collapse")) {
      let collapses = document.querySelectorAll(".navbar-nav .collapse");

      collapses.forEach((collapse) => {
        // Hide sibling collapses on `show.bs.collapse`
        collapse.addEventListener("show.bs.collapse", (e) => {
          e.stopPropagation();
          let closestCollapse = collapse.parentElement.closest(".collapse");
          if (closestCollapse) {
            let siblingCollapses =
              closestCollapse.querySelectorAll(".collapse");
            siblingCollapses.forEach((siblingCollapse) => {
              if (siblingCollapse.classList.contains("show")) {
                siblingCollapse.classList.remove("show");
                siblingCollapse.parentElement.firstChild.setAttribute("aria-expanded", "false");
              }
            });
          } else {
            let getSiblings = (elem) => {
              // Setup siblings array and get the first sibling
              let siblings = [];
              let sibling = elem.parentNode.firstChild;
              // Loop through each sibling and push to the array
              while (sibling) {
                if (sibling.nodeType === 1 && sibling !== elem) {
                  siblings.push(sibling);
                }
                sibling = sibling.nextSibling;
              }
              return siblings;
            };
            let siblings = getSiblings(collapse.parentElement);
            siblings.forEach((item) => {
              if (item.childNodes.length > 2) {
                item.firstElementChild.setAttribute("aria-expanded", "false");
                item.firstElementChild.classList.remove("active");
              }
              let ids = item.querySelectorAll("*[id]");
              ids.forEach((item1) => {
                item1.classList.remove("show");
                item1.parentElement.firstChild.setAttribute("aria-expanded", "false");
                item1.parentElement.firstChild.classList.remove("active");
                if (item1.childNodes.length > 2) {
                  let val = item1.querySelectorAll("ul li a");

                  val.forEach((subitem) => {
                    if (subitem.hasAttribute("aria-expanded"))
                      subitem.setAttribute("aria-expanded", "false");
                  });
                }
              });
            });
          }
        });

        // Hide nested collapses on `hide.bs.collapse`
        collapse.addEventListener("hide.bs.collapse", (e) => {
          e.stopPropagation();
          let childCollapses = collapse.querySelectorAll(".collapse");
          childCollapses.forEach((childCollapse) => {
            let childCollapseInstance = childCollapse;
            childCollapseInstance.classList.remove("show");
            childCollapseInstance.parentElement.firstChild.setAttribute("aria-expanded", "false");
          });
        });
      });
    }

  },
};
</script>

<template>
  <div id="layout-wrapper">
    <NavBar />
    <div>
      <!-- ========== Left Sidebar Start ========== -->
      <!-- ========== App Menu ========== -->
      <div class="app-menu navbar-menu">
        <!-- LOGO -->
        <div class="navbar-brand-box">
          <!-- Dark Logo-->
          <router-link to="/" class="logo logo-dark">
            <span class="logo-sm">
              <img src="@/assets/images/logo-sm.png" alt="" height="22" />
            </span>
            <span class="logo-lg">
              <img src="@/assets/images/logo-dark.png" alt="" height="17" />
            </span>
          </router-link>
          <!-- Light Logo-->
          <router-link to="/" class="logo logo-light">
            <span class="logo-sm">
              <img src="@/assets/images/logo-sm.png" alt="" height="22" />
            </span>
            <span class="logo-lg">
              <img src="@/assets/images/logo-light.png" alt="" height="17" />
            </span>
          </router-link>
          <button type="button" class=" btn btn-sm p-0 fs-20 header-item float-end btn-vertical-sm-hover"
            id="vertical-hover">
            <i class="ri-record-circle-line"></i>
          </button>
        </div>

        <div id="scrollbar" v-if="rmenu == 'twocolumn'">
          <BContainer fluid>
            <div id="two-column-menu">
              <simplebar class="twocolumn-iconview list-unstyled">
                <a class="logo"><img src="@/assets/images/logo-sm.png" alt="Logo" height="22" /></a>
                <li>
                  <a href="#sidebarDashboards" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarDashboards', $event)">
                    <i class="ri-dashboard-2-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarApps" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarApps', $event)">
                    <i class="ri-apps-2-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarAuth" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarAuth', $event)">
                    <i class="ri-account-circle-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarPages" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarPages', $event)">
                    <i class="ri-pages-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarlanding" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarlanding', $event)">
                    <i class="ri-rocket-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarUI" class="nav-icon" role="button" @click.prevent="updateMenu('sidebarUI', $event)">
                    <i class="ri-pencil-ruler-2-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarAdvanceUI" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarAdvanceUI', $event)">
                    <i class="ri-stack-line"></i>
                  </a>
                </li>
                <li class="nav-item">
                  <router-link class="nav-icon" to="/widgets">
                    <i class="ri-honour-line"></i>
                  </router-link>
                </li>
                <li>
                  <a href="#sidebarForms" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarForms', $event)">
                    <i class="ri-file-list-3-line"></i>
                  </a>
                </li>
                <li>
                  <a href="#sidebarTables" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarTables', $event)">
                    <i class="ri-layout-grid-line"></i>
                  </a>
                </li>

                <li>
                  <a href="#sidebarCharts" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarCharts', $event)">
                    <i class="ri-pie-chart-line"></i>
                  </a>
                </li>

                <li>
                  <a href="#sidebarIcons" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarIcons', $event)">
                    <i class="ri-compasses-2-line"></i>
                  </a>
                </li>

                <li>
                  <a href="#sidebarMaps" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarMaps', $event)">
                    <i class="ri-map-pin-line"></i>
                  </a>
                </li>

                <li>
                  <a href="#sidebarMultilevel" class="nav-icon" role="button"
                    @click.prevent="updateMenu('sidebarMultilevel', $event)">
                    <i class="ri-share-line"></i>
                  </a>
                </li>
              </simplebar>
            </div>
            <template v-if="layoutType === 'twocolumn'">
              <simplebar class="navbar-nav" id="navbar-nav">
                <li class="menu-title">
                  <span data-key="t-menu"> {{ $t("t-menu") }}</span>
                </li>
                <li class="nav-item">

                  <div class="collapse menu-dropdown" id="sidebarDashboards">

                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/dashboard/analytics" class="nav-link custom-abc" data-key="t-analytics">
                          {{ $t("t-analytics") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/dashboard/crm" class="nav-link" data-key="t-crm">
                          {{ $t("t-crm") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/" class="nav-link" data-key="t-ecommerce">
                          {{ $t("t-ecommerce") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/dashboard/crypto" class="nav-link" data-key="t-crypto">
                          {{ $t("t-crypto") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/dashboard/projects" class="nav-link" data-key="t-projects">
                          {{ $t("t-projects") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/dashboard/nft" class="nav-link" data-key="t-nft">
                          {{ $t("t-nft") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/dashboard/job" class="nav-link" data-key="t-job">
                          {{ $t("t-job") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>
                <!-- end Dashboard Menu -->
                <li class="nav-item">

                  <div class="collapse menu-dropdown" id="sidebarApps">

                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <a class="nav-link" href="#sidebarCalendar" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebaremail" data-key="t-calendar">
                          {{ $t("t-calendar") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarCalendar">
                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/main-calendar" class="nav-link" data-key="t-main-calender"> {{
                                $t("t-main-calender") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/month-grid" class="nav-link" data-key="t-month-grid"> {{
                                $t("t-month-grid") }} </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">
                        <router-link to="/chat" class="nav-link" data-key="t-chat">
                          {{ $t("t-chat") }}
                        </router-link>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebaremail" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebaremail" data-key="t-projects">
                          {{ $t("t-email") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebaremail">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/mailbox" class="nav-link" data-key="t-mailbox">
                                {{ $t("t-mailbox") }}
                              </router-link>
                            </li>
                            <li class="nav-item">

                              <a class="nav-link" href="#sidebarsubemail" data-bs-toggle="collapse" role="button"
                                aria-expanded="false" aria-controls="sidebarsubemail" data-key="t-projects">
                                {{ $t("t-email-templates") }}
                              </a>
                              <div class="collapse menu-dropdown" id="sidebarsubemail">

                                <ul class="nav nav-sm flex-column">
                                  <li class="nav-item">
                                    <router-link to="/email/email-basic" class="nav-link" data-key="t-products">
                                      {{ $t("t-basic-action") }}
                                    </router-link>
                                  </li>
                                  <li class="nav-item">
                                    <router-link to="/email/email-ecommerce" class="nav-link" data-key="t-products">
                                      {{ $t("t-ecommerce-action") }}
                                    </router-link>
                                  </li>
                                </ul>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarEcommerce" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarEcommerce" data-key="t-ecommerce">
                          {{ $t("t-ecommerce") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarEcommerce">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/ecommerce/products" class="nav-link" data-key="t-products">
                                {{ $t("t-products") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/product-details" class="nav-link" data-key="t-product-Details">
                                {{ $t("t-product-Details") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/add-product" class="nav-link" data-key="t-create-product">
                                {{ $t("t-create-product") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/orders" class="nav-link" data-key="t-orders">
                                {{ $t("t-orders") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/order-details" class="nav-link" data-key="t-order-details">
                                {{ $t("t-order-details") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/customers" class="nav-link" data-key="t-customers">
                                {{ $t("t-customers") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/shopping-cart" class="nav-link" data-key="t-shopping-cart">
                                {{ $t("t-shopping-cart") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/checkout" class="nav-link" data-key="t-checkout">
                                {{ $t("t-checkout") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/sellers" class="nav-link" data-key="t-sellers">
                                {{ $t("t-sellers") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/ecommerce/seller-details" class="nav-link" data-key="t-sellers-details">
                                {{ $t("t-sellers-details") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarProjects" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarProjects" data-key="t-projects">
                          {{ $t("t-projects") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarProjects">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/apps/projects-list" class="nav-link" data-key="t-list">
                                {{ $t("t-list") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/projects-overview" class="nav-link" data-key="t-overview">
                                {{ $t("t-overview") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/projects-create" class="nav-link" data-key="t-create-project">
                                {{ $t("t-create-project") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarTasks" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarTasks" data-key="t-tasks">
                          {{ $t("t-tasks") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarTasks">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/apps/tasks-kanban" class="nav-link" data-key="t-kanbanboard">
                                {{ $t("t-kanbanboard") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/tasks-list-view" class="nav-link" data-key="t-list-view">
                                {{ $t("t-list-view") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/tasks-details" class="nav-link" data-key="t-task-details">
                                {{ $t("t-task-details") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarCRM" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarCRM" data-key="t-crm">
                          {{ $t("t-crm") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarCRM">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/apps/crm-contacts" class="nav-link" data-key="t-contacts">
                                {{ $t("t-contacts") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/crm-companies" class="nav-link" data-key="t-companies">
                                {{ $t("t-companies") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/crm-deals" class="nav-link" data-key="t-deals">
                                {{ $t("t-deals") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/crm-leads" class="nav-link" data-key="t-leads">
                                {{ $t("t-leads") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarCrypto" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarCrypto" data-key="t-crypto">
                          {{ $t("t-crypto") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarCrypto">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/crypto/transactions" class="nav-link" data-key="t-transactions">
                                {{ $t("t-transactions") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/crypto/buy-sell" class="nav-link" data-key="t-buy-sell">
                                {{ $t("t-buy-sell") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/crypto/orders" class="nav-link" data-key="t-orders">
                                {{ $t("t-orders") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/crypto/wallet" class="nav-link" data-key="t-my-wallet">
                                {{ $t("t-my-wallet") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/crypto/ico" class="nav-link" data-key="t-ico-list">
                                {{ $t("t-ico-list") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/crypto/kyc" class="nav-link" data-key="t-kyc-application">
                                {{ $t("t-kyc-application") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarInvoices" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarInvoices" data-key="t-invoices">
                          {{ $t("t-invoices") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarInvoices">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/invoices/list" class="nav-link" data-key="t-list-view">
                                {{ $t("t-list-view") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/invoices/detail" class="nav-link" data-key="t-details">
                                {{ $t("t-details") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/invoices/create" class="nav-link" data-key="t-create-invoice">
                                {{ $t("t-create-invoice") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarTickets" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarTickets" data-key="t-supprt-tickets">
                          {{ $t("t-supprt-tickets") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarTickets">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/apps/tickets-list" class="nav-link" data-key="t-list-view">
                                {{ $t("t-list-view") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/tickets-details" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-ticket-details") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#nftmarketplace" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="nftmarketplace" data-key="t-supprt-tickets">
                          {{ $t("t-nft-marketplace") }}
                        </a>
                        <div class="collapse menu-dropdown" id="nftmarketplace">


                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/apps/nft-marketplace" class="nav-link" data-key="t-list-view">
                                {{ $t("t-marketplace") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-explore" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-explore-now") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-auction" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-live-auction") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-item-detail" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-item-details") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-collection" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-collections") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-creators" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-creators") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-ranking" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-ranking") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-wallet" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-wallet-connect") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/apps/nft-create" class="nav-link" data-key="t-ticket-details">
                                {{ $t("t-create-nft") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">
                        <router-link to="/apps-file-manager" class="nav-link" data-key="t-file-manager">
                          {{ $t("t-file-manager") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/apps-todo" class="nav-link" data-key="t-to-do">
                          {{ $t("t-to-do") }}
                        </router-link>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#jobs" data-bs-toggle="collapse" role="button" aria-expanded="false"
                          aria-controls="jobs" data-key="t-jobs">
                          {{ $t("t-jobs") }}
                        </a>
                        <div class="collapse menu-dropdown" id="jobs">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/jobs/statistics" class="nav-link" data-key="t-job-statistics">
                                {{ $t("t-statistics") }}
                              </router-link>
                            </li>

                            <li class="nav-item">

                              <a class="nav-link" href="#sidebarjoblist" data-bs-toggle="collapse" role="button"
                                aria-expanded="false" aria-controls="sidebarjoblist" data-key="t-job-list">
                                {{ $t("t-job-lists") }}
                              </a>
                              <div class="collapse menu-dropdown" id="sidebarjoblist">

                                <ul class="nav nav-sm flex-column">
                                  <li class="nav-item">
                                    <router-link to="/jobs/lists" class="nav-link" data-key="t-lists">
                                      {{ $t("t-list") }}
                                    </router-link>
                                  </li>
                                  <li class="nav-item">
                                    <router-link to="/jobs/grid-lists" class="nav-link" data-key="t-grid">
                                      {{ $t("t-grid") }}
                                    </router-link>
                                  </li>
                                  <li class="nav-item">
                                    <router-link to="/jobs/details" class="nav-link" data-key="t-overview">
                                      {{ $t("t-overview") }}
                                    </router-link>
                                  </li>
                                </ul>
                              </div>
                            </li>

                            <li class="nav-item">

                              <a class="nav-link" href="#sidebarcandidatelists" data-bs-toggle="collapse" role="button"
                                aria-expanded="false" aria-controls="sidebarcandidatelists" data-key="t-job-list">
                                {{ $t("t-candidate-lists") }}
                              </a>
                              <div class="collapse menu-dropdown" id="sidebarcandidatelists">

                                <ul class="nav nav-sm flex-column">
                                  <li class="nav-item">
                                    <router-link to="/jobs/candidate-lists" class="nav-link" data-key="t-lists">
                                      {{ $t("t-list-view") }}
                                    </router-link>
                                  </li>
                                  <li class="nav-item">
                                    <router-link to="/jobs/candidate-grid" class="nav-link" data-key="t-grid">
                                      {{ $t("t-grid-view") }}
                                    </router-link>
                                  </li>
                                </ul>
                              </div>
                            </li>
                            <li class="nav-item">
                              <router-link to="/jobs/application" class="nav-link" data-key="t-application">
                                {{ $t("t-application") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/jobs/new" class="nav-link" data-key="t-new">
                                {{ $t("t-new-job") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/jobs/companies-list" class="nav-link" data-key="t-companies-list">
                                {{ $t("t-companies-list") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/jobs/categories" class="nav-link" data-key="t-job-categories">
                                {{ $t("t-job-categories") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">
                        <router-link to="/apps-api-key" class="nav-link" data-key="t-api-key">
                          {{ $t("t-api-key") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarAuth">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarSignIn" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarSignIn" data-key="t-signin">{{ $t("t-signin") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarSignIn">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/signin-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/signin-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarSignUp" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarSignUp" data-key="t-signup">{{ $t("t-signup") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarSignUp">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/signup-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/signup-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>

                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarResetPass" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarResetPass" data-key="t-password-reset">
                          {{ $t("t-password-reset") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarResetPass">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/reset-pwd-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/reset-pwd-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarcreatepass" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarcreatepass" data-key="t-password-reset">
                          {{ $t("t-password-create") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarcreatepass">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/create-pwd-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/create-pwd-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarLockScreen" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarLockScreen" data-key="t-lock-screen">
                          {{ $t("t-lock-screen") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarLockScreen">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/lockscreen-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/lockscreen-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>

                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarLogout" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarLogout" data-key="t-logout">
                          {{ $t("t-logout") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarLogout">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/logout-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/logout-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarSuccessMsg" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarSuccessMsg" data-key="t-success-message">
                          {{ $t("t-success-message") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarSuccessMsg">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/success-msg-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/success-msg-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarTwoStep" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarTwoStep" data-key="t-two-step-verification">
                          {{ $t("t-two-step-verification") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarTwoStep">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/twostep-basic" class="nav-link" data-key="t-basic">
                                {{ $t("t-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/twostep-cover" class="nav-link" data-key="t-cover">
                                {{ $t("t-cover") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarErrors" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarErrors" data-key="t-errors">
                          {{ $t("t-errors") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarErrors">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/auth/404-basic" class="nav-link" data-key="t-404-basic">
                                {{ $t("t-404-basic") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/404-cover" class="nav-link" data-key="t-404-cover">
                                {{ $t("t-404-cover") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/404" class="nav-link" data-key="t-404-alt">
                                {{ $t("t-404-alt") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/500" class="nav-link" data-key="t-500">
                                {{ $t("t-500") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/auth/ofline" class="nav-link" data-key="t-500">
                                {{ $t("t-offline-page") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarPages">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/pages/starter" class="nav-link" data-key="t-starter">{{ $t("t-starter") }}
                        </router-link>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarProfile" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarProfile" data-key="t-profile">{{ $t("t-profile")
                          }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarProfile">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/pages/profile" class="nav-link" data-key="t-simple-page">
                                {{ $t("t-simple-page") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/pages/profile-setting" class="nav-link" data-key="t-settings">
                                {{ $t("t-settings") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/team" class="nav-link" data-key="t-team">
                          {{ $t("t-team") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/timeline" class="nav-link" data-key="t-timeline">
                          {{ $t("t-timeline") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/faqs" class="nav-link" data-key="t-faqs">
                          {{ $t("t-faqs") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/pricing" class="nav-link" data-key="t-pricing">
                          {{ $t("t-pricing") }}
                        </router-link>
                      </li>

                      <li class="nav-item">
                        <router-link to="/pages/maintenance" class="nav-link" data-key="t-maintenance">
                          {{ $t("t-maintenance") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/coming-soon" class="nav-link" data-key="t-coming-soon">
                          {{ $t("t-coming-soon") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/sitemap" class="nav-link" data-key="t-sitemap">
                          {{ $t("t-sitemap") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/search-results" class="nav-link" data-key="t-search-results">
                          {{ $t("t-search-results") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/privacy-policy" class="nav-link" data-key="t-privacy-policy">
                          {{ $t("t-privacy-policy") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/pages/term-conditions" class="nav-link" data-key="t-term-conditions">
                          {{ $t("t-term-conditions") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>
                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarlanding">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/landing" target="_blank" class="nav-link" data-key="t-one-page">{{
                          $t("t-one-page") }}</router-link>
                      </li>

                      <li class="nav-item">
                        <router-link to="/nft-landing" target="_blank" class="nav-link" data-key="t-nft-landing">{{
                          $t("t-nft-landing") }}</router-link>
                      </li>

                      <li class="nav-item">
                        <router-link to="/job-landing" target="_blank" class="nav-link" data-key="t-nft-landing">{{
                          $t("t-job") }}</router-link>
                      </li>

                    </ul>
                  </div>
                </li>
                <li class="nav-item">
                  <div class="collapse menu-dropdown mega-dropdown-menu" id="sidebarUI">
                    <BRow>
                      <BCol lg="4">
                        <ul class="nav nav-sm flex-column">
                          <li class="nav-item">
                            <router-link to="/ui/alerts" class="nav-link" data-key="t-alerts">{{ $t("t-alerts") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/badges" class="nav-link" data-key="t-badges">{{ $t("t-badges") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/buttons" class="nav-link" data-key="t-buttons">{{ $t("t-buttons") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/colors" class="nav-link" data-key="t-colors">{{ $t("t-colors") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/cards" class="nav-link" data-key="t-cards">{{ $t("t-cards") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/carousel" class="nav-link" data-key="t-carousel">{{ $t("t-carousel") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/dropdowns" class="nav-link" data-key="t-dropdowns">
                              {{ $t("t-dropdowns") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/grid" class="nav-link" data-key="t-grid">{{ $t("t-grid") }}
                            </router-link>
                          </li>
                        </ul>
                      </BCol>
                      <BCol lg="4">
                        <ul class="nav nav-sm flex-column">
                          <li class="nav-item">
                            <router-link to="/ui/images" class="nav-link" data-key="t-images">{{ $t("t-images") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/tabs" class="nav-link" data-key="t-tabs">{{ $t("t-tabs") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/accordions" class="nav-link" data-key="t-accordion-collapse">
                              {{ $t("t-accordion-collapse") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/modals" class="nav-link" data-key="t-modals">{{ $t("t-modals") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/offcanvas" class="nav-link" data-key="t-offcanvas">
                              {{ $t("t-offcanvas") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/placeholders" class="nav-link" data-key="t-placeholders">
                              {{ $t("t-placeholders") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/progress" class="nav-link" data-key="t-progress">{{ $t("t-progress") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/notifications" class="nav-link" data-key="t-notifications">
                              {{ $t("t-notifications") }}</router-link>
                          </li>
                        </ul>
                      </BCol>
                      <BCol lg="4">
                        <ul class="nav nav-sm flex-column">
                          <li class="nav-item">
                            <router-link to="/ui/media" class="nav-link" data-key="t-media-object">
                              {{ $t("t-media-object") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/embed-video" class="nav-link" data-key="t-embed-video">
                              {{ $t("t-embed-video") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/typography" class="nav-link" data-key="t-typography">
                              {{ $t("t-typography") }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/lists" class="nav-link" data-key="t-lists">{{ $t("t-lists")
                            }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/links" class="nav-link" data-key="t-links">{{ $t("t-links") }}
                              <BBadge variant="success" class="badge-pill" data-key="t-new">{{ $t("t-new") }}</BBadge>
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/general" class="nav-link" data-key="t-general">{{ $t("t-general")
                            }}</router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/ribbons" class="nav-link" data-key="t-ribbons">{{ $t("t-ribbons") }}
                            </router-link>
                          </li>
                          <li class="nav-item">
                            <router-link to="/ui/utilities" class="nav-link" data-key="t-utilities">
                              {{ $t("t-utilities") }}</router-link>
                          </li>
                        </ul>
                      </BCol>
                    </BRow>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarAdvanceUI">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/advance-ui/sweetalerts" class="nav-link" data-key="t-sweet-alerts">
                          {{ $t("t-sweet-alerts") }}</router-link>
                      </li>

                      <li class="nav-item">
                        <router-link to="/advance-ui/scrollbar" class="nav-link" data-key="t-scrollbar">
                          {{ $t("t-scrollbar") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/advance-ui/animation" class="nav-link" data-key="t-animation">
                          {{ $t("t-animation") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/advance-ui/swiper" class="nav-link" data-key="t-swiper-slider">
                          {{ $t("t-swiper-slider") }}</router-link>
                      </li>

                      <li class="nav-item">
                        <router-link to="/advance-ui/highlight" class="nav-link" data-key="t-highlight">
                          {{ $t("t-highlight") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/advance-ui/scrollspy" class="nav-link" data-key="t-scrollSpy">
                          {{ $t("t-scrollSpy") }}</router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarForms">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/form/elements" class="nav-link" data-key="t-basic-elements">
                          {{ $t("t-basic-elements") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/select" class="nav-link" data-key="t-form-select">
                          {{ $t("t-form-select") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/checkboxs-radios" class="nav-link" data-key="t-checkboxs-radios">
                          {{ $t("t-checkboxs-radios") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/pickers" class="nav-link" data-key="t-pickers">
                          {{ $t("t-pickers") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/masks" class="nav-link" data-key="t-input-masks">
                          {{ $t("t-input-masks") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/advanced" class="nav-link" data-key="t-advanced">
                          {{ $t("t-advanced") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/range-sliders" class="nav-link" data-key="t-range-slider">
                          {{ $t("t-range-slider") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/validation" class="nav-link" data-key="t-validation">
                          {{ $t("t-validation") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/wizard" class="nav-link" data-key="t-wizard">{{ $t("t-wizard") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/editors" class="nav-link" data-key="t-editors">{{ $t("t-editors") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/file-uploads" class="nav-link" data-key="t-file-uploads">
                          {{ $t("t-file-uploads") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/form/layouts" class="nav-link" data-key="t-form-layouts">
                          {{ $t("t-form-layouts") }}</router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarTables">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/tables/basic" class="nav-link" data-key="t-basic-tables">
                          {{ $t("t-basic-tables") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/tables/gridjs" class="nav-link" data-key="t-grid-js">{{ $t("t-grid-js") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarCharts">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarApexcharts" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarApexcharts" data-key="t-apexcharts">
                          {{ $t("t-apexcharts") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarApexcharts">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <router-link to="/charts/apex-line" class="nav-link" data-key="t-line">
                                {{ $t("t-line") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-area" class="nav-link" data-key="t-area">
                                {{ $t("t-area") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-column" class="nav-link" data-key="t-column">
                                {{ $t("t-column") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-bar" class="nav-link" data-key="t-bar">
                                {{ $t("t-bar") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-mixed" class="nav-link" data-key="t-mixed">{{ $t("t-mixed")
                              }}</router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-range-area" class="nav-link" data-key="t-range-area">{{
                                $t("t-range-area") }}
                                <BBadge variant="success" class="badge-pill" data-key="t-new">{{ $t("t-new") }}</BBadge>
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-funnel" class="nav-link" data-key="t-funnel">{{ $t("t-funnel")
                              }}
                                <BBadge variant="success" class="badge-pill" data-key="t-new">{{ $t("t-new") }}</BBadge>
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-candlestick" class="nav-link" data-key="t-candlstick">
                                {{ $t("t-candlstick") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-boxplot" class="nav-link" data-key="t-boxplot">
                                {{ $t("t-boxplot") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-bubble" class="nav-link" data-key="t-bubble">
                                {{ $t("t-bubble") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-scatter" class="nav-link" data-key="t-scatter">
                                {{ $t("t-scatter") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-heatmap" class="nav-link" data-key="t-heatmap">
                                {{ $t("t-heatmap") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-treemap" class="nav-link" data-key="t-treemap">
                                {{ $t("t-treemap") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-pie" class="nav-link" data-key="t-pie">
                                {{ $t("t-pie") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-radialbar" class="nav-link" data-key="t-radialbar">
                                {{ $t("t-radialbar") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-radar" class="nav-link" data-key="t-radar">
                                {{ $t("t-radar") }}
                              </router-link>
                            </li>
                            <li class="nav-item">
                              <router-link to="/charts/apex-polararea" class="nav-link" data-key="t-polar-area">
                                {{ $t("t-polar-area") }}
                              </router-link>
                            </li>
                          </ul>
                        </div>
                      </li>
                      <li class="nav-item">
                        <router-link to="/charts/chartjs" class="nav-link" data-key="t-chartjs">{{ $t("t-chartjs") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/charts/echart" class="nav-link" data-key="t-echarts">{{ $t("t-echarts") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarIcons">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/icons/remix" class="nav-link" data-key="t-remix">{{ $t("t-remix") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/icons/boxicons" class="nav-link" data-key="t-boxicons">{{ $t("t-boxicons") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/icons/materialdesign" class="nav-link" data-key="t-material-design">
                          {{ $t("t-material-design") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/icons/lineawesome" class="nav-link" data-key="t-line-awesome">
                          {{ $t("t-line-awesome") }}</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/icons/feather" class="nav-link" data-key="t-feather">{{ $t("t-feather") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/icons/crypto" class="nav-link" data-key="t-feather">{{ $t("t-crypto-svg")
                        }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarMaps">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">
                        <router-link to="/maps/google" class="nav-link" data-key="t-google">
                          {{ $t("t-google") }}
                        </router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/maps/leaflet" class="nav-link" data-key="t-leaflet">
                          {{ $t("t-leaflet") }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </li>

                <li class="nav-item">
                  <div class="collapse menu-dropdown" id="sidebarMultilevel">
                    <ul class="nav nav-sm flex-column">
                      <li class="nav-item">

                        <a class="nav-link" data-key="t-level-1.1">

                          {{ $t("t-level-1.1") }}
                        </a>
                      </li>
                      <li class="nav-item">

                        <a class="nav-link" href="#sidebarAccount" data-bs-toggle="collapse" role="button"
                          aria-expanded="false" aria-controls="sidebarAccount" data-key="t-level-1.2">
                          {{ $t("t-level-1.2") }}
                        </a>
                        <div class="collapse menu-dropdown" id="sidebarAccount">

                          <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                              <a class="nav-link" data-key="t-level-2.1">
                                {{ $t("t-level-2.1") }}
                              </a>
                            </li>
                            <li class="nav-item">

                              <a class="nav-link" href="#sidebarCrm" data-bs-toggle="collapse" role="button"
                                aria-expanded="false" aria-controls="sidebarCrm" data-key="t-level-2.2">
                                {{ $t("t-level-2.2") }}
                              </a>
                              <div class="collapse menu-dropdown" id="sidebarCrm">

                                <ul class="nav nav-sm flex-column">
                                  <li class="nav-item">
                                    <a class="nav-link" data-key="t-level-3.1">
                                      {{ $t("t-level-3.1") }}
                                    </a>
                                  </li>
                                  <li class="nav-item">
                                    <a class="nav-link" data-key="t-level-3.2">
                                      {{ $t("t-level-3.2") }}
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </li>
                    </ul>
                  </div>
                </li>
              </simplebar>
            </template>
          </BContainer>
        </div>

        <simplebar id="scrollbar" class="h-100" ref="scrollbar" v-if="rmenu == 'vertical'">
          <Menu></Menu>
        </simplebar>

        <div class="sidebar-background"></div>
      </div>
      <!-- Left Sidebar End -->
      <!-- Vertical Overlay-->
      <div class="vertical-overlay" id="overlay"></div>
    </div>
    <!-- ============================================================== -->
    <!-- Start Page Content here -->
    <!-- ============================================================== -->

    <div class="main-content">
    <div class="page-content">
      <!-- Start Content-->
      <BContainer fluid>
        <slot />
      </BContainer>
    </div>
    <Footer />
  </div>
  <RightBar />
</div></template>