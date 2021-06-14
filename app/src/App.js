import React from 'react';

import shareServices, * as shareServies from './services/shareService';
import shareCategoryServices from './services/shareCategories';

import Routes from './Routes';

import TIME_INTERVAL_TYPE from './constants/timeIntervalType';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      shareCategories: [],
      shareDailyData: {},
      shareWeekData: {},
      shareMonthlyData: {},
      shareQuaterlyData: {},
      shareYearlyData: {},
      selectedCategoryId: null,
      loading: false,
    };
  }

  componentDidMount = () => {
    this.fetchCategory();
  };

  onChangeCategory = (categoryId) => {
    this.setState({ selectedCategoryId: categoryId });
  };

  fetchSharePriceData = async (timeIntervalType) => {
    const { shareCategories, selectedCategoryId } = this.state;

    const selectedCategory = shareCategories.find(
      ({ id }) => id === selectedCategoryId
    );

    if (!selectedCategory) {
      console.log('Error');
      return;
    }

    if (timeIntervalType === TIME_INTERVAL_TYPE.DAILY) {
      return this.test(
        selectedCategory,
        shareServices.fetchDailyData,
        'shareDailyData'
      );
    }

    if (timeIntervalType === TIME_INTERVAL_TYPE.WEEKLY) {
      return this.test(
        selectedCategory,
        shareServices.fetchWeeklyData,
        'shareWeekData'
      );
    }

    if (timeIntervalType === TIME_INTERVAL_TYPE.MONTHLY) {
      return this.test(
        selectedCategory,
        shareServices.fetchMonthlyData,
        'shareMonthlyData'
      );
    }

    if (timeIntervalType === TIME_INTERVAL_TYPE.QUATERLY) {
      return this.test(
        selectedCategory,
        shareServices.fetchQuaterData,
        'shareQuaterlyData'
      );
    }

    if (timeIntervalType === TIME_INTERVAL_TYPE.YEARLY) {
      return this.test(
        selectedCategory,
        shareServices.fetchYearlyData,
        'shareYearlyData'
      );
    }
  };

  test = async (selectedCategory, func, arrayName) => {
    selectedCategory.share.forEach(({ symbol, name }) => {
      func(symbol, name).then((data) => {
        this.setState({
          [arrayName]: {
            ...this.state[arrayName],
            [selectedCategory.name]: !this.state[arrayName][
              selectedCategory.name
            ]
              ? [data]
              : [...this.state[arrayName][selectedCategory.name], data],
          },
        });
      });
    });
  };

  fetchCategory = async () => {
    this.setState({ loading: true });

    const shareCategories = await shareCategoryServices.fetch();

    this.setState({
      shareCategories,
      loading: false,
      selectedCategoryId: shareCategories[0].id,
    });
  };

  /**
   * Render function
   */
  render() {
    const {
      shareCategories,
      shareDailyData,
      shareWeekData,
      selectedCategoryId,
      shareMonthlyData,
      shareQuaterlyData,
      shareYearlyData,
      loading,
    } = this.state;

    const selectedCategory = shareCategories.find(
      ({ id }) => id === selectedCategoryId
    );

    const dailyData = [];

    const quaterlyData =
      (selectedCategory && shareQuaterlyData[selectedCategory.name]) || [];

    const weeklyData =
      (selectedCategory && shareWeekData[selectedCategory.name]) || [];

    const monthlyData =
      (selectedCategory && shareMonthlyData[selectedCategory.name]) || [];

    const yearlyData =
      (selectedCategory && shareYearlyData[selectedCategory.name]) || [];

    console.log('===================== ', selectedCategory);
    return (
      <div className="container-fluid">
        <Routes
          selectedCategory={selectedCategory}
          shareCategories={shareCategories}
          shareDailyData={dailyData}
          shareWeekData={weeklyData}
          shareMonthlyData={monthlyData}
          shareQuaterlyData={quaterlyData}
          shareYearlyData={yearlyData}
          loading={loading}
          fetchSharePriceData={this.fetchSharePriceData}
          onChangeCategory={this.onChangeCategory}
        />
      </div>
    );
  }
}

export default App;
