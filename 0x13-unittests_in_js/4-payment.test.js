const chai = require("chai");
const should = chai.should();
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment.js");

describe("with Stub: #sendPaymentRequestToApi()", function () {
  it("validates functionality of Utils.calculateNumber()", function () {
    const elStub = sinon.stub(Utils, "calculateNumber").returns(10);
    const jamesBond = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);

    elStub.calledWith("SUM", 100, 20).should.equal(true);
    jamesBond.calledWith('The total is: 10').should.equal(true);
    elStub.alwaysReturned(10).should.equal(true);

    elStub.restore();
    jamesBond.restore();
  });
});
