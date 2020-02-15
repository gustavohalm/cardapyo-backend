const mongoose = require('mongoose');

const OrderSchema = mongoose.Schema({
    restaurant: String,
    table: String,
    status: String,
},{
    timestamps: true
}
);

module.exports = mongoose.model('Order', OrderSchema);