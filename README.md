# Nexus — Personal Task Manager

> A lightweight full-stack task management application built to solve a real problem in my daily workflow.

Nexus is a personal task management application designed and developed for my own use.

I wanted a simple and focused way to manage daily tasks without the complexity of large productivity platforms. Instead of adopting another tool, I decided to build one that matched my needs.

**Nexus is now deployed and actively used by me to manage my tasks.**

---

## Why I Built Nexus

Managing daily tasks can become difficult when they are scattered across notes, reminders, messages, and different applications.

I faced this problem myself and decided to build a simple solution.

My goal was to create a task manager that is:

- **Simple** — focused on essential task management
- **Fast** — quick to add and manage tasks
- **Accessible** — available directly from a web browser
- **Minimal** — without unnecessary productivity features
- **Practical** — built around my actual workflow

What started as a personal productivity problem became my first deployed full-stack web application.

---

## Features

### Task Management

- Create tasks
- Mark tasks as completed
- Delete tasks
- View all tasks
- Filter tasks by **All**, **Active**, and **Completed**

### Task Statistics

Nexus provides an overview of:

- Total tasks
- Active tasks
- Completed tasks

### User Experience

- Clean and minimal interface
- Responsive design
- Keyboard support
- Dynamic UI updates
- Simple productivity-focused workflow

---

## Tech Stack

### Frontend

- **HTML5**
- **CSS3**
- **JavaScript**
- **Fetch API**

### Backend

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

### Tools & Deployment

- **Git**
- **GitHub**
- **Vercel**
- **Render**

---

## Architecture

```text
                         GitHub
                            │
                     Nexus Repository
                       /           \
                      /             \
                     ▼               ▼
                 Vercel           Render
                Frontend          Backend
              HTML / CSS / JS     FastAPI
                     │               │
                     └──── REST API ─┘
