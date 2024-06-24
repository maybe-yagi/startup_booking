'use client';

import { useState, useEffect } from 'react';

const Home = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL + '/users';

  useEffect(() => {
    fetch(apiUrl, {
      credentials: 'include'
    })
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name} ({user.email})</li>
        ))}
      </ul>
      <a href="/user_register">ユーザー登録へ</a>
    </div>
  );
};

export default Home;
