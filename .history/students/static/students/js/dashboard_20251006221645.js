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

document.addEventListener('DOMContentLoaded', function () { // Đảm bảo mã chạy sau khi DOM đã tải xong 
  if (typeof academicData !== 'undefined') {  //  Kiểm tra nếu biến academicData đã được định nghĩa
    renderAcademicChart(academicData); // Gọi hàm vẽ biểu đồ với dữ liệu học lực 
  }
});

// Biến toàn cục để lưu trữ instance của biểu đồ giới tính
let genderChartInstance = null;

function renderGenderChart(data) {
  const ctx = document.getElementById('genderChart');
  if (!ctx) return;

  if (genderChartInstance !== null) {
    genderChartInstance.destroy();
  }

  genderChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Phân bố giới tính',
        data: data.counts,
        backgroundColor: ['#2196f3', '#e91e63'],
      }]
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  if (typeof academicData !== 'undefined') {
    renderAcademicChart(academicData);
  }
  if (typeof genderData !== 'undefined') {
    renderGenderChart(genderData);
  }
});



console.log("JS đã chạy");
console.log("Canvas:", document.getElementById('academicChart'));
console.log("Chart:", typeof Chart);
console.log("Dữ liệu:", academicData);
