/**
 * Maneja los clics en los enlaces de la aplicación. Cambia la URL sin recargar la página
 * y renderiza la nueva ruta.
 * 
 * @param {Event} event - El evento del click sobre el enlace.
 * @param {HTMLElement} root - El contenedor raíz donde se renderizarán las páginas.
 * @param {Array} routes - Las rutas definidas para la aplicación.
 */
function LinkListener(event, root, routes) {
    const target = event.target.closest('a');
    if (target && target.matches('[data-link]')) {
        event.preventDefault();
        const path = target.getAttribute('href');
        history.pushState({}, '', path);
        RouteController(null, root, routes);
    }
}

/**
 * Controla la lógica de las rutas activas, cargando el contenido correspondiente
 * y actualizando el contenedor raíz.
 * 
 * @param {Event|null} event - El evento del popstate o null para la carga inicial.
 * @param {HTMLElement} root - El contenedor raíz donde se renderizarán las páginas.
 * @param {Array} routes - Las rutas definidas para la aplicación.
 */
async function RouteController(event, root, routes) {
    const path = window.location.pathname;
    const match = searchRoute(path, routes);

    if (!match) {
        root.innerHTML = '<h1>404 - Página no encontrada</h1>';
        console.error("No se encontró la ruta: ", path);
    }

    try {
        const mod = await importModule(match.route.module);
        root.innerHTML = '';
        root.appendChild(mod.default());
    } catch (error) {
        console.error("No se pudo importar la página: ", error);
    }
}

/**
 * Busca una ruta que coincida con la URL actual.
 * 
 * @param {string} path - La ruta actual de la URL.
 * @param {Array} routes - Las rutas definidas para la aplicación.
 * @returns {Object|null} - El objeto de la ruta que coincide o null si no se encuentra.
 */
function searchRoute(path, routes) {
    for (const route of routes) {
        if (path === route.path) return { route };

        if (route.children) {
            const match = searchRoute(path, route.children);
            if (match) return match;
        }
    }
    return null;
}

/**
 * Carga perezosamente un módulo de acuerdo con la ruta especificada.
 * 
 * @param {string} path - La ruta del módulo a cargar.
 * @returns {Promise} - Promesa que resuelve el módulo importado.
 */
function importModule(path) {
    const module = import.meta.glob('../pages/**/*.js')[`../pages/${path}`];
    if (module) {
        return module();
    }
    return Promise.reject(new Error('Módulo no encontrado'));
}

/**
 * Inicializa los eventos del router y la carga inicial de la ruta.
 * 
 * @param {HTMLElement} root - El contenedor raíz donde se renderizarán las páginas.
 * @param {Array} routes - Las rutas definidas para la aplicación.
 */
function RouterProvider(root, routes) {
    window.addEventListener('popstate', (event) => RouteController(event, root, routes));
    document.body.addEventListener('click', (event) => LinkListener(event, root, routes));
    RouteController(null, root, routes);
}

export default RouterProvider;