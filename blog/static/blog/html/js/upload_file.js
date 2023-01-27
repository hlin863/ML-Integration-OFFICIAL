function upload_file(){

    // updates the file and produce a message to state that the file has been updated
    var file = document.getElementById('inputMLFile').files[0];

    // get the file name and size
    var fileName = file.name;

    // check the file type to see if it is Python.
    var fileType = file.type;

    if (fileType == "text/x-python") {
        document.getElementById('display-file-details').innerHTML += "Python file uploaded" + "<br>";        
    }

    document.getElementById('display-file-details').innerHTML += "File " + fileName + " has been uploaded";

}