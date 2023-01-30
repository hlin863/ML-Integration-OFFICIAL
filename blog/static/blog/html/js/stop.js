function run_stop(){
    console.log("The stop operation is running...");

    // stops the current operation and adds a new column into the table. 
    var build_table = document.getElementById("ci-result-table");

    var stop_time = new Date();

    console.log(build_table.rows.length - 1);

    // edit the last row of the table
    var last_row = build_table.rows.length - 1;

    // update the 3rd column in the last row
    build_table.rows[last_row].cells[2].innerHTML = stop_time;

    console.log("The stop operation is done.");

    console.log(stop_time);

}