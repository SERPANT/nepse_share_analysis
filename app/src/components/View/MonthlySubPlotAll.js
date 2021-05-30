import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import SideBar from '../common/sidebar/sidebar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function MonthlySubPlotAll(props) {
  const { shareMonthlyData, loading } = props;
  const { onChangeCategory } = props;

  return (
    <div>
      <Header />
      <NavBar />
      <div className="row">
        <div className="col-sm-2">
          <SideBar onNavItemClick={onChangeCategory} />
        </div>
        <div className="col-sm-10">
          <ChartMapperLine shareData={shareMonthlyData} dateOnly={true} />
        </div>
      </div>
    </div>
  );
}

export default MonthlySubPlotAll;
