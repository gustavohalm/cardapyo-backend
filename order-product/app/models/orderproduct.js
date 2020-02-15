const mongoose = require('mongoose');

const OrderProductSchema = mongoose.Schema({
    order: String,
    product: String
}, {
    timestamps: true
});

module.exports = mongoose.model('OrderProduct', OrderProductSchema);

