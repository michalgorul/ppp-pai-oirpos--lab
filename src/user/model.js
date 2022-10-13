const Sequelize = require('sequelize');
const sequelize = require('../database/db');

const User = sequelize.define('user', {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  userName: Sequelize.STRING,
  userPassword: Sequelize.STRING,
});

module.exports = User;
