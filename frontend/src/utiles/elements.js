/**
 * Crea un elemento <p> (párrafo).
 * @param {string} content - El contenido del párrafo.
 * @param {Object} [attrs] - Atributos adicionales para el párrafo (opcional).
 * @returns {HTMLElement} El nodo de párrafo.
 */
export function p(content = '', attrs = {}) {
    const el = document.createElement('p');
    el.textContent = content;
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}

/**
 * Crea un elemento <a> (enlace).
 * @param {string} href - El enlace de destino.
 * @param {string} content - El texto del enlace.
 * @param {Object} [attrs] - Atributos adicionales para el enlace (opcional).
 * @returns {HTMLElement} El nodo de enlace.
 */
export function a(href, content = '', attrs = {}) {
    const el = document.createElement('a');
    el.href = href;
    el.textContent = content;
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}

/**
 * Crea un elemento <h1> (encabezado 1).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h1(content = '', attrs = {}) {
    const el = document.createElement('h1');
    el.textContent = content;
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}

/**
 * Crea un elemento <h2> (encabezado 2).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h2(content = '', attrs = {}) {
    const el = document.createElement('h2');
    el.textContent = content;
    Object.assign(el, attrs);
    return el;
}

/**
 * Crea un elemento <h3> (encabezado 3).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h3(content = '', attrs = {}) {
    const el = document.createElement('h3');
    el.textContent = content;
    Object.assign(el, attrs);
    return el;
}

/**
 * Crea un elemento <h4> (encabezado 4).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h4(content = '', attrs = {}) {
    const el = document.createElement('h4');
    el.textContent = content;
    Object.assign(el, attrs);
    return el;
}

/**
 * Crea un elemento <h5> (encabezado 5).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h5(content = '', attrs = {}) {
    const el = document.createElement('h5');
    el.textContent = content;
    Object.assign(el, attrs);
    return el;
}

/**
 * Crea un elemento <h6> (encabezado 6).
 * @param {string} content - El contenido del encabezado.
 * @param {Object} [attrs] - Atributos adicionales para el encabezado (opcional).
 * @returns {HTMLElement} El nodo de encabezado.
 */
export function h6(content = '', attrs = {}) {
    const el = document.createElement('h6');
    el.textContent = content;
    Object.assign(el, attrs);
    return el;
}

/**
 * Crea un elemento <div>.
 * @param {Object} [attrs] - Atributos adicionales para el div (opcional).
 * @returns {HTMLElement} El nodo <div>.
 */
export function div(attrs = {}) {
    const el = document.createElement('div');
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}

/**
 * Crea un elemento <img>.
 * @param {string} src - El enlace a la imagen.
 * @param {Object} [attrs] - Atributos adicionales para la imagen (opcional).
 * @returns {HTMLElement} El nodo <img>.
 */
export function img(src, attrs = {}) {
    const el = document.createElement('img');
    el.src = src;
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}

/**
 * Crea un elemento <button>.
 * @param {string} content - El texto del botón.
 * @param {Object} [attrs] - Atributos adicionales para el botón (opcional).
 * @returns {HTMLElement} El nodo <button>.
 */
export function button(content = '', attrs = {}) {
    const el = document.createElement('button');
    el.textContent = content;
    Object.assign(el, attrs);  // Asigna los atributos si se pasan
    return el;
}
