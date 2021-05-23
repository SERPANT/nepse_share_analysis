import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function DailySubPlot(props) {
  return (
    <div>
      <Header />
      <NavBar />
      <ChartMapperLine shareData={props.bankShareDailyData} />
    </div>
  );
}

export default DailySubPlot;
