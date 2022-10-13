// noinspection JSCheckFunctionSignatures

const express = require('express');
const cors = require('cors');
const session = require('express-session');

const app = express();

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

app.use('/api/test-get', (req, res) => res.send('testGet working'));
app.use('/api/users', usersRouter);

app.listen(PORT, () => console.log('Server started'));

module.exports = app;
