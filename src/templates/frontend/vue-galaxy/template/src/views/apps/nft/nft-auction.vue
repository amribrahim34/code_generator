<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

export default {
    components: {
        Layout,
        PageHeader,
    },
    methods: {
        startCountDownDate(dateVal) {
            var countDownDate = new Date(dateVal).getTime();
            return countDownDate;
        },
        // countDownTimer(start, targetDOM) {
        //     // Get todays date and time

        // }
    },
    mounted() {
        var setEndDate1 = "March 19, 2024 6:0:0";
        var setEndDate2 = "April 16, 2023 5:3:1";
        var setEndDate3 = "Dec 01, 2023 1:0:1";
        var setEndDate4 = "Nov 26, 2024 1:2:1";
        var setEndDate5 = "May 27, 2023 1:6:6";
        var setEndDate6 = "May 20, 2023 2:5:5";
        var setEndDate7 = "June 10, 2023 5:1:4";
        var setEndDate8 = "June 25, 2023 1:6:3";
        var setEndDate9 = "July 08, 2023 1:5:2";

        var cdd1 = this.startCountDownDate(setEndDate1);
        var cdd2 = this.startCountDownDate(setEndDate2);
        var cdd3 = this.startCountDownDate(setEndDate3);
        var cdd4 = this.startCountDownDate(setEndDate4);
        var cdd5 = this.startCountDownDate(setEndDate5);
        var cdd6 = this.startCountDownDate(setEndDate6);
        var cdd7 = this.startCountDownDate(setEndDate7);
        var cdd8 = this.startCountDownDate(setEndDate8);
        var cdd9 = this.startCountDownDate(setEndDate9);

        if (document.getElementById("auction-time-1"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd1 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-1") ? document.querySelector("#" + "auction-time-1").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    document.querySelector("#" + "auction-time-1").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-2"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd2 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-2") ? document.querySelector("#" + "auction-time-2").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-2").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-3"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd3 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-3") ? document.querySelector("#" + "auction-time-3").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-3").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-4"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd4 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-4") ? document.querySelector("#" + "auction-time-4").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-4").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-5"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd5 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-5") ? document.querySelector("#" + "auction-time-5").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-5").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-6"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd6 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-6") ? document.querySelector("#" + "auction-time-6").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-6").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-7"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd7 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-7") ? document.querySelector("#" + "auction-time-7").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-7").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-8"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd8 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-8") ? document.querySelector("#" + "auction-time-8").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-8").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        if (document.getElementById("auction-time-9"))
            setInterval(function () {
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = cdd9 - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                document.querySelector("#" + "auction-time-9") ? document.querySelector("#" + "auction-time-9").textContent =
                    days + " : " + hours + " : " + minutes + " : " + seconds : "";

                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    // document.querySelector("#" + "auction-time-9").textContent = "00 : 00 : 00 : 00";
                }
            }, 1000);
        // filter btn
        var filterBtns = document.querySelectorAll(".filter-btns .nav-link");
        var productItems = document.querySelectorAll(".product-item");

        filterBtns.forEach(function (button) {
            button.addEventListener("click", function (e) {
                e.preventDefault();

                for (var i = 0; i < filterBtns.length; i++) {
                    filterBtns[i].classList.remove("active");
                }
                this.classList.add("active");

                var filter = e.target.dataset.filter;

                productItems.forEach(function (item) {
                    if (filter === "all") {
                        item.style.display = "block";
                    } else {
                        if (item.classList.contains(filter)) {
                            item.style.display = "block";
                        } else {
                            item.style.display = "none";
                        }
                    }
                });
            });
        });

    },
};
</script>

<template>
    <Layout>
        <PageHeader title="Live Auction" pageTitle="NFT Marketplace" />
        <BRow>
            <BCol xxl="9">
                <BCard no-body>
                    <BCardHeader class="border-0">
                        <div class="d-lg-flex align-items-center">
                            <div class="flex-grow-1">
                                <h5 class="card-title mb-0">Live Auction</h5>
                            </div>
                            <div class="flex-shrink-0 mt-4 mt-lg-0">
                                <ul class="nav nav-pills filter-btns" role="tablist">
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link fw-medium active" type="button" data-filter="all">All
                                            Items</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link fw-medium" type="button" data-filter="upto-15">Up to
                                            15%</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link fw-medium" type="button" data-filter="upto-30">Up to
                                            30%</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link fw-medium" type="button" data-filter="upto-40">Up to
                                            40%</button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </BCardHeader>
                </BCard>
                <BRow>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-15">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="@/assets/images/nft/img-01.jpg" alt="" class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-1" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 19.29k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 97.8 ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Abstract face painting</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 436</span>
                                    <span class="text-muted">Sold: 4187</span>
                                    <BProgress striped :value="67" class="progress-sm mt-2" variant="warning" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-30">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                                    class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-2" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 8.42k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 245.23ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Patterns arts & culture</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 8974</span>
                                    <span class="text-muted">Sold: 13</span>
                                    <BProgress striped :value="10" class="progress-sm mt-2" variant="primary" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-40">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="@/assets/images/nft/img-03.jpg" alt="" class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-3" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 19.29k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 67.36 ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Creative filtered portrait</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 3620</span>
                                    <span class="text-muted">Sold: 345</span>
                                    <BProgress striped :value="45" class="progress-sm mt-2" variant="warning" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-15">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="@/assets/images/nft/img-04.jpg" alt="" class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-4" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 34.12k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 34.81 ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Smillevers Crypto</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 3521</span>
                                    <span class="text-muted">Sold: 1457</span>
                                    <BProgress striped :value="67" class="progress-sm mt-2" variant="warning" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-40">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt=""
                                    class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-5" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 47.12k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 245.23ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Long-tailed Macaque</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 30</span>
                                    <span class="text-muted">Sold: 1369</span>
                                    <BProgress striped :value="95" class="progress-sm mt-2" variant="danger" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-15">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="@/assets/images/nft/img-02.jpg" alt="" class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-6" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 23.63k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 394.7 ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">The Chirstoper</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 1474</span>
                                    <span class="text-muted">Sold: 7451</span>
                                    <BProgress striped :value="83" class="progress-sm mt-2" variant="warning" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-30">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="@/assets/images/nft/img-06.jpg" alt="" class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-7" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 36.42k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 745.14 ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Robotic Body Art</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 4563</span>
                                    <span class="text-muted">Sold: 1024</span>
                                    <BProgress striped :value="24" class="progress-sm mt-2" variant="primary" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol xxl="3" lg="4" md="6" class="product-item upto-15">
                        <BCard no-body class="explore-box card-animate">
                            <div class="position-relative rounded overflow-hidden">
                                <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                                    class="card-img-top explore-img">
                                <div class="discount-time">
                                    <h5 id="auction-time-8" class="mb-0 text-white"></h5>
                                </div>
                            </div>
                            <BCardBody>
                                <p class="fw-medium mb-0 float-end"><i
                                        class="mdi mdi-heart text-danger align-middle"></i> 94.1k </p>
                                <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 245.23ETH </h5>
                                <h6 class="fs-16 mb-3">
                                    <router-link to="/apps/nft-item-detail">Evolved Reality</router-link>
                                </h6>
                                <div>
                                    <span class="text-muted float-end">Available: 26</span>
                                    <span class="text-muted">Sold: 9974</span>
                                    <BProgress striped :value="97" class="progress-sm mt-2" variant="danger" />
                                </div>
                            </BCardBody>
                        </BCard>
                    </BCol>
                </BRow>
                <BRow>
                    <BCol lg="12">
                        <div class="text-center mb-3">
                            <BButton variant="link" class="text-success mt-2"><i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i> Load more </BButton>
                        </div>
                    </BCol>
                </BRow>
            </BCol>
            <BCol xxl="3">
                <BCard no-body>
                    <BCardHeader class="d-flex align-items-center">
                        <h6 class="card-title mb-0 flex-grow-1">Top Drop</h6>
                        <BLink class="text-muted" href="#">
                            See All <i class="ri-arrow-right-line align-bottom"></i>
                        </BLink>
                    </BCardHeader>
                    <BCardBody>
                        <div class="table-responsive table-card">
                            <table class="table table-borderless align-middle">
                                <tbody>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/nft/img-03.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Creative filtered portrait</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 34.81 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>Just Now</small></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Patterns arts & culture</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 147.83 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>3 sec ago</small></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Evolved Reality</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 34.81 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>2 min ago</small></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/nft/img-04.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Smillevers Crypto</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 47.9 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>26 min ago</small></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/nft/img-05.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Robotic Body Art</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 134.32 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>1 hrs ago</small></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/nft/img-02.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <router-link to="/apps/nft-item-detail">
                                                        <h6 class="fs-15 mb-1">Trendy Fashion Portraits</h6>
                                                    </router-link>
                                                    <p class="mb-0 text-muted">Sold at 643.19 ETH</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><small>3 hrs ago</small></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </BCardBody>
                </BCard>
                <BCard no-body>
                    <BCardHeader class="d-flex align-items-center">
                        <h6 class="card-title mb-0 flex-grow-1">Top Creator</h6>
                        <router-link class="text-muted" to="/apps/nft-item-detail">
                            See All <i class="ri-arrow-right-line align-bottom"></i>
                        </router-link>
                    </BCardHeader>
                    <BCardBody>
                        <div class="table-responsive table-card">
                            <table class="table table-borderless align-middle">
                                <tbody>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/users/avatar-1.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <BLink href="#!">
                                                        <h6 class="fs-15 mb-1">Herbert Stokes</h6>
                                                    </BLink>
                                                    <p class="mb-0 text-muted">23 Products</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><BButton variant="primary" size="sm">Follow</BButton></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/users/avatar-3.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <BLink href="#!">
                                                        <h6 class="fs-15 mb-1">Thomas Taylor</h6>
                                                    </BLink>
                                                    <p class="mb-0 text-muted">123 Products</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><BButton variant="soft-primary" size="sm">Unfllow</BButton></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/users/avatar-5.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <BLink href="#!">
                                                        <h6 class="fs-15 mb-1">Henry Baird</h6>
                                                    </BLink>
                                                    <p class="mb-0 text-muted">46 Products</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><BButton variant="primary" size="sm">Follow</BButton></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/users/avatar-10.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <BLink href="#!">
                                                        <h6 class="fs-15 mb-1">Nancy Martino</h6>
                                                    </BLink>
                                                    <p class="mb-0 text-muted">845 Products</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><BButton variant="primary" size="sm">Follow</BButton></td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <img src="@/assets/images/users/avatar-8.jpg" alt=""
                                                    class="avatar-sm object-fit-cover rounded-circle">
                                                <div class="ms-2">
                                                    <BLink href="#!">
                                                        <h6 class="fs-15 mb-1">James Price</h6>
                                                    </BLink>
                                                    <p class="mb-0 text-muted">318 Products</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td><BButton variant="soft-primary" size="sm">Unfllow</BButton></td>
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