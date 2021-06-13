import React from 'react';

import LineChart from './LineChart';
import ShareDetails from './ShareDetails';

import dateUtil from '../../../utils/date';
import { SUB_PLOT_HEIGHT } from '../../../constants/graph';

class ChartMapperLine extends React.Component {
  componentDidMount = () => {
    this.fetchShareData();
  };

  componentDidUpdate = () => {
    this.fetchShareData();
  };

  fetchShareData = () => {
    const { shareData } = this.props;

    if (shareData.length > 0) return;

    this.props.fetchSharePriceData(this.props.timeIntervalType);
  };

  render() {
    return (
      <div>
        {this.props.shareData.map(({ timeList, share, shareName }) => {
          let smallestValue = { y: Number.MAX_VALUE };
          let largestValue = { y: Number.MIN_VALUE };
          let valueAtTheStart = {};
          let valueAtTheEnd = {};

          const sorted_value = timeList.map(({ date_time, price }) => {
            return {
              x: this.props.dateOnly
                ? dateUtil.getOnlyDate(date_time)
                : date_time,
              y: price,
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
                <h3>{`${shareName} (${share})`}</h3>
              </div>
              <div className="card-body">
                <LineChart
                  key={share}
                  height={SUB_PLOT_HEIGHT}
                  datasets={[{ label: share, data: sorted_value }]}
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
}

export default ChartMapperLine;
