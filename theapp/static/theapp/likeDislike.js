
//this function is used to make an ajax request to call likedislike function in views.
$(function(){
    checkButtons();

		 $('.likeDislike').on('click',function () {
            $.ajax({
                type: 'POST',
                url: '/likeDislike/',
                data: {
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
					'ld': this.value,
                    'article_id':$('#test').text()
                },
                success: function() {
                    var data = $.parseJSON(this.success.arguments[0])
                    if (data.list == 'AddLike') {
                        $('#allLikes').html(parseInt($('#allLikes').text())+1)
                        $('#userLikes').html(parseInt($('#userLikes').text())+1)

                    }
                    else if (data.list == 'RemoveLike') {
                        $('#allLikes').html(parseInt($('#allLikes').text())-1)
                        $('#userLikes').html(parseInt($('#userLikes').text())-1)
                    }
                    else if (data.list == 'AddDislike') {
                        $('#allDislikes').html(parseInt($('#allDislikes').text())+1)
                        $('#userDislikes').html(parseInt($('#userDislikes').text())+1)
                    }
                    else if (data.list == 'RemoveDislike') {
                        $('#allDislikes').html(parseInt($('#allDislikes').text())-1)
                        $('#userDislikes').html(parseInt($('#userDislikes').text())-1)
                    }
                    else{
                        window.alert('HERE blya(!!!')
                    }

                checkButtons()
                },

                failure: function () {
                    window.alert('Failed ajax')

                 },
                dataType: 'html'
            });

        })



	});

//this function is used to enable/disable like or dislike button taking into consideration what user has selected
function checkButtons() {

     if(parseInt($('#userLikes').text())==1){
            //disable dislike button

            $('#dislikeButton').attr("disabled",true);

        }
        else if(parseInt($('#userDislikes').text())==1) {
            //disable like button
            $('#likeButton').attr("disabled", true);


        }
        else if(parseInt($('#userLikes').text())==0)

         {
             if(parseInt($('#userDislikes').text())==0){
            //enable like and dislike button
            $('#likeButton').attr("disabled", false);
            $('#dislikeButton').attr("disabled", false);
             }

        }


}