function add_entry(){
    var date = new Date();

    var y = date.getFullYear();

    var m = date.getMonth() + 1;

    var d = date.getDate();

    console.log("y: " + y + " m: " + m + " d: " + d);

    var table = document.getElementById("ci-result-table");

    // count the number of rows in the table.
    var rowCount = table.rows.length;

    // create a new row.
    var row = table.insertRow(rowCount);

    var columnCount = table.rows[0].cells.length;

    console.log("columnCount: " + columnCount);

    for (let i = 0; i < columnCount; i++){

      if (i == 1){

        var cell = row.insertCell(i);
        cell.innerHTML = d + "-" + m + "-" + y;

      } else {
          
        var cell = row.insertCell(i);
        cell.innerHTML = i;
  
      }

    }

}