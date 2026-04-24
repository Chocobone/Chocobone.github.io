document.addEventListener("DOMContentLoaded", () => {
  const balloon = document.createElement("div");
  balloon.className = "nes-balloon from-right copied-balloon";
  balloon.innerHTML = "<p>Copied!</p>";
  document.body.appendChild(balloon);

  function showCopiedBalloon(top, left) {
    balloon.style.display = "block";
    balloon.style.top = `${top - 60}px`;
    balloon.style.left = `${left - 100}px`;
    setTimeout(() => {
      balloon.style.display = "none";
    }, 1000);
  }

  document.querySelectorAll(".highlight").forEach((block) => {
    if (block.querySelector(".copy-code-button")) return;

    const button = document.createElement("button");
    button.className = "nes-btn is-primary copy-code-button";
    button.type = "button";
    button.innerText = "Copy";

    button.addEventListener("click", (e) => {
      const code = block.querySelector("code").innerText;
      const textarea = document.createElement("textarea");
      textarea.value = code;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);

      showCopiedBalloon(e.pageY, e.pageX);
    });

    block.style.position = "relative";
    block.appendChild(button);
  });
});
