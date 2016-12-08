// Elimina Cliente
$('.btn-delete-client').on('click', function(e){
	e.preventDefault();
	var target = $(e.target);
	var url = '/panel/order/delete/'+ target.attr('name');
	$('#modal-btn-delete').attr('href',url);
});



