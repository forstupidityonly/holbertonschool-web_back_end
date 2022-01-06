const Utils = require('./utils');
const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const rez = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${rez}`);
}

module.exports = sendPaymentRequestToApi;
