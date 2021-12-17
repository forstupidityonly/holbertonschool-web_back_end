#!/usr/bin/node
import Currency from "./3-currency.js";

export default class Pricing {
  constructor(amount, Currency) {
    this._amount = amount;
    this._Currency = Currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  get currency() {
    return this._Currency;
  }

  set currency(newCurrency) {
    this._Currency = newCurrency;
  }

  displayFullPrice() {
    return `${this._amount} ${this.Currency._name} (${this._Currency._code})`
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
