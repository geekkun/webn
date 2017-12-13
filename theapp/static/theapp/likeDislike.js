$(function(){

		 $('#likeDislike').on('click',function () {
		     window.alert('In LD')
            $.ajax({
                type: 'POST',
                url: '/likeDislike/',
                data: {
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
					'ld': $('#likeDislike').value(),
                    'article_id':$('#article_title').val()
                },
                success: function() {
                    window.alert('HERE!!!')
                    var data = $.parseJSON(this.success.arguments[0])
                    if (data.list == 'AddLike') {
                        $('#allLikes').html($('#allLikes').valueOf()+1)
                        $('#userLikes').html($('#allLikes').valueOf()+1)

                    }
                    if (data.list == 'RemoveLike') {
                        $('#allLikes').html($('#allLikes').valueOf()-1)
                        $('#userLikes').html($('#allLikes').valueOf()-1)
                    }
                    if (data.list == 'AddDislike') {
                        $('#allDislikes').html($('#allLikes').valueOf()+1)
                        $('#userDislikes').html($('#allLikes').valueOf()+1)
                    }
                    if (data.list == 'RemoveDislike') {
                        $('#allDislikes').html($('#allLikes').valueOf()-1)
                        $('#userDislikes').html($('#allLikes').valueOf()-1)
                    }

                },

                failure: function () {
                    window.alert('Failed ajax')

                 },
                dataType: 'html'
            });

        })



	});
