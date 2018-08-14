// ck.datasets('#example-1', 'https://opendata.swiss/', 'statistik');
ck.datasets('#example-1', 'https://opendata.swiss/', {
	fq:       'tags:health',
	rows:     3,
	lang:     'de',
	jsonp:    true
});
ck.datasets('#example-2', 'https://opendata.swiss/', {
	fq:       'tags:zürich',
	rows:     3,
	lang:     'de',
	jsonp:    true
});
ck.datasets('#example-3', 'https://opendata.swiss/', {
	fq:       'tags:hospitals',
	rows:     1,
	lang:     'de',
	jsonp:    true
});
