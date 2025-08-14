var tools = document.getElementById('home');
    let mountains_behind = document.getElementById('mountains_behind')
    let text = document.getElementById('text')
    let btn = document.getElementById('btn')
    let mountains_front = document.getElementById('mountains_front')
  

    window.addEventListener('scroll', function(){
      let value = window.scrollY;
      mountains_behind.style.top = value * 0.5 + 'px'
      mountains_front.style.top = value * 0 + 'px'
      text.style.marginRight = value * 4 + 'px'
      text.style.marginTop = value * 1.5 + 'px'
      btn.style.marginTop = value * 1.5 + 'px'

    })
