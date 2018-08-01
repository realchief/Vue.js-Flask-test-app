import axios from 'axios'

export function fetchVariations () {
    // write code to do ajax call with axios to get variations from /api/variations
  var apiURL = 'http://localhost:8000/api'
  return axios.get(apiURL + '/variations').then(response => {
    return response
  })
  .catch (e => {
    this.errors.push(e)
  })
}
