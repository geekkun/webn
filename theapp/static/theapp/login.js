//this function is used validate and apply css styling to input fields and buttons in login webpage
function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
	if($('#info').text()=="Unknown username"){
        $('#submButton').attr("disabled", true);
        window.alert($('#logusername').css('border-color'))
        $('#logusername').css('border-color', 'red');

    }
    else{
	    $('#submButton').attr("disabled", false);
	    $('#logusername').css('border-color', '#ccc');
    }
}

//this function is used to make an ajax request to cal checkUsername function in views.
$(function(){
     $('#logusername').on('change',function () {
        $.ajax({
            type: 'POST',
            url: '/checkUsername/',
            data: {
                'username': $('#logusername').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                'action':'login'
            },
            success: checkuseranswer,
            dataType: 'html'
        });
    });

});