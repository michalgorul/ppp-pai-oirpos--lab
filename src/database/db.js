const Sequelize = require('sequelize');

const sequelize = new Sequelize('database ', 'root ', 'root ', {
  dialect: 'sqlite',
  storage: ' orm-db.sqlite',
});

sequelize.sync() // sequelize.sync({ force: true })
  .then(() => {
    console.log('Database & tables created!');
  });

module.exports = sequelize;
