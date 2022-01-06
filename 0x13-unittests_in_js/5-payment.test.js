const chai = require("chai");
const should = chai.should();
const sinon = require("sinon");

const sendPaymentRequestToApi = require("./5-payment.js");

describe("#sendPaymentRequestToApi()", function () {
  let jamesBond;
  beforeEach(function() {
    jamesBond = sinon.spy(console, "log");
  });

  afterEach(function() {
    jamesBond.calledOnce.should.equal(true);
    jamesBond.restore();
  });

  it("validate sendPaymentRequestToApi return with 100 and 20", function() {
    sendPaymentRequestToApi(100, 20);
    jamesBond.calledWith("The total is: 120").should.equal(true);
  });
  it("validate sendPaymentRequestToApi return with 10 and 10", function() {
    sendPaymentRequestToApi(10, 10);
    jamesBond.calledWith("The total is: 20").should.equal(true);
  });
});
