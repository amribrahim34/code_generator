<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Autoplay, Navigation, Pagination } from "swiper/modules";


import "swiper/css";
import "swiper/css/autoplay";
import 'swiper/css/navigation';
import 'swiper/css/pagination';

export default {
    methods: {
        getInputElement(index) {
            return document.getElementById('digit' + index + '-input');
        },

        moveToNext(index) {
            if (this.getInputElement(index).value.length === 1) {
                if (index !== 4) {
                    this.getInputElement(index + 1).focus();
                } else {
                    this.getInputElement(index).blur();
                    // Submit code
                    console.log('submit code');
                }
            }
        }
    },
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
    }
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
                                        <div class="mb-4">
                                            <div class="avatar-lg mx-auto">
                                                <div class="avatar-title bg-light text-primary display-5 rounded-circle">
                                                    <i class="ri-mail-line"></i>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="text-muted text-center mx-lg-3">
                                            <h4 class="">Verify Your Email</h4>
                                            <p>Please enter the 4 digit code sent to <span
                                                    class="fw-semibold">example@abc.com</span></p>
                                        </div>

                                        <div class="mt-4">
                                            <form>
                                                <BRow>
                                                    <BCol cols="3">
                                                        <div class="mb-3">
                                                            <label for="digit1-input" class="visually-hidden">Dight
                                                                1</label>
                                                            <input type="text"
                                                                class="form-control form-control-lg bg-light border-light text-center"
                                                                v-on:keyup="moveToNext(1)" maxLength="1" id="digit1-input">
                                                        </div>
                                                    </BCol>

                                                    <BCol cols="3">
                                                        <div class="mb-3">
                                                            <label for="digit2-input" class="visually-hidden">Dight
                                                                2</label>
                                                            <input type="text"
                                                                class="form-control form-control-lg bg-light border-light text-center"
                                                                v-on:keyup="moveToNext(2)" maxLength="1" id="digit2-input">
                                                        </div>
                                                    </BCol>

                                                    <BCol cols="3">
                                                        <div class="mb-3">
                                                            <label for="digit3-input" class="visually-hidden">Dight
                                                                3</label>
                                                            <input type="text"
                                                                class="form-control form-control-lg bg-light border-light text-center"
                                                                v-on:keyup="moveToNext(3)" maxLength="1" id="digit3-input">
                                                        </div>
                                                    </BCol>

                                                    <BCol cols="3">
                                                        <div class="mb-3">
                                                            <label for="digit4-input" class="visually-hidden">Dight
                                                                4</label>
                                                            <input type="text"
                                                                class="form-control form-control-lg bg-light border-light text-center"
                                                                v-on:keyup="moveToNext(4)" maxLength="1" id="digit4-input">
                                                        </div>
                                                    </BCol>
                                                </BRow>

                                                <div class="mt-3">
                                                    <BButton type="button" variant="primary" class="w-100">Confirm</BButton>
                                                </div>

                                            </form>

                                        </div>

                                        <div class="mt-5 text-center">
                                            <p class="mb-0">Didn't receive a code ? <router-link to="/auth/reset-pwd-cover"
                                                    class="fw-semibold text-primary text-decoration-underline">Resend
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