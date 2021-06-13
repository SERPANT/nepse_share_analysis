import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';
import SideBar from '../common/sidebar/sidebar';

import dateUtil from '../../utils/date';
import { MAIN_GRAPH_HEIGHT } from '../../constants/graph';

import TIME_INTERVAL_TYPE from '../../constants/timeIntervalType';

class WeeklyMainGraph extends React.Component {
  componentDidMount = () => {
    this.fetchWeeklyData();
  };

  componentDidUpdate = () => {
    this.fetchWeeklyData();
  };

  fetchWeeklyData = () => {
    const { shareWeekData } = this.props;

    if (shareWeekData.length > 0) return;

    this.props.fetchSharePriceData(TIME_INTERVAL_TYPE.WEEKLY);
  };

  render() {
    const { shareWeekData, loading, shareCategories } = this.props;
    const { onChangeCategory } = this.props;

    const final_data = shareWeekData.map((shareData) => {
      const { share, timeList } = shareData;

      const time_line_data = timeList.map(({ date_time, price }) => {
        return {
          x: dateUtil.getOnlyDate(date_time),
          y: price,
        };
      });

      return {
        label: share,
        data: time_line_data,
      };
    });

    return (
      <div>
        <Header />
        <NavBar />
        <div className="row">
          <div className="col-sm-2">
            <SideBar
              onNavItemClick={onChangeCategory}
              shareCategories={shareCategories}
            />
          </div>
          <div className="col-sm-10">
            <LineChart datasets={final_data} height={MAIN_GRAPH_HEIGHT} />
          </div>
        </div>
      </div>
    );
  }
}

export default WeeklyMainGraph;
