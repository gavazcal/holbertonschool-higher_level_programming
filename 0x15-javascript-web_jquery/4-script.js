#!/usr/bin/nodejs

$('DIV#toggle_header').click(function () {
	const $h = $('header');
	if ($h.hasClass('green')) {
		$h.removeClass('green').addClass('red');
	} else {
		$h.removeClass('red').addClass('green');
	}
});
