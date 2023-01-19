// create a table for processing the JavaScript files. 
const realTimeData = $('#realtime').DataTable({
    data: DataSet,
    columns: [
        { title: "Start Time" },
        { title: "End Time" },
        { title: "Duration" },
        { title: "Status" }
    ]
})