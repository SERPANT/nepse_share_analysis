import React from 'react';

import { Line } from 'react-chartjs-2';

class LineChart extends React.Component {
  render() {
    const { datasets } = this.props;

    const finalDatasets = datasets.map(({ data, label }) => {
      return {
        barPercentage: 0.5,
        barThickness: 6,
        maxBarThickness: 8,
        minBarLength: 2,
        borderColor: 'rgb(75, 192, 192)',
        data,
        tension: 0.1,
        label,
        fill: false,
        backgroundColor: 'rgb(255, 99, 132)',
      };
    });

    return (
      <div className="chart-container">
        <Line
          data={{
            datasets: finalDatasets,
          }}
          options={{
            maintainAspectRatio: false,
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Chart.js Line Chart',
              },
            },
          }}
        />
      </div>
    );
  }
}

export default LineChart;
