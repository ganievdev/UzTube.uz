$(function () {
  $('[data-toggle="tooltip"]').tooltip()
  $('[data-toggle="ajax"]').on('click',function(e){
    e.preventDefault();
    let obj = $(this);
    $.ajax({
      method: 'GET',
      url: $(this).attr('href'),
      success: function(res){
        let like = res.split('/')[0];
        let dislike = res.split('/')[1];

        obj.parent().find('.like').html(like);
        obj.parent().find('.dislike').html(dislike);
      },
      error: function(){
        alert('ERROR')
      }
    });
    return false;

  });
});

