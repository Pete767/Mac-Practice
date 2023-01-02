document.addEventListener("DOMContentLoaded",function(){
    let todoForm = document.getElementById("newTodoForm");
    let todoList = document.getElementById("todoList");
    todoForm.addEventListener("submit", function(event) {
        event.preventDefault();
        let newTodo = document.createElement("li");
        newTodo.innerText = document.getElementById("add").value;
        let removeButton = document.createElement("button");
        removeButton.innerText = "Remove"
        todoList.appendChild(newTodo);
        newTodo.appendChild(removeButton)
        todoForm.reset();
});
todoList.addEventListener("click", function(event){
    const makeLower = event.target.tagName.toLowerCase();
    if (makeLower === "li") {
        event.target.style.textDecoration = "line-through";
      } else if (makeLower === "button") {
        event.target.parentNode.remove();
      }
});
});