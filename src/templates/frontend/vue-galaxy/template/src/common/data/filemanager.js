// Apps > FileManager

const folderList = [{
    id: 1,
    name: "Projects",
    files: "349",
    storage: "4.10",
    ischecked: true,
},
{
    id: 2,
    name: "Documents",
    files: "2348",
    storage: "27.01",
    ischecked: false,
},
{
    id: 3,
    name: "Media",
    files: "12480",
    storage: "20.87",
    ischecked: false,
},
{
    id: 4,
    name: "Velzon v1.7.0",
    files: "180",
    storage: "478.65MB",
    ischecked: true,
}];

const fileList = [{
    id: 1,
    icon: "ri-gallery-fill",
    iconClass: "success",
    fileName: "logo-dark.png",
    fileType: "Media",
    fileItem: "01",
    fileSize: "1.3 MB",
    date: "24 May, 2022",
},
{
    id: 2,
    icon: "ri-file-pdf-fill",
    iconClass: "danger",
    fileName: "velzon-invoice.pdf",
    fileType: "Documents",
    fileItem: "01",
    fileSize: "1.1 MB",
    date: "05 May, 2022",
},
{
    id: 3,
    icon: "ri-folder-2-fill",
    iconClass: "warning",
    fileName: "Velzon React",
    fileType: "Media",
    fileItem: "367",
    fileSize: "934 MB",
    date: "28 Apr, 2022",
},
{
    id: 4,
    icon: "ri-file-text-fill",
    iconClass: "secondary",
    fileName: "html.docx",
    fileType: "Documents",
    fileItem: "01",
    fileSize: "0.3 KB",
    date: "19 Apr, 2022",
},
{
    id: 5,
    icon: "ri-gallery-fill",
    iconClass: "success",
    fileName: "default.jpg",
    fileType: "Media",
    fileItem: "01",
    fileSize: "1.7 MB",
    date: "06 Apr, 2022",
}];

export { folderList, fileList };