import { BrowserRouter, Switch, Route } from 'react-router-dom';

import DailyMainGraph from './components/View/DailyMainGraph';
import WeeklyMainGraph from './components/View/WeeklyMainGraph';
import DailySubPlotAll from './components/View/DailySubPlotAll';
import WeeklySubPlotAll from './components/View/WeeklySubPlotAll';
import MonthlySubPlotAll from './components/View/MonthlySubPlotAll';
import MonthlyMainGraph from './components/View/MonthlyMainGraph';
import YearlyMainGraph from './components/View/YearlyMainGraph';
import YearlySubPlotAll from './components/View/YearlySubPlotAll';
import EPSComparision from './components/View/EPSComparision';
import PEComparision from './components/View/PEComparision';
import TechnicalInfo from './components/View/TechnicalInfo';

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
              selectedCategory={props.selectedCategory}
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
              selectedCategory={props.selectedCategory}
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
              selectedCategory={props.selectedCategory}
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
              selectedCategory={props.selectedCategory}
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
              selectedCategory={props.selectedCategory}
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
          path={ROUTES.EPS_COMPARISIONS}
          render={() => (
            <EPSComparision
              shareCategories={props.shareCategories}
              onChangeCategory={props.onChangeCategory}
            />
          )}
        />
        <Route
          path={ROUTES.PE_COMPARISION}
          render={() => (
            <PEComparision
              shareCategories={props.shareCategories}
              onChangeCategory={props.onChangeCategory}
            />
          )}
        />
        <Route path={ROUTES.TECHNICAL_INFO} component={TechnicalInfo} />
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
