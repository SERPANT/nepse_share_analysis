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

  fetchBankData = async () => {
    const bankShareDailyDataPromise = bankService.fetchBankDayData();
    const bankShareWeekDataPromise = bankService.fetchBankWeeklyData();
    const bankShareMonthlyDataPromise = bankService.fetchBankMontlyData();
    const bankShareQuaterlyDataPromise = bankService.fetchBankQuaterData();
    const bankShareYearlyDataPromise = bankService.fetchBankYearlyData();

    const [
      bankShareDailyData,
      bankShareWeekData,
      bankShareMonthlyData,
      bankShareQuaterlyData,
      bankShareYearlyData,
    ] = await Promise.all([
      bankShareDailyDataPromise,
      bankShareWeekDataPromise,
      bankShareMonthlyDataPromise,
      bankShareQuaterlyDataPromise,
      bankShareYearlyDataPromise,
    ]);

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
