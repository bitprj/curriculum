const path = require('path')
const express = require('express');
const Event = require('../models/events')
const hbs = require('hbs')
require('../db/mongoose')

const router = express();

const publicDirectoryPath = path.join(__dirname, '../../public')
const viewsPath = path.join(__dirname, '../templates/views')

// TODO

router.get('/events', async (req, res) => { 
})

router.get('/turkey-trot', async (req, res) => {
})

router.get('/coastal-cleanup', async (req, res) => {
})

router.get('*', (req, res) => { 
	router.render('404 error')
})

module.exports = router