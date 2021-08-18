import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';
import SideBar from '../common/sidebar/sidebar';

import dateUtil from '../../utils/date';
import { MAIN_GRAPH_HEIGHT } from '../../constants/graph';

import TIME_INTERVAL_TYPE from '../../constants/timeIntervalType';

// import LineChart fromc
class DailyMainGraph extends React.Component {
  componentDidMount = () => {
    this.fetchDailyData();
  };

  componentDidUpdate = () => {
    this.fetchDailyData();
  };

  fetchDailyData = () => {
    const { shareDailyData } = this.props;

    if (shareDailyData.length > 0) return;

    this.props.fetchSharePriceData(TIME_INTERVAL_TYPE.DAILY);
  };

  render() {
    const { shareDailyData, loading, shareCategories } = this.props;

    const { onChangeCategory } = this.props;

    const final_data = shareDailyData.map((bankData) => {
      const { share, timeList } = bankData;
      
      const time_line_data = timeList.map(({ date_time, price }) => {
        return {
          x: dateUtil.getTimeOnly(date_time),
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

export default DailyMainGraph;
