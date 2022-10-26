<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<body>
File Uploaded
<a href="Upload.html">Click here to upload another file</a> <br>
<a href="index.html">Home</a>
<?php
$target_dir = "files/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
?>
</body>
</html>
