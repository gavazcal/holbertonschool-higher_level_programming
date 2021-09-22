#!/usr/bin/nodejs

$(function () {
	$.ajax({
		type: 'GET',
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		success: fucntion (hello) {
			$('DIV#hello').text(hello.hello);
		}
	});
});
