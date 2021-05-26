import React from 'react';

import * as shareServies from './services/shareService';

import Routes from './Routes';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      shareDailyData: [],
      shareWeekData: [],
      shareMonthlyData: [],
      shareQuaterlyData: [],
      shareYearlyData: [],
    };
  }

  componentDidMount = () => {
    this.fetchShareData();
  };

  fetchShareData = async () => {
    const shareDailyDataPromise = shareServies.fetchDailyData('commercialBank');
    const shareWeekDataPromise = shareServies.fetchWeeklyData('commercialBank');
    const shareMonthlyDataPromise = shareServies.fetchMonthlyData(
      'commercialBank'
    );
    const shareQuaterlyDataPromise = shareServies.fetchQuaterData(
      'commercialBank'
    );
    const shareYearlyDataPromise = shareServies.fetchYearlyData(
      'commercialBank'
    );

    const [
      shareDailyData,
      shareWeekData,
      shareMonthlyData,
      shareQuaterlyData,
      shareYearlyData,
    ] = await Promise.all([
      shareDailyDataPromise,
      shareWeekDataPromise,
      shareMonthlyDataPromise,
      shareQuaterlyDataPromise,
      shareYearlyDataPromise,
    ]);

    this.setState({
      shareDailyData,
      shareWeekData,
      shareMonthlyData,
      shareQuaterlyData,
      shareYearlyData,
    });
  };

  /**
   * Render function
   */
  render() {
    const {
      shareDailyData,
      shareWeekData,
      shareMonthlyData,
      shareQuaterlyData,
      shareYearlyData,
    } = this.state;

    return (
      <div className="container-fluid">
        <Routes
          shareDailyData={shareDailyData}
          shareWeekData={shareWeekData}
          shareMonthlyData={shareMonthlyData}
          shareQuaterlyData={shareQuaterlyData}
          shareYearlyData={shareYearlyData}
        />
      </div>
    );
  }
}

export default App;
