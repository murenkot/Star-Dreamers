
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
                    <a href="{% url 'edit_comment' pk=${response.data.photo_pk} comment_pk=${response.data.comment_pk} %}">Edit</a>
                    <a href="{% url 'delete_comment' pk=${response.data.photo_pk} comment_pk=${response.data.comment_pk} %}">Delete</a>
                </div>
            </div>
        </p>
    </div>
    `
    $('#comments').append(template);
}

const addLike = (response)=>{
    console.log(response.data);
    $('.total-likes').text(response.data.likes);
}

// Listen to LIKE button
$('.toggle-icon').click(function(){
    $(this).toggleClass('-checked');
  });





// Listen to LIKE button on the main page
// $('.toggle-icon').on('click', (event) => {
//     let photo_pk = event.target.parentNode.parentNode.parentNode.parentNode.parentNode.getAttribute("val");
//     console.log(`api/v1/photo/${photo_pk}/add_like`);                               
//     $.ajax({
//         method: "POST",
//         url: `api/v1/photo/${photo_pk}/add_like`,
//         success: addLike,
//         error: onError,
//     })
// });