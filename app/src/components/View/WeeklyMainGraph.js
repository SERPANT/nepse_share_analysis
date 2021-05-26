import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';

function WeeklyMainGraph(props) {
  const final_data = props.bankShareWeekData.map((bankData) => {
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
      <h1>Yearly Main Grapy</h1>
      <div>
        <LineChart datasets={final_data} height={700} />
      </div>
    </div>
  );
}

export default WeeklyMainGraph;
