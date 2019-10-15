(function() {
  window.addEventListener('load', function() {
    let items = document.getElementsByClassName('index-pic'),
        index = 0,
        timer = null;

    document.querySelector('.index-image-1').classList.add('animate');

    setInterval(function() {
      let image = items[index].querySelector('.index-image');

      items[index].classList.remove('index-pic-current');

      timer = setTimeout(stopAnimation(index), 500);

      if (items[index + 2]) {
        items[index + 2].classList.add('index-pic-next');
      } else {
        items[0].classList.add('index-pic-next');
      }

      if (items[index + 1]) {
        items[index + 1].classList.remove('index-pic-next');
        items[index + 1].classList.add('index-pic-current');
        items[index + 1].querySelector('.index-image').classList.add('animate');
      } else {
        items[0].classList.remove('index-pic-next');
        items[0].classList.add('index-pic-current');
        items[0].querySelector('.index-image').classList.add('animate');
        items[1].classList.add('index-pic-next');

        index = -1;
      }

      index++;
    }, 15000)
  })

  function stopAnimation(index) {
    return function() {
      document.getElementsByClassName('index-pic')[index].querySelector('.index-image').classList.remove('animate');
    }
  }

})();