import {applyAuthTokenInterceptor,
        setAuthTokens,
        clearAuthTokens} from 'axios-jwt';

import axios from 'axios';

const BASE_URL = 'http://localhost:8000'
const REDIRECT_URL_AFTER_LOGIN = '/contacts';
import Router from 'vue-router';


var router = new Router({
   mode: 'history',
});

export const axiosDefault = axios.create({ baseURL: BASE_URL })

// 1. Create an axios instance that you wish to apply the interceptor to
const axiosAuth = axios.create({ baseURL: BASE_URL })

// 2. Define token refresh function.
const requestRefresh = (refresh) => {
    // Notice that this is the global axios instance, not the axiosAuth!  <-- important
    return axios.post(`${BASE_URL}/auth/refresh_token/`, { refresh })
      .then(response => response.data.access)
};

// 3. Apply interceptor
applyAuthTokenInterceptor(axiosAuth, {
  requestRefresh,
  header: "Authorization",
  headerPrefix: "Bearer ",
})

// 4. Logging in
export const login = async (username, password) => {
  const response = await axiosAuth.post('/auth/token/', {username: username, password: password})
  .then(function (response) {
      setAuthTokens({
        accessToken: response.data.access,
        refreshToken: response.data.refresh
      });
      router.push(REDIRECT_URL_AFTER_LOGIN);
      router.go();
    })
    .catch(function (error) {
      // console.log(error) // FIXME: Only for debugging
    })
}

// 5. Logging out
export const logout = () => {
  clearAuthTokens();
  router.push('/');
  router.go();
}

// Now just make all requests using your axiosAuth instance
// axiosAuth.get('/api/endpoint/that/requires/login').then(response => { })
export default axiosAuth
