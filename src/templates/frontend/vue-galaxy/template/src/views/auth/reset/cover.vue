<script>
import Lottie from "@/components/widgets/lottie.vue";
import animationData from "@/components/widgets/rhvddzym.json";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay, Navigation, Pagination } from "swiper/modules";


import "swiper/css";
import "swiper/css/autoplay";
import 'swiper/css/navigation';
import 'swiper/css/pagination';
export default {
    components: {
        lottie: Lottie, Swiper,
        SwiperSlide,
    },
    data() {
        return {
            defaultOptions: { animationData: animationData },
            Autoplay: Autoplay, Pagination: Pagination, Navigation: Navigation,
            pagination: {
                clickable: true,
                el: '.swiper-pagination',
                renderBullet: function (index, className) {
                    return '<span class=' + className + '>' + (index + 1) + '</span>';
                },
            },
        };
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
                            <BRow class="justify-content-center g-0">
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
                                        <h5 class="text-primary">Forgot Password?</h5>
                                        <p class="text-muted">Reset password with velzon</p>

                                        <div class="mt-2 text-center">
                                            <lottie class="avatar-xl" colors="primary:#8c68cd,secondary:#405189"
                                                :options="defaultOptions" :height="120" :width="120" />
                                        </div>

                                        <BAlert :model-value="true" variant="warning"
                                            class="mb-2 mx-2 border-0 text-center">Enter your email and
                                            instructions will be sent to you!</BAlert>

                                        <div class="p-2">
                                            <form>
                                                <div class="mb-4">
                                                    <label class="form-label">Email</label>
                                                    <input type="email" class="form-control" id="email"
                                                        placeholder="Enter email address">
                                                </div>

                                                <div class="text-center mt-4">
                                                    <BButton variant="primary" class="w-100" type="submit">Send Reset Link</BButton>
                                                </div>
                                            </form>
                                        </div>

                                        <div class="mt-5 text-center">
                                            <p class="mb-0">Wait, I remember my password... <router-link
                                                    to="/auth/signin-cover"
                                                    class="fw-semibold text-primary text-decoration-underline"> Click
                                                    here </router-link>
                                            </p>
                                        </div>
                                    </div>
                                </BCol>
                            </BRow>
                        </Bcard>
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