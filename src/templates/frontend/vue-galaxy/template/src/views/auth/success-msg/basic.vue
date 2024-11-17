<script>
export default {};
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
                  <img src="@/assets/images/logo-light.png" alt="" height="20" />
                </router-link>
              </div>
              <p class="mt-3 fs-15 fw-medium">
                Premium Admin & Dashboard Template
              </p>
            </div>
          </BCol>
        </BRow>

        <BRow class="justify-content-center">
          <BCol md="8" lg="6" xl="5">
            <BCard no-body class="mt-4 card-bg-fill">
              <BcardBody class="p-4 text-center">
                <div class="avatar-lg mx-auto mt-2">
                  <div class="
                      avatar-title
                      bg-light
                      text-primary
                      display-3
                      rounded-circle
                    ">
                    <i class="ri-checkbox-circle-fill"></i>
                  </div>
                </div>
                <div class="mt-4 pt-2">
                  <h4>Well done !</h4>
                  <p class="text-muted mx-4">
                    Aww yeah, you successfully read this important message.
                  </p>
                  <div class="mt-4">
                    <router-link to="/auth/signin-basic" class="btn btn-primary w-100">Back to Dashboard
                    </router-link>
                  </div>
                </div>
              </BcardBody>
            </BCard>
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