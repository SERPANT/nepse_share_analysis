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
            <DailyMainGraph bankShareDailyData={props.bankShareDailyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.DAILY_SUB_PLOT_ALL}
          render={() => (
            <DailySubPlotAll bankShareDailyData={props.bankShareDailyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_SUB_PLOT_ALL}
          render={() => (
            <MonthlySubPlotAll
              bankShareMonthlyData={props.bankShareMonthlyData}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.MONTHLY_MAIN_GRAPH}
          render={() => (
            <MonthlyMainGraph
              bankShareMonthlyData={props.bankShareMonthlyData}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_MAIN_GRAPH}
          render={() => (
            <WeeklyMainGraph bankShareWeekData={props.bankShareWeekData} />
          )}
        />
        <Route
          exact
          path={ROUTES.WEEKLY_SUB_PLOT_ALL}
          render={() => (
            <WeeklySubPlotAll bankShareWeekData={props.bankShareWeekData} />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_SUB_PLOT_ALL}
          render={() => (
            <QuaterlySubPlotAll
              bankShareQuaterlyData={props.bankShareQuaterlyData}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.QUATERLY_MAIN_GRAPH}
          render={() => (
            <QuaterlyMainGraph
              bankShareQuaterlyData={props.bankShareQuaterlyData}
            />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_SUB_PLOT_ALL}
          render={() => (
            <YearlySubPlotAll bankShareYearlyData={props.bankShareYearlyData} />
          )}
        />
        <Route
          exact
          path={ROUTES.YEARLY_MAIN_GRAPH}
          render={() => (
            <YearlyMainGraph bankShareYearlyData={props.bankShareYearlyData} />
          )}
        />
        <Route
          path={ROUTES.HOME}
          render={() => (
            <DailyMainGraph bankShareDailyData={props.bankShareDailyData} />
          )}
        />
      </Switch>
    </BrowserRouter>
  );
};

export default Routes;
