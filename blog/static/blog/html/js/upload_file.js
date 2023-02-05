function upload_file(){

    var filename = document.getElementById('inputMLFile').files[0].name; 

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