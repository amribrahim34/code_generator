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
                                        <div>
                                            <h5 class="text-primary">Lock Screen</h5>
                                            <p class="text-muted">Enter your password to unlock the screen!</p>
                                        </div>
                                        <div class="user-thumb text-center">
                                            <img src="@/assets/images/users/avatar-1.jpg"
                                                class="rounded-circle img-thumbnail avatar-lg" alt="thumbnail">
                                            <h5 class="font-size-15 mt-3">Anna Adame</h5>
                                        </div>

                                        <div class="mt-4">
                                            <form>
                                                <div class="mb-3">
                                                    <label class="form-label" for="userpassword">Password</label>
                                                    <input type="password" class="form-control" id="userpassword"
                                                        placeholder="Enter password" required>
                                                </div>
                                                <div class="mb-2 mt-4">
                                                    <BButton class="btn btn-primary w-100" variant="primary" type="submit">Unlock</BButton>
                                                </div>
                                            </form>
                                        </div>

                                        <div class="mt-5 text-center">
                                            <p class="mb-0">Not you ? return <router-link to="/auth/signin-cover"
                                                    class="fw-semibold text-primary text-decoration-underline"> Signin
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