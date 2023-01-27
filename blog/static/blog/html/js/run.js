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
}