<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";

export default {
    components: {
        Layout,
        PageHeader,
    },
};
</script>

<template>
    <Layout>
        <PageHeader title="Marketplace" pageTitle="NFT Marketplace" />
        <BRow>
            <BCol xl="8">
                <BRow>
                    <BCol lg="4" md="6">
                        <BCard no-body>
                            <BCardBody>
                                <BRow class="g-1 mb-3">
                                    <BCol lg="6">
                                        <img src="@/assets/images/nft/img-05.jpg" alt="" class="img-fluid rounded">
                                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                                            class="img-fluid rounded mt-1">
                                    </BCol>
                                    <BCol lg="6">
                                        <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                                            class="img-fluid rounded mb-1">
                                        <img src="@/assets/images/nft/img-04.jpg" alt="" class="img-fluid rounded">
                                    </BCol>
                                </BRow>
                                <BLink href="#!" class="float-end"> View All <i
                                        class="ri-arrow-right-line align-bottom"></i></BLink>
                                <h5 class="mb-0 fs-16">
                                    <BLink href="#!">Crypto Card <BBadge variant="success-subtle" class="bg-success-subtle text-success">743</BBadge>
                                    </BLink>
                                </h5>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol lg="4" md="6">
                        <BCard no-body>
                            <BCardBody>
                                <BRow class="g-1 mb-3">
                                    <BCol lg="6">
                                        <img src="@/assets/images/nft/img-06.jpg" alt="" class="img-fluid rounded">
                                        <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                                            class="img-fluid rounded mt-1">
                                    </BCol>
                                    <BCol lg="6">
                                        <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt=""
                                            class="img-fluid rounded mb-1">
                                        <img src="@/assets/images/nft/img-03.jpg" alt="" class="img-fluid rounded">
                                    </BCol>
                                </BRow>
                                <BLink href="#!" class="float-end"> View All <i
                                        class="ri-arrow-right-line align-bottom"></i></BLink>
                                <h5 class="mb-0 fs-16">
                                    <BLink href="#!">Artwork <BBadge variant="success-subtle" class="bg-success-subtle text-success">206</BBadge></BLink>
                                </h5>
                            </BCardBody>
                        </BCard>
                    </BCol>
                    <BCol lg="4" md="6">
                        <BCard no-body>
                            <BCardBody>
                                <BRow class="g-1 mb-3">
                                    <BCol lg="6">
                                        <img src="@/assets/images/nft/img-02.jpg" alt="" class="img-fluid rounded">
                                        <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt=""
                                            class="img-fluid rounded mt-1">
                                    </BCol>
                                    <BCol lg="6">
                                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                                            class="img-fluid rounded mb-1">
                                        <img src="@/assets/images/nft/img-01.jpg" alt="" class="img-fluid rounded">
                                    </BCol>
                                </BRow>
                                <BLink href="#!" class="float-end"> View All <i
                                        class="ri-arrow-right-line align-bottom"></i></BLink>
                                <h5 class="mb-0 fs-16">
                                    <BLink href="#!">Music <BBadge variant="success-subtle" class="bg-success-subtle text-success">679</BBadge></BLink>
                                </h5>
                            </BCardBody>
                        </BCard>
                    </BCol>
                </BRow>
            </BCol>
            <BCol xl="4">
                <BAlert variant="danger" :model-value="true" show>
                    Up to <b>50% OFF</b>, Hurry up before the stock ends
                </BAlert>
                <BCard no-body class="bg-primary pattern">
                    <BCardBody class="p-4">
                        <BBadge class="bg-info fw-medium mb-3 fs-12">Trending Artwork</BBadge>
                        <h3 class="text-white lh-base">Discover, Collect, Sell and Create your own NFT</h3>
                        <p class="text-white text-opacity-75 mb-3">Take advantage of the first text-based NFT. Select a text or write
                            your own and let it live forever on the Ethereum blockchain you or future owners can add
                            text to an existing ChainText token..</p>
                        <div class="hstack gap-2">
                            <BLink href="/apps/nft-create" class="btn btn-secondary">Create NFT</BLink>
                            <BLink href="/apps/nft-explore" class="btn btn-danger">Explore Now</BLink>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <BCard no-body class="overflow-hidden shadow-none border-0">
                    <BCardBody class="bg-primary-subtle text-primary fw-semibold d-flex">
                        <marquee class="fs-14">
                            NFT art is a digital asset that is collectable, unique, and non-transferrable, Cortes
                            explained. Every NFT is unique in it's creative design and cannot be duplicated, making them
                            limited and rare. NFTs get their value because the transaction proves ownership of the art.
                        </marquee>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">Trending Artwork</h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <BLink href="/apps/nft-explore" class="btn btn-soft-primary">View All <i
                                class="ri-arrow-right-line align-bottom"></i></BLink>
                    </div>
                </div>
            </BCol>
        </BRow>

        <BRow class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            <BCol>
                <BCard no-body class="explore-box">
                    <BCardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src="@/assets/images/users/avatar-2.jpg" alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <h6 class="mb-0 fs-15">Nancy Martino</h6>
                                <p class="mb-0 text-muted">Owners</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class="btn btn-icon active" data-bs-toggle="button"
                                    aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src="@/assets/images/nft/img-05.jpg" alt="" class="img-fluid explore-img">
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <BLink href="#!" class="btn btn-primary"><i
                                        class="ri-auction-fill align-bottom me-1"></i>
                                    Place Bid</BLink>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                                19.29k </p>
                            <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 97.8 ETH </h5>
                            <h6 class="fs-16 mb-0">
                                <BLink href="/apps/nft-item-detail">Patterns arts & culture</BLink>
                            </h6>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box">
                    <BCardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src="@/assets/images/users/avatar-9.jpg" alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <h6 class="mb-0 fs-15">Henry Baird</h6>
                                <p class="mb-0 text-muted">Creators</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class="btn btn-icon" data-bs-toggle="button"
                                    aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src="@/assets/images/nft/img-03.jpg" alt="" class="img-fluid explore-img">
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <BLink href="#!" class="btn btn-primary"><i
                                        class="ri-auction-fill align-bottom me-1"></i>
                                    Place Bid</BLink>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                                31.64k </p>
                            <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 475.23 ETH </h5>
                            <h6 class="fs-16 mb-0">
                                <BLink href="/apps/nft-item-detail">Evolved Reality</BLink>
                            </h6>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box">
                    <BCardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src="@/assets/images/users/avatar-10.jpg" alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <h6 class="mb-0 fs-15">Diana Kohler</h6>
                                <p class="mb-0 text-muted">Owners</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class="btn btn-icon active" data-bs-toggle="button"
                                    aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                                class="img-fluid explore-img">
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <BLink href="#!" class="btn btn-primary"><i
                                        class="ri-auction-fill align-bottom me-1"></i>
                                    Place Bid</BLink>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                                8.34k </p>
                            <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 701.38 ETH </h5>
                            <h6 class="fs-16 mb-0">
                                <BLink href="/apps/nft-item-detail">Long-tailed macaque</BLink>
                            </h6>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box">
                    <BCardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src="@/assets/images/users/avatar-8.jpg" alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <h6 class="mb-0 fs-15">James Price</h6>
                                <p class="mb-0 text-muted">Owners</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class="btn btn-icon" data-bs-toggle="button"
                                    aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src="@/assets/images/nft/img-06.jpg" alt="" class="img-fluid explore-img">
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <BLink href="#!" class="btn btn-primary"><i
                                        class="ri-auction-fill align-bottom me-1"></i>
                                    Place Bid</BLink>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                                29.20k </p>
                            <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 917.83 ETH </h5>
                            <h6 class="fs-16 mb-0">
                                <BLink href="/apps/nft-item-detail">Robotic Body Art</BLink>
                            </h6>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box">
                    <BCardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src="@/assets/images/users/avatar-2.jpg" alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <h6 class="mb-0 fs-15">Rickey Teran</h6>
                                <p class="mb-0 text-muted">Creators</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class="btn btn-icon" data-bs-toggle="button"
                                    aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt=""
                                class="img-fluid explore-img">
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <BLink href="#!" class="btn btn-primary"><i
                                        class="ri-auction-fill align-bottom me-1"></i>
                                    Place Bid</BLink>
                            </div>
                        </div>

                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                                78.34k </p>
                            <h5 class="text-primary"><i class="mdi mdi-ethereum"></i> 571.24 ETH </h5>
                            <h6 class="fs-16 mb-0">
                                <BLink href="/apps/nft-item-detail">Creative filtered portrait</BLink>
                            </h6>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">Recent NFTs Artwork</h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <BLink href="/apps/nft-creators" class="btn btn-soft-primary">View All <i
                                class="ri-arrow-right-line align-bottom"></i></BLink>
                    </div>
                </div>
            </BCol>
        </BRow>

        <BRow class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
                    </div>
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-02.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-primary"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            23.63k </p>
                        <h5 class="mb-1">
                            <BLink href="/apps/nft-item-detail">The Chirstoper</BLink>
                        </h5>
                        <p class="text-muted mb-0">Music</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">412.30ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">394.7 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
                    </div>
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-primary"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i> 94.1k
                        </p>
                        <h5 class="mb-1">
                            <BLink href="/apps/nft-item-detail">Trendy Fashion Portraits</BLink>
                        </h5>
                        <p class="text-muted mb-0">3d Style</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">674.92 ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">563.81 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
                    </div>
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-04.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-primary"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            34.12k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Smillevers Crypto</router-link>
                        </h5>
                        <p class="text-muted mb-0">Crypto Card</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">41.658 ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">34.81 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
                    </div>
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-primary"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            15.93k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Evolved Reality</router-link>
                        </h5>
                        <p class="text-muted mb-0">Video</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">2.75ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">3.167 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
                    </div>
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-01.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-primary"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            14.85k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Abstract face painting</router-link>
                        </h5>
                        <p class="text-muted mb-0">Collectibles</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">122.34ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">97.8 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">Popular Creators</h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <router-link to="/apps/nft-creators" class="btn btn-soft-primary">View All <i
                                class="ri-arrow-right-line align-bottom"></i></router-link>
                    </div>
                </div>
            </BCol>
        </BRow>

        <BRow class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-03.jpg" alt="" class="card-img-top object-fit-cover" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-1.jpg" alt=""
                            class="avatar-md mt-n5 rounded-circle mx-auto d-block object-fit-cover">
                        <h5 class="mt-3 mb-1">
                            <router-link to="/pages/profile">Tonya Noble</router-link>
                        </h5>
                        <p class="text-muted">5048 Products</p>
                        <div>
                            <BButton variant="primary" size="sm">Follow</BButton>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt=""
                        class="card-img-top object-fit-cover" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/nft/img-04.jpg" alt=""
                            class="avatar-md mt-n5 rounded-circle mx-auto d-block object-fit-cover">
                        <h5 class="mt-3 mb-1">
                            <router-link to="/pages/profile">Kevin Dawson</router-link>
                        </h5>
                        <p class="text-muted">649 Products</p>
                        <div>
                            <BButton variant="soft-primary" size="sm">Unfollow</BButton>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-01.jpg" alt="" class="card-img-top object-fit-cover" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/nft/img-06.jpg" alt=""
                            class="avatar-md mt-n5 rounded-circle mx-auto d-block object-fit-cover">
                        <h5 class="mt-3 mb-1">
                            <router-link to="/pages/profile">Herbert Stokes</router-link>
                        </h5>
                        <p class="text-muted">918 Products</p>
                        <div>
                            <BButton variant="soft-primary" size="sm">Unfollow</BButton>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-05.jpg" alt="" class="card-img-top object-fit-cover" height="120">
                    <BCardBody class="text-center">
                        <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                            class="avatar-md mt-n5 rounded-circle mx-auto d-block object-fit-cover">
                        <h5 class="mt-3 mb-1">
                            <router-link to="/pages/profile">Thomas Taylor</router-link>
                        </h5>
                        <p class="text-muted">345 Products</p>
                        <div>
                            <BButton variant="primary" size="sm">Follow</BButton>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-02.jpg" alt="" class="card-img-top object-fit-cover" height="120">
                    <BCardBody class="text-center">
                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                            class="avatar-md mt-n5 rounded-circle mx-auto d-block object-fit-cover">
                        <h5 class="mt-3 mb-1">
                            <router-link to="/pages/profile">James Price</router-link>
                        </h5>
                        <p class="text-muted">745 Products</p>
                        <div>
                            <BButton variant="primary" size="sm">Follow</BButton>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </Layout>
</template>

<style scoped>
.pattern{
    background-image: url('../../../assets/images/nft/bg-pattern.png');
}
</style>