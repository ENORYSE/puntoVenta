export function render() {
    const div = document.createElement('div');
    div.innerHTML = `
        <h1>Inicio</h1>
        <p>Bienvenido a la página principal.</p>
        <a href="about" data-link>Ir a About</a>
    `;
    return div;
}