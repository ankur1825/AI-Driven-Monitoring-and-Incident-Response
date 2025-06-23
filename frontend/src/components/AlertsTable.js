import React, { useEffect, useState } from 'react';
import api from '../services/api';

console.log('React API base:', process.env.REACT_APP_API_URL);

const AlertsTable = () => {
  const [alerts, setAlerts] = useState([]);

  const sendAlert = () => {
    const newAlert = {
      timestamp: new Date().toISOString(),
      summary: 'Simulated CPU spike on node-3',
      status: 'firing',
      details: 'CPU usage exceeded 90% for more than 5 mins on node-3'
    };

    api.post('/api/alerts/webhook', newAlert)
      .then(() => fetchAlerts())
      .catch(err => {
        console.error('Failed to send alert:', err.message);
        console.error(err);
      });
  };

  const fetchAlerts = () => {
    api.get('/api/alerts/')
      .then(res => setAlerts(res.data))
      .catch(err => {
        console.error('Failed to fetch alerts:', err.message);
        console.error(err);
      });
  };

  useEffect(() => {
    fetchAlerts();
  }, []);

  return (
    <div>
      <button onClick={sendAlert}>Send Test Alert</button>
      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Summary</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((alert, index) => (
            <tr key={index}>
              <td>{alert.timestamp}</td>
              <td>{alert.summary}</td>
              <td>{alert.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AlertsTable;
