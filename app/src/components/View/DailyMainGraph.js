import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';
import SideBar from '../common/sidebar/sidebar';

import dateUtil from '../../utils/date';
import { MAIN_GRAPH_HEIGHT } from '../../constants/graph';

// import LineChart from
function DailyMainGraph(props) {
  const { shareDailyData, loading } = props;
  const { onChangeCategory } = props;

  const final_data = shareDailyData.map((bankData) => {
    const { symbol, time_list } = bankData;

    const time_line_data = time_list.map(({ time, value }) => {
      return {
        x: dateUtil.getTimeOnly(time),
        y: value,
      };
    });

    return {
      label: symbol,
      data: time_line_data,
    };
  });

  return (
    <div>
      <Header />
      <NavBar />
      <div className="row">
        <div className="col-sm-2">
          <SideBar onNavItemClick={onChangeCategory} />
        </div>
        <div className="col-sm-10">
          <LineChart datasets={final_data} height={MAIN_GRAPH_HEIGHT} />
        </div>
      </div>
    </div>
  );
}

export default DailyMainGraph;
