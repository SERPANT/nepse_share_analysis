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
  console.log(props);
  return (
    <BrowserRouter>
      <Switch>
        <Route
          exact
          path={ROUTES.DAILY_MAIN_GRAPH}
          render={() => (
            <DailyMainGraph shareDailyData={props.shareDailyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.DAILY_SUB_PLOT_ALL}
          render={() => (
            <DailySubPlotAll shareDailyData={props.shareDailyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_SUB_PLOT_ALL}
          render={() => (
            <MonthlySubPlotAll shareMonthlyData={props.shareMonthlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_MAIN_GRAPH}
          render={() => (
            <MonthlyMainGraph shareMonthlyData={props.shareMonthlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_MAIN_GRAPH}
          render={() => <WeeklyMainGraph shareWeekData={props.shareWeekData} />}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_SUB_PLOT_ALL}
          render={() => (
            <WeeklySubPlotAll shareWeekData={props.shareWeekData} />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_SUB_PLOT_ALL}
          render={() => (
            <QuaterlySubPlotAll shareQuaterlyData={props.shareQuaterlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_MAIN_GRAPH}
          render={() => (
            <QuaterlyMainGraph shareQuaterlyData={props.shareQuaterlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_SUB_PLOT_ALL}
          render={() => (
            <YearlySubPlotAll shareYearlyData={props.shareYearlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_MAIN_GRAPH}
          render={() => (
            <YearlyMainGraph shareYearlyData={props.shareYearlyData} />
          )}
        />
        <Route
          path={ROUTES.HOME}
          render={() => (
            <DailyMainGraph shareDailyData={props.shareDailyData} />
          )}
        />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;
