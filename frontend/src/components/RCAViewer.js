import React, { useEffect, useState } from 'react';
import api from '../services/api';

const RCAViewer = ({ alert }) => {
  const [rca, setRca] = useState('');

  useEffect(() => {
    if (alert) {
      api.post('/rca/generate', { logs: alert.logs, traces: '', metrics: '' })
        .then(res => setRca(res.data.rca));
    }
  }, [alert]);

  return (
    <div>
      <h3>Root Cause Analysis</h3>
      <pre>{rca}</pre>
    </div>
  );
};

export default RCAViewer;