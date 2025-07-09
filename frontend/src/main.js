import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'
import { useApiGetProductos } from './api/productos.js'

async function buscar() {
  try {
    const response = await useApiGetProductos();
    if (response.ok) {
      const data = await response.json();
      renderProductos(data);
    } else {
      console.error('Error en la respuesta:', response.status);
    }
  } catch (error) {
    console.error('Error al buscar productos:', error);
  }
}

function renderProductos(productos) {
  const app = document.querySelector('#app');

  if (!Array.isArray(productos)) {
    app.innerHTML = '<p>No se encontraron productos.</p>';
    return;
  }

  const listaHTML = productos.map(producto => `
    <li>
      <strong>${producto.name || 'Sin nombre'}</strong> - 
      ${producto.price != null ? `$${producto.price}` : 'Sin precio'}
    </li>
  `).join('');

  app.innerHTML = `
    <h1>Lista de Productos</h1>
    <h1 class="text-2xl font-bold underline w-[100px]">
      Hello world!
    </h1>
    <ul class="flex gap-[20px] bg-[#222]">
      ${listaHTML}
    </ul>
  `;
}

// Ejecutar búsqueda
//buscar();

const root = document.getElementById("app");
//root.innerHTML =

buscar()