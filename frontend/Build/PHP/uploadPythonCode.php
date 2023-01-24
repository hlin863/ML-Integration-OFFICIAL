<?php
$target_dir = "upload/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
$allowedTypes = ['jpg', 'png'];

if (isset($_POST["submit"])) {
    // check type
    if (!in_array($imageFileType, $allowedTypes)) {
        $msg = "Type is not allowed";
    } // Check if file already exists
    elseif (file_exists($target_file)) {
        $msg = "Sorry, file already exists.";
    } // Check file size
    elseif ($_FILES["fileToUpload"]["size"] > 5000000) {
        $msg = "Sorry, your file is too large.";
    } elseif (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $msg = "The file " . basename($_FILES["fileToUpload"]["name"]) . " has been uploaded.";
    }
}

?>