import { api } from "./api-urls";

export function useApiGetProductos(){
    return fetch(api.traerProductos);
}