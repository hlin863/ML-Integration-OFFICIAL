function run_uploaded_file(file) {

    // get the file name and size
    var fileName = file.name;

    // check the file type to see if it is Python.
    var fileType = file.type;

    // check the file size to see if it is less than 1MB.
    var fileSize = file.size;

    // check the file type to see if it is Python.

    if (fileType == "text/x-python") {



    }

}

const dropBox = document.querySelector("#dropbox");
dropBox.addEventListener("dragenter",dragEnter,false);
dropBox.addEventListener("dragover",dragOver,false);
dropBox.addEventListener("drop",drop,false);

function dragEnter(e){
	e.stopPropagation();
	e.preventDefault();
}

function dragOver(e){
	e.stopPropagation();
	e.preventDefault();
}

function drop(e){
	// 当文件拖拽到dropBox区域时,可以在该事件取到files
	const files = e.dataTransfer.files;
}

function upload_file(){

    // updates the file and produce a message to state that the file has been updated
    var file = document.getElementById('inputMLFile').files[0];

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

            // implement a function to run the uploaded file
            run_uploaded_file(file);

        }

        

        reader.readAsText(file);
    } else {
        document.getElementById('display-code-details').innerHTML += '<pyscript>';

        document.getElementById('display-code-details').innerHTML += '</pyscript>'; 
    }

    document.getElementById('display-file-details').innerHTML += "File " + fileName + " has been uploaded";

}