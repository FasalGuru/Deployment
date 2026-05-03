rangeInputs = document.querySelectorAll("input[type='range']");
rangeInputs.forEach((rangeInput) => {
  rangeInput.addEventListener("input", () => {
    const rangeOutput = document.getElementById(`${rangeInput.id}-output`);
    if (rangeOutput) rangeOutput.textContent = rangeInput.value;
  });
});

submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", () => {
  setTimeout(() => {
    submitBtn.disabled = true;
  }, 10);
});
