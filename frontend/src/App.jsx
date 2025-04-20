import React, { useState } from 'react';
import CategoryTree from './components/CategoryTree';
import SubCategoryTree from './components/SubCategoryTree';
import ItemTable from './components/ItemTable';
import SubItemTable from './components/SubItemTable';

export default function App() {
  const [catId, setCatId] = useState(null);
  const [subcatId, setSubcatId] = useState(null);
  const [itemId, setItemId] = useState(null);

  return (
    <div style={{ display: 'flex', gap: '20px' }}>
      <div>
        <h3>Grupos</h3>
        <CategoryTree onSelect={id => {
          setCatId(id);
          setSubcatId(null);
          setItemId(null);
        }} />
      </div>
      <div>
        <h3>Subgrupos</h3>
        {catId && <SubCategoryTree categoryId={catId} onSelect={id => {
          setSubcatId(id);
          setItemId(null);
        }} />}
      </div>
      <div>
        <h3>Items</h3>
        {subcatId && <ItemTable subcategoryId={subcatId} onSelect={setItemId} />}
      </div>
      <div>
        <h3>SubItems</h3>
        {itemId && <SubItemTable itemId={itemId} />}
      </div>
    </div>
  );
}
