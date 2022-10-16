const express = require('express');

const router = express.Router();

const service = require('./services');

router.get('/:id', [service.checkSessions, service.getMessages]);
router.post('/', [service.checkSessions, service.sendMessages]);

module.exports = router;
