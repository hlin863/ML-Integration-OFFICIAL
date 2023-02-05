function upload_file(){

    var filename = document.getElementById('inputMLFile').files[0].name; 

    var file = document.getElementById('inputMLFile').files[0];  // stores the file details..

    // download file onto a local document
    

    console.log(filename);

    // var form_data = new FormData();
    // form_data.append('file', file);

    // $.ajax({
    //     url: '/upload_file/',
    //     type: 'POST',
    //     data: form_data,
    //     contentType: false,
    //     processData: false,
    //     success: function (data) {
    //         alert(data);
    //     },
    //     error: function (data) {
    //         alert(data);
    //     }
    // });

}

// function download(filename, text) {
//     var element = document.createElement('a');
//     element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
//     element.setAttribute('download', filename);
  
//     element.style.display = 'none';
//     document.body.appendChild(element);
  
//     element.click();
  
//     document.body.removeChild(element);
// }

// // Example usage
// document.getElementById("downloadLink").addEventListener("click", function() {
//     download("example.txt", "This is some example text to be downloaded.");
// });
