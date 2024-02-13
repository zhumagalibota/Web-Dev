const input = document.getElementById("input");
const tasks = document.getElementById("tasks");
function newTask(){
    if(input.value === ''){
        alert("No input");
    }
    else{
        let li = document.createElement("li");
        li.innerHTML = input.value;
        tasks.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    input.value = "";
    saveData();
}
tasks.addEventListener("Click", function(e){
    if(e.targer.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData(){
    localStorage.setItem("data", tasks.innerHTML);
}
function showTask(){
    tasks.innerHTML = localStorage.getItem("data");
}
showTask();