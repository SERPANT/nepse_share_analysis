import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import SideBar from '../common/sidebar/sidebar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function YearlySubPlotAll(props) {
  const { shareYearlyData, loading } = props;
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
          {loading && (
            <div>
              <h3>Loading...</h3>
            </div>
          )}
          {!loading && (
            <ChartMapperLine shareData={shareYearlyData} dateOnly={true} />
          )}
        </div>
      </div>
    </div>
  );
}

export default YearlySubPlotAll;
