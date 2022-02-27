const form = document.querySelector("form");
const inputs = document.querySelectorAll(".form-control");
// const progressBar = document.getElementById("progress-bar");
let firstname, lastname, email, password, confirmPass;

const errorDisplay = (tag, message, valid) => {
  const container = document.querySelector("." + tag + "-container");
  const span = document.querySelector("." + tag + "-container > span");

  if (!valid) {
    container.classList.add("error");
    span.textContent = message;
  } else {
    container.classList.remove("error");
    span.textContent = message;
  }
};

const firstnamechecker = (value) => {
  if (value.length > 0 && (value.length < 2 || value.length > 50)) {
    errorDisplay(
      "firstname",
      "Le prénom doit contenir entre 2 et 50 caractères"
    );
    firstname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      "firstname",
      "Le prénom ne doit pas contenir de caractères spéciaux"
    );
    firstname = null;
  } else {
    errorDisplay("firstname", "", true);
    firstname = value;
  }
};

const lastnamechecker = (value) => {
  if (value.length > 0 && (value.length < 2 || value.length > 50)) {
    errorDisplay("lastname", "Le nom doit contenir entre 2 et 50 caractères");
    lastname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      "lastname",
      "Le nom ne doit pas contenir de caractères spéciaux"
    );
    lastname = null;
  } else {
    errorDisplay("lastname", "", true);
    lastname = value;
  }
};

const emailChecker = (value) => {
  if (!value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/)) {
    errorDisplay("email", "Le mail n'est pas valide");
    email = null;
  } else {
    errorDisplay("email", "", true);
    email = value;
  }
};

const passwordChecker = (value) => {
  //   progressBar.classList = "";

  if (
    !value.match(
      /^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/
    )
  ) {
    errorDisplay(
      "password",
      "Minimum de 8 caractères, une majuscule, un chiffre et un caractère spécial"
    );
    // progressBar.classList.add("progressRed");
    password = null;
  } else if (value.length < 12) {
    // progressBar.classList.add("progressBlue");
    errorDisplay("password", "", true);
    password = value;
  } else {
    // progressBar.classList.add("progressGreen");
    errorDisplay("password", "", true);
    password = value;
  }
  if (confirmPass) confirmChecker(confirmPass);
};

const confirmChecker = (value) => {
  if (value !== password) {
    errorDisplay("confirm", "Les mots de passe ne correspondent pas");
    confirmPass = false;
  } else {
    errorDisplay("confirm", "", true);
    confirmPass = true;
  }
};

inputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    switch (e.target.id) {
      case "firstname":
        firstnamechecker(e.target.value);
        break;
      case "lastname":
        lastnamechecker(e.target.value);
        break;
      case "email":
        emailChecker(e.target.value);
        break;
      case "password":
        passwordChecker(e.target.value);
        break;
      case "confirm":
        confirmChecker(e.target.value);
        break;
      default:
        nul;
    }
  });
});

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (firstname && email && password && confirmPass) {
    const data = {
      firstname,
      email,
      password,
    };
    console.log(data);

    inputs.forEach((input) => (input.value = ""));
    // progressBar.classList = "";

    firstname = null;
    email = null;
    password = null;
    confirmPass = null;
    alert("Inscription validée !");
  } else {
    alert("veuillez remplir correctement les champs");
  }
});
