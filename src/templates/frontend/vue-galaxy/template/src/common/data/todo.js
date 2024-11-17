// Apps > Todo

const todoList = [{
    id: 1,
    checkedElem: false,
    todo: 'Added Email Templates',
    assignedto: [{
        assigneeName: "Test 01",
        assigneeImg: require("@/assets/images/users/avatar-1.jpg"),
    }, {
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }
    ],
    dueDate: '03 Apr, 2022',
    status: 'Inprogress',
    priority: "High"
}, {
    id: 2,
    checkedElem: false,
    todo: 'Additional Mailbox',
    assignedto: [{
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }, {
        assigneeName: "Diego Norris",
        assigneeImg: require("@/assets/images/users/avatar-9.jpg"),
    }, {
        assigneeName: "Anthony Mills",
        assigneeImg: require("@/assets/images/users/avatar-10.jpg"),
    }
    ],
    dueDate: '02 Apr, 2022',
    status: 'Pending',
    priority: "Medium"
}, {
    id: 3,
    checkedElem: true,
    todo: 'Make a creating an account profile',
    assignedto: [{
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }, {
        assigneeName: "Marian Angel",
        assigneeImg: require("@/assets/images/users/avatar-6.jpg"),
    }, {
        assigneeName: "Johnnie Walton",
        assigneeImg: require("@/assets/images/users/avatar-7.jpg"),
    }, {
        assigneeName: "Donna Weston",
        assigneeImg: require("@/assets/images/users/avatar-8.jpg"),
    }
    ],
    dueDate: '02 May, 2022',
    status: 'Completed',
    priority: "Low"
}, {
    id: 4,
    checkedElem: false,
    todo: 'Added new tabs styles',
    assignedto: [{
        assigneeName: "James Forbes",
        assigneeImg: require("@/assets/images/users/avatar-2.jpg"),
    }
    ],
    dueDate: '01 May, 2022',
    status: 'New',
    priority: "Low"
}, {
    id: 5,
    checkedElem: false,
    todo: 'Added bdge new style - gradient',
    assignedto: [{
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }, {
        assigneeName: "Anthony Mills",
        assigneeImg: require("@/assets/images/users/avatar-10.jpg"),
    }, {
        assigneeName: "Diego Norris",
        assigneeImg: require("@/assets/images/users/avatar-9.jpg"),
    }
    ],
    dueDate: '01 May, 2022',
    status: 'Inprogress',
    priority: "Medium"
}, {
    id: 6,
    checkedElem: false,
    todo: 'Added Back to Top button',
    assignedto: [{
        assigneeName: "Marian Angel",
        assigneeImg: require("@/assets/images/users/avatar-6.jpg"),
    }, {
        assigneeName: "Johnnie Walton",
        assigneeImg: require("@/assets/images/users/avatar-7.jpg"),
    }
    ],
    dueDate: '30 Apr, 2022',
    status: 'Inprogress',
    priority: "High"
}, {
    id: 7,
    checkedElem: true,
    todo: 'Added File Manager Apps',
    assignedto: [{
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }, {
        assigneeName: "Mary Gant",
        assigneeImg: require("@/assets/images/users/avatar-4.jpg"),
    }, {
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }
    ],
    dueDate: '29 Apr, 2022',
    status: 'Completed',
    priority: "Medium"
}, {
    id: 8,
    checkedElem: false,
    todo: 'Datatable with jQuery cdn',
    assignedto: [{
        assigneeName: "Marian Angel",
        assigneeImg: require("@/assets/images/users/avatar-6.jpg"),
    }, {
        assigneeName: "Johnnie Walton",
        assigneeImg: require("@/assets/images/users/avatar-7.jpg"),
    }, {
        assigneeName: "Donna Weston",
        assigneeImg: require("@/assets/images/users/avatar-8.jpg"),
    }
    ],
    dueDate: '28 Apr, 2022',
    status: 'Pending',
    priority: "High"
}, {
    id: 9,
    checkedElem: false,
    todo: 'Profile Page Structure',
    assignedto: [{
        assigneeName: "Mary Gant",
        assigneeImg: require("@/assets/images/users/avatar-4.jpg"),
    }, {
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }
    ],
    dueDate: '27 Apr, 2022',
    status: 'New',
    priority: "Low"
}, {
    id: 10,
    checkedElem: true,
    todo: 'Make a creating an account profile',
    assignedto: [{
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }
    ],
    dueDate: '26 Apr, 2022',
    status: 'Completed',
    priority: "Medium"
}, {
    id: 11,
    checkedElem: true,
    todo: 'Change email option process',
    assignedto: [{
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }, {
        assigneeName: "Anthony Mills",
        assigneeImg: require("@/assets/images/users/avatar-10.jpg"),
    }, {
        assigneeName: "Diego Norris",
        assigneeImg: require("@/assets/images/users/avatar-9.jpg"),
    }
    ],
    dueDate: '25 Apr, 2022',
    status: 'Completed',
    priority: "High"
}, {
    id: 12,
    checkedElem: false,
    todo: 'Brand Logo design',
    assignedto: [{
        assigneeName: "James Forbes",
        assigneeImg: require("@/assets/images/users/avatar-2.jpg"),
    }, {
        assigneeName: "Anthony Mills",
        assigneeImg: require("@/assets/images/users/avatar-10.jpg"),
    }, {
        assigneeName: "Diego Norris",
        assigneeImg: require("@/assets/images/users/avatar-9.jpg"),
    }
    ],
    dueDate: '25 Apr, 2022',
    status: 'New',
    priority: "Medium",
}, {
    id: 13,
    checkedElem: false,
    todo: 'Add Dynamic Contact List',
    assignedto: [{
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }, {
        assigneeName: "Marian Angel",
        assigneeImg: require("@/assets/images/users/avatar-6.jpg"),
    }, {
        assigneeName: "Johnnie Walton",
        assigneeImg: require("@/assets/images/users/avatar-7.jpg"),
    }, {
        assigneeName: "Donna Weston",
        assigneeImg: require("@/assets/images/users/avatar-8.jpg"),
    }
    ],
    dueDate: '24 Apr, 2022',
    status: 'Inprogress',
    priority: "Low"
}, {
    id: 14,
    checkedElem: true,
    todo: 'Additional Calendar',
    assignedto: [{
        assigneeName: "Virgie Price",
        assigneeImg: require("@/assets/images/users/avatar-5.jpg"),
    }, {
        assigneeName: "Diego Norris",
        assigneeImg: require("@/assets/images/users/avatar-9.jpg"),
    }, {
        assigneeName: "Anthony Mills",
        assigneeImg: require("@/assets/images/users/avatar-10.jpg"),
    }
    ],
    dueDate: '23 Apr, 2022',
    status: 'Completed',
    priority: "Medium",
}, {
    id: 15,
    checkedElem: false,
    todo: 'Added Select2',
    assignedto: [{
        assigneeName: "Curtis Saenz",
        assigneeImg: require("@/assets/images/users/avatar-1.jpg"),
    }, {
        assigneeName: "John Robles",
        assigneeImg: require("@/assets/images/users/avatar-3.jpg"),
    }
    ],
    dueDate: '23 Apr, 2022',
    status: 'Pending',
    priority: "High"
}];

export { todoList };