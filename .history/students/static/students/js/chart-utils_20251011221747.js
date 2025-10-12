// chart-utils.js

export function getChartDataFromClass(classAcademicData, cls) {
  const key = (cls || '').trim();
  const data = classAcademicData[key] || {};
  return [
    Number(data['G'] || 0),
    Number(data['K'] || 0),
    Number(data['TB'] || 0),
    Number(data['Y'] || 0)
  ];
}

export function updateChartInstance(chart, newData, label, maxVal) {
  chart.data.datasets[0].data = newData;
  chart.data.datasets[0].label = label;
  chart.options.scales.y.suggestedMax = maxVal > 0 ? maxVal + 3 : 10;
  chart.update();
}
