
function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
	if($('#info').text()=="This username is already taken, please choose a different one"){
	                             $('#submButton').attr("disabled", true);

    }

}
 //https://stackoverflow.com/questions/2507030/email-validation-using-jquery
 function validateEmail(email) {
    console.log('validating')
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  if (!emailReg.test( email )){
    $('#info2').html('Invalid email address');
  }
  else
      $('#info2').html('');
  return emailReg.test( email );
}

$(function(){
     $('#email').on('change',function () {
        $.ajax({
            type: 'POST',
            url: '/checkUsername/',
            data: {
                'username': $('#email').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                'action':'regitsration'
            },
            success: checkuseranswer,
            dataType: 'html'
        });
    });

$('#email,#pwd, #name, #phone').on('blur focus keyup',function () {

    console.log('changed')

        if(validateEmail(($('#email')).val())&&$('#email').val()!=''&&($('#pwd')).val()!=''&&($('#name')).val()!=''&&($('#phone')).val()!=''&&$('#info').text()!="This username is already taken, please choose a different one"){

            $('#submButton').attr("disabled", false);
        }
        else{
            $('#submButton').attr("disabled", true);

        }
    })
});