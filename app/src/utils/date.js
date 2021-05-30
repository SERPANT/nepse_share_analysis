export const getOnlyDate = (dateString) => {
  const dateObj = new Date(dateString);

  return (
    dateObj.getYear() + '-' + (dateObj.getMonth() + 1) + '-' + dateObj.getDate()
  );
};

export const getTimeOnly = (dateString) => {
  const dateObj = new Date(dateString);

  return `${dateObj.getHours()}:${dateObj.getMinutes()}:${dateObj.getSeconds()}`;
};

const dateUtil = {
  getOnlyDate,
  getTimeOnly,
};

export default dateUtil;
