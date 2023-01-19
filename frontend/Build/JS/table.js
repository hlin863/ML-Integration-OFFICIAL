function add_entry(){

    var table = document.getElementById("ci-result-table");

    // count the number of rows in the table.
    var rowCount = table.rows.length;

    // create a new row.
    var row = table.insertRow(rowCount);

    var columnCount = table.rows[0].cells.length;

    console.log("columnCount: " + columnCount);

    for (let i = 0; i < columnCount; i++){

      var cell = row.insertCell(i);
      cell.innerHTML = i;

    }

}