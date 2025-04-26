// Modal show/hide logic
const infoIcon = document.getElementById("infoIcon");
const infoModal = document.getElementById("infoModal");
const closeModal = document.getElementById("closeModal");
const uploadForm = document.getElementById("uploadForm");

// Open modal and hide form
infoIcon.addEventListener("click", function() {
  infoModal.style.display = "flex";
  uploadForm.style.display = "none";  // Hide the form when modal is open
});

// Close modal and show form
closeModal.addEventListener("click", function() {
  infoModal.style.display = "none";
  uploadForm.style.display = "block";  // Show the form when modal is closed
});

// Close modal when clicked outside the modal
window.addEventListener("click", function(event) {
  if (event.target === infoModal) {
    infoModal.style.display = "none";
    uploadForm.style.display = "block";  // Show the form when modal is closed
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const enableNumberInputCheckbox = document.getElementById("enableNumberInput");
  const numberInputContainer = document.getElementById("numberInputContainer");

  // Toggle visibility of the number input field when checkbox is clicked
  enableNumberInputCheckbox.addEventListener("change", () => {
    if (enableNumberInputCheckbox.checked) {
      numberInputContainer.style.display = "table-row"; // Show the row
    } else {
      numberInputContainer.style.display = "none"; // Hide the row
    }
  });
  // Initially hide the number input field
  numberInputContainer.style.display = "none";
});


document.addEventListener("DOMContentLoaded", () => {
  const uploadForm = document.getElementById("uploadForm")
  const resultsDiv = document.getElementById("results")
  const fileList = document.getElementById("file-list")

  uploadForm.addEventListener("submit", (e) => {
    e.preventDefault()
    const formData = new FormData()
    formData.append("student_data", document.getElementById("student_data").files[0])
    formData.append("classroom_data", document.getElementById("classroom_data").files[0])
    fetch("../index.php", {
      method: "POST",
      body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
    // Update status message
    if (!data.success) {
      alert(data.message)
    }
    else(){
      window.location.replace("downloads.html");
    }
    })
      })
    })
