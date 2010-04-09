/* Estonian initialisation for the jQuery UI date picker plugin. */
/* Written by Agne Lund (gness@gness.net). */
jQuery(function($){
    $.datepicker.regional['et'] = {
		closeText: 'Sulge',
		prevText: '&laquo;Eelmine',
		nextText: 'Järgmine&raquo;',
		currentText: 'Täna',
		monthNames: ['Jaanuar','Veebruar','Märts','Aprill','Mai','Juuni','Juuli','August','September','Oktoober','November','Detsember'],
		monthNamesShort: ['Jaan','Veebr','Mär','Apr','Mai','Jun',
		'Jul','Aug','Sept','Okt','Nov','Dets'],
		dayNamesShort: ['P','E','T','K','N','R','L'],
		dayNames: ['Pühapäev','Esmaspäev','Teisipäev','Kolmapäev','Neljapäev','Reede','Laupäev'],
		dayNamesMin: ['P','E','T','K','N','R','L'],
		dateFormat: 'dd.mm.yy', firstDay: 1,
		isRTL: false};
    $.datepicker.setDefaults($.datepicker.regional['et']);
});
