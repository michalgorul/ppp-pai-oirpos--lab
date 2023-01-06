import Cookies from 'universal-cookie';
const host = 'http://localhost:8080/api';
const cookies = new Cookies();

/**
 * Zarejestruj użytkownika
 * @param {string} userName
 * @param {string} userPassword
 * @returns Promise
 */
const register = async (userName, userPassword) => {
  const response = await fetch(`${host}/users/register/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userName, userPassword }),
  });
  return response.json(); // Promise
};

/**
 * Zaloguj użytkownika
 * @param {string} userName
 * @param {string} userPassword
 * @returns Promise
 */
const login = async (userName, userPassword) => {
  const response = await fetch(`${host}/users/login`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userName, userPassword }),
  });
  return response.json(); // Promise
};

/**
 * Wyloguj
 * @returns Promise
 */
const logout = async () => {
  const response = await fetch(`${host}/users/logout`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json(); // Promise
};

/**
 * Sprawdź czy użytkownik jest zalogowany
 * @returns Promise
 */
const loginTest = async () => {

  const response = await fetch(`${host}/users/login/test`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      "Cookie": cookies.get("connect.sid")
    },
  });
  return response.json(); // Promise
};

/**
 * Dostań liste użytkowników
 * @returns Promise
 */
const getUsers = async () => {
  const response = await fetch(`${host}/users`);
  return response.json(); // Promise
};

/**
 * Dostań liste wiadomości
 * @param {number} id - id użytkownika
 * @returns Promise
 */
const getMessages = async id => {
  const response = await fetch(`${host}/messages/${id}`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json(); // Promise
};

/**
 * Wyślij wiadomość
 * @param {string} messageText - treść wiadomości
 * @param {number} messageToUserId - id użytkownika do którego zostanie wysłana wiadomość
 * @returns Promise
 */
const sendMessages = async (messageText, messageToUserId) => {
  const response = await fetch(`${host}/messages/`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ messageText, messageToUserId }),
  });
  return response.json(); // Promise
};

const apiClient = {
  register,
  login,
  logout,
  loginTest,
  getUsers,
  getMessages,
  sendMessages,
};

export default apiClient;
