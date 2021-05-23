import React from 'react';

import ChartistGraph from 'react-chartist';

class LineChart extends React.Component {
  render() {
    const { data, height } = this.props;

    var options = {
      height: height || 200,
    };

    var type = 'Bar';

    const finalData = data.map(({ time, value }) => {
      return {
        x: new Date(time),
        y: value,
      };
    });

    return (
      <div>
        <ChartistGraph
          data={{
            series: [
              {
                name: 'series-1',
                data: finalData,
              },
            ],
          }}
          options={options}
          type={type}
        />
      </div>
    );
  }
}

export default LineChart;
