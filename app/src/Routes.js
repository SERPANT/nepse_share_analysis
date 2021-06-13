import { BrowserRouter, Switch, Route } from 'react-router-dom';

import DailyMainGraph from './components/View/DailyMainGraph';
import WeeklyMainGraph from './components/View/WeeklyMainGraph';
import DailySubPlotAll from './components/View/DailySubPlotAll';
import WeeklySubPlotAll from './components/View/WeeklySubPlotAll';
import MonthlySubPlotAll from './components/View/MonthlySubPlotAll';
import MonthlyMainGraph from './components/View/MonthlyMainGraph';
import YearlyMainGraph from './components/View/YearlyMainGraph';
import YearlySubPlotAll from './components/View/YearlySubPlotAll';

import QuaterlyMainGraph from './components/View/QuaterlyMainGraphAll';
import QuaterlySubPlotAll from './components/View/QuaterlySubPlotAll';

import ROUTES from './constants/routes';

const Routes = (props) => {
  return (
    <BrowserRouter>
      <Switch>
        <Route
          exact
          path={ROUTES.DAILY_MAIN_GRAPH}
          render={() => (
            <DailyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareDailyData={props.shareDailyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.DAILY_SUB_PLOT_ALL}
          render={() => (
            <DailySubPlotAll
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareDailyData={props.shareDailyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_SUB_PLOT_ALL}
          render={() => (
            <MonthlySubPlotAll
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareMonthlyData={props.shareMonthlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_MAIN_GRAPH}
          render={() => (
            <MonthlyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareMonthlyData={props.shareMonthlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_MAIN_GRAPH}
          render={() => (
            <WeeklyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareWeekData={props.shareWeekData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_SUB_PLOT_ALL}
          render={() => (
            <WeeklySubPlotAll
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareWeekData={props.shareWeekData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_SUB_PLOT_ALL}
          render={() => (
            <QuaterlySubPlotAll
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareQuaterlyData={props.shareQuaterlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_MAIN_GRAPH}
          render={() => (
            <QuaterlyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareQuaterlyData={props.shareQuaterlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_SUB_PLOT_ALL}
          render={() => (
            <YearlySubPlotAll
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareYearlyData={props.shareYearlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_MAIN_GRAPH}
          render={() => (
            <YearlyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareYearlyData={props.shareYearlyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
        <Route
          path={ROUTES.HOME}
          render={() => (
            <DailyMainGraph
              fetchSharePriceData={props.fetchSharePriceData}
              shareCategories={props.shareCategories}
              shareDailyData={props.shareDailyData}
              onChangeCategory={props.onChangeCategory}
              loading={props.loading}
            />
          )}
        />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;
