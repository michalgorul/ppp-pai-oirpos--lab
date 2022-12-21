import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../AuthContextProvider';
import apiClient from '../apiClient';

import UserListItem from '../components/UserListItem';

const UserListPage = () => {
  const { isLoggedIn } = useContext(AuthContext);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    apiClient.getUsers().then(r => setUsers(r));
  }, []);

  // TODO:WEBSOCKET Jeśli zostanie utworzony nowy użytkownik zaktualizuj
  // listę użytkowników przez WebSocket.

  if (!isLoggedIn) {
    return <p>Zaloguj się aby wyświetlić użytkowników czatu</p>;
  }
  return (
    <div>
      <h1>Lista użytkowników</h1>
      {users.map(user => (
        <UserListItem user={user} key={user.id} />
      ))}
    </div>
  );
};

export default UserListPage;
