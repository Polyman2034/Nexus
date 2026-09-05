const API_URL = "http://127.0.0.1:8000";

let tasks = [];
let currentFilter = "all";


// -------------------------
// DOM Elements
// -------------------------

const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const taskList = document.getElementById("taskList");
const emptyMessage = document.getElementById("emptyMessage");

const totalTasks = document.getElementById("totalTasks");
const activeTasks = document.getElementById("activeTasks");
const completedTasks = document.getElementById("completedTasks");

const filterButtons = document.querySelectorAll(".filter");


// -------------------------
// Load Tasks
// -------------------------

async function loadTasks() {

    try {

        const response = await fetch(`${API_URL}/tasks`);

        if (!response.ok) {
            throw new Error("Failed to load tasks");
        }

        tasks = await response.json();

        renderTasks();

    } catch (error) {

        console.error(error);

        emptyMessage.textContent =
            "Could not connect to the server.";

    }
}


// -------------------------
// Add Task
// -------------------------

async function addTask() {

    const title = taskInput.value.trim();

    if (title === "") {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/tasks`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    title: title
                })
            }
        );

        if (!response.ok) {
            throw new Error("Failed to create task");
        }

        const newTask = await response.json();

        tasks.push(newTask);

        taskInput.value = "";

        renderTasks();

    } catch (error) {

        console.error(error);

        alert("Could not add task.");

    }
}


// -------------------------
// Toggle Task
// -------------------------

async function toggleTask(id) {

    const task = tasks.find(task => task.id === id);

    if (!task) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/tasks/${id}`,
            {
                method: "PATCH",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    completed: !task.completed
                })
            }
        );

        if (!response.ok) {
            throw new Error("Failed to update task");
        }

        const updatedTask = await response.json();

        tasks = tasks.map(task =>
            task.id === id
                ? updatedTask
                : task
        );

        renderTasks();

    } catch (error) {

        console.error(error);

        alert("Could not update task.");

    }
}


// -------------------------
// Delete Task
// -------------------------

async function deleteTask(id) {

    try {

        const response = await fetch(
            `${API_URL}/tasks/${id}`,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            throw new Error("Failed to delete task");
        }

        tasks = tasks.filter(task => task.id !== id);

        renderTasks();

    } catch (error) {

        console.error(error);

        alert("Could not delete task.");

    }
}


// -------------------------
// Render Tasks
// -------------------------

function renderTasks() {

    taskList.innerHTML = "";

    let filteredTasks = tasks;

    if (currentFilter === "active") {

        filteredTasks =
            tasks.filter(task => !task.completed);

    }

    if (currentFilter === "completed") {

        filteredTasks =
            tasks.filter(task => task.completed);

    }


    if (filteredTasks.length === 0) {

        emptyMessage.style.display = "block";

    } else {

        emptyMessage.style.display = "none";
    }


    filteredTasks.forEach(task => {

        const li = document.createElement("li");

        li.className = "task";

        if (task.completed) {
            li.classList.add("completed");
        }


        const checkbox =
            document.createElement("input");

        checkbox.type = "checkbox";

        checkbox.className = "complete-button";

        checkbox.checked = task.completed;


        checkbox.addEventListener(
            "change",
            () => toggleTask(task.id)
        );


        const text =
            document.createElement("span");

        text.className = "task-text";

        text.textContent = task.title;


        const deleteButton =
            document.createElement("button");

        deleteButton.className = "delete-button";

        deleteButton.textContent = "Delete";


        deleteButton.addEventListener(
            "click",
            () => deleteTask(task.id)
        );


        li.appendChild(checkbox);
        li.appendChild(text);
        li.appendChild(deleteButton);

        taskList.appendChild(li);

    });


    updateStatistics();
}


// -------------------------
// Statistics
// -------------------------

function updateStatistics() {

    const total = tasks.length;

    const completed =
        tasks.filter(task => task.completed).length;

    const active = total - completed;


    totalTasks.textContent = total;
    activeTasks.textContent = active;
    completedTasks.textContent = completed;
}


// -------------------------
// Filters
// -------------------------

filterButtons.forEach(button => {

    button.addEventListener(
        "click",
        () => {

            filterButtons.forEach(
                button => button.classList.remove("active")
            );

            button.classList.add("active");

            currentFilter =
                button.dataset.filter;

            renderTasks();
        }
    );

});


// -------------------------
// Events
// -------------------------

addButton.addEventListener(
    "click",
    addTask
);


taskInput.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {
            addTask();
        }

    }
);


// -------------------------
// Start Application
// -------------------------

loadTasks();