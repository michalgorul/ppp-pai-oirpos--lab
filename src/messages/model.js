const Sequelize = require('sequelize');
const sequelize = require('../database/db');

const Message = sequelize.define('massages', {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  messageFromUserId: Sequelize.INTEGER,
  messageToUserId: Sequelize.INTEGER,
  messageText: Sequelize.STRING,
});

module.exports = Message;
