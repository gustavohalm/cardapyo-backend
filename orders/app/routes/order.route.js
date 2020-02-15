module.exports = (app) => {
    const Order = require('../controllers/order.controller');

    app.get('/orders/', Order.findAll);
    app.get('/orders./', Order.find);
}