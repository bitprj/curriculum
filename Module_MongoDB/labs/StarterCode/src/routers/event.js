
const express = require('express')
const path = require('path')
require('../db/mongoose')
const Event = require('../models/events')
const router = new express.Router()

// TODO REST APIs

// POST
router.post('/events', async (req, res) =>{
    const event = new Event(req.body)
})

// GET specific event using query 
router.get('/event', async (req, res) => { 
})

module.exports = router