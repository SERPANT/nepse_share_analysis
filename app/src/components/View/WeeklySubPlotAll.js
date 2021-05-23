import Header from '../common/Header';
import NavBar from '../common/navbar/NavBar';
import ChartMapperLine from '../common/charts/ChartMapperLine';

function WeeklySubPlotAll(props) {
  return (
    <div>
      <Header />
      <NavBar />
      <ChartMapperLine shareData={props.bankShareWeekData} />
    </div>
  );
}

export default WeeklySubPlotAll;
