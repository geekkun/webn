$(function(){
    console.log('Here sooka')
	$('#regusername').blur(function(){
		$.ajax({
			type: 'POST',
			url: '/regcheckuser/',
			data : {
				'username' : $('#regusername').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: checkuseranswer,
			dataType: 'html'
		});
	});



});


