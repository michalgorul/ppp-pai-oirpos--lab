import React, { useState } from "react";

import apiClient from "../apiClient";

const RegisterPage = () => {
  const [userName, setUserName] = useState("");
  const [userPassword, setUserPassword] = useState("");

  return (
    <div>
      <h1>Rejestracja</h1>
      <form>
        <div>
          <label>Nazwa Użytkownika</label>
          <input
            type="text"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
          />
        </div>
        <div>
          <label>Hasło</label>
          <input
            type="password"
            value={userPassword}
            onChange={(e) => setUserPassword(e.target.value)}
          />
        </div>
        <div>
          <button
            type="submit"
            onClick={(e) => {
              // Zapobiega submit'owi formy
              e.preventDefault();
              // Zarejestruj się
              apiClient.register(userName, userPassword).then((data) => {
                alert(
                  data.register
                    ? "Stworzono użytkownika"
                    : "Nie udało się stworzyć użytkownika"
                );
              });
            }}
          >
            Zarejestruj się
          </button>
        </div>
      </form>
    </div>
  );
};

export default RegisterPage;
