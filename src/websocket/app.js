function showMessage(message) {
  const tag = document.createElement('p');
  const text = document.createTextNode(`${message}`);
  tag.appendChild(text);
  const messages = document.getElementById('messages');
  messages.appendChild(tag);
  messages.scrollTop = messages.scrollHeight;
}

function handleResponse(response) {
  return response.ok
    ? response.json().then((data) => JSON.stringify(data, null, 2))
    : Promise.reject(new Error(response.error));
}

const login = () => {
  const inputLogin = document.getElementById('input_login');
  const inputPassword = document.getElementById('input_password');
  fetch('/api/users/login', {
    method: 'POST',
    credentials: 'same-origin',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userName: inputLogin.value, userPassword: inputPassword.value }),
  })
    .then((res) => handleResponse(res))
    .then((mes) => showMessage(mes))
    .catch((err) => {
      showMessage(err.message);
    });
};

const testLogin = () => {
  fetch('/api/users/login/test', {
    method: 'GET',
    credentials: 'same-origin',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
  })
    .then((res) => handleResponse(res))
    .then((mes) => showMessage(mes))
    .catch((err) => {
      showMessage(err.message);
    });
};

const logout = () => {
  fetch('/api/users/logout', { method: 'POST', credentials: 'same-origin' })
    .then((res) => handleResponse(res))
    .then((mes) => showMessage(mes))
    .catch((err) => {
      showMessage(err.message);
    });
};

let ws;

const wsBtn = () => {
  if (ws) {
    ws.onerror = null;
    ws.onopen = null;
    ws.onclose = null;
    ws.close();
  }

  ws = new WebSocket('ws://localhost:8080');
  ws.onerror = () => {
    showMessage('WebSocket error');
  };
  ws.onopen = () => {
    showMessage('WebSocket connection established');
  };
  ws.onclose = () => {
    showMessage('WebSocket connection closed');
    ws = null;
  };
  ws.onmessage = (message) => {
    showMessage(message.data);
  };
};

const wsSendBtn = () => {
  if (!ws) {
    showMessage('No WebSocket connection');
    return;
  }

  ws.send('"Hello world!');
  showMessage('Sent "Hello World!"');
};

const send = () => {
  const user = document.getElementById('user');

  fetch('/api/messages/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ messageToUserId: user.value, messageText: 'test' }),
  })
    .then((res) => handleResponse(res))
    .catch((err) => {
      showMessage(err.message);
    });
};
