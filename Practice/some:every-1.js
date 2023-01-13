
function oddNum(arr){
    return arr.some(function(val){
    return val % 2 !== 0;
})
}
function zero(num){
    return num.toString().split('').some(function(val){
      return val === '0';
    })
  }
  
  function onlyOdd(arr){
    return arr.every(function(val){
      return val % 2 !== 0;
    })
  }
  
  function noDuplicates(arr){
    return arr.every(function(val){
      return arr.indexOf(val) === arr.lastIndexOf(val);
    });
  }
  
  function hasKey(arr, key){
    return arr.every(function(val){
      return key in val
    })
  }
  
  function hasValue(arr, key, searchValue){
    return arr.every(function(val){
      return val[key] === searchValue;
    })
}