const express = require('express');

const router = express.Router();

const model = require('./model');

router.get('/', (req, res) => {
  model.findAll().then((users) => res.json(users));
});

router.get('/:id', (req, res) => {
  model.findByPk(req.params.id).then((users) => res.json(users));
});

router.post('/register', (req, res) => {
  console.log(`registering in, body=${req.body}`);
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
    );
  } else {
    res.send({ register: false });
  }
});

router.post('/login', (req, res) => {
  console.log(`logging in, body=${req.body}`);
  const { userName, userPassword } = req.body;

  if (!userPassword || !userName) {
    req.session.loggedin = false;
    res.send({ loggedin: req.session.loggedin });
    return;
  }
  const user = model.findOne({ where: { userName, userPassword } });
  if (!user) return;

  req.session.loggedin = true;
  res.send({ loggedin: req.session.loggedin });
});

router.delete('/:id', (req, res) => {
  model.destroy({ where: { id: req.params.id } }).then((r) => res.json(r));
});

module.exports = router;
