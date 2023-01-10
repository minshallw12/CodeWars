function countConsonants(str) {
    let consanants = 'bcdfghjklmnpqrstvwxyz';
    let chars = str.toLowerCase().split('');
    let consanantsArr = [];
    let counter = 0;
    for (let i=0; i<chars.length; i++) {
      if (consanants.includes(chars[i]) && !consanantsArr.includes(chars[i])) {
          consanantsArr.push(chars[i]);
          counter++;
          }
    }
    return counter;
  };