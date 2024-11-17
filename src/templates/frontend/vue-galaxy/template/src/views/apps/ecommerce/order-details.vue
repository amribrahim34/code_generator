<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import animationData from "@/components/widgets/uetqnvvg.json";
import Lottie from "@/components/widgets/lottie.vue";

export default {
  data() {
    return {
      orderSummary: [
        {
          id: 1,
          img: require("@/assets/images/products/img-8.png"),
          product: "Sweatshirt for Men (Pink)",
          price: 119.99,
          quantity: 2,
          size: "M",
          color: "Pink"
        },
        {
          id: 2,
          img: require("@/assets/images/products/img-7.png"),
          product: "Noise NoiseFit Endure Smart Watch",
          price: 94.99,
          quantity: 1,
          size: "32.5mm",
          color: "Black"
        },
        {
          id: 3,
          img: require("@/assets/images/products/img-3.png"),
          product: "350 ml Glass Grocery Container",
          price: 24.99,
          quantity: 1,
          size: "350 ml",
          color: "White"
        },
      ],
      defaultOptions: { animationData: animationData },
    };
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Order Details" pageTitle="Ecommerce" />
    <BRow>
      <BCol xl="9">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex align-items-center">
              <h5 class="card-title flex-grow-1 mb-0">Order #VL2667</h5>
              <div class="flex-shrink-0">
                <router-link to="/invoices/detail" class="btn btn-primary btn-sm"><i
                    class="ri-download-2-fill align-middle me-1"></i>
                  Invoice</router-link>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <div class="table-responsive table-card">
              <table class="table table-nowrap align-middle table-borderless mb-0">
                <thead class="table-light text-muted">
                  <tr>
                    <th scope="col">Product Details</th>
                    <th scope="col">Item Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Rating</th>
                    <th scope="col" class="text-end">Total Amount</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) of orderSummary" :key="index">
                    <td>
                      <div class="d-flex">
                        <div class="flex-shrink-0 avatar-md bg-light rounded p-1">
                          <img :src="item.img" alt="" class="img-fluid d-block" />
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h5 class="fs-15">
                            <router-link to="/ecommerce/product-details" class="link-primary">{{ item.product }}
                            </router-link>
                          </h5>
                          <p class="text-muted mb-0">
                            Color: <span class="fw-medium">{{ item.color }}</span>
                          </p>
                          <p class="text-muted mb-0">
                            Size: <span class="fw-medium">{{ item.size }}</span>
                          </p>
                        </div>
                      </div>
                    </td>
                    <td>${{ item.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>
                      <div class="text-warning fs-15">
                        <i class="ri-star-fill"></i><i class="ri-star-fill"></i><i class="ri-star-fill"></i><i
                          class="ri-star-fill"></i><i class="ri-star-half-fill"></i>
                      </div>
                    </td>
                    <td class="fw-medium text-end">$239.98</td>
                  </tr>
                  <tr class="border-top border-top-dashed">
                    <td colspan="3"></td>
                    <td colspan="2" class="fw-medium p-0">
                      <table class="table table-borderless mb-0">
                        <tbody>
                          <tr>
                            <td>Sub Total :</td>
                            <td class="text-end">$359.96</td>
                          </tr>
                          <tr>
                            <td>
                              Discount
                              <span class="text-muted">(VELZON15)</span> : :
                            </td>
                            <td class="text-end">-$53.99</td>
                          </tr>
                          <tr>
                            <td>Shipping Charge :</td>
                            <td class="text-end">$65.00</td>
                          </tr>
                          <tr>
                            <td>Estimated Tax :</td>
                            <td class="text-end">$44.99</td>
                          </tr>
                          <tr class="border-top border-top-dashed">
                            <th scope="row">Total (USD) :</th>
                            <th class="text-end">$415.96</th>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardHeader>
            <div class="d-sm-flex align-items-center">
              <h5 class="card-title flex-grow-1 mb-0">Order Status</h5>
              <div class="flex-shrink-0 mt-2 mt-sm-0">
                <BLink href="javascript:void(0);" class="btn btn-soft-primary btn-sm mt-2 mt-sm-0"><i
                    class="ri-map-pin-line align-middle me-1"></i> Change
                  Address</BLink>
                <BLink href="javascript:void(0);" class="btn btn-soft-secondary btn-sm mt-2 mt-sm-0 ms-1"><i
                    class="mdi mdi-archive-remove-outline align-middle me-1"></i>
                  Cancel Order</BLink>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <div class="profile-timeline">
              <div class="accordion accordion-flush" id="accordionFlushExample">
                <div class="accordion-item border-0">
                  <div class="accordion-header" id="headingOne">
                    <BLink class="accordion-button p-2 shadow-none" v-b-toggle.collapseOne>
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0 avatar-xs">
                          <div class="avatar-title bg-primary rounded-circle">
                            <i class="ri-shopping-bag-line"></i>
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h6 class="fs-15 mb-0 fw-semibold">
                            Order Placed -
                            <span class="fw-normal">Wed, 15 Dec 2021</span>
                          </h6>
                        </div>
                      </div>
                    </BLink>
                  </div>
                  <BCollapse id="collapseOne" visible>
                    <div class="accordion-body ms-2 ps-5 pt-0">
                      <h6 class="mb-1">An order has been placed.</h6>
                      <p class="text-muted">Wed, 15 Dec 2021 - 05:34PM</p>
                      <h6 class="mb-1">Seller has processed your order.</h6>
                      <p class="text-muted mb-0">Thu, 16 Dec 2021 - 5:48AM</p>
                    </div>
                  </BCollapse>
                </div>
                <div class="accordion-item border-0">
                  <div class="accordion-header" id="headingTwo">
                    <BLink class="accordion-button p-2 shadow-none" v-b-toggle.collapseTwo>
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0 avatar-xs">
                          <div class="avatar-title bg-primary rounded-circle">
                            <i class="mdi mdi-gift-outline"></i>
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h6 class="fs-15 mb-1 fw-semibold">
                            Packed -
                            <span class="fw-normal">Thu, 16 Dec 2021</span>
                          </h6>
                        </div>
                      </div>
                    </BLink>
                  </div>
                  <BCollapse id="collapseTwo" visible>
                    <div class="accordion-body ms-2 ps-5 pt-0">
                      <h6 class="mb-1">
                        Your Item has been picked up by courier partner
                      </h6>
                      <p class="text-muted mb-0">Fri, 17 Dec 2021 - 9:45AM</p>
                    </div>
                  </BCollapse>
                </div>
                <div class="accordion-item border-0">
                  <div class="accordion-header" id="headingThree">
                    <BLink class="accordion-button p-2 shadow-none" v-b-toggle.collapseThree>
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0 avatar-xs">
                          <div class="avatar-title bg-primary rounded-circle">
                            <i class="ri-truck-line"></i>
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h6 class="fs-15 mb-1 fw-semibold">
                            Shipping -
                            <span class="fw-normal">Thu, 16 Dec 2021</span>
                          </h6>
                        </div>
                      </div>
                    </BLink>
                  </div>
                  <BCollapse id="collapseThree" visible>
                    <div class="accordion-body ms-2 ps-5 pt-0">
                      <h6 class="fs-14">RQK Logistics - MFDS1400457854</h6>
                      <h6 class="mb-1">Your item has been shipped.</h6>
                      <p class="text-muted mb-0">Sat, 18 Dec 2021 - 4.54PM</p>
                    </div>
                  </BCollapse>
                </div>
                <div class="accordion-item border-0">
                  <div class="accordion-header" id="headingFour">
                    <BLink class="accordion-button p-2 shadow-none" data-bs-toggle="collapse" href="#collapseFour"
                      aria-expanded="false">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0 avatar-xs">
                          <div class="avatar-title bg-light text-primary rounded-circle">
                            <i class="ri-takeaway-fill"></i>
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h6 class="fs-14 mb-0 fw-semibold">
                            Out For Delivery
                          </h6>
                        </div>
                      </div>
                    </BLink>
                  </div>
                </div>
                <div class="accordion-item border-0">
                  <div class="accordion-header" id="headingFive">
                    <BLink class="accordion-button p-2 shadow-none" data-bs-toggle="collapse" href="#collapseFile"
                      aria-expanded="false">
                      <div class="d-flex align-items-center">
                        <div class="flex-shrink-0 avatar-xs">
                          <div class="avatar-title bg-light text-primary rounded-circle">
                            <i class="mdi mdi-package-variant"></i>
                          </div>
                        </div>
                        <div class="flex-grow-1 ms-3">
                          <h6 class="fs-14 mb-0 fw-semibold">Delivered</h6>
                        </div>
                      </div>
                    </BLink>
                  </div>
                </div>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol xl="3">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex">
              <h5 class="card-title flex-grow-1 mb-0">
                <i class="mdi mdi-truck-fast-outline align-middle me-1 text-muted"></i>
                Logistics Details
              </h5>
              <div class="flex-shrink-0">
                <BLink href="javascript:void(0);" class="badge bg-primary-subtle text-primary fs-11">Track Order</BLink>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <div class="text-center">
              <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions" :height="80" :width="80" />
              <h5 class="fs-16 mt-2">RQK Logistics</h5>
              <p class="text-muted mb-0">ID: MFDS1400457854</p>
              <p class="text-muted mb-0">Payment Mode : Debit Card</p>
            </div>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <div class="d-flex">
              <h5 class="card-title flex-grow-1 mb-0">Customer Details</h5>
              <div class="flex-shrink-0">
                <BLink href="javascript:void(0);" class="link-secondary">View Profile</BLink>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <ul class="list-unstyled mb-0 vstack gap-3">
              <li>
                <div class="d-flex align-items-center">
                  <div class="flex-shrink-0">
                    <img src="@/assets/images/users/avatar-3.jpg" alt="" class="avatar-sm rounded" />
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="fs-14 mb-1">Joseph Parkers</h6>
                    <p class="text-muted mb-0">Customer</p>
                  </div>
                </div>
              </li>
              <li>
                <i class="ri-mail-line me-2 align-middle text-muted fs-16"></i>josephparker@gmail.com
              </li>
              <li>
                <i class="ri-phone-line me-2 align-middle text-muted fs-16"></i>+(256) 245451 441
              </li>
            </ul>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">
              <i class="ri-map-pin-line align-middle me-1 text-muted"></i>
              Billing Address
            </h5>
          </BCardHeader>
          <BCardBody>
            <ul class="list-unstyled vstack gap-2 fs-13 mb-0">
              <li class="fw-medium fs-14">Joseph Parker</li>
              <li>+(256) 245451 451</li>
              <li>2186 Joyce Street Rocky Mount</li>
              <li>New York - 25645</li>
              <li>United States</li>
            </ul>
          </BCardBody>
        </BCard>
        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">
              <i class="ri-map-pin-line align-middle me-1 text-muted"></i>
              Shipping Address
            </h5>
          </BCardHeader>
          <BCardBody>
            <ul class="list-unstyled vstack gap-2 fs-13 mb-0">
              <li class="fw-medium fs-14">Joseph Parker</li>
              <li>+(256) 245451 451</li>
              <li>2186 Joyce Street Rocky Mount</li>
              <li>California - 24567</li>
              <li>United States</li>
            </ul>
          </BCardBody>
        </BCard>

        <BCard no-body>
          <BCardHeader>
            <h5 class="card-title mb-0">
              <i class="ri-secure-payment-line align-bottom me-1 text-muted"></i>
              Payment Details
            </h5>
          </BCardHeader>
          <BCardBody>
            <div class="d-flex align-items-center mb-2">
              <div class="flex-shrink-0">
                <p class="text-muted mb-0">Transactions:</p>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="mb-0">#VLZ124561278124</h6>
              </div>
            </div>
            <div class="d-flex align-items-center mb-2">
              <div class="flex-shrink-0">
                <p class="text-muted mb-0">Payment Method:</p>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="mb-0">Debit Card</h6>
              </div>
            </div>
            <div class="d-flex align-items-center mb-2">
              <div class="flex-shrink-0">
                <p class="text-muted mb-0">Card Holder Name:</p>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="mb-0">Joseph Parker</h6>
              </div>
            </div>
            <div class="d-flex align-items-center mb-2">
              <div class="flex-shrink-0">
                <p class="text-muted mb-0">Card Number:</p>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="mb-0">xxxx xxxx xxxx 2456</h6>
              </div>
            </div>
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0">
                <p class="text-muted mb-0">Total Amount:</p>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="mb-0">$415.96</h6>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
