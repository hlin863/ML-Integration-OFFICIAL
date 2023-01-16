<?php
    if (isset($_FILES['file'])) {
        $host = "http://192.168.56.1:8081/Build/build.html";
        $user = "username";
        $pass = "password";
        $destDir = "";    
        $workDir = "C:\Users\haoch\OneDrive\Documents\UCL\COMPSI-Yr4\Final_Year_Project\OFFICIAL-REPO\ML-Integration-OFFICIAL\frontend";

        $tmpName = basename($_FILES['file']['tmp_name']);
        move_uploaded_file($_FILES['file']['tmp_name'], $workDir.$tmpName) or die("Cannot move uploaded file to working directory");

        $conn = ftp_connect($host) or die ("Cannot initiate connection to host");
        ftp_login($conn, $user, $pass) or die("Cannot login");
        $upload = ftp_put($conn, $destDir."/".$_FILES['file']['name'], $workDir.$tmpName, FTP_BINARY);
        if (!$upload) {
            echo "Cannot upload\n";
        } else {
            echo "Upload complete\n";
        }
        ftp_close($conn);

        unlink($workDir.$tmpName) or die("Cannot delete uploaded file from working directory -- manual deletion recommended");
    }
?>
