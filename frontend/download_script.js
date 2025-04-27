document.addEventListener('DOMContentLoaded', function() {
  const downloadButton = document.getElementById('downloadBtn');

  downloadButton.addEventListener('click', function() {
    const link = document.createElement('a');
    link.href = '../final/final.xlsx'; // The file you want to download
    link.download = 'schedule.xlsx'; // The name you want to save it as
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });
});
