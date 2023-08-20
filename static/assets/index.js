import { dbank } from "../../declarations/dbank";


const updateBalance = async () => {
  const value = await dbank.checkBalance()
  document.getElementById("value").innerHTML = value.toFixed(2);
};

window.addEventListener("load", async () => {
  await updateBalance();
});

document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const inputAmount = parseFloat(document.querySelector("#input-amount").value);
  const withdrawalAmount = parseFloat(document.querySelector("#withdrawal-amount").value);
  const btn = document.querySelector("#submit-btn");
  const error = document.querySelector("#error");

  
  try {
    if (!inputAmount && !withdrawalAmount) throw new Error("Please enter an amount");
    if (inputAmount && withdrawalAmount) throw new Error("Please enter only one amount");
    if (inputAmount && inputAmount < 0) throw new Error("Please enter a positive amount");
    if (withdrawalAmount && withdrawalAmount < 0) throw new Error("Please enter a positive amount");
    if (inputAmount && inputAmount > 100) throw new Error("Please enter an amount less than 100");
    if (withdrawalAmount && withdrawalAmount > 100) throw new Error("Please enter an amount less than 100");

    btn.setAttribute("disabled", true);
    btn.value = "Processing...";
    if (inputAmount) {
      await dbank.topUp(inputAmount);
    }
    if (withdrawalAmount) {
      await dbank.withdraw(withdrawalAmount);
    }
    await updateBalance();
    btn.value = "Compounding Interest..."
    await dbank.compound();
  } catch (err) {
    console.log(err)
    error.innerHTML = err.message;
    setTimeout(() => {
      error.innerHTML = "";
    }, 3000);
  } finally {
    await updateBalance();
    document.querySelector("#input-amount").value = "";
    document.querySelector("#withdrawal-amount").value = "";
    btn.removeAttribute("disabled");
    btn.value = "Finalise Transaction";
  }
});
