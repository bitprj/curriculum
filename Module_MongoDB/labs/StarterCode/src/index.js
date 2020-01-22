
const express = require('express')
const eventRouter = require('./routers/event')
const appRouter = require('./routers/app')
const app = express()
const port = process.env.PORT || 3000

// auto parses json
app.use(express.json())

// register router with express
app.use(eventRouter)
app.use(appRouter)


app.listen(port, () => {
    console.log('Server is up on port', port);
})