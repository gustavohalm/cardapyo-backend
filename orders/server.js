const express = require("express");
const bodyParser = require("body-parser");
const cors = require('cors');

const app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.use(bodyParser.json());

app.use(cors());

const dbConfig = require("./config/database.config.js");
const mongoose = require("mongoose");

mongoose.Promise = global.Promise;

// Connecting to the database
mongoose.connect(dbConfig.url, {
    useNewUrlParser: true
}).then(() => {
    console.log("Successfully connected to the database");    
}).catch(err => {
    console.log("Could not connect to the database. Exiting now...", err);
    process.exit();
});

app.get("/", (req, res) => {
        res.json({"message": "Hello World Restfull from Node.JS!"});
} );
require("./app/routes/order.route.js")(app);

app.listen(3030, () => {
    console.log("Server is listening on port 3000");
});