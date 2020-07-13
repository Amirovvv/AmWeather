let wrap = document.querySelector('.wrap');
let date = new Date();

setInterval(() => {
	render(date);
}, 400);


function render(date) {
	let hours = date.getHours();

	if (hours > 6) {
		wrap.classList.add('morning')
	} else if (hours > 12) {
		wrap.classList.add('afternoon')
	} else if (hours > 17) {
		wrap.classList.add('evening')
	} else if (hours > 21 || hours < 6) {
		wrap.classList.add('night')
	} else {
		wrap.classList.add('none')
	}

}
