import {
  ProSidebar,
  SidebarHeader,
  Menu,
  MenuItem,
  SubMenu,
} from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

import NAV_BAR_CATEGORIES from '../../../constants/navbarCategory';

const SideBar = (props) => {
  return (
    <ProSidebar>
      <SidebarHeader>
        <div className="dashboard-header">
          <h5>Dashboard</h5>
        </div>
      </SidebarHeader>
      <Menu iconShape="square">
        {NAV_BAR_CATEGORIES.map(({ label, category }) => (
          <MenuItem
            key={category}
            onClick={() => {
              props.onNavItemClick(category);
            }}
            value={category}
            id={category}
          >
            {label}
          </MenuItem>
        ))}
        <SubMenu title="Components">
          <MenuItem>Component 1</MenuItem>
          <MenuItem>Component 2</MenuItem>
        </SubMenu>
      </Menu>
    </ProSidebar>
  );
};

export default SideBar;
