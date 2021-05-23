import React from 'react';

import ChartistGraph from 'react-chartist';

class LineChart extends React.Component {
  render() {
    const { data, height } = this.props;

    const options = {
      height: height || 200,
      axisX: {
        showLabel: true,
      },
    };

    return (
      <div>
        <ChartistGraph
          data={{ series: data }}
          options={options}
          type={'Line'}
        />
      </div>
    );
  }
}

export default LineChart;
