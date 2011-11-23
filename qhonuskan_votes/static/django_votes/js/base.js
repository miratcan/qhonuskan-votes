$(function(){
    load();
    
    $(document).bind('tabLoaded', load);
    $(document).bind('contentLoaded', load);
    
    function load(){
        $('.updownvotes').each(function(){
            var id = $(this).attr('x:id');
            var model_name = $(this).attr('x:model-name');
            var result_url = $(this).attr('x:url');
            var container = $(this);
        
            $(this).find('.vote-up').live('click', function(){
                var url = $(this).attr('x:url');
        
                $.ajax({type:'POST',
                        url: url,
                        data: {'model': model_name, 'object_id': id},
                        success : loadResults});
        
                return false;
            });
            $(this).find('.vote-down').live('click', function(){
                var url = $(this).attr('x:url');
        
                $.ajax({type:'POST',
                        url: url,
                        data: {'model': model_name, 'object_id': id},
                        success : loadResults});
        
                return false;
            });
            
            function loadResults(data) {
                container.replaceWith(data);
                container.find('.vote-results').slideDown();
                load();
            }
        });
                
        var rating_types = [gettext('Awful'),
                            gettext('Poor'),
                            gettext('Average'),
                            gettext('Good'),
                            gettext('Excellent')];
                            
        $('.rating').each(function(){    
            var parent = $(this);
            var static_url = $(this).attr('x:static-url');
            var url = $(this).attr('x:url');
            var gray = static_url + 'django_votes/img/gray_star.png';
            var yellow = static_url + 'django_votes/img/star.png';
            var model_name = $(this).attr('x:model-name');
            var id = $(this).attr('x:id');
            var rating = $(this).attr('x:rating');
            
            function resetStars(limit) {
                parent.find('.star').each(function(){
                    
                    var idx = $(this).attr('x:index');
                    if (idx <= limit)
                    {
                        $(this).attr('src', yellow);
                    }      
                    else
                    {
                        $(this).attr('src', gray);
                    }              
                });
            }      
                  
            $(this).find('.star').each(function(){
                $(this).click(function(){                                    
                    var index = $(this).attr('x:index');                                        
                    
                    $.ajax({type:'POST',
                                 url:url,
                                 data: {'model': model_name, 'object_id': id, 'rating': index},
                                 success: loadResults})     
                                                                                
                    return false;
                });
                
                $(this).mouseover(function(){                    
                    var index = $(this).attr('x:index');
                    
                    resetStars(index);
                    
                    $('.rating-title').text(rating_types[index]);
                });
                
                function loadResults(data) {
                    $('.rating-container').replaceWith(data);                
                    load();
                }
            }).mouseleave(function(){
                $('.rating-title').text('');   
                
                resetStars(rating);               
            });
        });
        
        $('.rating')
            .live('hover', function(){
                $(this).css('cursor', 'hand').css('cursor', 'pointer');
            });                    
    }    
});