import React, { useEffect, useState } from 'react';

export default function CategoryTree({ onSelect }) {
  const [cats, setCats] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/categories')
      .then(r => r.json())
      .then(setCats);
  }, []);

  return (
    <ul>
      {cats.map(c => (
        <li key={c.id} onClick={() => onSelect(c.id)}>
          {c.name}
        </li>
      ))}
    </ul>
  );
}