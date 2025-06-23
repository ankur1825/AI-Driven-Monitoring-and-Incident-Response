// import React, { useEffect, useState } from 'react';
// import api from '../services/api';
// import ForecastChart from './ForecastChart';

// const Dashboard = () => {
//   const [forecast, setForecast] = useState([]);

//   useEffect(() => {
//     api.get('/predict/cpu').then(res => setForecast(res.data));
//   }, []);

//   return (
//     <div>
//       <h2>CPU Forecast</h2>
//       <ForecastChart data={forecast} />
//     </div>
//   );
// };

// export default Dashboard;

//---------------------------------
// import React from 'react';

// const Dashboard = () => {
//   return (
//     <div>
//       <h2>CPU Forecast</h2>
//     </div>
//   );
// };

// export default Dashboard;
//---------------------------------
import React, { useEffect, useState } from 'react';
import api from '../services/api';
import ForecastChart from './ForecastChart';

const Dashboard = () => {
  const [forecast, setForecast] = useState([]);

  useEffect(() => {
    api.get('/predict/cpu')
      .then(res => setForecast(res.data))
      .catch(err => console.error('API Error:', err));
  }, []);

  console.log('ForecastChart:', ForecastChart);

  return (
    <div>
      <h2>CPU Forecast</h2>
      <pre>{JSON.stringify(forecast, null, 2)}</pre>
      <ForecastChart data={forecast} />
    </div>
  );
};

export default Dashboard;


