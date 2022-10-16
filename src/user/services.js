require('express-session');
const a = require('../app');
const model = require('./model');

const register = (req, res) => {
  console.log(`registering in, body={userName:${req.body.userName}, userPassword:${req.body.userPassword}}`);
  const { userName, userPassword } = req.body;
  if (userName && userPassword) {
    model.count({ where: { userName } }).then(
      (count) => {
        if (count !== 0) {
          res.send({ register: false });
        } else {
          model.create({ userName, userPassword })
            .then(() => res.send({ register: true }))
            .catch((err) => {
              res.send({ register: false });
              console.log(err);
            });
        }
      },
    ).catch((e) => console.log(e));
  } else {
    res.send({ register: false });
  }
};

const login = (req, res) => {
  console.log(`logging in, body=${req.body}`);
  const { userName, userPassword } = req.body;

  if (!userPassword || !userName) {
    req.session.loggedin = false;
    res.send({ loggedin: req.session.loggedin });
    return;
  }
  model.findOne({ where: { userName, userPassword } })
    .then((user) => {
      console.log(user);
      if (!user) {
        req.session.loggedin = false;
        res.send({ loggedin: req.session.loggedin });
      }
      req.session.loggedin = true;
      req.session.userId = user.id;
      res.send({ loggedin: req.session.loggedin });
    })
    .catch((e) => console.log(e));
};

const checkSessions = (req, res, next) => {
  if (req.session.loggedin) {
    next();
  } else {
    res.send({ loggedin: false });
  }
};

const loginTest = (req, res) => {
  res.send({ loggedin: true });
};

const logout = (req, res) => {
  console.log(`logging out, body=${req.body}`);

  req.session.destroy();
  res.send({ loggedin: false });
};

const getUsers = (req, res) => {
  model.findAll()
    .then((users) => {
      const us = users.map((u) => u.toJSON());
      const onlineUsers = a.users();
      for (const user of us) {
        try {
          user.online = !!onlineUsers[user.id];
        } catch (e) {
          console.log(e);
        }
      }
      res.send(us);
    })
    .catch((e) => console.log(e));
};

const getUser = (req, res) => {
  model.findByPk(req.params.id).then((users) => res.json(users)).catch((e) => console.log(e));
};

const deleteUser = (req, res) => {
  model.destroy({ where: { id: req.params.id } })
    .then((r) => res.json(r)
      .catch((e) => console.log(e)));
};

module.exports = {
  register, login, checkSessions, loginTest, logout, getUsers, getUser, deleteUser,
};
