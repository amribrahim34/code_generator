// Apps > Tasks

// Tasks > Kanban Board
const unassigned = [{
    board_id: 1,
    title: "Profile Page Structure",
    description: "Profile Page means a web page accessible to the public or to guests.",
    features: ["Admin"],
    users: [require("@/assets/images/users/avatar-6.jpg"), require("@/assets/images/users/avatar-5.jpg")],
    id: "#VL2436",
    watch: "04",
    message: "19",
    file: "2"
},
{
    board_id: 2,
    title: "Velzon - Admin Layout Design",
    description: "The dashboard is the front page of the Administration UI.",
    features: ["Layout", "Admin", "Dashboard"],
    users: [require("@/assets/images/users/avatar-7.jpg"), require("@/assets/images/users/avatar-6.jpg"), require("@/assets/images/users/avatar-1.jpg")],
    id: "#VL2436",
    watch: "04",
    message: "19",
    file: "2",
    date: " 07 Jan, 2022"
}];

const todo = [{
    board_id: 1,
    title: "Admin Layout Design",
    description: "Landing page template with clean, minimal and modern design.",
    features: ["Design", "Wensite"],
    users: [require("@/assets/images/users/avatar-10.jpg"), require("@/assets/images/users/avatar-3.jpg")],
    id: "#VL2436",
    watch: "13",
    message: "52",
    file: "17",
    date: " 07 Jan, 2022"
},
{
    board_id: 2,
    title: "Marketing & Sales",
    description: "Sales and marketing are two business functions within an organization.",
    features: ["Marketing", "Business"],
    users: [require("@/assets/images/users/avatar-9.jpg"), require("@/assets/images/users/avatar-8.jpg")],
    id: "#VL2436",
    watch: "24",
    message: "10",
    file: "10",
    date: " 27 Dec, 2021"
}];

const inprogress = [{
    board_id: 1,
    title: "Brand Logo Design ",
    description: "BrandCrowd's brand logo maker allows you to generate and customize stand-out brand logos in minutes.",
    features: ["Logo", "Design", "UI/UX"],
    users: [require("@/assets/images/users/avatar-10.jpg"), require("@/assets/images/users/avatar-3.jpg")],
    id: "#VL2436",
    watch: "24",
    message: "10",
    file: "10",
    date: " 22 Dec, 2022"
},
{
    board_id: 2,
    title: "Change Old App Icon",
    description: "Change app icons on Android: How do you change the look of your apps.",
    features: ["Marketing", "Business"],
    users: [require("@/assets/images/users/avatar-9.jpg"), require("@/assets/images/users/avatar-8.jpg")],
    id: "#VL2436",
    watch: "64",
    message: "35",
    file: "23",
    date: " 24 Oct, 2021"
}];

const reviews = [{
    board_id: 1,
    title: "Product Features Analysis",
    description: "An essential part of strategic planning is running a product feature analysis.",
    features: ["Project", "Analysis"],
    users: [require("@/assets/images/users/avatar-5.jpg"), require("@/assets/images/users/avatar-6.jpg")],
    id: "#VL2436",
    watch: "14",
    message: "31",
    file: "07",
    date: " 05 Jan, 2022"
},
{
    board_id: 2,
    title: "Create a Graph of Sketch",
    description: "To make a pie chart with equal slices create a perfect circle by selecting an Oval Tool.",
    features: ["Sketch", "Marketing", "Design"],
    users: [require("@/assets/images/users/avatar-4.jpg"), require("@/assets/images/users/avatar-8.jpg"), require("@/assets/images/users/avatar-2.jpg"), require("@/assets/images/users/avatar-1.jpg")],
    id: "#VL2436",
    watch: "64",
    message: "35",
    file: "23",
    date: " 24 Oct, 2021"
}];

const completed = [{
    board_id: 1,
    title: "Create a Blog Template UI",
    description: "Landing page template with clean, minimal and modern design.",
    features: ["Design", "Website"],
    users: [require("@/assets/images/users/avatar-8.jpg"), require("@/assets/images/users/avatar-7.jpg"), require("@/assets/images/users/avatar-6.jpg")],
    id: "#VL2451",
    watch: "24",
    message: "10",
    file: "10",
    date: " 05 Jan, 2022"
}];

const newData = [{
    board_id: 1,
    title: "Banner Design for FB & Twitter",
    image: require("@/assets/images/small/img-4.jpg"),
    features: ["UI/UX", "Graphic"],
    users: [require("@/assets/images/users/avatar-8.jpg"), require("@/assets/images/users/avatar-7.jpg"), require("@/assets/images/users/avatar-6.jpg")],
    id: "#VL2451",
    watch: "24",
    message: "10",
    file: "10",
    date: " 05 Jan, 2022"
}];

// Tasks > List View
const allTask = [{
    id: 1,
    taskId: "#VLZ632",
    project: "Velzon - v1.0.0",
    task: "Error message when placing an orders?",
    creater: "Robert McMahon",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-3.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-1.jpg")
    },
    ],
    dueDate: "25 Jan, 2022",
    status: "Inprogress",
    statusClass: "secondary",
    priority: "High",
    priorityClass: "danger",
},
{
    id: 2,
    taskId: "#VLZ453",
    project: "Skote - v1.0.0",
    task: "Profile Page Structure",
    creater: "Mary Cousar",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-10.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-9.jpg")
    },
    {
        id: 3,
        img: require("@/assets/images/users/avatar-5.jpg")
    },
    ],
    dueDate: "20 Dec, 2021",
    status: "New",
    statusClass: "info",
    priority: "Low",
    priorityClass: "success",
},
{
    id: 3,
    taskId: "#VLZ454",
    project: "Skote - v2.3.0",
    task: "Apologize for shopping Error!",
    creater: "Nathan Cole",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-5.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-6.jpg")
    },
    {
        id: 3,
        img: require("@/assets/images/users/avatar-7.jpg")
    },
    {
        id: 4,
        img: require("@/assets/images/users/avatar-8.jpg")
    },
    ],
    dueDate: "23 Oct, 2021",
    status: "Completed",
    statusClass: "success",
    priority: "Medium",
    priorityClass: "warning",
},
{
    id: 4,
    taskId: "#VLZ455",
    project: "Minia - v1.4.0",
    task: "Post launch reminder/ post list",
    creater: "Joseph Parker",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-2.jpg")
    },],
    dueDate: "05 Oct, 2021",
    status: "Pending",
    statusClass: "warning",
    priority: "High",
    priorityClass: "danger",
},
{
    id: 5,
    taskId: "#VLZ456",
    project: "Minia - v1.2.0",
    task: "Make a creating an account profile",
    creater: "Henry Baird",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-3.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-10.jpg")
    },
    {
        id: 3,
        img: require("@/assets/images/users/avatar-9.jpg")
    },
    ],
    dueDate: "17 Oct, 2021",
    status: "Inprogress",
    statusClass: "secondary",
    priority: "Medium",
    priorityClass: "warning",
},
{
    id: 6,
    taskId: "#VLZ657",
    project: "Minimal - v2.1.0",
    task: "Change email option process",
    creater: "Tonya Noble",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-6.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-7.jpg")
    },
    ],
    dueDate: "04 Dec, 2021",
    status: "Completed",
    statusClass: "success",
    priority: "High",
    priorityClass: "danger",
},
{
    id: 7,
    taskId: "#VLZ458",
    project: "Dason - v1.1.0",
    task: "User research",
    creater: "Donald Palmer",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-10.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-9.jpg")
    },
    {
        id: 3,
        img: require("@/assets/images/users/avatar-8.jpg")
    },
    {
        id: 4,
        img: require("@/assets/images/users/avatar-1.jpg")
    },
    ],
    dueDate: "11 Oct, 2021",
    status: "New",
    statusClass: "info",
    priority: "Low",
    priorityClass: "success",
},
{
    id: 8,
    taskId: "#VLZ459",
    project: "Dorsin - Landing Page",
    task: "Benner design for FB & Twitter",
    creater: "Carter",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-5.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-4.jpg")
    },
    ],
    dueDate: "16 Dec, 2021",
    status: "Pending",
    statusClass: "warning",
    priority: "Medium",
    priorityClass: "warning",
},
{
    id: 9,
    taskId: "#VLZ460",
    project: "Qexal - Landing Page",
    task: "Brand logo design",
    creater: "David Nichols",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-6.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-7.jpg")
    },
    {
        id: 3,
        img: require("@/assets/images/users/avatar-8.jpg")
    },
    ],
    dueDate: "29 Dec, 2021",
    status: "Pending",
    statusClass: "warning",
    priority: "High",
    priorityClass: "danger",
},
{
    id: 10,
    taskId: "#VLZ461",
    project: "Doot - Chat App Template",
    task: "Additional Calendar",
    creater: "Diana Kohler",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-4.jpg")
    },],
    dueDate: "13 Oct, 2021",
    status: "New",
    statusClass: "info",
    priority: "Low",
    priorityClass: "success",
},
{
    id: 11,
    taskId: "#VLZ462",
    project: "Skote - v2.1.0",
    task: "Edit customer testimonial",
    creater: "Nathan Cole",
    subItem: [{
        id: 1,
        img: require("@/assets/images/users/avatar-7.jpg")
    },
    {
        id: 2,
        img: require("@/assets/images/users/avatar-8.jpg")
    },
    ],
    dueDate: "02 Jan, 2021",
    status: "Inprogress",
    statusClass: "secondary",
    priority: "Medium",
    priorityClass: "warning",
}];

export { unassigned, todo, inprogress, reviews, completed, newData, allTask };