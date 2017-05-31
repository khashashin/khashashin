// ck.datasets('#example-1', 'https://opendata.swiss/', 'statistik');
ck.datasets('#example-1', 'https://opendata.swiss/', {
	fq:       'tags:hospitals',
	rows:     3,
	lang:     'de',
	jsonp:    true
});
