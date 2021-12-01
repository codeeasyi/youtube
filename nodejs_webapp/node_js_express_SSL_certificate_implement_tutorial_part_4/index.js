const express = require('express')
const app = express()
const port = 3000
const ip = "localhost"

const https = require('https')
const fs = require('fs')

const jwt = require("jsonwebtoken")
var bodyParser = require('body-parser'); 
var cookieParser = require('cookie-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'))
app.use(cookieParser())

app.post('/', urlencodedParser, (req, res) => {
    if(req.body.username==="admin" && req.body.password==="admin") {
        let token = jwt.sign({ "a": "b"}, "ganz_geheim111")

        res.cookie('token', token, { maxAge: 9000000, httpOnly: true, secure: true});
        res.redirect('/');
    } else {
        res.redirect('/login')
    } 
})

app.use((req, res, next) => {
    if (typeof req.cookies.token !== "undefined") {
        let token = req.cookies.token
        jwt.verify(token, "ganz_geheim111", (err, user) => {
            if (err)
                res.redirect("/login")

            return next()
        });
    } else {
        res.redirect("/login")
    }
}, express.static("restricted"))

app.use('/logout', (req, res) => {
    res.cookie('token', "", { maxAge: 0, httpOnly: true})
    res.redirect("/login")
})

https.createServer({
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem'),
    passphrase: "123456"
}, app)
.listen(port, ip, () => {
    console.log("listening at http://"+ip+":"+port)
})