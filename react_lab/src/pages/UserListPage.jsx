import React, { useContext, useEffect, useState, useRef } from "react";
import { AuthContext } from "../AuthContextProvider";
import apiClient from "../apiClient";

import UserListItem from "../components/UserListItem";

const UserListPage = () => {
  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);
  const [users, setUsers] = useState([]);

  // TODO: Jeśli użytkownik jest zalogowany ustaw listę użytkowników

  // TODO:WEBSOCKET Jeśli zostanie utworzony nowy użytkownik zaktualizuj
  // listę użytkowników przez WebSocket.

  if (!isLoggedIn) {
    return <p>Zaloguj się aby wyświetlić użytkowników czatu</p>;
  }
  return (
    <div>
      <h1>Lista użytkowników</h1>
      {users.map((user, idx) => (
        <p>Placeholder</p>
        // TODO: Wyświetl element z listy użytkowników
      ))}
    </div>
  );
};

export default UserListPage;
