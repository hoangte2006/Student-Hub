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
        backgroundColor: ['#2196f3', '#e91e63', '#ffeb3b'],
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

// Hàm để làm mới biểu đồ học lực
document.addEventListener('DOMContentLoaded', function () {
  if (typeof classAcademicData !== 'undefined') {
    const labels = Object.keys(classAcademicData); // Lấy danh sách lớp từ khóa của đối tượng classAcademicData 
    const dataG = labels.map(cls => classAcademicData[cls].G || 0); // Lấy dữ liệu học lực Giỏi cho từng lớp, nếu không có thì mặc định là 0
    const dataK = labels.map(cls => classAcademicData[cls].K || 0); // Lấy dữ liệu học lực Khá cho từng lớp, nếu không có thì mặc định là 0
    const dataTB = labels.map(cls => classAcademicData[cls].TB || 0); // Lấy dữ liệu học lực Trung bình cho từng lớp, nếu không có thì mặc định là 0
    const dataY = labels.map(cls => classAcademicData[cls].Y || 0); // Lấy dữ liệu học lực Yếu cho từng lớp, nếu không có thì mặc định là 0

    // Vẽ biểu đồ cột học lực theo lớp
const selector = document.getElementById('classSelector');    if (ctx) {
      new Chart(ctx.getContext('2d'), {
        type: 'bar', // Loại biểu đồ là bar (cột)
        data: { 
          labels: labels, // Nhãn là danh sách lớp
          datasets: [
            { label: 'Giỏi', data: dataG, backgroundColor: '#28a745' }, // Dữ liệu học lực Giỏi với màu xanh lá
            { label: 'Khá', data: dataK, backgroundColor: '#007bff' },
            { label: 'Trung bình', data: dataTB, backgroundColor: '#ffc107' },
            { label: 'Yếu', data: dataY, backgroundColor: '#dc3545' },
          ]
        },
        options: { // Cấu hình biểu đồ
          responsive: true,
          plugins: {
            title: { display: true, text: 'Phân bố học lực theo lớp' }
          }
        }
      });
    }
  }
});
