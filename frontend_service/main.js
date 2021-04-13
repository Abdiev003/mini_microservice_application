async function renderPost(post){
    // let commentList = await getComments(post.id)
    let comments = post.comments
    return `<div class="col-md-3 mb-4">
                    <div class="card" style="background-color: #dae8fc;">
                        <div class="card-body">
                            <h3 class="card-title">${post.title}</h3>
                            <span>${comments ? comments.length : "0"} comments</span>
                            <ul class="ms-3">
                               ${comments ? comments.map(comment => `<li>${comment.content}</li>`).join(' ') : ''}
                            </ul>
                            <form action="" method="post" data-id="${post.id}" id="post-comment-form">
                                <span>Comment</span>
                                <input type="text" name="comment" class="mb-2">
                                <input type="submit" value="Submit">
                            </form>
                        </div>
                    </div>
                </div>`
}


// async function getComments(post_id) {
//     let response = await fetch(`http://localhost:5002/api/v1.0/posts/${post_id}/comments/`)
//     let commentData = await response.json()
//     return commentData
//
// }

async function getPosts() {
    let response = await fetch('http://localhost:5000/api/v1.0/posts/')
    return await response.json()
}

window.onload = async function (){
    let postList = await getPosts()
    let htmlContent = ''
    for (let post of postList){
        htmlContent += await renderPost(post)
    }
    document.getElementById('post_list').innerHTML += htmlContent
}

document.addEventListener('submit',  async function (e) {
    e.preventDefault()
    if (!e.target.id === 'post-comment-form'){
        console.log('ee')
        throw Error('Not form')
    }
    let form = e.target
    let postId = form.dataset.id
    let commentData = {
        content: form.comment.value,
    }
    let response = await fetch(`http://localhost:5002/api/v1.0/posts/${postId}/comments/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(commentData)
    });

    if (!response.ok){
        alert(response.status)
        throw Error('Error')
    }
    let data = await response.json()
    let ulElement = form.previousSibling.previousSibling
    let liElement = document.createElement('li')
    liElement.innerText = data.content
    ulElement.appendChild(liElement)
    form.reset()
})

let formPost = document.getElementById('post-form')

formPost.addEventListener('submit', async function (e){
    e.preventDefault()
    let postTitle = formPost.title.value
    console.log(postTitle)
    let postData = {
        title: postTitle
    }
    let response = await fetch('http://localhost:5001/api/v1.0/posts/', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })

    let data = await response.json()
    let htmlContent = await renderPost(data)
    document.getElementById('post_list').innerHTML += htmlContent
})