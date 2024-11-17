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
        <PageHeader title="Creators" pageTitle="NFT Marketplace" />
        <BRow class="g-4 mb-3">
            <BCol sm>
                <div>
                    <router-link to="/apps/projects-create" class="btn btn-primary"><i
                            class="ri-add-line align-bottom me-1"></i> Add New</router-link>
                </div>
            </BCol>
            <BCol sm="auto">
                <div class="d-flex justify-content-sm-end gap-2">
                    <div class="search-box ms-2">
                        <input type="text" class="form-control" placeholder="Search...">
                        <i class="ri-search-line search-icon"></i>
                    </div>
                    <select class="form-control w-md" data-choices data-choices-search-false>
                        <option value="All">All</option>
                        <option value="Today">Today</option>
                        <option value="Yesterday" selected>Yesterday</option>
                        <option value="Last 7 Days">Last 7 Days</option>
                        <option value="Last 30 Days">Last 30 Days</option>
                        <option value="This Month">This Month</option>
                        <option value="Last Year">Last Year</option>
                    </select>
                </div>
            </BCol>
        </BRow>

        <BRow>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/nft/img-01.jpg" alt="" class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Timothy Smith</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 4,754 ETH
                                </p>
                            </div>
                            <BDropdown class="float-end" variant="button"
                                toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                <BDropdownItem>Share</BDropdownItem>
                                <BDropdownItem> Report</BDropdownItem>
                            </BDropdown>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/users/avatar-5.jpg" alt=""
                                    class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Alexis Clarke</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 81,369
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/nft/img-06.jpg" alt="" class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Glen Matney</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 13,156
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt=""
                                    class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Herbert Stokes</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 34,754
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/users/avatar-8.jpg" alt=""
                                    class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Michael Morris</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 13,841
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/nft/img-04.jpg" alt="" class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Nancy Martino</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 26,834
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/nft/img-05.jpg" alt="" class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">Mary Cousar</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 18,034
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol xl="3" lg="4" md="6">
                <BCard no-body>
                    <BCardBody>
                        <div class="d-flex">
                            <div class="flex-shrink-0">
                                <img src="@/assets/images/nft/img-02.jpg" alt="" class="avatar-sm object-fit-cover rounded">
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <router-link to="/pages/profile">
                                    <h5 class="mb-1">James Morris</h5>
                                </router-link>
                                <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> 63,710
                                    ETH</p>
                            </div>
                            <div>
                                <BDropdown class="float-end" variant="button"
                                    toggle-class="btn btn-ghost-primary btn-icon arrow-none" size="sm" no-caret
                                    :offset="{ alignmentAxis: -130, crossAxis: 0, mainAxis: 10 }">
                                    <template #button-content> <i class="ri-more-fill align-middle fs-16"></i> </template>
                                    <BDropdownItem>Share</BDropdownItem>
                                    <BDropdownItem> Report</BDropdownItem>
                                </BDropdown>
                            </div>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <h5 class="card-title mb-4 fw-semibold fs-16">Creators Grid Lists</h5>
            </BCol>
        </BRow>

        <BRow class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-03.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-2.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Michael Morris</h5>
                        </router-link>
                        <p class="text-muted mb-2">9784 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                        class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-6.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Charles Kubik</h5>
                        </router-link>
                        <p class="text-muted mb-2">4678 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="primary" class="w-100">Follow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-05.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/nft/img-06.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Alexis Clarke</h5>
                        </router-link>
                        <p class="text-muted mb-2">861 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-06.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">James Morris</h5>
                        </router-link>
                        <p class="text-muted mb-2">30174 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt=""
                        class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-8.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Herbert Stokes</h5>
                        </router-link>
                        <p class="text-muted mb-2">6487 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="primary" class="w-100">Follow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-03.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-2.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Michael Morris</h5>
                        </router-link>
                        <p class="text-muted mb-2">10137/ Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt=""
                        class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-6.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Tonya Noble</h5>
                        </router-link>
                        <p class="text-muted mb-2">364 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="primary" class="w-100">Follow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-05.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/nft/img-06.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Nancy Martino</h5>
                        </router-link>
                        <p class="text-muted mb-2">9513 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="@/assets/images/nft/img-01.jpg" alt="" class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Kevin Dawson</h5>
                        </router-link>
                        <p class="text-muted mb-2">6374 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="primary" class="w-100">Follow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol>
                <BCard no-body>
                    <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt=""
                        class="object-fit-cover card-img-top" height="120">
                    <BCardBody class="text-center">
                        <img src="@/assets/images/users/avatar-10.jpg" alt=""
                            class="avatar-md rounded-circle object-fit-cover mt-n5 border border-5 border-light mx-auto d-block">
                        <router-link to="/pages/profile">
                            <h5 class="mt-2 mb-1">Glen Matney</h5>
                        </router-link>
                        <p class="text-muted mb-2">7809 Products</p>
                        <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a
                            video.</p>
                        <BButton variant="soft-primary" class="w-100">Unfollow</BButton>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow class="g-0 text-center text-sm-start align-items-center mb-4">
            <BCol sm="6">
                <div>
                    <p class="mb-sm-0 text-muted">Showing <span class="fw-semibold">1</span> to <span
                            class="fw-semibold">10</span> of <span class="fw-semibold text-decoration-underline">12</span>
                        entries</p>
                </div>
            </BCol>

            <BCol sm="6">
                <ul class="pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0">
                    <li class="page-item disabled">
                        <router-link to="#" class="page-link">Previous</router-link>
                    </li>
                    <li class="page-item active">
                        <router-link to="#" class="page-link">1</router-link>
                    </li>
                    <li class="page-item ">
                        <router-link to="#" class="page-link">2</router-link>
                    </li>
                    <li class="page-item">
                        <router-link to="#" class="page-link">3</router-link>
                    </li>
                    <li class="page-item">
                        <router-link to="#" class="page-link">4</router-link>
                    </li>
                    <li class="page-item">
                        <router-link to="#" class="page-link">5</router-link>
                    </li>
                    <li class="page-item">
                        <router-link to="#" class="page-link">Next</router-link>
                    </li>
                </ul>
            </BCol>
        </BRow>
    </Layout>
</template>