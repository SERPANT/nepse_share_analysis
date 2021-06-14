import {
  ProSidebar,
  SidebarHeader,
  Menu,
  MenuItem,
  SubMenu,
} from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

import { NavLink } from 'react-router-dom';

import ROUTES from '../../../constants/routes';

const SideBar = (props) => {
  const { shareCategories, onNavItemClick } = props;

  return (
    <ProSidebar>
      <SidebarHeader>
        <div className="dashboard-header">
          <h5>Dashboard</h5>
        </div>
      </SidebarHeader>
      <Menu iconShape="square">
        <SubMenu title="Price Chart">
          {shareCategories.map(({ name, id }) => (
            <MenuItem
              key={id}
              onClick={() => {
                onNavItemClick(id);
              }}
              value={id}
              id={id}
            >
              {name}
            </MenuItem>
          ))}
        </SubMenu>
        <MenuItem>
          <NavLink to={ROUTES.EPS_COMPARISIONS}>EPS Comparision chart</NavLink>
        </MenuItem>
        <MenuItem>PE Ration Comparision chart</MenuItem>
      </Menu>
    </ProSidebar>
  );
};

export default SideBar;
