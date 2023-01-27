function get_date(){

    // initialise a date variable to process when the operation started.
    var date = new Date();

    return date;

}

function run_workflow(){
    console.log("The workflow is running...");

    var start_date = get_date();
    
    // The workflow is running...
    console.log("The workflow started at " + start_date);

    var workflow_table = document.getElementById("ci-result-table");

    // insert a row at the end of the table
    var row = workflow_table.insertRow(-1);

    // count the number of columns in the workflow table
    var col = workflow_table.rows[0].cells.length;

    for (var i = 0; i < col; i++) {
        var newcell = row.insertCell(i);
        if (i == 1){
            newcell.innerHTML = start_date; // inserted the start date into the ci work flow table.
        } else {
            newcell.innerHTML = i;
        }
    }
}