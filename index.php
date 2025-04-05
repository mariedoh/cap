<?php
// Set error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] === 'POST'){

    // Check if files were uploaded
    if (!isset($_FILES['student_data']) || !isset($_FILES['classroom_data'])) {
        exit;
    }
    // Function to check if file is an Excel file
    function isExcelFile($file) {
        $allowedExtensions = array('xlsx', 'xls');
        $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
        return in_array($fileExtension, $allowedExtensions);
    }

    // Validate file types
    if (!isExcelFile($_FILES['student_data']) || !isExcelFile($_FILES['classroom_data'])) {
        exit;
    }
    
    // Create files directory if it doesn't exist
    $uploadDir = 'files/';
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    // Process student data file
    $studentFile = $_FILES['student_data'];
    $studentFileName = basename($studentFile['name']);
    $studentFilePath = $uploadDir . $studentFileName;

    // Process classroom data file
    $classroomFile = $_FILES['classroom_data'];
    $classroomFileName = basename($classroomFile['name']);
    $classroomFilePath = $uploadDir . $classroomFileName;

    // Move uploaded files to the files directory
    $uploadSuccess = move_uploaded_file($studentFile['tmp_name'], $studentFilePath) &&
                     move_uploaded_file($classroomFile['tmp_name'], $classroomFilePath);
}
else{
    exit;
}