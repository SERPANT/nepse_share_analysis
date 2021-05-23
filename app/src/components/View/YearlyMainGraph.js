import React from 'react';

import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import LineChart from '../common/charts/LineChart';

function YearlyMainGraph(props) {
  const final_data = props.bankShareYearlyData.map((bankData) => {
    const { symbol, time_list } = bankData;

    const time_line_data = time_list.map(({ time, value }) => {
      return {
        x: new Date(time),
        y: value,
      };
    });

    return {
      name: symbol,
      data: time_line_data,
    };
  });

  return (
    <div>
      <Header />
      <NavBar />
      <h1>Yearly Main Grapy</h1>
      <div>
        <LineChart data={final_data} height={700} />
      </div>
    </div>
  );
}

export default YearlyMainGraph;
