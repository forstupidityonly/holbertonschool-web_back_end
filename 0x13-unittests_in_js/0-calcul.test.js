const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("#calculateNumber()", function () {
  it("should return 4 when calculateNumber is passed 1 and 3", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it("should return 5 when calculateNumber is passed 1 and 3.7", function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it("should return 5 when calculateNumber is passed 1.2 and 3.7", function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("should return 6 when calculateNumber is passed 1.5 and 3.7", function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it("should return 0 when calculateNumber is passed -0.8 and 0.8", function () {
    assert.strictEqual(calculateNumber(-0.8, 0.8), 0);
  });
  it("should return 0 when calculateNumber is passed 0.1 and 0.2", function () {
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
  });
  it("should return -3 when calculateNumber is passed -1.6 and -0.7", function () {
    assert.strictEqual(calculateNumber(-1.6, -0.7), 3);
  });
});
