const input = document.getElementById("input");
const tasks = document.getElementById("tasks");

function newTask() {
    if (input.value === '') {
        alert("No input");
    } else {
        let li = document.createElement("li");
        li.textContent = input.value; 
        tasks.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    input.value = "";
    saveData();
}

tasks.addEventListener("click", function(e) {
    if (e.target.tagName === "LI") { 
        e.target.classList.toggle("checked");
        saveData();
    } else if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData() {
    localStorage.setItem("data", tasks.innerHTML);
}

function showTask() {
    const savedData = localStorage.getItem("data");
    if (savedData) {
        tasks.innerHTML = savedData;
    }
}

showTask();
