// ---- G L O B A L S
let newPostBtn = false;


// ---- F L A G   P O S T
btnFlag = post_id => alert(`Post ${post_id} has been flagged!`);


// ---- L I K E   P O S T
function btnLike(post_id) {
    var numLikes = parseInt($(`#likes-${post_id}`).text());
    $(`#likes-${post_id}`).html(`&nbsp ${numLikes + 1} &nbsp`);

    $.ajax({
        url: `/post/${post_id}/like`,
        type: 'GET',
        data: { post_id: post_id },
        success: res => {
            console.log("liked");
        },
        error: err => console.log(err)
    });
}


// ---- D I S L I K E   P O S T
function btnDislike(post_id) {
    var numLikes = parseInt($(`#dislikes-${post_id}`).text());
    $(`#dislikes-${post_id}`).html(`&nbsp ${numLikes + 1} &nbsp`);

    $.ajax({
        url: `/post/${post_id}/dislike`,
        type: 'GET',
        data: { post_id: post_id },
        success: res => {
            console.log("disliked");
        },
        error: err => console.log(err)
    });
}


// ---- N E W   P O S T
function newPost() {
    if (!newPostBtn) {
        newPostBtn = true;
        $("#new-post").slideDown();
        $("#new-post-btn").removeClass("btn-primary");
        $("#new-post-btn").addClass("btn-danger").text("Cancel");
    }

    else {
        newPostBtn = false;
        $("#new-post").slideUp();
        $("#new-post-btn").removeClass("btn-danger");
        $("#new-post-btn").addClass("btn-primary").text("New Post");
    }

}


// ---- I N I T
function init() {
    console.log("Document ready");

    $("#new-post").hide();
}

window.onload = init;