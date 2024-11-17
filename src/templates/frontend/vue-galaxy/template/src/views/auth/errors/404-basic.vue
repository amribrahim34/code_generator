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
            <div class="text-center pt-4">
              <div class="">
                <img src="@/assets/images/error.svg" alt="" class="error-basic-img move-animation">
              </div>
              <div class="mt-n4">
                <h1 class="display-1 fw-medium">404</h1>
                <h3 class="text-uppercase">Sorry, Page not Found 😭</h3>
                <p class="text-muted mb-4">The page you are looking for not available!</p>
                <router-link to="/" class="btn btn-success"><i class="mdi mdi-home me-1"></i>Back to
                  home</router-link>
              </div>
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