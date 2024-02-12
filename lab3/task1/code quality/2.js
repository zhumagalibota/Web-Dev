it("Raises x to the power n", function() {
    let x = 5;
  
    let result = x;
    assert.equal(pow(x, 1), result);
  
    result *= x;
    assert.equal(pow(x, 2), result);
  
    result *= x;
    assert.equal(pow(x, 3), result);
  });   // here we have 3 tests layed out as a single function with 3 assets. if an error occures itll be arder to identify the problem. its easier to use it blocks to avoid it