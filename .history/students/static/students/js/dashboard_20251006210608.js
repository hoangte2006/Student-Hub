function renderAcademicChart(data) {
  const ctx = document.getElementById('academicChart');
  if (!ctx) {
    console.warn("Không tìm thấy thẻ canvas với ID 'academicChart'");
    return;
  }

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Phân bố học lực',
        data: data.counts,
        backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#f44336'],
      }]
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  if (typeof academicData !== 'undefined') {
    renderAcademicChart(academicData);
  } else {
    console.warn("academicData chưa được định nghĩa");
  }
});
