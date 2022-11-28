/**
 * Zarejestruj użytkownika
 * @param {string} user_name
 * @param {string} user_password
 * @returns Promise
 */
const register = async (user_name, user_password) => {
  const response = await fetch("/api/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_name, user_password }),
  });
  return response.json(); // Promise
};

/**
 * Zaloguj użytkownika
 * @param {string} user_name
 * @param {string} user_password
 * @returns Promise
 */
const login = async (user_name, user_password) => {
  // TODO: Uzupełnić w opraciu o inne funkcje, zwłaszcza register(user_name, user_password).
  const response = await fetch("/api/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_name, user_password }),
  });
  return response.json(); // Promise
};

/**
 * Wyloguj
 * @returns Promise
 */
const logout = async (id) => {
  const response = await fetch("/api/logout/");
  return response.json(); // Promise
};

/**
 * Sprawdź czy użytkownik jest zalogowany
 * @returns Promise
 */
const loginTest = async () => {
  const response = await fetch("/api/login-test/");
  return response.json(); // Promise
};

/**
 * Dostań liste użytkowników
 * @returns Promise
 */
const getUsers = async () => {
  const response = await fetch("/api/users/");
  return response.json(); // Promise
};

/**
 * Dostań liste wiadomości
 * @param {number} id - id użytkownika
 * @returns Promise
 */
const getMessages = async (id) => {
  const response = await fetch(`/api/messages/${id}`);
  return response.json(); // Promise
};

/**
 * Wyślij wiadomość
 * @param {string} message_text - treść wiadomości
 * @param {number} message_to_user_id - id użytkownika do którego zostanie wysłana wiadomość
 * @returns Promise
 */
const sendMessages = async (message_text, message_to_user_id) => {
  const response = await fetch("/api/messages/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
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
