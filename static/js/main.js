function saveCategory() {
  let newCategoryName=document.getElementById('newCategoryName').value;
  axios.post('', { name: newCategoryName } ).then((response) => {
    window.location.href = '../../';
  });
}

function editCategory() {
  let updatedCategoryName=document.getElementById('editCategoryField').value;
  axios.put('', { name: updatedCategoryName }).then((response) => {
    window.location.href = '../../../'
  });
}

function deleteCategory() {
  axios.delete('').then((response)=> {
    window.location.href='../../../'
  });
}

function savePost() {
  let postTitle = document.getElementById('post-title').value;
  let postContent = document.getElementById('post-content').value;

  let data = { title: postTitle, content: postContent }

  axios.post('', data )
  .then((response) => {
    window.location.href='../view'
  })
}

function editPost() {
  let updatedPostTitle=document.getElementById('editPostTitleField').value;
  let updatedPostContent=document.getElementById('editPostContentField').value;
  let data = { title: updatedPostTitle, content: updatedPostContent }
  axios.post('', data)
  .then((response) => {
    window.location.href='./view'
  })

}

function deletePost() {
  axios.delete('').then((rewponse) => {
    window.location.href='../../view'
  });
}

