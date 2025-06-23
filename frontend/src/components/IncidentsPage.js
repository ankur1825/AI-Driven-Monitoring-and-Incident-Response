import React, { useEffect, useState } from 'react';
import api from '../services/api';

const IncidentsPage = () => {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    api.get('/api/incidents')
      .then(res => setIncidents(res.data))
      .catch(err => console.error('Incident API Error:', err));
  }, []);

  return (
    <div>
      <h2>Active Incidents</h2>
      <table>
        <thead>
          <tr>
            <th>Key</th>
            <th>Summary</th>
            <th>Status</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map((incident, index) => (
            <tr key={index}>
              <td>{incident.key}</td>
              <td>{incident.summary}</td>
              <td>{incident.status}</td>
              <td><a href={incident.url} target="_blank" rel="noreferrer">View</a></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default IncidentsPage;