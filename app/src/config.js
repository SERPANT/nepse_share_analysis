const BASE_URL = process.env.REACT_APP_BASE_URL;

const END_POINTS = {
  shareinfo: `${BASE_URL}/shareprice/`,
  shareCategory: `${BASE_URL}/sharecategory/`,
};

const config = {
  BASE_URL,
  END_POINTS,
};

export default config;
