/**
 * Realiza una solicitud GET a una URL genérica y maneja los estados de la solicitud.
 * 
 * Esta función maneja los estados de la solicitud, como si está cargando (`isFetching`), si ocurrió un error (`isError`),
 * si fue exitosa (`isSuccess`), y devuelve los datos o el error.
 * 
 * @param {string} url - La URL de la API a la que hacer la solicitud.
 * @param {string} [mensajeError] - Un mensaje personalizado que describe el error (opcional).
 * @returns {Object} Un objeto con los estados de la solicitud:
 * - isFetching: Indica si la solicitud está en curso.
 * - isError: Indica si hubo un error en la solicitud.
 * - isSuccess: Indica si la solicitud fue exitosa.
 * - data: Los datos devueltos por la API en caso de éxito.
 * - error: El error que ocurrió en caso de fallo.
 */
export async function get({url, mensajeError}) {
    let state = {
        isFetching: true,
        isError: false,
        isSuccess: false,
        data: null,
        error: null,
    };

    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`${mensajeError || 'Error al obtener los datos'}: ${response.statusText}`);
        }

        const data = await response.json();

        state = {
            isFetching: false,
            isError: false,
            isSuccess: true,
            data,
            error: null,
        };
    } catch (error) {
        state = {
            isFetching: false,
            isError: true,
            isSuccess: false,
            data: null,
            error: error.message,
        };
    }

    return state;
}
