const mongoose = require('mongoose')

const urlAndDBName = 'mongodb://127.0.0.1:27017/event-api'

mongoose.connect(urlAndDBName, {
    useNewUrlParser: true,
    useCreateIndex: true // quickly access data using indices
})