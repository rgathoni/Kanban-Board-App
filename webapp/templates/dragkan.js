const draggables = document.querySelectorAll(".task");
const description = document.querySelectorAll(".task");
const droppables = document.querySelectorAll(".lanes");
const html = document.querySelector("html");

const list = document.createElement("ul");
const info = document.createElement("p");

description.forEach((task) => {
  task.onclick = function () {
    const listItem = document.createElement("li");
    const listContent = prompt("Provide a description of the task to be added");
    listItem.textContent = listContent;
    list.appendChild(listItem);
    task.appendChild(list);

    listItem.onclick = function (e) {
      e.stopPropagation();
      const listContent = prompt("Enter Text");
      this.textContent = listContent;
    };
  };
});

draggables.forEach((task) => {
  task.addEventListener("dragstart", () => {
    task.classList.add("is-dragging");
  });
  task.addEventListener("dragend", () => {
    task.classList.remove("is-dragging");
  });
});

droppables.forEach((zone) => {
  zone.addEventListener("dragover", (e) => {
    e.preventDefault();

    const bottomTask = insertAboveTask(zone, e.clientY);
    const curTask = document.querySelector(".is-dragging");

    if (!bottomTask) {
      zone.appendChild(curTask);
    } else {
      zone.insertBefore(curTask, bottomTask);
    }
  });
});

const insertAboveTask = (zone, mouseY) => {
  const els = zone.querySelectorAll(".task:not(.is-dragging)");

  let closestTask = null;
  let closestOffset = Number.NEGATIVE_INFINITY;

  els.forEach((task) => {
    const { top } = task.getBoundingClientRect();

    const offset = mouseY - top;

    if (offset < 0 && offset > closestOffset) {
      closestOffset = offset;
      closestTask = task;
    }
  });

  return closestTask;
};

var dragKan = new DragKan(".kanban-board");

dragula([document.querySelector(".categories")], {
  copy: function (el, source) {
    return source === document.querySelector(".categories");
  },
  accepts: function (el, target) {
    return target !== document.querySelector(".categories");
  },
});
