import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function YearlySubPlotAll(props) {
  return (
    <div>
      <Header />
      <NavBar />
      <ChartMapperLine shareData={props.bankShareYearlyData} />
    </div>
  );
}

export default YearlySubPlotAll;
