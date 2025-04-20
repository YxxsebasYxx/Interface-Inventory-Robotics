import React, { useEffect, useState } from 'react';

export default function ItemTable({ subcategoryId, onSelect }) {
  const [items, setItems] = useState([]);

  useEffect(() => {
    if (subcategoryId) {
      fetch(`http://127.0.0.1:8000/subcategories/${subcategoryId}/items`)
        .then(r => r.json())
        .then(setItems);
    }
  }, [subcategoryId]);

  return (
    <table>
      <thead>
        <tr><th>Nombre</th><th>Cantidad</th></tr>
      </thead>
      <tbody>
        {items.map(i => (
          <tr key={i.id} onClick={() => onSelect(i.id)}>
            <td>{i.name}</td>
            <td>{i.quantity}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}