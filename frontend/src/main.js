import NavLink from "./componentes/NavLink";
import routes from "./router";
import RouterProvider from "./router/routerLazy";
import './style.css';

const root = document.querySelector('#app');

RouterProvider(root, routes);

const nav = document.querySelector('#navlinks');
routes.forEach((route) => {
    const navLink = NavLink(route);
    nav.appendChild(navLink);
})