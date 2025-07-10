/**
 * Agrega contenido a un contenedor, ya sea un nodo del DOM o una cadena de HTML.
 * Si es una cadena de HTML, lo convierte en nodos y los agrega.
 * Si es un nodo, lo agrega directamente.
 * 
 * @param {HTMLElement} container - El contenedor donde se añadirá el contenido.
 * @param {string|HTMLElement} content - El contenido a agregar, puede ser una cadena de HTML o un nodo del DOM.
 */
export function addHtml(container, content) {
    if (!(container instanceof HTMLElement)) {
        throw new Error('El primer parámetro debe ser un elemento del DOM (HTMLElement)');
    }

    if (typeof content === 'string') {
        const parser = new DOMParser();
        const doc = parser.parseFromString(content, 'text/html');
        Array.from(doc.body.childNodes).forEach(child => {
            container.appendChild(child);
        });
    }
    else if (content instanceof Node) {
        container.appendChild(content);
    } else {
        throw new Error('El segundo parámetro debe ser un string o un nodo del DOM (HTMLElement)');
    }
}

/**
 * Agrega múltiples elementos (strings o nodos del DOM) a un contenedor.
 * Puedes pasar varios elementos como parámetros y se agregarán uno por uno.
 * 
 * @param {HTMLElement} container - El contenedor donde se añadirá el contenido.
 * @param {...(string|HTMLElement)} elements - Los elementos a agregar, pueden ser strings de HTML o nodos del DOM.
 */
export function render(container, ...elements) {
    // Verificar que el contenedor sea un nodo válido
    if (!(container instanceof HTMLElement)) {
        throw new Error('El primer parámetro debe ser un elemento del DOM (HTMLElement)');
    }

    elements.forEach(element => {
        if (typeof element === 'string') {
            addHtml(container, element);
        }
        else if (element instanceof Node) {
            container.appendChild(element);
        } else {
            throw new Error('Cada elemento debe ser un string o un nodo del DOM (HTMLElement)');
        }
    });

    return container;
}
