<script>
export default {};
</script>

<template>
  <div class="auth-page-wrapper pt-5">

    <div class="auth-one-bg-position auth-one-bg" id="auth-particles">
      <div class="bg-overlay"></div>

      <div class="shape">

        <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink"
          viewBox="0 0 1440 120">
          <path d="M 0,36 C 144,53.6 432,123.2 720,124 C 1008,124.8 1296,56.8 1440,40L1440 140L0 140z"></path>
        </svg>
      </div>
    </div>

    <div class="auth-page-content">
      <BContainer>
        <BRow>
          <BCol lg="12">
            <div class="text-center mt-sm-5 pt-4">
              <div class="mb-5 text-white-50">
                <h1 class="display-5 coming-soon-text">
                  Site is Under Maintenance
                </h1>
                <p class="fs-14">Please check back in sometime</p>
                <div class="mt-4 pt-2">
                  <router-link to="/" class="btn btn-success"><i class="mdi mdi-home me-1"></i> Back to Home
                  </router-link>
                </div>
              </div>
              <BRow class="justify-content-center mb-5">
                <BCol xl="4" lg="8">
                  <div>
                    <img src="@/assets/images/maintenance.png" alt="" class="img-fluid" />
                  </div>
                </BCol>
              </BRow>
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
              <p class="mb-0 text-muted">
                &copy; {{ new Date().getFullYear() }} Velzon. Crafted with
                <i class="mdi mdi-heart text-danger"></i> by Themesbrand
              </p>
            </div>
          </BCol>
        </BRow>
      </BContainer>
    </footer>
  </div>
</template>
