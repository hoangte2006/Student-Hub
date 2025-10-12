
console.log("✅ JS đã load xong");
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
  if (typeof classAcademicData !== 'undefined') {
    const selector = document.getElementById('classSelector');
    const canvasEl = document.getElementById('classAcademicChart');

    // Đảm bảo canvas hiện hữu và có kích thước hiển thị
    if (!canvasEl) {
      console.warn('Không tìm thấy canvas #classAcademicChart');
      return;
    }
    // Tăng chiều cao để dễ quan sát
    canvasEl.style.height = '320px';

    const ctx = canvasEl.getContext('2d');
    const tableBody = document.querySelector('#classTable tbody');

    const getChartData = (cls) => {
      const key = (cls || '').trim();
      const data = classAcademicData[key] || {};
      const arr = [
        Number(data['G'] || 0),
        Number(data['K'] || 0),
        Number(data['TB'] || 0),
        Number(data['Y'] || 0)
      ];
      // Debug
      console.log('📊 Lớp chọn:', key);
      console.log('📊 Dữ liệu lấy được:', classAcademicData[key]);
      console.log('📊 Mảng data:', arr);
      return arr;
    };

    const updateTable = (cls) => {
      const key = (cls || '').trim();
      const data = classAcademicData[key] || {};
      tableBody.innerHTML = `
        <tr>
          <td>${key}</td>
          <td>${Number(data['G'] || 0)}</td>
          <td>${Number(data['K'] || 0)}</td>
          <td>${Number(data['TB'] || 0)}</td>
          <td>${Number(data['Y'] || 0)}</td>
        </tr>
      `;
    };

    // Lớp mặc định: lớp đầu tiên có trong dữ liệu hoặc giá trị từ selector (nếu hợp lệ)
    const keys = Object.keys(classAcademicData);
    let defaultClass = (selector && selector.value ? selector.value.trim() : '') || keys[0];

    // Nếu selector chưa có giá trị hợp lệ, set về lớp đầu tiên
    if (!classAcademicData[defaultClass]) {
      defaultClass = keys[0];
      if (selector) selector.value = defaultClass;
    }

    const initialData = getChartData(defaultClass);
    const maxVal = Math.max(...initialData, 0);

    let chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Giỏi', 'Khá', 'Trung bình', 'Yếu'],
        datasets: [{
          label: `Học lực lớp ${defaultClass}`,
          data: initialData,
          backgroundColor: ['#4CAF50', '#2196F3', '#FFC107', '#F44336']
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false, // Cho phép cao rộng linh hoạt
        scales: {
          y: {
            beginAtZero: true,
            ticks: { precision: 0 },
            suggestedMax: maxVal > 0 ? maxVal + 3 : 10 // Kéo trục Y đủ cao để thấy cột
          },
          x: {
            ticks: { autoSkip: false }
          }
        },
        plugins: {
          title: { display: true, text: 'Phân bố học lực theo lớp' },
          legend: { display: true }
        },
        animation: {
          duration: 500
        }
      }
    });

    // Lần đầu render bảng
    updateTable(defaultClass);

    // Khi đổi lớp
    if (selector) {
      selector.addEventListener('change', function () {
        const selectedClass = (this.value || '').trim();
        const newData = getChartData(selectedClass);
        const newMax = Math.max(...newData, 0);

        chart.data.datasets[0].data = newData;
        chart.data.datasets[0].label = `Học lực lớp ${selectedClass}`;
        chart.options.scales.y.suggestedMax = newMax > 0 ? newMax + 3 : 10;
        chart.update();

        updateTable(selectedClass);
      });
    }

    // Nếu container ban đầu ẩn, sau khi hiện cần resize
    const ensureVisibleUpdate = () => {
      chart.resize();
      chart.update();
    };
    setTimeout(ensureVisibleUpdate, 100); // nhẹ để đảm bảo layout ổn rồi mới update
  }
});
