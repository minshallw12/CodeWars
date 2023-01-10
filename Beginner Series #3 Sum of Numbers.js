function getSum( a,b ) {
    let start = null;
    let end = null;
    let counter = null;
    if (a === b) {
      return a;
    }
    if ( a>b){
      start = b;
      end = a;
    } else {
      start = a;
      end = b;
    }
    for (let i=start; i <= end; i++) {
      counter += i;
    }
    return counter; 
  };