const host = 'http://localhost:8080/api';

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
  const response = await fetch(`${host}/users/logout`);
  return response.json(); // Promise
};

/**
 * Sprawdź czy użytkownik jest zalogowany
 * @returns Promise
 */
const loginTest = async () => {
  const response = await fetch(`${host}/users/login/test`);
  return response.json(); // Promise
};

/**
 * Dostań liste użytkowników
 * @returns Promise
 */
const getUsers = async () => {
  const response = await fetch(`${host}/api/users/`);
  return response.json(); // Promise
};

/**
 * Dostań liste wiadomości
 * @param {number} id - id użytkownika
 * @returns Promise
 */
const getMessages = async id => {
  const response = await fetch(`${host}/api/messages/${id}`);
  return response.json(); // Promise
};

/**
 * Wyślij wiadomość
 * @param {string} message_text - treść wiadomości
 * @param {number} message_to_user_id - id użytkownika do którego zostanie wysłana wiadomość
 * @returns Promise
 */
const sendMessages = async (message_text, message_to_user_id) => {
  const response = await fetch('/api/messages/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message_text, message_to_user_id }),
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
