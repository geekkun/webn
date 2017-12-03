$(function(){
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
	$('#logusername').blur(function(){
		$.ajax({
			type: 'POST',
			url: '/logcheckuser/',
			data : {
				'username' : $('#logusername').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: checkuseranswer,
			dataType: 'html'
		});
	});
});

function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
}