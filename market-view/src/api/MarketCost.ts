import axios from 'axios'

const request = axios.create({
  baseURL: 'http://localhost:5000', 
  timeout: 5000,
})

export function getAllRes(){
    return request.get('/api/items')
}

export function getItemCost(params: Record<string, any>){
    return request.get('/api/item_cost',{params})
}