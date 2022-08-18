const simple_about = document.querySelector('.simple-about-text');
const more_about = document.querySelector('.more-about-text');
const change_btn = document.querySelector('.change-btn');
const about_title = document.getElementById('about-title')
const about_title_bkp = about_title.innerText;

change_btn.addEventListener('click', () => {
    simple_about.classList.toggle('hidden');
    more_about.classList.toggle('hidden');
    if(change_btn.innerText === 'Saiba mais'){
        change_btn.innerText = 'Menos';
        about_title.innerText = ''
    }else{
        change_btn.innerText = 'Saiba mais';
        about_title.innerText = about_title_bkp;
    }
    window.location.href = '#about-me';

})