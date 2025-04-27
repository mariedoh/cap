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

function toggleChecks(){
  const checkbox = document.getElementById("enableNumberInput");
  const element = document.getElementById("numberInputContainer");

  if (checkbox.checked) {
    element.style.display = "block";
  } else {
    element.style.display = "none";
  }
}


document.addEventListener("DOMContentLoaded", () => {
  const uploadForm = document.getElementById("uploadForm")

  uploadForm.addEventListener("submit", (e) => {
    e.preventDefault()
    const formData = new FormData();
    formData.append("student_data", document.getElementById("student_data").files[0]);
    formData.append("classroom_data", document.getElementById("classroom_data").files[0]);

    const dateInput = document.getElementById("datee").value;
    if (dateInput) {
        const [year, month, day] = dateInput.split("-");
        const yearInt = parseInt(year);
        const monthInt = parseInt(month);
        const dayInt = parseInt(day);
        
        // Check if all values are valid numbers
        if (!isNaN(yearInt) && !isNaN(monthInt) && !isNaN(dayInt)) {
            formData.append("exam_date", [yearInt, monthInt, dayInt]);
        } else {
            alert("Invalid date input");
        }
    }

    // Get the number input if it's not null or empty
    const numberInput = document.getElementById("numberInput").value;
    if (numberInput) {
        const numberInt = parseInt(numberInput);
        if (!isNaN(numberInt)) {
            formData.append("exam_period", numberInt);
        } else {
            alert("Invalid exam period input");
        }
    }
    else{
      formData.append("exam_period", 8);
    }

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
    else{
      window.location.assign("download.html");
    }
    })
      })
    })