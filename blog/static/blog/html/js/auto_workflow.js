function run_auto_workflow(){
    // function aims to run an automated workflow using the GitHub link, train script
    // and test script provided by the user
    // the function will run the train script and then the test script

    // get the GitHub link
    var git_link = document.getElementById("git_link").value;

    // get the train script
    var train_script = document.getElementById("train_script").value;

    // get the test script
    var test_script = document.getElementById("test_script").value;

    // get the user's email
    var email = document.getElementById("email").value;

    var user_name = document.getElementById("git_user_name").value;

    const personal_access_token = "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";

    const repo = git_link;

    const owner = user_name;

    fetch(repo, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${personal_access_token}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          ref: 'main',
          inputs: {
            message: 'Hello from JavaScript!'
          }
        })
    });

    // run the train script
    // $.ajax({
    //     type: "POST",
    //     url: "/run_train_script",
    //     data: {
    //         git_link: git_link,
    //         train_script: train_script,
    //         email: email
    //     },
    //     success: function(data){
    //         // run the test script
    //         $.ajax({
    //             type: "POST",
    //             url: "/run_test_script",
    //             data: {
    //                 git_link: git_link,
    //                 test_script: test_script,
    //                 email: email
    //             },
    //             success: function(data){
    //                 // display the results
    //                 document.getElementById("results").innerHTML = data;
    //             }
    //         });
    //     }
    // });
}