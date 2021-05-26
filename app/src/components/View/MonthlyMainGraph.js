import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';

function MonthlyMainGraph(props) {
  const final_data = props.bankShareMonthlyData.map((bankData) => {
    const { symbol, time_list } = bankData;

    const time_line_data = time_list.map(({ time, value }) => {
      return {
        x: time,
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
      <h1>Weekly Main Grapy</h1>
      <div>
        <LineChart datasets={final_data} />
      </div>
    </div>
  );
}

export default MonthlyMainGraph;
