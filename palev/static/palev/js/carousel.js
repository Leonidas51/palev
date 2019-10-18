(function() {
  window.addEventListener('load', function() {
    let items = document.getElementsByClassName('carousel__container'),
        index = 0,
        timer = null;

    document.querySelector('.carousel__image_initial').classList.add('animate');

    setInterval(function() {
      let image = items[index].querySelector('.carousel__image');

      items[index].classList.remove('carousel__container_current');

      timer = setTimeout(stopAnimation(index), 500);

      if (items[index + 2]) {
        items[index + 2].classList.add('carousel__container_next');
      } else {
        items[0].classList.add('carousel__container_next');
      }

      if (items[index + 1]) {
        items[index + 1].classList.remove('carousel__container_next');
        items[index + 1].classList.add('carousel__container_current');
        items[index + 1].querySelector('.carousel__image').classList.add('animate');
      } else {
        items[0].classList.remove('carousel__container_next');
        items[0].classList.add('carousel__container_current');
        items[0].querySelector('.carousel__image').classList.add('animate');
        items[1].classList.add('carousel__container_next');

        index = -1;
      }

      index++;
    }, 15000)
  })

  function stopAnimation(index) {
    return function() {
      document.getElementsByClassName('carousel__container')[index].querySelector('.carousel__image').classList.remove('animate');
    }
  }

})();