import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import SideBar from '../common/sidebar/sidebar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

import TIME_INTERVAL_TYPE from '../../constants/timeIntervalType';

function WeeklySubPlotAll(props) {
  const { shareWeekData, shareCategories, selectedCategory } = props;
  const { onChangeCategory } = props;

  return (
    <div>
      <Header />
      <NavBar />
      <div className="row">
        <div className="col-sm-2">
          <SideBar
            onNavItemClick={onChangeCategory}
            shareCategories={shareCategories}
          />
        </div>
        <div className="col-sm-10">
          <ChartMapperLine
            shareBasicData={selectedCategory?.share}
            shareData={shareWeekData}
            dateOnly={true}
            timeIntervalType={TIME_INTERVAL_TYPE.WEEKLY}
            fetchSharePriceData={props.fetchSharePriceData}
          />
        </div>
      </div>
    </div>
  );
}

export default WeeklySubPlotAll;
