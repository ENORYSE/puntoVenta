import { api } from "./api-urls";
import { get } from './requests';

/**
 * Realiza una solicitud para obtener productos desde la API.
 * 
 * @returns {Object} Los estados de la solicitud (isFetching, isError, isSuccess, data, error).
 */
export async function getProductos() {
    return await get({
        url: api.traerProductos,
        mensajeError: 'Error al obtener productos',
    });
}
