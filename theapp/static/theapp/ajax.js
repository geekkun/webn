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

    $('#np, #np_confirm').on('keyup', function () {
        if ($('#np').val() == $('#np_confirm').val()) {
         $('#message').html('Matching').css('color', 'green');
        }
        else
            $('#message').html('Not Matching').css('color', 'red');
    });

});


