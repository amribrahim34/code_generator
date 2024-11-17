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
        <PageHeader title="Sitemap" pageTitle="Pages" />
        <BRow>
            <BCol lg="12">
                <BCard no-body>
                    <BCardHeader>
                        <BCardTitle class="mb-0">Responsive Sitemap</BCardTitle>
                    </BCardHeader>
                    <BCardBody>
                        <div class="sitemap-content">
                            <figure class="sitemap-horizontal">
                                <ul class="administration">
                                    <li>
                                        <ul class="director">
                                            <li>
                                                <BLink href="javascript:void(0);" class="fw-semibold"><span>Velzon
                                                        Admin</span></BLink>
                                                <ul class="subdirector">
                                                    <li>
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>Contact
                                                                Us</span></BLink>
                                                    </li>
                                                </ul>
                                                <ul class="departments">
                                                    <li>
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>Main
                                                                Pages</span></BLink>
                                                    </li>

                                                    <li class="department">
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>Account
                                                                Management</span></BLink>
                                                        <ul>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Sign Up</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Login</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Profile
                                                                        Settings</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Modify
                                                                        Reservation</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Cancel
                                                                        Reservation</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Write
                                                                        Reviews</span></BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                    <li class="department">
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>About
                                                                Us</span></BLink>
                                                        <ul>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Overview</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Connect Via Social
                                                                        Media</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Careers</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Team
                                                                        Members</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Policies</span>
                                                                </BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                    <li class="department">
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>Book a
                                                                Trip</span></BLink>
                                                        <ul>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Travel
                                                                        Details</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Reservation
                                                                        Process</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Payment
                                                                        Option</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Confirmation</span>
                                                                </BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                    <li class="department">
                                                        <BLink href="javascript:void(0);" class="fw-semibold">
                                                            <span>Destination</span>
                                                        </BLink>
                                                        <ul>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Architecture</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Art</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Entertainment</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>History</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Science</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Sports</span>
                                                                </BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Music</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Tracking
                                                                        Camp</span></BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                    <li class="department">
                                                        <BLink href="javascript:void(0);" class="fw-semibold"><span>Travel
                                                                Tips</span></BLink>
                                                        <ul>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>General
                                                                        Travel</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Helpth
                                                                        Concerns</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>Safety
                                                                        Measures</span></BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript:void(0);"><span>FAQ's</span></BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </figure>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <BCard no-body>
                    <BCardHeader>
                        <BCardTitle class="mb-0">Horizontal</BCardTitle>
                    </BCardHeader>
                    <BCardBody>
                        <div class="hori-sitemap">
                            <ul class="list-unstyled mb-0">
                                <li class="p-0 parent-title">
                                    <BLink href="javascript: void(0);" class="fw-semibold fs-14">My
                                        Account</BLink>
                                </li>
                                <ul class="list-unstyled row g-0">
                                    <li class="col-sm-3">
                                        <BLink href="javascript: void(0);" class="fw-semibold sub-title">About Us</BLink>
                                        <ul class="list-unstyled row g-0 second-list">
                                            <li class="col-sm-6">
                                                <BLink href="javascript: void(0);">Overview</BLink>
                                            </li>
                                            <li class="col-sm-6">
                                                <BLink href="javascript: void(0);">History</BLink>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="col-sm-3">
                                        <BLink href="javascript: void(0);" class="fw-semibold">My self-care Plan</BLink>
                                        <ul class="list-unstyled second-list pt-0">
                                            <li>
                                                <div>
                                                    <BLink href="javascript: void(0);">Basic</BLink>
                                                    <BLink href="javascript: void(0);">Early Physiotherapy</BLink>
                                                    <BLink href="javascript: void(0);">Intermediate Physiotherapy</BLink>
                                                    <BLink href="javascript: void(0);">Return to Normal Activity</BLink>
                                                </div>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="col-sm-3">
                                        <BLink href="javascript: void(0);" class="fw-semibold sub-title">Support Us</BLink>
                                        <ul class="list-unstyled row g-0 sub-list">
                                            <li class="col-sm-6">
                                                <BLink href="javascript: void(0);">Contact Us</BLink>
                                            </li>
                                            <li class="col-sm-6">
                                                <BLink href="javascript: void(0);">Customer Services</BLink>
                                                <ul class="list-unstyled second-list">
                                                    <li>
                                                        <div>
                                                            <BLink href="javascript: void(0);">Chat With Us</BLink>
                                                            <BLink href="javascript: void(0);">Connect Information</BLink>
                                                            <BLink href="javascript: void(0);">FAQ'S</BLink>
                                                        </div>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="col-sm-3">
                                        <BLink href="javascript: void(0);" class="fw-semibold">Terms & Conditions</BLink>
                                    </li>
                                </ul>
                            </ul>
                        </div>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>

        <BRow>
            <BCol lg="12">
                <BCard no-body>
                    <BCardHeader>
                        <BCardTitle class="mb-0">Vertical</BCardTitle>
                    </BCardHeader>
                    <BCardBody>
                        <BRow>
                            <BCol sm="6">
                                <div class="verti-sitemap">
                                    <ul class="list-unstyled mb-0">
                                        <li class="p-0 parent-title">
                                            <BLink href="javascript: void(0);" class="fw-medium fs-14">Nancy Martino -
                                                Project Director</BLink>
                                        </li>
                                        <li>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary">Erica
                                                        Kernan - Team Leader</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Jason McQuaid -
                                                            Member</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Elwood Arter -
                                                            Member</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary">Mary
                                                        Jones
                                                        - Project Manager</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Jordyn Jones -
                                                            Designer</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Ashlee Haney -
                                                            Developer</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Rashad Charles -
                                                            BackEnd Developer</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Walter Newman -
                                                            Frontend Developer</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Adam Moss -
                                                            Designer</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary">Tilly
                                                        Kent
                                                        - Executive Manager</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Tyler Porter -
                                                            Account Executive</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Alicia Thompson -
                                                            Sales Executive</BLink>
                                                        <ul class="third-list list-unstyled">
                                                            <li>
                                                                <BLink href="javascript: void(0);">Jack
                                                                    Coates -
                                                                    Member</BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript: void(0);">Owen
                                                                    Jarvis -
                                                                    Member</BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript: void(0);">Ashlee
                                                                    Haney
                                                                    - Member</BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript: void(0);">Archie
                                                                    Cook -
                                                                    Member</BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary">Rachel
                                                        Rose
                                                        - HR</BLink>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </BCol>

                            <BCol sm="6">
                                <div class="verti-sitemap">
                                    <ul class="list-unstyled mb-0">
                                        <li class="p-0 parent-title">
                                            <BLink href="javascript: void(0);" class="fw-medium fs-14">Velzon</BLink>
                                        </li>
                                        <li>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary"><i
                                                            class="ri-airplay-line me-1 align-bottom"></i>
                                                        Dashboards</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Analytics</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">CRM</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary"><i
                                                            class="ri-pencil-ruler-2-line me-1 align-bottom"></i>
                                                        App Pages</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Calender</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Chat</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Email</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Ecommerce</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Projects</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Tasks</BLink>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary"><i
                                                            class="ri-file-list-3-line me-1 align-bottom"></i>
                                                        Pages</BLink>
                                                </div>
                                            </div>
                                            <div class="first-list">
                                                <div class="list-wrap">
                                                    <BLink href="javascript: void(0);" class="fw-medium text-primary"><i
                                                            class="ri-stack-line me-1 align-bottom"></i>
                                                        Components</BLink>
                                                </div>
                                                <ul class="second-list list-unstyled">
                                                    <li>
                                                        <BLink href="javascript: void(0);">Base UI</BLink>
                                                    </li>
                                                    <li>
                                                        <BLink href="javascript: void(0);">Advance UI</BLink>
                                                        <ul class="third-list list-unstyled">
                                                            <li>
                                                                <BLink href="javascript: void(0);">Sweet
                                                                    Alerts</BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript: void(0);">Range
                                                                    Slider</BLink>
                                                            </li>
                                                            <li>
                                                                <BLink href="javascript: void(0);">Nestable
                                                                    List</BLink>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </BCol>
                        </BRow>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </Layout>
</template>