import routes from "./router";
import RouterProvider from "./router/routerLazy";
import './style.css';

const root = document.querySelector('#app');

RouterProvider(root, routes);