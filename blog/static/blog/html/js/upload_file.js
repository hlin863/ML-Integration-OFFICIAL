function upload_file(){

    var file = document.getElementById('inputMLFile').files[0]; 

    console.log(file);

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