 function validateEmail(email) {
    console.log('validating')
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    console.log(email)
  if (!emailReg.test( email )){
    $('#info2').html('Invalid email address');
    $('#info2').css("color", "red");
  }
  else
      $('#info2').html('');
  return emailReg.test( email );
}
function validatePhone(number) {
    var filter = /^[0-9-+]+$/;
    if (filter.test(number)) {
        $('#info3').html('');
        return true;
    }
    else {
        $('#info3').html('Invalid phone number');
        $('#info3').css("color", "red");
        return false;
    }
}

function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
	if($('#info').text()=="This username is already taken, please choose a different one"){
	                             $('#submit_but').attr("disabled", true);

    }

}

$(function(){
    $originalEmail = $('#logusername').val()
     $('#logusername').on('change',function () {
         if($('#logusername').val()!=$originalEmail) {
             $.ajax({
                 type: 'POST',
                 url: '/checkUsername/',
                 data: {
                     'username': $('#logusername').val(),
                     'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                     'action': 'regitsration'
                 },
                 success: checkuseranswer,
                 dataType: 'html'
             });
         }
    });

$('#logusername, #loguserphone, #name').on('blur focus keyup',function () {

    // console.log('changed')
    // console.log(($('#name')).text())

        if(validateEmail(($('#logusername')).val())&&($('#name')).val()!=''&&($('#loguserphone')).val()!=''&&$('#info').text()!="This username is already taken, please choose a different one"&&validatePhone(($('#loguserphone')).val())){

            $('#submit_but').attr("disabled", false);
        }
        else{
            $('#submit_but').attr("disabled", true);

        }
    })
});