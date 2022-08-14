const simple_about = document.querySelector('.simple-about-text');
const more_about = document.querySelector('.more-about-text');
const change_btn = document.querySelector('.change-btn');

change_btn.addEventListener('click', () => {
    simple_about.classList.toggle('hidden');
    more_about.classList.toggle('hidden');
    if(change_btn.innerText === 'Saiba mais'){
        change_btn.innerText = 'Menos';
    }else{
        change_btn.innerText = 'Saiba mais';
    }
    window.location.href = '#about-me';

})