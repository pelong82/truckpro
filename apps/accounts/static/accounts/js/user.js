// Elimina Cliente
$('.btn-delete-user').on('click', function(e){
	e.preventDefault();
	var target = $(e.target);
	var url = '/accounts/user/delete/'+ target.attr('name');
	$('#modal-btn-delete').attr('href',url);
});
