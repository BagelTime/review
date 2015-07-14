$(function() {
$( ".progressbar" ).each(function( index ) {
var rate = parseInt($(this).attr('rate'));
$(this).progressbar({value: rate, max: 10});
});
});