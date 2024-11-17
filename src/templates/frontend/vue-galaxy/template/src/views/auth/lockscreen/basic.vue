<script>
export default {

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
                  <h5 class="text-primary">Lock Screen</h5>
                  <p class="text-muted">Enter your password to unlock the screen!</p>
                </div>
                <div class="user-thumb text-center">
                  <img src="@/assets/images/users/avatar-1.jpg" class="rounded-circle img-thumbnail avatar-lg"
                    alt="thumbnail">
                  <h5 class="font-size-15 mt-3">Anna Adame</h5>
                </div>
                <div class="p-2 mt-4">
                  <form>
                    <div class="mb-3">
                      <label class="form-label" for="userpassword">Password</label>
                      <input type="password" class="form-control" id="userpassword" placeholder="Enter password" required>
                    </div>
                    <div class="mb-2 mt-4">
                      <BButton variant="primary" class="w-100" type="submit">Unlock</BButton>
                    </div>
                  </form>

                </div>
              </BCardBody>
            </BCard>

            <div class="mt-4 text-center">
              <p class="mb-0">Not you ? return <router-link to="/auth/signin-basic"
                  class="fw-semibold text-primary text-decoration-underline"> Signin </router-link>
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