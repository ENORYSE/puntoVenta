import Button from "../componentes/button";
import { div } from "../utiles/elements";
import { render } from "../utiles/html";

function Home() {
    return render(div(),
        `
        <h1>Inicio</h1>
        <p>Bienvenido a la página principal.</p>
        `,
        Button(),
        '<a href="about" data-link>Ir a About</a>'
    );
}

export default Home;