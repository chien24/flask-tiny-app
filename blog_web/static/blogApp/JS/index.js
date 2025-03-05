const select_list = document.querySelectorAll('.select');
select_list.forEach(element=>{
    element.style.display='none';
});
if (window.UserID){
    const select_mypost_button = document.querySelector('.select-mypost-button');
    const select_button = document.querySelector('.select-button');
    const post_select_checkbox_list = document.querySelectorAll('.post-select-checkbox');
    const select_all_button = document.querySelector('.select-all-button');
    const delete_select_button = document.querySelector('.delete-select-button');
    const post_content_list = document.querySelectorAll('.post-content');

    

    
    let isMyPost = false;
    let isSelect = false;
    let isSelectAll = false;

    select_mypost_button.addEventListener('click', ()=>{
        isMyPost = !isMyPost;
        if (isMyPost){
            post_content_list.forEach(element => {
                if (element.classList[1]!=window.UserID){
                    element.style.display = 'none';
                }
            });
            // select_mypost_button.textContent = 'All posts';
            // select_button.style.display = 'inline-block';
            select_all_button.textContent = 'Select All';
        }else{
            post_content_list.forEach(element => {
                element.style.display = 'block';
            });
            // select_mypost_button.textContent = 'My posts';
            // select_button.style.display = 'none';
            select_list.forEach(element => {
                element.style.display = 'none';
            });
            post_select_checkbox_list.forEach(element => {
                element.checked = false;
            });
            isSelect = false;
            select_button.textContent = 'Select';
            isSelectAll = false;
        }
    });

    
    select_button.addEventListener('click', ()=>{
        isSelect = !isSelect;
        if (isSelect){
            select_button.textContent = 'Cancel';
            select_all_button.style.display = 'inline-block';   // test
            post_select_checkbox_list.forEach(element => {
                element.style.display = 'inline-block'
            });
            delete_select_button.style.display = 'inline-block';
        }else{
            select_button.textContent = 'Select';
            select_all_button.style.display = 'none';   // test
            post_select_checkbox_list.forEach(element => {
                element.checked = false;
                element.style.display = 'none'
            });
            // delete_select_button.style.display = 'none';
            select_all_button.textContent = 'Select All';
            isSelectAll = false;
        }
    });


    select_all_button.addEventListener('click', ()=>{
        isSelectAll = !isSelectAll;
        if (isSelectAll){
            select_all_button.textContent = 'Reject';
            post_select_checkbox_list.forEach(element => {
                if (element.classList[2].slice(-1)==window.UserID)
                    element.checked = true;
            });
            // delete_select_button.style.display = 'inline-block';
        }else{
            select_all_button.textContent = 'Select All';
            post_select_checkbox_list.forEach(element => {
                element.checked = false;
            });
            // delete_select_button.style.display = 'none';
        }
    });

}