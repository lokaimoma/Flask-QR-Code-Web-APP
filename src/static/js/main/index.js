"use strict";

let prevColorMode = "solid";

document
  .querySelector("select[name='color-mode']")
  .addEventListener("change", (e) => {
    handleColorModeChange(e.target.value.toLowerCase());
  });

function handleColorModeChange(newMode) {
  if (newMode === "" || newMode === " ") return;
  const prev = document.querySelector(`div.${prevColorMode}`);
  prev && (prev.style.display = "none");
  prevColorMode = newMode;
  const next = document.querySelector(`div.${newMode}`);
  next && (next.style.display = "block");
}
