import NavTab from './NavTab';

import ROUTES from '../../../constants/routes';

function NavBar() {
  return (
    <nav className="navbar nav-pills nav-fill">
      <NavTab label="Daily Main Graph" to={ROUTES.HOME} isActive={false} />

      <NavTab
        label="Daily Sub plots"
        to={ROUTES.DAILY_SUB_PLOT_ALL}
        isActive={false}
      />

      <NavTab
        label="Weekly Main Graph"
        to={ROUTES.WEEKLY_MAIN_GRAPH}
        isActive={false}
      />
      <NavTab
        label="Weekly Sub plots"
        to={ROUTES.WEEKLY_SUB_PLOT_ALL}
        isActive={false}
      />

      <NavTab
        label="Monthly Main Graph"
        to={ROUTES.MONTHLY_MAIN_GRAPH}
        isActive={false}
      />

      <NavTab
        label="Monthly Sub plots"
        to={ROUTES.MONTHLY_SUB_PLOT_ALL}
        isActive={false}
      />

      <NavTab
        label="Quaterly Sub plots"
        to={ROUTES.QUATERLY_SUB_PLOT_ALL}
        isActive={false}
      />

      <NavTab
        label="Quaterly Main graph"
        to={ROUTES.QUATERLY_MAIN_GRAPH}
        isActive={false}
      />

      <NavTab
        label="Yearly Sub plots"
        to={ROUTES.YEARLY_SUB_PLOT_ALL}
        isActive={false}
      />

      <NavTab
        label="Yearly Main graph"
        to={ROUTES.YEARLY_MAIN_GRAPH}
        isActive={false}
      />
    </nav>
  );
}

export default NavBar;
