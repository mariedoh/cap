<?php
// Set error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

$response = [
    'success' => false,
    'message' => '',
    'export_path' => ''
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_FILES['student_data']) || !isset($_FILES['classroom_data'])) {
        $response['message'] = "Files Not Uploaded";
        echo json_encode($response);
        exit;
    }

    function isExcelFile($file) {
        $allowedExtensions = ['xlsx', 'xls'];
        $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
        return in_array($fileExtension, $allowedExtensions);
    }

    if (!isExcelFile($_FILES['student_data']) || !isExcelFile($_FILES['classroom_data'])) {
        $response['message'] = "Only Excel Files Please";
        echo json_encode($response);
        exit;
    }

    $uploadDir = 'files/';
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    $studentFile = $_FILES['student_data'];
    $studentFileName = basename($studentFile['name']);
    $studentFilePath = $uploadDir . $studentFileName;

    $classroomFile = $_FILES['classroom_data'];
    $classroomFileName = basename($classroomFile['name']);
    $classroomFilePath = $uploadDir . $classroomFileName;

    $uploadSuccess = move_uploaded_file($studentFile['tmp_name'], $studentFilePath) &&
                     move_uploaded_file($classroomFile['tmp_name'], $classroomFilePath);

    if (!$uploadSuccess) {
        $response['message'] = "Failed to upload files.";
        echo json_encode($response);
        exit;
    }

    if (!isset($_POST["exam_date"])) {
        $response['message'] = "Select a start date for the exam please";
        echo json_encode($response);
        exit;
    }
    if (!isset($_POST["exam_period"])) {
        $response['message'] = "Exam period not provided.";
        echo json_encode($response);
        exit;
    }

<<<<<<< HEAD
    $start_date = [
        (int)$_POST["exam_date"][2],
        (int)$_POST["exam_date"][0],
        (int)$_POST["exam_date"][1]
    ];
    $numDays = (int) $_POST["exam_period"];
    // $py_path = "C:\Users\gyaba\AppData\Local\Programs\Python\Python312\python.exe";

    $command = escapeshellcmd("python algo.py " .
        escapeshellarg($studentFilePath) . " " .
        escapeshellarg($classroomFilePath) . " " .
        escapeshellarg($numDays) . " " .
        escapeshellarg(implode("-", $start_date))
    ) . " 2>&1";  // <-- capture stderr too

    $output = shell_exec($command);

    if ($output === null || $output === '') {
        $response['message'] = "Python script did not return output.";
=======
    $numDays = (int) $_POST["exam_period"];
    
    // Create a DateTime object from the provided date
    $date = new DateTime();
    $date->setDate(2025, 5, 2); // Set the year, month, and day

    // Format the date to 'Y-m-d' (Year-Month-Day)
    $formatted_date = $date->format('Y-m-d');

    $check = 



    // $command = escapeshellcmd("/var/www/html/cap/venv/algo.py " .
    $command = escapeshellcmd("/var/www/html/cap/venv/bin/python /var/www/html/cap/algo.py " . 
        escapeshellarg($studentFilePath) . " " .
        escapeshellarg($classroomFilePath) . " " .
        escapeshellarg($numDays) . " " .
        escapeshellarg($formatted_date)
    ) . " 2>&1";  // <-- capture stderr too
    // Clean up any carets (^) or unwanted characters from the output
    $command = str_replace('^', '', $command);
    $output = shell_exec($command);
    
    if ($output === null || $output === '') {
        $response['message'] = $output;
>>>>>>> 2617ad3030c6632b9aaff66b1dfc6e29ee15e85f
        echo json_encode($response);
        exit;
    }

    $responseFromPython = json_decode($output, true);
<<<<<<< HEAD

=======
>>>>>>> 2617ad3030c6632b9aaff66b1dfc6e29ee15e85f
    if ($responseFromPython === null) {
        $response['message'] = "Invalid JSON returned by Python script. Output: $output";
        echo json_encode($response);
        exit;
    }

    if ($responseFromPython["success"] === false) {
        echo json_encode($responseFromPython);
        exit;
    } else {
<<<<<<< HEAD
        echo json_encode($responseFromPython['export_path']);
=======
        echo json_encode($responseFromPython);
>>>>>>> 2617ad3030c6632b9aaff66b1dfc6e29ee15e85f
        exit;
    }
} else {
    exit;
}
?>