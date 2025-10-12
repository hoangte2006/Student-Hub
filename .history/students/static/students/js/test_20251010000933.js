console.log("Test JS loaded!");
// Biến toàn cục để lưu trữ instance của biểu đồ học lực
let academicChartInstance = null;

function renderAcademicChart(data) {
  const ctx = document.getElementById('academicChart');
  if (!ctx) return;         
