const Order = require('../models/order');

exports.create = (req, res) => {
    const order = new Order(req.body);
    order.save().then( data =>{
        res.send(data);
    }).catch( err => {
        return res.status(500).send({
            error_message: err.message || 'A unexpected erro happen. Sorry'
        });
    });
}

exports.findAll = (req, res) => {
    if(req.query.restaurant){
        Order.find({restaurant: req.query.restaurant}).then( orders => {
            res.send(orders);
        }).catch( err => {
            return res.status(500).send({
                error_message: err.message || 'A unexpected error happen. Sorry!'
            });
        });
    }

    if(req.query.table) {
        Order.find({table: req.query.table}).then( orders => {
            res.send(orders);
        } ).catch( err => {
            return res.status(500).send({
                error_message: err.message || 'A unexpected erro happen. Sorry!!'
            });
        });
    }

    Order.find().then(orders => {
        res.send(orders);
    }).catch( err => {
        return res.status(500).send( {
            error_message: err.message || 'Error, a unexpected erro happen. Sorry!'
        })
    });
}

exports.findOne = (req, res) => {

}

exports.update = (req, res) => {

}

exports.delete = (req, res) => {

}