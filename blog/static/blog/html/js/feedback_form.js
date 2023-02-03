function sendFeedback(){
    let feedbackElement = document.getElementById("feedback-display");

    let currentTime = new Date();

    // add the time of feedback to the feedback
    feedbackElement.value += currentTime + "\n";
}