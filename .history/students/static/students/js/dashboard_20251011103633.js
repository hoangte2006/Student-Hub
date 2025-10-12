console.log("✅ JS đã load xong");
chart = new Chart(ctx, { /* config như trước */ });
console.log('✅ chart instance created:', !!chart, chart);

// ===== Biểu đồ phân bố học lực toàn hệ (pie) =====
let academicChartInstance = null;

function renderAcademicChart(data) {
  const canvasEl = document.getElementById('academicChart');
  if (!canvasEl) {
    console.warn("Không tìm thấy canvas #academicChart");
    return;
  }
  if (academicChartInstance) academicChartInstance.destroy();

  const ctx = canvasEl.getContext('2d');
  academicChartInstance = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Phân bố học lực',
        data: data.counts.map(Number),
        backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#f44336'],
      }]
    }
  });
}

// ===== Biểu đồ phân bố giới tính (doughnut) =====
let genderChartInstance = null;

function renderGenderChart(data) {
  const canvasEl = document.getElementById('genderChart');
  if (!canvasEl) return;
  if (genderChartInstance) genderChartInstance.destroy();

  const ctx = canvasEl.getContext('2d');
  genderChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        label: 'Phân bố giới tính',
        data: data.counts.map(Number),
        backgroundColor: ['#2196f3', '#e91e63', '#ffeb3b'],
      }]
    }
  });
}

// ===== Biểu đồ học lực theo lớp (bar) =====
document.addEventListener('DOMContentLoaded', function () {
  // Vẽ 2 biểu đồ tổng
  if (typeof academicData !== 'undefined') renderAcademicChart(academicData);
  if (typeof genderData !== 'undefined') renderGenderChart(genderData);

  // Vẽ biểu đồ theo lớp
  if (typeof classAcademicData === 'undefined') {
    console.warn('classAcademicData chưa được truyền từ template');
    return;
  }

  const selector = document.getElementById('classSelector');
  const canvasEl = document.getElementById('classAcademicChart');
  const tableBody = document.querySelector('#classTable tbody');

  if (!selector || !canvasEl || !tableBody) {
    console.warn('Thiếu selector/canvas/table trong DOM');
    return;
  }

  // Tăng chiều cao để dễ quan sát
  canvasEl.style.height = '320px';
  const ctx = canvasEl.getContext('2d');

  const getChartData = (cls) => {
    const key = (cls || '').trim();
    const data = classAcademicData[key] || {};
    const arr = [
      Number(data['G'] || 0),
      Number(data['K'] || 0),
      Number(data['TB'] || 0),
      Number(data['Y'] || 0)
    ];
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

  const keys = Object.keys(classAcademicData);
  let defaultClass = (selector.value || '').trim();
  if (!classAcademicData[defaultClass]) {
    defaultClass = keys[0];
    selector.value = defaultClass;
  }

  const initialData = getChartData(defaultClass);
  const maxVal = Math.max(...initialData, 0);
// ngay trước khi gọi new Chart(...)
  console.log('⏱ before new Chart, ctx:', !!ctx, ctx);

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
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          ticks: { precision: 0 },
          suggestedMax: maxVal > 0 ? maxVal + 3 : 10
        },
        x: { ticks: { autoSkip: false } }
      },
      plugins: {
        title: { display: true, text: 'Phân bố học lực theo lớp' },
        legend: { display: true }
      },
      animation: { duration: 500 }
    }
  });

  updateTable(defaultClass);

  selector.addEventListener('change', function () {
    const selectedClass = (this.value || '').trim();
    const newData = getChartData(selectedClass);
    const newMax = Math.max(...newData, 0);

    console.log('📊 Update chart với:', newData);

    chart.data.datasets[0].data = newData;
    chart.data.datasets[0].label = `Học lực lớp ${selectedClass}`;
    chart.options.scales.y.suggestedMax = newMax > 0 ? newMax + 3 : 10;
    chart.update();

    updateTable(selectedClass);
  });

  // Nếu layout đổi kích thước sau khi render, force update
  setTimeout(() => { chart.resize(); chart.update(); }, 100);
});
