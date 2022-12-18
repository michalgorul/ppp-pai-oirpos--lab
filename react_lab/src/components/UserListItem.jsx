import React from 'react';

import { Link } from 'react-router-dom';

const UserListItem = ({ user }) => {
  // user_id, user_name, online
  return (
    <div>
      <h5>
        <p>
          <span>{`Username: ${user.userName}, `}</span>
          <span>{`ID: ${user.id}, `}</span>
          <span>{user.online ? 'online' : 'offline'}</span>
        </p>
        <p>
          <Link to={`/chat/${user.id}`}>Przejdź do chatu</Link>
        </p>
      </h5>
      <hr />
    </div>
  );
};

export default UserListItem;
