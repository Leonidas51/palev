(function() {
  let carpets = 1;

  window.addEventListener('load', function() {
    addEvents(document.querySelector('#carpet-1'));
    console.log(1);
    document.querySelector('#add-more').addEventListener('click', addCarpet);
  });

  function calcPrice(e) {
    var el = e.target.closest('.carpet');

    var width = el.querySelector('.cm-w').value,
        length = el.querySelector('.cm-h').value,
        type_mul = el.querySelector('input[value="York"]').checked == true ? 687 : 795,
        amount = el.querySelector('.amount').value;

    el.querySelector('.carpet-total').innerHTML = Math.round(Number((width * length) / 10000 * type_mul * amount));
    calcTotal();
  }

  function calcTotal() {
    var prices = document.querySelectorAll('.carpet-total'),
        sum = 0;

    for(var i=0; i < prices.length; i++) {
      sum += Number(prices[i].innerHTML);
    }

    document.querySelector('#total').innerHTML = sum;
  }

  function addCarpet(e) {
    e.preventDefault();
    carpets++;

    e.target.insertAdjacentHTML('beforebegin', 
    '<div class="carpet" id="carpet-' + carpets + '">' +
    '<div>' +
    '<span>Выбор типа покрытия</span>' +
    '<label>' +
    '<input class="carp-type" name="' + carpets +'-type" type="radio" checked="checked" value="York">' +
    '<span>York</span>' +
    '</label>' +
    '<label>' +
    '<input class="carp-type" name="' + carpets +'-type" type="radio" value="NovaNop">' +
    '<span>Nova Nop</span>' +
    '</label>' +
    '</div>' +
    '<div class="carp-size">' +
    '<p>Размер ковра</p>' +
    '<input class="cm-w" name="' + carpets +'-size-w" type="text" placeholder="см" required><span> X </span><input class="cm-h" name="' + carpets + '-size-h" type="text" placeholder="см" required>' +
    '</div>' +
    '<div class="carp-amount">' +
    '<p>Количество</p>' +
    '<input class="amount" name="' + carpets + '-amount" type="number" min="1" value="1">' +
    '</div>' +
    '<p>Итого в месяц: <span class="carpet-total" id="' + carpets + '-total">0</span>р</p>' +
    '</div>'
    )

    addEvents(document.querySelector('#carpet-' + carpets));
  }

  function addEvents(el) {
    var widths = el.querySelectorAll('.cm-w'),
    heights = el.querySelectorAll('.cm-h'),
    types = el.querySelectorAll('.carp-type'),
    amounts = el.querySelectorAll('.amount');

    for(var i=0; i < widths.length; i++) {
    widths[i].addEventListener('change', calcPrice);
    }

    for(var i=0; i < heights.length; i++) {
    heights[i].addEventListener('change', calcPrice);
    }

    for(var i=0; i < types.length; i++) {
    types[i].addEventListener('change', calcPrice);
    }

    for(var i=0; i < amounts.length; i++) {
    amounts[i].addEventListener('change', calcPrice);
    }
  }
})()