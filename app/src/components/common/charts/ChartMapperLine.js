import React from 'react';

import LineChart from './LineChart';
import ShareDetails from './ShareDetails';

function ChartMapperLine(props) {
  return (
    <div>
      {props.shareData.map(({ time_list, share_name, symbol }) => {
        let smallestValue = { y: Number.MAX_VALUE };
        let largestValue = { y: Number.MIN_VALUE };
        let valueAtTheStart = {};
        let valueAtTheEnd = {};

        const sorted_value = time_list.map(({ time, value }) => {
          return {
            x: time,
            y: value,
          };
        });

        // const sorted_value = chartUtil.sortChartData(final_time_list);

        if (sorted_value.length > 0) {
          valueAtTheStart = sorted_value[0];
        }

        if (sorted_value.length > 0) {
          valueAtTheEnd = sorted_value[sorted_value.length - 1];
        }

        sorted_value.forEach((timeValue) => {
          if (timeValue.y < smallestValue.y) {
            smallestValue = timeValue;
          }

          if (timeValue.y > largestValue.y) {
            largestValue = timeValue;
          }
        });

        return (
          <div className="card share-daily-card">
            <div className="card-header">
              <h3>{`${share_name} (${symbol})`}</h3>
            </div>
            <div className="card-body">
              <LineChart
                key={symbol}
                height={200}
                datasets={[{ label: symbol, data: sorted_value }]}
              />
              <ShareDetails
                smallestValue={smallestValue}
                largestValue={largestValue}
                valueAtTheStart={valueAtTheStart}
                valueAtTheEnd={valueAtTheEnd}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default ChartMapperLine;
