// Dòng này để đảm bảo Chart.js đã được tải trước khi sử dụng 
let academicChartInstance = null;

// Hàm để vẽ biểu đồ học lực 
function renderAcademicChart(data) {
  const ctx = document.getElementById('academicChart'); // Lấy thẻ canvas theo ID, academicChart là ID của thẻ canvas trong HTML 
  if (!ctx) { // Kiểm tra nếu thẻ canvas tồn tại 
    console.warn("Không tìm thấy thẻ canvas với ID 'academicChart'"); // Nếu không tồn tại, ghi cảnh báo và dừng hàm 
    return; // Dừng hàm nếu không tìm thấy canvas 
  }

  // Nếu đã có biểu đồ → hủy trước khi vẽ lại
  if (academicChartInstance !== null) {
    academicChartInstance.destroy(); // Hủy biểu đồ cũ để tránh vẽ chồng lên nhau 
  }

  academicChartInstance = new Chart(ctx, { // Tạo biểu đồ mới và lưu vào biến toàn cục 
    type: 'pie',  // Loại biểu đồ là pie (tròn) 
    data: { // Dữ liệu cho biểu đồ 
      labels: data.labels, // Nhãn cho các phần của biểu đồ
      datasets: [{ // Tập dữ liệu cho biểu đồ
        label: 'Phân bố học lực', // Tiêu đề của tập dữ liệu
        data: data.counts,// Dữ liệu số lượng cho mỗi nhãn
        backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#f44336'],
      }]
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  // Kiểm tra và vẽ biểu đồ học lực tổng nếu có
  if (typeof academicData !== 'undefined') {
    renderAcademicChart(academicData);
  }

  // Kiểm tra và vẽ biểu đồ giới tính nếu có
  if (typeof genderData !== 'undefined') {
    renderGenderChart(genderData);
  }

  // Biểu đồ học lực theo lớp
  const selector = document.getElementById('classSelector');
  const ctx = document.getElementById('classAcademicChart');
  const tableBody = document.querySelector('#classTable tbody');

  if (!selector || !ctx || !tableBody || typeof classAcademicData === 'undefined') return;

  const getChartData = (cls) => {
    const data = classAcademicData[cls] || {};
    return [
      data['G'] || 0,
      data['K'] || 0,
      data['TB'] || 0,
      data['Y'] || 0
    ];
  };

  const updateTable = (cls) => {
    const data = classAcademicData[cls] || {};
    tableBody.innerHTML = `
      <tr>
        <td>${cls}</td>
        <td>${data['G'] || 0}</td>
        <td>${data['K'] || 0}</td>
        <td>${data['TB'] || 0}</td>
        <td>${data['Y'] || 0}</td>
      </tr>
    `;
  };

  const chart = new Chart(ctx.getContext('2d'), {
    type: 'bar',
    data: {
      labels: ['Giỏi', 'Khá', 'Trung bình', 'Yếu'],
      datasets: [{
        label: `Học lực lớp ${selector.value}`,
        data: getChartData(selector.value),
        backgroundColor: ['#4CAF50', '#2196F3', '#FFC107', '#F44336']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Phân bố học lực theo lớp'
        }
      }
    }
  });

  updateTable(selector.value);

  selector.addEventListener('change', function () {
    const selectedClass = this.value;
    chart.data.datasets[0].data = getChartData(selectedClass);
    chart.data.datasets[0].label = `Học lực lớp ${selectedClass}`;
    chart.update();
    updateTable(selectedClass);
  });
});

