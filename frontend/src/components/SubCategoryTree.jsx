import React, { useEffect, useState } from 'react';

export default function SubCategoryTree({ categoryId, onSelect }) {
  const [subcats, setSubcats] = useState([]);

  useEffect(() => {
    if(categoryId) { 
    fetch(`http://127.0.0.1:8000/categories/${categoryId}/subcategories`)
      .then(r => r.json())
      .then(setSubcats);
    }
  }, [categoryId]);

  return (
    <ul>
      {subcats.map(sc => (
        <li key={sc.id} onClick={() => onSelect(sc.id)}>
          {sc.name}
        </li>
      ))}
    </ul>
  );
}