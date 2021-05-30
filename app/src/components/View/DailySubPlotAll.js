import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

import SideBar from '../common/sidebar/sidebar';

function DailySubPlot(props) {
  const { shareDailyData, loading } = props;
  const { onChangeCategory } = props;

  return (
    <div>
      <Header />
      <NavBar />
      <div className="row">
        <div className="col-sm-2">
          <SideBar onNavItemClick={onChangeCategory} />
        </div>
        <div className="col-sm-10">
          <ChartMapperLine shareData={shareDailyData} />
        </div>
      </div>
    </div>
  );
}

export default DailySubPlot;
