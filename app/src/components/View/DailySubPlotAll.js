import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

import SideBar from '../common/sidebar/sidebar';

import TIME_INTERVAL_TYPE from '../../constants/timeIntervalType';

function DailySubPlot(props) {
  const { shareDailyData, loading, shareCategories, selectedCategory } = props;
  const { onChangeCategory } = props;

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
          <ChartMapperLine
            shareBasicData={selectedCategory?.share}
            shareData={shareDailyData}
            timeOnly = {true}
            timeIntervalType={TIME_INTERVAL_TYPE.DAILY}
            fetchSharePriceData={props.fetchSharePriceData}
          />
        </div>
      </div>
    </div>
  );
}

export default DailySubPlot;
