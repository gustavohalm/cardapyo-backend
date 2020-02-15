module.exports = (app) => {
    const OrderProduct = require('../controllers/orderproduct.controller');
    app.get('/order-product/', OrderProduct.create);
}