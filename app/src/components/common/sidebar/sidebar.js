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
  const { shareCategories } = props;

  return (
    <ProSidebar>
      <SidebarHeader>
        <div className="dashboard-header">
          <h5>Dashboard</h5>
        </div>
      </SidebarHeader>
      <Menu iconShape="square">
        {shareCategories.map(({ name, id }) => (
          <MenuItem
            key={id}
            onClick={() => {
              props.onNavItemClick(id);
            }}
            value={id}
            id={id}
          >
            {name}
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
