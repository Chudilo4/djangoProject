

let list = document.querySelectorAll('.nav-link')



for(let i=0; i<list.length; i++) {
    list[i].addEventListener('click', function(){

        for(let i = 0; i<list.length; i++) {
            list[i].classList.remove('active')
        }

        if(this.classList.contains('active')) {
            this.classList.remove('active')
        } else {
            this.classList.add('active')
        }
    })
}

