<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

import animationData from "@/components/widgets/lupuorrc.json";
import Lottie from "@/components/widgets/lottie.vue";

export default {
  data() {
    return {
      defaultOptions: { animationData: animationData },
    }
  },
  components: {
    Layout,
    PageHeader,
    lottie: Lottie,
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Checkout" pageTitle="Ecommerce" />
    <BRow>
      <BCol class="col-xl-8">
        <BCard no-body>
          <BCardBody class="checkout-tab">
            <BForm action="#">
              <div class="step-arrow-nav mt-n3 mx-n3 mb-3">
                <BTabs nav-class="nav-pills nav-justified custom-nav">
                  <BTab active class="nav-item nav-link p-3">
                    <template #title>
                      <div class="fs-15">
                        <i class="
                      ri-user-2-line
                      fs-16
                      avatar-xs d-inline-flex align-items-center justify-content-center
                      bg-primary-subtle
                      text-primary
                      rounded-circle
                      align-middle
                      me-2
                      "></i>
                        Personal Info
                      </div>
                    </template>
                    <div>
                      <h5 class="mb-1">Billing Information</h5>
                      <p class="text-muted mb-4">
                        Please fill all information below
                      </p>
                    </div>

                    <div>
                      <BRow>
                        <BCol sm="6">
                          <div class="mb-3">
                            <label for="billinginfo-firstName" class="form-label">First Name</label>
                            <input type="text" class="form-control" id="billinginfo-firstName"
                              placeholder="Enter first name" value="" />
                          </div>
                        </BCol>

                        <BCol sm="6">
                          <div class="mb-3">
                            <label for="billinginfo-lastName" class="form-label">Last Name</label>
                            <input type="text" class="form-control" id="billinginfo-lastName"
                              placeholder="Enter last name" value="" />
                          </div>
                        </BCol>
                      </BRow>

                      <BRow>
                        <BCol sm="6">
                          <div class="mb-3">
                            <label for="billinginfo-email" class="form-label">Email
                              <span class="text-muted">(Optional)</span></label>
                            <input type="email" class="form-control" id="billinginfo-email" placeholder="Enter email" />
                          </div>
                        </BCol>

                        <BCol sm="6">
                          <div class="mb-3">
                            <label for="billinginfo-phone" class="form-label">Phone</label>
                            <input type="text" class="form-control" id="billinginfo-phone"
                              placeholder="Enter phone no." />
                          </div>
                        </BCol>
                      </BRow>

                      <div class="mb-3">
                        <label for="billinginfo-address" class="form-label">Address</label>
                        <textarea class="form-control" id="billinginfo-address" placeholder="Enter address"
                          rows="3"></textarea>
                      </div>

                      <BRow>
                        <BCol md="4">
                          <div class="mb-3">
                            <label for="country" class="form-label">Country</label>
                            <select class="form-select" id="country" data-plugin="choices">
                              <option value="">Select Country...</option>
                              <option selected>United States</option>
                            </select>
                          </div>
                        </BCol>

                        <BCol md="4">
                          <div class="mb-3">
                            <label for="state" class="form-label">State</label>
                            <select class="form-select" id="state" data-plugin="choices">
                              <option value="">Select State...</option>
                              <option value="Alabama">Alabama</option>
                              <option value="Alaska">Alaska</option>
                              <option value="American Samoa">
                                American Samoa
                              </option>
                              <option value="California" selected>
                                California
                              </option>
                              <option value="Colorado">Colorado</option>
                              <option value="District Of Columbia">
                                District Of Columbia
                              </option>
                              <option value="Florida">Florida</option>
                              <option value="Georgia">Georgia</option>
                              <option value="Guam">Guam</option>
                              <option value="Hawaii">Hawaii</option>
                              <option value="Idaho">Idaho</option>
                              <option value="Kansas">Kansas</option>
                              <option value="Louisiana">Louisiana</option>
                              <option value="Montana">Montana</option>
                              <option value="Nevada">Nevada</option>
                              <option value="New Jersey">New Jersey</option>
                              <option value="New Mexico">New Mexico</option>
                              <option value="New York">New York</option>
                            </select>
                          </div>
                        </BCol>

                        <BCol md="4">
                          <div class="mb-3">
                            <label for="zip" class="form-label">Zip Code</label>
                            <input type="text" class="form-control" id="zip" placeholder="Enter zip code" />
                          </div>
                        </BCol>
                      </BRow>

                      <div class="d-flex align-items-start gap-3 mt-3">
                        <BButton variant="primary" type="button" class="btn-label right ms-auto nexttab"
                          data-nexttab="pills-bill-address-tab">
                          <i class="
                            ri-truck-line
                            label-icon
                            align-middle
                            fs-16
                            ms-2
                          "></i>Proceed to Shipping
                        </BButton>
                      </div>
                    </div>
                  </BTab>
                  <BTab class="nav-item nav-link fs-15 p-3">
                    <template #title>
                      <div class="fs-15">
                        <i class="
                          ri-truck-line
                          fs-16
                          avatar-xs d-inline-flex align-items-center justify-content-center
                          bg-primary-subtle
                          text-primary
                          rounded-circle
                          align-middle
                          me-2
                        "></i>
                        Shipping Info
                      </div>
                    </template>
                    <div>
                      <h5 class="mb-1">Shipping Information</h5>
                      <p class="text-muted mb-4">
                        Please fill all information below
                      </p>
                    </div>

                    <div class="mt-4">
                      <div class="d-flex align-items-center mb-2">
                        <div class="flex-grow-1">
                          <h5 class="fs-14 mb-0">Saved Address</h5>
                        </div>
                        <div class="flex-shrink-0">
                          <BButton type="button" variant="primary" size="sm" class="mb-3">
                            Add Address
                          </BButton>
                        </div>
                      </div>
                      <BRow class="gy-3">
                        <BCol lg="4" sm="6">
                          <div class="form-check card-radio">
                            <input id="shippingAddress01" name="shippingAddress" type="radio" class="form-check-input"
                              checked />
                            <label class="form-check-label bg-transparent" for="shippingAddress01">
                              <span class="
                                mb-4
                                fw-semibold
                                d-block
                                text-muted text-uppercase
                              ">Home Address</span>

                              <span class="fs-14 mb-2 d-block">Marcus Alfaro</span>
                              <span class="
                                text-muted
                                fw-normal
                                text-wrap
                                mb-1
                                d-block
                              ">4739 Bubby Drive Austin, TX 78729</span>
                              <span class="text-muted fw-normal d-block">Mo. 012-345-6789</span>
                            </label>
                          </div>
                          <div class="
                            d-flex
                            flex-wrap
                            p-2
                            py-1
                            bg-light
                            rounded-bottom
                            border
                            mt-n1
                          ">
                            <div>
                              <BLink href="#" class="d-block text-body p-1 px-2">
                                <i class="ri-pencil-fill text-muted align-bottom me-1"></i>
                                Edit
                              </BLink>
                            </div>
                            <div>
                              <BLink href="#" class="d-block text-body p-1 px-2">
                                <i class="ri-delete-bin-fill text-muted align-bottom me-1"></i>
                                Remove
                              </BLink>
                            </div>
                          </div>
                        </BCol>
                        <BCol lg="4" sm="6">
                          <div class="form-check card-radio">
                            <input id="shippingAddress02" name="shippingAddress" type="radio" class="form-check-input" />
                            <label class="form-check-label bg-transparent" for="shippingAddress02">
                              <span class="
                                mb-4
                                fw-semibold
                                d-block
                                text-muted text-uppercase
                              ">Office Address</span>

                              <span class="fs-14 mb-2 d-block">James Honda</span>
                              <span class="
                                text-muted
                                fw-normal
                                text-wrap
                                mb-1
                                d-block
                              ">1246 Virgil Street Pensacola, FL 32501
                              </span>
                              <span class="text-muted fw-normal d-block">Mo. 012-345-6789</span>
                            </label>
                          </div>
                          <div class="
                            d-flex
                            flex-wrap
                            p-2
                            py-1
                            bg-light
                            rounded-bottom
                            border
                            mt-n1
                          ">
                            <div>
                              <BLink href="#" class="d-block text-body p-1 px-2">
                                <i class=" ri-pencil-fill text-muted align-bottom me-1"></i>
                                Edit
                              </BLink>
                            </div>
                            <div>
                              <BLink href="#" class="d-block text-body p-1 px-2"><i
                                  class="ri-delete-bin-fill text-muted align-bottom me-1"></i>
                                Remove</BLink>
                            </div>
                          </div>
                        </BCol>
                      </BRow>

                      <div class="mt-4">
                        <h5 class="fs-14 mb-3">Shipping Method</h5>

                        <BRow class="g-4">
                          <BCol lg="6">
                            <div class="form-check card-radio">
                              <input id="shippingMethod01" name="shippingMethod" type="radio" class="form-check-input"
                                checked />
                              <label class="form-check-label bg-transparent" for="shippingMethod01">
                                <span class="
                                  fs-20
                                  float-end
                                  mt-2
                                  text-wrap
                                  d-block
                                  fw-semibold
                                ">Free</span>
                                <span class="fs-14 mb-1 text-wrap d-block">Free Delivery</span>
                                <span class="text-muted fw-normal text-wrap d-block">Expected Delivery 3 to 5
                                  Days</span>
                              </label>
                            </div>
                          </BCol>
                          <BCol lg="6">
                            <div class="form-check card-radio">
                              <input id="shippingMethod02" name="shippingMethod" type="radio" class="form-check-input"
                                checked />
                              <label class="form-check-label" for="shippingMethod02">
                                <span class="
                                  fs-20
                                  float-end
                                  mt-2
                                  text-wrap
                                  d-block
                                  fw-semibold
                                ">$24.99</span>
                                <span class="fs-14 mb-1 text-wrap d-block">Express Delivery</span>
                                <span class="text-muted fw-normal text-wrap d-block">Delivery within 24hrs.</span>
                              </label>
                            </div>
                          </BCol>
                        </BRow>
                      </div>
                    </div>

                    <div class="d-flex align-items-start gap-3 mt-4">
                      <BButton type="button" variant="light" class="btn-label previestab"
                        data-previous="pills-bill-info-tab">
                        <i class="
                          ri-arrow-left-line
                          label-icon
                          align-middle
                          fs-16
                          me-2
                        "></i>Back to Personal Info
                      </BButton>
                      <BButton type="button" variant="primary" class="btn-label right ms-auto nexttab"
                        data-nexttab="pills-payment-tab">
                        <i class="
                          ri-bank-card-line
                          label-icon
                          align-middle
                          fs-16
                          ms-2
                        "></i>Continue to Payment
                      </BButton>
                    </div>
                  </BTab>

                  <BTab class="nav-item nav-link fs-15 p-3">
                    <template #title>
                      <div class="fs-15">
                        <i class="
                          ri-bank-card-line
                          fs-16
                          avatar-xs d-inline-flex align-items-center justify-content-center
                          bg-primary-subtle
                          text-primary
                          rounded-circle
                          align-middle
                          me-2
                        "></i>
                        Payment Info
                      </div>
                    </template>
                    <div>
                      <h5 class="mb-1">Payment Selection</h5>
                      <p class="text-muted mb-4">
                        Please select and enter your billing information
                      </p>
                    </div>

                    <BRow class="g-4">
                      <BCol lg="4" sm="6">
                        <div data-bs-toggle="collapse" data-bs-target="#paymentmethodCollapse.show" aria-expanded="false"
                          aria-controls="paymentmethodCollapse">
                          <div class="form-check card-radio">
                            <input id="paymentMethod01" name="paymentMethod" type="radio" class="form-check-input" />
                            <label class="form-check-label bg-transparent" for="paymentMethod01">
                              <span class="fs-16 text-muted me-2"><i class="ri-paypal-fill align-bottom"></i></span>
                              <span class="fs-14 text-wrap">Paypal</span>
                            </label>
                          </div>
                        </div>
                      </BCol>
                      <BCol lg="4" sm="6">
                        <div data-bs-toggle="collapse" data-bs-target="#paymentmethodCollapse" aria-expanded="true"
                          aria-controls="paymentmethodCollapse">
                          <div class="form-check card-radio">
                            <input id="paymentMethod02" name="paymentMethod" type="radio" class="form-check-input"
                              checked />
                            <label class="form-check-label bg-transparent" for="paymentMethod02">
                              <span class="fs-16 text-muted me-2"><i class="ri-bank-card-fill align-bottom"></i></span>
                              <span class="fs-14 text-wrap">Credit / Debit Card</span>
                            </label>
                          </div>
                        </div>
                      </BCol>

                      <BCol lg="4" sm="6">
                        <div data-bs-toggle="collapse" data-bs-target="#paymentmethodCollapse.show" aria-expanded="false"
                          aria-controls="paymentmethodCollapse">
                          <div class="form-check card-radio">
                            <input id="paymentMethod03" name="paymentMethod" type="radio" class="form-check-input" />
                            <label class="form-check-label bg-transparent" for="paymentMethod03">
                              <span class="fs-16 text-muted me-2"><i
                                  class="ri-money-dollar-box-fill align-bottom"></i></span>
                              <span class="fs-14 text-wrap">Cash on Delivery</span>
                            </label>
                          </div>
                        </div>
                      </BCol>
                    </BRow>

                    <div class="collapse show" id="paymentmethodCollapse">
                      <BCard no-body class="p-4 border shadow-none mb-0 mt-4">
                        <BRow class="gy-3">
                          <BCol md="12">
                            <label for="cc-name" class="form-label">Name on card</label>
                            <input type="text" class="form-control" id="cc-name" placeholder="Enter name" />
                            <small class="text-muted">Full name as displayed on card</small>
                          </BCol>

                          <BCol md="6">
                            <label for="cc-number" class="form-label">Credit card number</label>
                            <input type="text" class="form-control" id="cc-number" placeholder="xxxx xxxx xxxx xxxx" />
                          </BCol>

                          <BCol md="3">
                            <label for="cc-expiration" class="form-label">Expiration</label>
                            <input type="text" class="form-control" id="cc-expiration" placeholder="MM/YY" />
                          </BCol>

                          <BCol md="3">
                            <label for="cc-cvv" class="form-label">CVV</label>
                            <input type="text" class="form-control" id="cc-cvv" placeholder="xxx" />
                          </BCol>
                        </BRow>
                      </BCard>
                      <div class="text-muted mt-2 fst-italic">
                        <i data-feather="lock" class="text-muted icon-xs"></i>
                        Your transaction is secured with SSL encryption
                      </div>
                    </div>

                    <div class="d-flex align-items-start gap-3 mt-4">
                      <BButton type="button" variant="light" class="btn-label previestab"
                        data-previous="pills-bill-address-tab">
                        <i class="
                          ri-arrow-left-line
                          label-icon
                          align-middle
                          fs-16
                          me-2
                        "></i>Back to Shipping
                      </BButton>
                      <BButton type="button" variant="primary" class="btn-label right ms-auto nexttab"
                        data-nexttab="pills-finish-tab">
                        <i class="
                          ri-shopping-basket-line
                          label-icon
                          align-middle
                          fs-16
                          ms-2
                        "></i>Complete Order
                      </BButton>
                    </div>
                  </BTab>

                  <BTab class="nav-item nav-link fs-15 p-3">
                    <template #title>
                      <div class="fs-15">
                        <i class="
                          ri-checkbox-circle-line
                          fs-16
                          avatar-xs d-inline-flex align-items-center justify-content-center
                          bg-primary-subtle
                          text-primary
                          rounded-circle
                          align-middle
                          me-2
                        "></i>
                        Finish
                      </div>
                    </template>
                    <div class="text-center py-5">
                      <div class="mb-4">
                        <lottie colors="primary:#8c68cd,secondary:#4788ff" :options="defaultOptions" :height="120"
                          :width="120" />
                      </div>
                      <h5>Thank you ! Your Order is Completed !</h5>
                      <p class="text-muted">
                        You will receive an order confirmation email with details
                        of your order.
                      </p>

                      <h3 class="fw-semibold">
                        Order ID:
                        <router-link to="/ecommerce/order-details" class="text-decoration-underline">VZ2451</router-link>
                      </h3>
                    </div>
                  </BTab>
                </BTabs>
              </div>
            </BForm>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xl="4">
        <BCard no-body>
          <BCardHeader>
            <div class="d-flex">
              <div class="flex-grow-1">
                <h5 class="card-title mb-0">Order Summary</h5>
              </div>
            </div>
          </BCardHeader>
          <BCardBody>
            <div class="table-responsive table-card">
              <table class="table table-borderless align-middle mb-0">
                <thead class="table-light text-muted">
                  <tr>
                    <th style="width: 90px" scope="col">Product</th>
                    <th scope="col">Product Info</th>
                    <th scope="col" class="text-end">Price</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <div class="avatar-md bg-light rounded p-1">
                        <img src="@/assets/images/products/img-8.png" alt="" class="img-fluid d-block" />
                      </div>
                    </td>
                    <td>
                      <h5 class="fs-14">
                        <router-link to="/ecommerce/product-details" class="text-body">Sweatshirt for Men (Pink)
                        </router-link>
                      </h5>
                      <p class="text-muted mb-0">$ 119.99 x 2</p>
                    </td>
                    <td class="text-end">$ 239.98</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="avatar-md bg-light rounded p-1">
                        <img src="@/assets/images/products/img-7.png" alt="" class="img-fluid d-block" />
                      </div>
                    </td>
                    <td>
                      <h5 class="fs-14">
                        <router-link to="/ecommerce/product-details" class="text-body">Noise Evolve Smartwatch
                        </router-link>
                      </h5>
                      <p class="text-muted mb-0">$ 94.99 x 1</p>
                    </td>
                    <td class="text-end">$ 94.99</td>
                  </tr>
                  <tr>
                    <td>
                      <div class="avatar-md bg-light rounded p-1">
                        <img src="@/assets/images/products/img-3.png" alt="" class="img-fluid d-block" />
                      </div>
                    </td>
                    <td>
                      <h5 class="fs-14">
                        <router-link to="/ecommerce/product-details" class="text-body">350 ml Glass Grocery Container
                        </router-link>
                      </h5>
                      <p class="text-muted mb-0">$ 24.99 x 1</p>
                    </td>
                    <td class="text-end">$ 24.99</td>
                  </tr>
                  <tr>
                    <td class="fw-semibold" colspan="2">Sub Total :</td>
                    <td class="fw-semibold text-end">$ 359.96</td>
                  </tr>
                  <tr>
                    <td colspan="2">
                      Discount <span class="text-muted">(VELZON15)</span> :
                    </td>
                    <td class="text-end">- $ 50.00</td>
                  </tr>
                  <tr>
                    <td colspan="2">Shipping Charge :</td>
                    <td class="text-end">$ 24.99</td>
                  </tr>
                  <tr>
                    <td colspan="2">Estimated Tax (12%):</td>
                    <td class="text-end">$ 18.20</td>
                  </tr>
                  <tr class="table-active">
                    <th colspan="2">Total (USD) :</th>
                    <td class="text-end">
                      <span class="fw-semibold"> $353.15 </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
  </Layout>
</template>
