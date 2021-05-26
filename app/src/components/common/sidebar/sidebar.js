import {
  ProSidebar,
  SidebarHeader,
  Menu,
  MenuItem,
  SubMenu,
} from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

const SideBar = () => {
  return (
    <ProSidebar>
      <SidebarHeader>
        <div className="dashboard-header">
          <h5>Dashboard</h5>
        </div>
      </SidebarHeader>
      <Menu iconShape="square">
        <MenuItem>Commercial Banks</MenuItem>
        <MenuItem>Development Banks</MenuItem>
        <MenuItem>Finance Companies</MenuItem>
        <MenuItem>Micro Fiinance Companies</MenuItem>
        <MenuItem>Life Insurance Companies</MenuItem>
        <MenuItem>Non-Life Insurance Companies</MenuItem>
        <MenuItem>Hydropower Companies</MenuItem>
        <MenuItem>Manufacturing and Processing Companies</MenuItem>
        <MenuItem>Trading Companies</MenuItem>
        <MenuItem> Hotel Lists </MenuItem>
        <SubMenu title="Components">
          <MenuItem>Component 1</MenuItem>
          <MenuItem>Component 2</MenuItem>
        </SubMenu>
      </Menu>
    </ProSidebar>
  );
};

export default SideBar;
