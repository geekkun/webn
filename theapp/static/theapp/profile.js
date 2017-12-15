$(function(){
		$('#np, #np_confirm, #op').on('keyup', function () {
		if($('#passmessage').html()!='Correct'){
		    $('#submit_but').attr("disabled",'disabled');
		}
		if ($('#np').val() == $('#np_confirm').val()&&$('#np').val()!='') {
		 $('#message').html('Matching').css('color', 'green');
		 $('#np, #np_confirm').css('border-color', 'green');
		 if($('#passmessage').html()=='Correct'){
		    $('#submit_but').removeAttr("disabled");
		 }
		}
		else if ($('#np').val()=='' && $('#np_confirm').val()=='') {
                $('#message').html('')
            }

        else {
			$('#message').html('Not Matching').css('color', 'red');
			$('#submit_but').attr("disabled",'disabled');
			$('#np #np_confirm').css('border-color', '#ccc');
		    }

		});

		 $('#op').bind('input propertychange',function () {
            $.ajax({
                type: 'GET',
                url: '/checkpassword/',
                data: {
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
					'passw': $('#op').val()
                },
                success: function() {
                    var data = $.parseJSON(this.success.arguments[0])
                    if (data.list == 'True'&&$('#op').val()) {
                        $('#passmessage').html('Correct');
                        $('#op').css('border-color', 'green');

                    }
                    if (data.list == 'False'&&$('#op').val()) {
                        $('#op').css('border-color', 'red');
                        $('#passmessage').html('Incorrect');
                    }
                    if(!$('#op').val()){
                        $('#passmessage').css('border-color','#ccc');
                        $('#passmessage').html('');
                    }


                },

                failure: function () {
                    $('#passmessage').html('failed ajax')

                 },
                dataType: 'html'
            });

        })



	});
