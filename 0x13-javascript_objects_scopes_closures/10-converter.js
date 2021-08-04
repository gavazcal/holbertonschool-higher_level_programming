#!/usr/bin/nodejs
// converts a number into another base

exports.converter = function (base) {
	return function (arg) {
		return arg.toString(base);
	};
};
