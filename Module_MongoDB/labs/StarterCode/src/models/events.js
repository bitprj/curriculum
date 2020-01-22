// const validator = require('validator')
const mongoose = require('mongoose')

const Event = mongoose.model('Event', {
    eventName: {
        type: String,
    },
    coordinator: {
        type: String,
    },
    date: {
        type: String,
    }
    // Add more
})

module.exports = Event