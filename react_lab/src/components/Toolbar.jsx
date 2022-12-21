import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContextProvider';

import apiClient from '../apiClient';

const Toolbar = () => {
  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);

  return (
    <>
      <div>
        <ul>
          <li>
            <Link to=''>Lista użytkowników</Link>
          </li>
          <li>
            <Link to='/login'>Logowanie</Link>
          </li>
          <li>
            <Link to='/register'>Rejestracja</Link>
          </li>
        </ul>
        <span style={{ color: isLoggedIn ? 'green' : 'crimson' }}>
          <b>
            {isLoggedIn
              ? 'Użytkownik jest zalogowany'
              : 'Użytkownik nie jest zalogowany'}
          </b>
        </span>
        <span
          style={{ float: 'right', marginRight: '1rem', cursor: 'pointer' }}
          onClick={e => {
            e.preventDefault();
            apiClient.logout().then(data => {
              const { loggedin } = data;
              setIsLoggedIn(loggedin);
            });
          }}
        >
          Wyloguj
        </span>
        <span
          style={{ float: 'right', marginRight: '1rem', cursor: 'pointer' }}
          onClick={e => {
            e.preventDefault();
            apiClient.loginTest().then(data => {
              const { loggedin } = data;
              setIsLoggedIn(loggedin);
            });
          }}
        >
          Test login
        </span>
      </div>
      <hr />
    </>
  );
};

export default Toolbar;
