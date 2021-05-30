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
      category: 'commercialBank',
      loading: false,
    };
  }

  componentDidMount = () => {
    this.fetchShareData();
  };

  onChangeCategory = (category) => {
    this.setState({ category }, this.fetchShareData);
  };

  fetchShareData = async () => {
    this.setState({ loading: true });
    const { category } = this.state;
    const shareDailyDataPromise = shareServies.fetchDailyData(category);
    const shareWeekDataPromise = shareServies.fetchWeeklyData(category);
    const shareMonthlyDataPromise = shareServies.fetchMonthlyData(category);
    const shareQuaterlyDataPromise = shareServies.fetchQuaterData(category);
    const shareYearlyDataPromise = shareServies.fetchYearlyData(category);

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
      loading: false,
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
      loading,
    } = this.state;

    return (
      <div className="container-fluid">
        <Routes
          shareDailyData={shareDailyData}
          shareWeekData={shareWeekData}
          shareMonthlyData={shareMonthlyData}
          shareQuaterlyData={shareQuaterlyData}
          shareYearlyData={shareYearlyData}
          loading={loading}
          onChangeCategory={this.onChangeCategory}
        />
      </div>
    );
  }
}

export default App;
