import React, { useState, useEffect } from 'react';

import apiClient from './apiClient';

export const AuthContext = React.createContext();

const AuthContextProvider = props => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Sprawdz czy użytkownik jest zalogowany
  useEffect(() => {
    apiClient.loginTest().then(data => {
      setIsLoggedIn(data.loggedin);
    });
  }, []);

  return (
    <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn }}>
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContextProvider;
