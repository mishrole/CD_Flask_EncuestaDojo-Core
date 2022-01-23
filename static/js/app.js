const form = document.querySelector('#survey');
const inputFullname = document.querySelector('#fullname');
const inputLocation = document.querySelector('#location');
const inputLanguage = document.querySelector('#language');

form.addEventListener('submit', (e) => {
    if (parseInt(inputLocation.value) > 0 && parseInt(inputLanguage.value) > 0 && inputFullname.value.length > 0) {
        return true;
    } else {
        e.preventDefault();
        alert('Name, Location, and Language are required fields')
    }
});