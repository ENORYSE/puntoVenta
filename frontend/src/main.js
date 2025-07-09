import routes from './router'

function initRouter() {
    window.addEventListener('popstate', handleRoute)
    document.body.addEventListener('click', onLinkClick)
    handleRoute()
}

function onLinkClick(e) {
    const target = e.target.closest('a')
    if (target && target.matches('[data-link]')) {
        e.preventDefault()
        const path = target.getAttribute('href')
        history.pushState({}, '', path)
        handleRoute()
    }
}

async function handleRoute() {
  const path = window.location.pathname
  const root = document.getElementById('app')
  const match = findRoute(path, routes)

  if (match) {
    const mod = await importModule(match.route.module)
    root.innerHTML = ''
    root.appendChild(mod.render(match.params || {}))
  } else {
    root.innerHTML = '<h1>404</h1>'
  }
}

function findRoute(path, routeList, basePath = ''){
  for (const route of routeList){
    const fullPath = basePath+route.path
    if (path === fullPath) return { route }

    if (route.children) {
      const match = findRoute(path, route.children, fullPath)
      if (match) return match;
    }
  }
  return null;
}

function importModule(path){
  return import.meta.glob('./pages/**/*.js')[path]()
}

initRouter()