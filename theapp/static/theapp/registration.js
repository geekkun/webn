//function used by ajax call where usernamecheck is called this function is called on success
function checkuseranswer(data, textStatus, jqHXR)
{
	if($('#email').val()&&validateEmail($('#email').val())) {
        $('#info').html(data);
    }
	if($('#info').text()=="This username is already taken, please choose a different one"){
	                             $('#submButton').attr("disabled", true);
	                             $('#email').css('border-color', 'red');

    }

}
 //https://stackoverflow.com/questions/2507030/email-validation-using-jquery
//function used to apply some styling when validating email in signup webpage
 function validateEmail(email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  if (!emailReg.test( email )){
    $('#info2').html('Invalid email address');
    $('#email').css('border-color', 'red');
  }
  else {
      $('#info2').html('');
  }
  return emailReg.test( email );
}
//fucntion used to apply some styling when validating phone number in signup webpage
function validatePhone(number) {
    var filter = /^[0-9-+]+$/;
    if (filter.test(number)) {
        $('#info3').html('');
        $('#phone').css('border-color', 'green');

        return true;
    }
    else {
        $('#info3').html('Invalid phone number');
        $('#phone').css('border-color', 'red');
        return false;
    }
}
//function used to make an ajax call to checkusername function in views.
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

//function used to apply styling to signup webpage when validating user input
$('#email,#pwd, #name, #phone').on('blur focus keyup',function () {
    if(!$('#email').val()){
        $('#email').css('border-color', '#ccc');
    }
    if(!$('#phone').val()){
        $('#phone').css('border-color', '#ccc');
    }

         if (validateEmail(($('#email')).val())&&($('#info').text()!="This username is already taken, please choose a different one")&&$('#email').val()!=''){
      $('#email').css('border-color', 'green');
  }

        if(validateEmail(($('#email')).val())&&$('#email').val()!=''&&($('#pwd')).val()!=''&&($('#name')).val()!=''&&($('#phone')).val()!=''&&$('#info').text()!="This username is already taken, please choose a different one"&&validatePhone(($('#phone')).val())){

            $('#submButton').attr("disabled", false);
        }
        else{
            $('#submButton').attr("disabled", true);

        }
    })
});