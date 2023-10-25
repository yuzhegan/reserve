// 

var gyx;
var window = global;
var __webpack_module_cache__ = {};
!(function __webpack_require__(e) {
	console.log('require', e)
	var t = __webpack_module_cache__[e];
	if (void 0 !== t)
		return t.exports;
	var gyx = t;
	var n = __webpack_module_cache__[e] = {
		id: e,
		loaded: !1,
		exports: {}
	};
	return __webpack_modules__[e](n, n.exports, __webpack_require__),
		n.loaded = !0,
		n.exports
})(7213, function() {console.log("aaa")});

var M = gyx(7213);




function getpwd(e) {
	var rsaModulus = 'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb'
	var rsaExponent = '10001'
	var t = new M.default;
	return t.setPublic(rsaModulus, rsaExponent),
		t.encrypt(e)
}

// console.log(getpwd('123456'))
