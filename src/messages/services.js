const { Op } = require('sequelize');
const model = require('./model');
const User = require('../user/model');
const Message = require('./model');
const a = require('../app');

const checkSessions = (req, res, next) => {
  if (req.session.loggedin) {
    next();
  } else {
    res.send({ loggedin: false });
  }
};

const getMessages = (req, res) => {
  const loggedUserId = req.session.userId;
  model.findAll({
    where: {
      [Op.or]: [
        { messageFromUserId: req.params.id, messageToUserId: loggedUserId },
        { messageToUserId: req.params.id, messageFromUserId: loggedUserId },
      ],
    },
  })
    .then((messages) => {
      res.send(messages.map((m) => m.toJSON()));
    })
    .catch((e) => console.log(e));
};

const sendMessages = (request, response) => {
  const onlineUsers = a.users();

  const { messageText, messageToUserId } = request.body;
  console.log(`Received message => ${messageText} from ${request.session.userId} to ${messageToUserId}`);

  User.findAll({ where: { id: messageToUserId } }).then(
    (users) => {
      if (users.length >= 1) {
        const [addressee] = users;
        const mes = {
          messageFromUserId: request.session.userId,
          messageToUserId,
          messageText,
        };
        Message.create(mes)
          .then((message) => {
            console.log(`id: messageToUserId -> ${addressee.id}`);
            console.log(`online users -> ${onlineUsers}`);
            if (addressee.id in onlineUsers) {
              // Wysyłanie wiadomości do odiorcy
              onlineUsers[messageToUserId].send(messageText);
            }
            if (message.messageFromUserId !== message.messageToUserId) {
              if (message.messageFromUserId in onlineUsers) {
                // Wysyłanie wiadomości do nadawcy jeżeli odbiorca nie jest nadawca
                onlineUsers[request.session.userId].send(messageText);
              }
            }

            response.send({ sending: true });
          })
          .catch((err) => {
            console.log(err); response.send({ error: err });
          });
      } else {
        response.send({ error: 'User not exists' });
      }
    },
  )
    .catch((err) => {
      console.log(err); response.send({ error: err });
    });
};

module.exports = { checkSessions, getMessages, sendMessages };
