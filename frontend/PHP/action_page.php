<?php
    if(isset($_FILES["codename"]) && $_FILES["codename"]["error"] == 0){
        $allowed = array("py" => "text/python");
        $filename = $_FILES["codename"]["name"];
        $filetype = $_FILES["codename"]["type"];
        $filesize = $_FILES["codename"]["size"];

        // Verify file extension
        $ext = pathinfo($filename, PATHINFO_EXTENSION);
        if(!array_key_exists($ext, $allowed)) die("Error: Please select a valid file format.");

        // Verify file size - 50MB maximum
        $maxsize = 50 * 1024 * 1024;
        if($filesize > $maxsize) die("Error: File size is larger than the 50 MB limit.");

        // Verify MYME type of the file
        if(in_array($filetype, $allowed)){
            // Check whether file exists before uploading it
            if(file_exists("upload/" . $filename)){
                echo $filename . " is already exists.";
            } else{
                move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], "upload/" . $filename);
                echo "Your file was uploaded successfully.";
            } 
        } else{
            echo "Error: There was a problem uploading your file. Please try again."; 
        }
    } else{
        echo "Error: " . $_FILES["fileToUpload"]["error"];
    }
?>
