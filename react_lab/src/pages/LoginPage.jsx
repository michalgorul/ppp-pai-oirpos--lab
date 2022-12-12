import React, { useCallback, useContext, useState } from 'react';

import apiClient from '../apiClient';

import { AuthContext } from '../AuthContextProvider';

const LoginPage = () => {
  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);

  const [userName, setUserName] = useState('');
  const [userPassword, setUserPassword] = useState('');

  const onLogin = useCallback(
    e => {
      e.preventDefault();
      apiClient.login(userName, userPassword).then(data => {
        const { loggedin: looggedIn } = data;
        alert(looggedIn ? 'Zalogowano' : 'Nie udało się zalogować');
        if (looggedIn) setIsLoggedIn(true);
      });
    },
    [setIsLoggedIn, userName, userPassword]
  );

  return (
    <div>
      {isLoggedIn ? <h1>Zalogowany</h1> : <h1>Logowanie</h1>}
      <form onSubmit={onLogin}>
        <div>
          <label>Nazwa Użytkownika</label>
          <input
            type='text'
            value={userName}
            onChange={e => setUserName(e.target.value)}
          />
        </div>
        <div>
          <label>Hasło</label>
          <input
            type='password'
            value={userPassword}
            onChange={e => setUserPassword(e.target.value)}
          />
        </div>
        <div>
          <button type='submit'>Zaloguj się</button>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
