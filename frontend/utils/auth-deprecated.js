/*
 * This file is based on:
 * https://auth0.com/blog/vuejs2-authentication-tutorial/
 * Rewritten by Stein Roald Bolle, December 2017, for Django REST and JWT.
*/

// Own system of login

import decode from 'jwt-decode';
import axios from 'axios'
import Router from 'vue-router';


const ACCESS_TOKEN_KEY = 'access_token';
const REDIRECT_URL_AFTER_LOGIN = '/contacts';



const BACKEND_URL = 'http://localhost:8000'  // REPLACE with your own Backend-URL

var router = new Router({
   mode: 'history',
});


export function login(username, password) {
  const url = `${BACKEND_URL}/api/token/`
  axios.post(url, { username: username, password: password })
  .then(function (response) {
    // console.log('response: ', response)
    console.log('response.data.access: ', response.data.access)
    localStorage.setItem(ACCESS_TOKEN_KEY, response.data.access);
    router.push(REDIRECT_URL_AFTER_LOGIN);
    router.go();
  })
  .catch(function (error) {
    console.log(error) // FIXME: Only for debugging
  })
}

export function logout() {
  clearAccessToken();
  router.push('/');
  router.go();

}

export function getAccessToken() {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

function clearAccessToken() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
}

export function isLoggedIn() {
  const accessToken = getAccessToken();
  return !!accessToken && !isTokenExpired(accessToken);
}

function getTokenExpirationDate(encodedToken) {
  const token = decode(encodedToken);
  if (!token.exp) { return null; }

  const date = new Date(0);
  date.setUTCSeconds(token.exp);
  return date;
}

function isTokenExpired(token) {
  const expirationDate = getTokenExpirationDate(token);
  return expirationDate < new Date();
}
