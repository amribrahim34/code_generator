<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import Slider from "@vueform/slider";
export default {
    data() {
        return {
            isCollapsed: true,
            sliderCustomzie: [18.33, 75.00],
        }
    },
    components: {
        Layout,
        PageHeader,
        Slider,
    },
    methods: {
        toggleCollapse() {
            this.isCollapsed = !this.isCollapsed;
        },
    },
};
</script>

<template>
    <Layout>
        <PageHeader title="Explore Now" pageTitle="NFT Marketplace" />
        <BRow>
            <BCol lg="12">
                <BCard no-body>
                    <BCardHeader class="border-0">
                        <div class="d-flex align-items-center">
                            <h5 class="card-title mb-0 flex-grow-1">Explore Product</h5>
                            <div>
                                <Blink class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample"
                                    @click="toggleCollapse"><i class="ri-filter-2-line align-bottom"></i> Filters</Blink>
                            </div>
                        </div>
                        <div v-if="isCollapsed" class="collaps show" id="collapseExample">
                            <BRow class="row-cols-xxl-5 row-cols-lg-3 row-cols-md-2 row-cols-1 mt-3 g-3">
                                <BCol>
                                    <h6 class="text-uppercase fs-12 mb-2">Sort by Likes</h6>
                                    <select class="form-control" data-choices name="sort-by-likes" data-choices-search-false
                                        id="sort-by-likes">
                                        <option value="">Sort by Likes</option>
                                        <option value="Latest Likes">Latest Likes</option>
                                        <option value="Popular Likes">Popular Likes</option>
                                        <option value="Most Likes">Most Likes</option>
                                    </select>
                                </BCol>
                                <BCol>
                                    <h6 class="text-uppercase fs-12 mb-2">Select Category</h6>
                                    <select class="form-control" data-choices name="select-category"
                                        data-choices-search-false id="select-category">
                                        <option value="">Select Category</option>
                                        <option value="Artwork">Artwork</option>
                                        <option value="3d Style">3d Style</option>
                                        <option value="Photography">Photography</option>
                                        <option value="Collectibles">Collectibles</option>
                                        <option value="Crypto Card">Crypto Card</option>
                                        <option value="Games">Games</option>
                                        <option value="Music">Music</option>
                                    </select>
                                </BCol>
                                <BCol>
                                    <h6 class="text-uppercase fs-12 mb-2">File Type</h6>
                                    <select class="form-control" data-choices name="file-type" data-choices-search-false
                                        id="file-type">
                                        <option value="">File Type</option>
                                        <option value="Choice 1">Images</option>
                                        <option value="Choice 2">Video</option>
                                        <option value="Choice 3">Audio</option>
                                        <option value="Choice 3">Gif</option>
                                    </select>
                                </BCol>
                                <BCol>
                                    <h6 class="text-uppercase fs-12 mb-2">Sales Type</h6>
                                    <select class="form-control" data-choices name="all-sales-type"
                                        data-choices-search-false id="all-sales-type">
                                        <option value="">All Sales Type</option>
                                        <option value="All Sale">All Sale</option>
                                        <option value="On Auction">On Auction</option>
                                        <option value="New">New</option>
                                        <option value="Has Offers">Has Offers</option>
                                    </select>
                                </BCol>
                                <BCol>
                                    <h6 class="text-uppercase fs-12 mb-5">Price</h6>
                                    <Slider v-model="sliderCustomzie" :min="0" :max="100" />
                                </BCol>
                            </BRow>
                        </div>
                    </BCardHeader>
                </BCard>
            </BCol>
            <BCol lg="12">
                <div class="d-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <p class="text-muted fs-14 mb-0">Result: 8745</p>
                    </div>
                    <div class="flex-shrink-0">
                        <BDropdown variant="link" toggle-class="text-muted fs-14 " size="sm" no-caret>
                            <template #button-content> All View </template>
                            <BDropdownItem>Action</BDropdownItem>
                            <BDropdownItem>Another action</BDropdownItem>
                            <BDropdownItem>Something else here</BDropdownItem>
                        </BDropdown>
                    </div>
                </div>
            </BCol>
        </BRow>

        <BRow class="row-cols-xxl-5 row-cols-xl-4 row-cols-lg-3 row-cols-md-2 row-cols-1">
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            37.41k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Walking on air</router-link>
                        </h5>
                        <p class="text-muted mb-0">Artwork</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">10.35ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">14.167 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-03.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            19.29k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Creative filtered portrait</router-link>
                        </h5>
                        <p class="text-muted mb-0">Photography</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">75.3ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">67.36 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-02.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            23.63k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">The Chirstoper</router-link>
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
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <Blink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</Blink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
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
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-01.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <button type="button" class="btn btn-icon" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></button>
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
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-05.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            64.10k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Long-tailed macaque</router-link>
                        </h5>
                        <p class="text-muted mb-0">Artwork</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">874.01ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">745.14 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body class="explore-box card-animate">
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-06.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i>
                            36.42k </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Robotic Body Art</router-link>
                        </h5>
                        <p class="text-muted mb-0">Artwork</p>
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
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i> 94.1k
                        </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Trendy Fashion Portraits</router-link>
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
                    <div class="explore-place-bid-img">
                        <img src="@/assets/images/nft/img-04.jpg" alt="" class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
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
                    <div class="explore-place-bid-img">
                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                            class="card-img-top explore-img" />
                        <div class="bg-overlay"></div>
                        <div class="place-bid-btn">
                            <BLink href="#!" class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i>
                                Place
                                Bid</BLink>
                        </div>
                    </div>
                    <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                        <BButton type="button" class="btn-icon " data-bs-toggle="button" aria-pressed="true"><i
                                class="mdi mdi-cards-heart fs-16"></i></BButton>
                    </div>
                    <BCardBody>
                        <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i> 8.42k
                        </p>
                        <h5 class="mb-1">
                            <router-link to="/apps/nft-item-detail">Patterns arts & culture</router-link>
                        </h5>
                        <p class="text-muted mb-0">Artwork</p>
                    </BCardBody>
                    <BCardFooter class="border-top border-top-dashed">
                        <div class="d-flex align-items-center">
                            <div class="flex-grow-1 fs-14">
                                <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span
                                    class="fw-medium">9.64ETH</span>
                            </div>
                            <h5 class="flex-shrink-0 fs-14 text-primary mb-0">14.167 ETH</h5>
                        </div>
                    </BCardFooter>
                </BCard>
            </BCol>
        </BRow>
        <div class="text-center mb-3">
            <BButton variant="link" class="text-primary mt-2"><i
                    class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i> Load more </BButton>
        </div>
    </Layout>
</template>
<style lang="scss">
@import '@vueform/slider/themes/default.css';
</style>