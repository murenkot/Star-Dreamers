
// Listen to ADD COMMENT button:
$('#add-comment').on('click', ()=>{
    console.log("add-comment");
    $('.add-comment').toggleClass('hidden');
})


// Listen to SAVE button
const onError = (err1, err2, err3)=>{console.log({err3});}

const addComment = (response) => {
    $('.new-comment-body').val('');
    $('.add-comment').toggleClass('hidden');
    template = `
    <div class="comment-frame">
        <p class="comment">
            <p id="username">${response.data.username}: </p>
            <p>${response.data.body}</p>
            <div>
                <div class="flex-right">
                    <a href="{% url 'edit_comment' pk=${response.data.photo_pk} comment_pk=${response.data.comment_pk} %}" style="size: 16px;">Edit</a>
                    <a href="{% url 'delete_comment' pk=${response.data.photo_pk} comment_pk=${response.data.comment_pk} %}" style="size: 16px;">Delete</a>
                </div>
            </div>
        </p>
    </div>
    `
    $('.comment-frame:last-child').after(template);

}

const addLike = (response)=>{
    console.log("adding likes")
    console.log(response.data);
    $('.total-likes').text(response.data.likes);
}

// Listen to LIKE button
$('.toggle-icon').click(function(){
    $(this).toggleClass('-checked');
  });





