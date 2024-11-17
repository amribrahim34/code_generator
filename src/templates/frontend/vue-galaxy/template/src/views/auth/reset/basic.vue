<script>
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/rhvddzym.json";

export default {
  components: {
    lottie: Lottie
  },
  data() {
    return {
      defaultOptions: {
        animationData: animationData
      },
    };
  }
};
</script>

<template>
  <div class="auth-page-wrapper pt-5">

    <div class="auth-page-content">
      <BContainer>
        <BRow>
          <BCol lg="12">
            <div class="text-center mt-sm-5 mb-4 text-white-50">
              <div>
                <router-link to="/" class="d-inline-block auth-logo">
                  <img src="@/assets/images/logo-light.png" alt="" height="20">
                </router-link>
              </div>
              <p class="mt-3 fs-15 fw-medium">Premium Admin & Dashboard Template</p>
            </div>
          </BCol>
        </BRow>

        <BRow class="justify-content-center">
          <BCol md="8" lg="6" xl="5">
            <BCard no-body class="mt-4 card-bg-fill">

              <BCardBody class="p-4">
                <div class="text-center mt-2">
                  <h5 class="text-primary">Forgot Password?</h5>
                  <p class="text-muted">Reset password with velzon</p>

                  <lottie class="avatar-xl some-class" colors="primary:#8c68cd" :options="defaultOptions" :height="120"
                    :width="120" />

                </div>

                <BAlert :model-value="true" variant="warning" class="mb-2 mx-2 border-0 text-center">Enter your email and
                  instructions will be sent to you!</BAlert>

                <div class="p-2">
                  <form>
                    <div class="mb-4">
                      <label class="form-label">Email</label>
                      <input type="email" class="form-control" id="email" placeholder="Enter Email">
                    </div>

                    <div class="text-center mt-4">
                      <BButton variant="primary" class="w-100" type="submit">Send Reset Link</BButton>
                    </div>
                  </form>
                </div>
              </BCardBody>
            </BCard>

            <div class="mt-4 text-center">
              <p class="mb-0">Wait, I remember my password... <router-link to="/auth/signin-basic"
                  class="fw-semibold text-primary text-decoration-underline"> Click here
                </router-link>
              </p>
            </div>

          </BCol>
        </BRow>
      </BContainer>
    </div>

    <footer class="footer">
      <BContainer>
        <BRow>
          <BCol lg="12">
            <div class="text-center">
              <p class="mb-0 text-muted">&copy; {{ new Date().getFullYear() }} Velzon. Crafted with <i
                  class="mdi mdi-heart text-danger"></i> by Themesbrand</p>
            </div>
          </BCol>
        </BRow>
      </BContainer>
    </footer>
  </div>
</template>