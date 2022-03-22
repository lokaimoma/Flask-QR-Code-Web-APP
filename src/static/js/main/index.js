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

const generateButton = document.querySelector("#generate-btn");

generateButton.addEventListener("click", (_) => {
    const text = document.querySelector("#payload").value;
    if (text.trim() == "") {
        showModal("Invalid data", "The payload can't be empty");
        return;
    }
    generateButton.setAttribute("disabled", true);
    const payload = {
        ...getColorModeData(),
        ...getShape(),
        data: text,
    };
    fetch(`${window.origin}/app/generateQrCode/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    })
        .then((data) => {
            if (!data.ok) {
                data.json().then(
                    (d) => d && d.error && showModal("Error", d.error)
                );
                return;
            }
            data.blob().then((d) => {
                const objUrl = window.URL.createObjectURL(d);
                const a = document.createElement("a");
                a.download = "qr_code.png";
                a.href = objUrl;
                document.body.appendChild(a);
                a.click();
                a.remove();
            });
        })
        .catch((e) => showModal("Error", e))
        .finally((_) => {
            generateButton.removeAttribute("disabled");
        });
});

function getColorModeData() {
    const colorMode = document.querySelector("select[name='color-mode']").value;
    const data = {};
    data["color_mode"] = colorMode;
    switch (colorMode) {
        case "solid":
            data["bg_color"] = document.querySelector("#solid-bg").value;
            data["fg_color"] = document.querySelector("#solid-fg").value;
            return data;
        case "radial":
        case "square":
            data["bg_color"] = document.querySelector("#bg").value;
            data["center_color"] = document.querySelector("#center").value;
            data["edge_color"] = document.querySelector("#edge").value;
            return data;
        case "linear":
            data["bg_color"] = document.querySelector("#linear-bg").value;
            data["start_color"] = document.querySelector("#linear-start").value;
            data["end_color"] = document.querySelector("#linear-end").value;
            data["direction"] = document.querySelector("#direction").value;
            return data;
        default:
            return data;
    }
}

function getShape() {
    const data = {};
    Array.from(document.querySelectorAll("input[name='shape']")).every(
        (radio) => {
            if (radio.checked) {
                data["shape"] = radio.value;
            }
            return !radio.checked;
        }
    );
    return data;
}

function showModal(title, message) {
    const div = document.createElement("div");
    div.classList.add("modal-container");
    div.innerHTML = `
      <div class="modal">
        <h3 class="modal-title">${title}</h3>
        <p class="modal-message">${message}</p>
        <div class="modal-btn-container">
          <button id="modal-close" class="btn">Ok</button>
        </div>                              
      </div>
  `;
    document.querySelector("body").appendChild(div);
    document.querySelector("#modal-close").addEventListener("click", (e) => {
        div.remove();
    });
}

const decodeSubmitBtn = document.getElementById("decode-btn");

document.querySelector("#decode-form").addEventListener("submit", (e) => {
    e.preventDefault();
    decodeSubmitBtn.setAttribute("disabled", true);
    const formData = new FormData(e.target);
    fetch(`${window.origin}/app/decodeQrCode/`, {
        method: "POST",
        body: formData,
    })
        .then((data) => data.json())
        .then((json) => {
            if (json && json.data) {
                /** @type{string} */
                let result = json.data.reduce((pv, cv) => `${pv}\n${cv}`, "");
                result = result.trim();
                showModal("Decoded Data", result);
            }
        })
        .catch((error) => showModal("Error", error))
        .finally((_) => decodeSubmitBtn.removeAttribute("disabled"));
});
