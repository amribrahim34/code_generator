<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay, Navigation, Pagination } from "swiper/modules";


import "swiper/css";
import "swiper/css/autoplay";
import 'swiper/css/navigation';
import 'swiper/css/pagination';

export default {
    data() {
        return {
            togglePassword: false,
            Autoplay: Autoplay, Pagination: Pagination, Navigation: Navigation,
            pagination: {
                clickable: true,
                el: '.swiper-pagination',
                renderBullet: function (index, className) {
                    return '<span class=' + className + '>' + (index + 1) + '</span>';
                },
            },
        }
    },
    components: {
        Swiper,
        SwiperSlide,
    },
};
</script>

<template>
    <div class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100">
        <div class="bg-overlay"></div>
        <div class="auth-page-content overflow-hidden pt-lg-5">
            <BContainer>
                <BRow>
                    <BCol lg="12">
                        <BCard no-body class="overflow-hidden card-bg-fill border-0 card-border-effect-none">
                            <BRow class="g-0">
                                <BCol lg="6">
                                    <div class="p-lg-5 p-4 auth-one-bg h-100">
                                        <div class="bg-overlay"></div>
                                        <div class="position-relative h-100 d-flex flex-column">
                                            <div class="mb-4">
                                                <router-link to="/" class="d-block">
                                                    <img src="@/assets/images/logo-light.png" alt="" height="18">
                                                </router-link>
                                            </div>
                                            <div class="mt-auto">
                                                <div class="mb-3">
                                                    <i class="ri-double-quotes-l display-4 text-success"></i>
                                                </div>

                                                <div id="qoutescarouselIndicators" class="carousel slide"
                                                    data-bs-ride="carousel">
                                                    <Swiper class=" text-center text-white pb-5"
                                                        :autoplay="{ delay: 3000, disableOnInteraction: false }"
                                                        :loop="true" :modules="[Autoplay, Navigation, Pagination]"
                                                        :pagination="{ clickable: true, el: '.swiper-pagination' }">
                                                        <swiper-slide>
                                                            <div class="active">
                                                                <p class="fs-15 fst-italic">" Great! Clean code, clean
                                                                    design, easy for customization. Thanks very much! "</p>
                                                            </div>
                                                        </swiper-slide>
                                                        <swiper-slide>
                                                            <div>
                                                                <p class="fs-15 fst-italic">" The theme is really great with
                                                                    an amazing customer support."</p>
                                                            </div>
                                                        </swiper-slide>
                                                        <swiper-slide>
                                                            <div>
                                                                <p class="fs-15 fst-italic">" Great! Clean code, clean
                                                                    design, easy for customization. Thanks very much! "</p>
                                                            </div>
                                                        </swiper-slide>
                                                        <div class="swiper-pagination"></div>
                                                    </Swiper>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </BCol>

                                <BCol lg="6">
                                    <div class="p-lg-5 p-4">
                                        <div>
                                            <h5 class="text-primary">Welcome Back !</h5>
                                            <p class="text-muted">Sign in to continue to Velzon.</p>
                                        </div>

                                        <div class="mt-4">
                                            <form>

                                                <div class="mb-3">
                                                    <label for="username" class="form-label">Username</label>
                                                    <input type="text" class="form-control" id="username"
                                                        placeholder="Enter username">
                                                </div>

                                                <div class="mb-3">
                                                    <div class="float-end">
                                                        <router-link to="/auth/reset-pwd-cover" class="text-muted">
                                                            Forgot password?</router-link>
                                                    </div>
                                                    <label class="form-label" for="password-input">Password</label>
                                                    <div class="position-relative auth-pass-inputgroup mb-3">
                                                        <input :type="togglePassword ? 'text' : 'password'"
                                                            class="form-control pe-5" placeholder="Enter password"
                                                            id="password-input">
                                                        <BButton variant="link"
                                                            class="position-absolute end-0 top-0 text-decoration-none text-muted"
                                                            type="button" id="password-addon"
                                                            @click="togglePassword = !togglePassword"><i
                                                                class="ri-eye-fill align-middle"></i></BButton>
                                                    </div>
                                                </div>

                                                <div class="form-check">
                                                    <input class="form-check-input" type="checkbox" value=""
                                                        id="auth-remember-check">
                                                    <label class="form-check-label" for="auth-remember-check">Remember
                                                        me</label>
                                                </div>

                                                <div class="mt-4">
                                                    <BButton variant="primary" class="w-100" type="submit">Sign
                                                        In</BButton>
                                                </div>

                                                <div class="mt-4 text-center">
                                                    <div class="signin-other-title">
                                                        <h5 class="fs-13 mb-4 title">Sign In with</h5>
                                                    </div>

                                                    <div>
                                                        <BButton type="button" variant="primary" class="btn-icon"><i
                                                                class="ri-facebook-fill fs-16"></i></BButton>
                                                        <BButton type="button" variant="danger" class="btn-icon ms-1"><i
                                                                class="ri-google-fill fs-16"></i></BButton>
                                                        <BButton type="button" variant="dark" class="btn-icon ms-1"><i
                                                                class="ri-github-fill fs-16"></i></BButton>
                                                        <BButton type="button" variant="info" class="btn-icon ms-1"><i
                                                                class="ri-twitter-fill fs-16"></i></BButton>
                                                    </div>
                                                </div>

                                            </form>
                                        </div>

                                        <div class="mt-5 text-center">
                                            <p class="mb-0">Don't have an account ? <router-link to="/auth/signup-cover"
                                                    class="fw-semibold text-primary text-decoration-underline"> Signup
                                                </router-link>
                                            </p>
                                        </div>
                                    </div>
                                </BCol>
                            </BRow>
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
                            <p class="mb-0">&copy; {{ new Date().getFullYear() }} Velzon. Crafted with <i
                                    class="mdi mdi-heart text-danger"></i> by Themesbrand</p>
                        </div>
                    </BCol>
                </BRow>
            </BContainer>
        </footer>
    </div>
</template>