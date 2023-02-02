function upload_file(){

    // updates the file and produce a message to state that the file has been updated
    var file = document.getElementById('inputDataFile').files[0];

    // get the file name and size
    var fileName = file.name;

    // check the file type to see if it is Python.
    var fileType = file.type;

    document.getElementById('display-file-details').innerHTML = ""; // resets the display with each file upload.
    
    if (fileType == "text/x-python") {
        document.getElementById('display-file-details').innerHTML += "Python file uploaded" + "<br>";        

        // convert the file content into python code
        var reader = new FileReader();

        // document.getElementById('display-code-details').innerHTML = ''; 
        // resets the display with each file upload.

        reader.onload = function(e) {
            var fileContent = e.target.result;
            // document.getElementById('display-file-details').innerHTML += fileContent;
            document.getElementById('display-code-details').innerHTML += ('<pyscript>' + fileContent + '</pyscript>');
        }

        

        reader.readAsText(file);
    } else {
        document.getElementById('display-code-details').innerHTML += '<pyscript>';

        document.getElementById('display-code-details').innerHTML += '</pyscript>'; 
    }

    document.getElementById('display-file-details').innerHTML += "File " + fileName + " has been uploaded";

}