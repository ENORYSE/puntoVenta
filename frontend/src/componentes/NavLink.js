import { toHtml } from "../utiles/html";

function NavLink(route) {
    const className = [
        "nav-anchor flex items-center gap-3",
        "text-blue-600 hover:text-white hover:bg-blue-600",
        "rounded-full  pr-10 pl-6 py-2",
        "transition-colors duration-200"
    ].join(" ");

    return toHtml(`
        <li>
            <div class="bg-[red] ml-4 rounded-l-full">
                <a
                    class="${className}"
                    href="${route.path}" 
                    data-link
                >
                    <span class="w-6 h-6 shrink-0 ${route.icon}"></span>
                    <span class="nav-label transition-all duration-200 origin-left"> ${route.name} </span>
                </a>
            </div>
        </li>
    `);
}

export default NavLink;