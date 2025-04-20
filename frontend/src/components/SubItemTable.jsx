import React, { useEffect, useState } from 'react';

export default function SubItemTable({ itemId }) {
  const [subs, setSubs] = useState([]);

  useEffect(() => {
    if(itemId){
    fetch(`http://127.0.0.1:8000/items/${itemId}/subitems`)
      .then(r => r.json())
      .then(setSubs);
    }
  }, [itemId]);

  return (
    <table>
      <thead>
        <tr><th>Nombre</th><th>Cantidad</th></tr>
      </thead>
      <tbody>
        {subs.map(s => (
          <tr key={s.id}>
            <td>{s.name}</td>
            <td>{s.quantity}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}