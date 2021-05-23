import React from 'react';

import * as bankService from './services/bankService';

import Routes from './Routes';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      bankShareDailyData: [],
      bankShareWeekData: [],
      bankShareMonthlyData: [],
      bankShareQuaterlyData: [],
      bankShareYearlyData: [],
    };
  }

  componentDidMount = () => {
    this.fetchBankData();
  };

  fetchBankData = () => {
    const bankShareDailyData = bankService.fetchBankDayData();
    const bankShareWeekData = bankService.fetchBankWeeklyData();
    const bankShareMonthlyData = bankService.fetchBankMontlyData();
    const bankShareQuaterlyData = bankService.fetchBankQuaterData();
    const bankShareYearlyData = bankService.fetchBankYearlyData();

    this.setState({
      bankShareDailyData,
      bankShareWeekData,
      bankShareMonthlyData,
      bankShareQuaterlyData,
      bankShareYearlyData,
    });
  };

  /**
   * Render function
   */
  render() {
    const {
      bankShareDailyData,
      bankShareWeekData,
      bankShareMonthlyData,
      bankShareQuaterlyData,
      bankShareYearlyData,
    } = this.state;

    return (
      <div className="container-fluid">
        <Routes
          bankShareDailyData={bankShareDailyData}
          bankShareWeekData={bankShareWeekData}
          bankShareMonthlyData={bankShareMonthlyData}
          bankShareQuaterlyData={bankShareQuaterlyData}
          bankShareYearlyData={bankShareYearlyData}
        />
      </div>
    );
  }
}

export default App;
