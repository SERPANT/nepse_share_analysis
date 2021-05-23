import { NavLink } from 'react-router-dom';

const NavTab = (props) => {
  const { label, to, isActive } = props;

  return (
    <NavLink
      to={to}
      className={`nav-item nav-link ${isActive ? 'active' : ''}`}
    >
      {label}
    </NavLink>
  );
};

export default NavTab;
