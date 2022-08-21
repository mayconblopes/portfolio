const more_awards_btn = document.getElementById('more-awards-btn');
const more_pappers_btn = document.getElementById('more-pappers-btn');

const more_awards_content = document.getElementById('more-awards-content');
const more_pappers_content = document.getElementById('more-pappers-content');

more_awards_btn.addEventListener('click', () => {
    more_awards_content.classList.toggle('hidden');

    if(more_awards_btn.innerText === 'Saiba mais'){
        more_awards_btn.innerText = 'Menos';
    }else{
        more_awards_btn.innerText = 'Saiba mais';
    }
    window.location.href = '#banner-awards';

})

more_pappers_btn.addEventListener('click', () => {
    more_pappers_content.classList.toggle('hidden');

    if(more_pappers_btn.innerText === 'Saiba mais'){
        more_pappers_btn.innerText = 'Menos';
    }else{
        more_pappers_btn.innerText = 'Saiba mais';
    }
    window.location.href = '#banner-pappers';

})