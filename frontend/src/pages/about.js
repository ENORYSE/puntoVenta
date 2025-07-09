export function render() {
    const div = document.createElement('div');
    div.innerHTML = `
        <h1>Sobre nosotros</h1>
        <p>Esta es la página About.</p>
        <a href="/" data-link>Ir al Home</a>
    `;
    return div;
}