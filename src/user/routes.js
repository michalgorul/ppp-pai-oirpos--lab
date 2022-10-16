const express = require('express');

const router = express.Router();

const service = require('./services');

router.get('/', [service.getUsers]);

router.get('/:id', [service.getUser]);

router.post('/register', [service.register]);

router.post('/login', [service.login]);

router.get('/login/test', [service.checkSessions, service.loginTest]);

router.post('/logout', [service.logout]);

router.delete('/:id', [service.deleteUser]);

module.exports = router;
