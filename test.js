function need(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
  }

  var kenodev_was_here = "deputy_"

  var score = 1900

  function MyFunction(){
    kenodev_was_here = 'deputy_' + (score+25) * 44.5 + '_' + need(10)

    console.log(kenodev_was_here)
  }


