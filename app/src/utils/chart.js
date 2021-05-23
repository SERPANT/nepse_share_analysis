export function sortChartData(chartData) {
  return chartData.sort((a, b) => a.x.getTime() - b.x.getTime());
}
