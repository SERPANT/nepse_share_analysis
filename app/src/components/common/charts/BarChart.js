import React from 'react';

import { Bar } from 'react-chartjs-2';

class BarChart extends React.Component {
  render() {
    const { datasets, height, backgroundColor } = this.props;

    const finalDatasets = datasets.map(({ data, label }) => {
      return {
        barPercentage: 0.5,
        barThickness: 40,
        maxBarThickness: 100,
        minBarLength: 2,
        borderColor: 'rgb(34,139,34)',
        data,
        tension: 0.1,
        label,
        fill: false,
        backgroundColor,
      };
    });

    return (
      <div style={{ height: height || 500 }}>
        <Bar
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
                text: 'Chart.js Bar Chart',
              },
            },
          }}
        />
      </div>
    );
  }
}

export default BarChart;
