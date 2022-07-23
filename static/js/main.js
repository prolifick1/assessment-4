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

  console.log('dataaaaaaaaaaaaaaaaaaa', data)
  axios.post('', data )
  .then((response) => {
    console.log('clicked')
  })
}
