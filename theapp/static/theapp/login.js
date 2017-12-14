
function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
	if($('#info').text()=="Unknown username"){
        $('#submButton').attr("disabled", true);
    }
    else{
	    $('#submButton').attr("disabled", false);
    }
}

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