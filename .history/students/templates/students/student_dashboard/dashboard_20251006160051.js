function renderAcademicChart(data) {
  const ctx = document.getElementById('academicChart').getContext('2d');
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
