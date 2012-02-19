$(document).ready(function() {
    $(".vote_buttons").bind("vote", function(event, value) {
        var vote_el = $(this);
 	    $.ajax({
            type:'POST',
	        url: "/api/votes/vote/",
	        data: {
                'model': vote_el.attr("x:model"),
                'object_id': vote_el.attr("x:id"),
                'value': value
            },
	        success : function(data, textStatus, jqXHR) {	
	            vote_el.find(".score").html(data['score']);
                if (value == 1) {
                    vote_el.find("a.downVote").removeClass("voted");
                    vote_el.find("a.upVote").addClass("voted");
                }
                if (value == -1) {
                    vote_el.find("a.upVote").removeClass("voted");
                    vote_el.find("a.downVote").addClass("voted");
                }
                if (value == 0) {
                    vote_el.find("a.upVote, a.downVote").removeClass("voted");
                }
	        },
            statusCode: {
                401:  function(){
                    show_login();
                }
            }
        });
    });
    $('.upVote, .downVote').live('click', function(){
        $(this).parent().trigger("vote", $(this).attr("x:value"));
    });
}
