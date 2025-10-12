let academicChartInstance = null;

function renderAcademicChart(data) {
  const ctx = document.getElementById('academicChart');
  if (!ctx) {
    console.warn("Không tìm thấy thẻ canvas với ID 'academicChart'");
    return;
  }

  // Nếu đã có biểu đồ → hủy trước khi vẽ lại
  if (academicChartInstance !== null) {
    academicChartInstance.destroy();
  }

  academicChartInstance = new Chart(ctx, {
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
  }
});

console.log("JS đã chạy");
console.log("Canvas:", document.getElementById('academicChart'));
console.log("Chart:", typeof Chart);
console.log("Dữ liệu:", academicData);
