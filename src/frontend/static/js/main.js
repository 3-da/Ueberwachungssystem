const test = document.getElementsByTagName('div');
let bol = false;

test[0].addEventListener('click', () => {
    bol = !bol;

    if (bol) {
        test[0].style.backgroundColor = 'green';
    } else {
        test[0].style.backgroundColor = 'red';
    }
});