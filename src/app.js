// noinspection JSCheckFunctionSignatures
const WebSocket = require('ws');
const { WebSocketServer } = require('ws');

const express = require('express');
const cors = require('cors');
const session = require('express-session');

const app = express();

const server = require('http').createServer(app);

app.use(express.static(`${__dirname}/websocket/`));

app.use(cors());
app.use(express.json());

const sessionParser = session({
  saveUninitialized: false,
  secret: '$secret',
  resave: false,
});

app.use(sessionParser);

const PORT = process.env.PORT || 8080;

const usersRouter = require('./user/routes');
const messagesRouter = require('./messages/routes');

app.use('/api/test-get', (req, res) => res.send('testGet working'));
app.use('/api/users', usersRouter);
app.use('/api/messages', messagesRouter);

const wss = new WebSocketServer({ noServer: true });

server.on('upgrade', (request, socket, head) => {
  // Sprawdzenie czy dla danego połączenia istnieje sesja
  sessionParser(request, {}, () => {
    if (!request.session.userId) {
      socket.destroy();
      return;
    }
    wss.handleUpgrade(request, socket, head, (ws) => {
      wss.emit('connection', ws, request);
    });
  });
});

const onlineUsers = {};

wss.on('connection', (ws, request) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify({ status: 2 }));
    }
  });
  try {
    onlineUsers[request.session.userId] = ws;
  } catch (err) {
    console.log(err);
  }
  console.log('A new client connected');

  ws.on('message', (message) => {
    console.log(String(message));
    // parsowanie wiadomosci z JSONa na obiekt
    try {
      const data = JSON.parse(message);
    } catch (e) {
      console.log(e);
    }
  });

  ws.on('close', () => {
    delete onlineUsers[request.session.userId];
  });
});

server.listen(PORT, () => console.log('Server started'));

const users = () => onlineUsers;

module.exports = {
  app, server, sessionParser,
};

exports.users = users;
