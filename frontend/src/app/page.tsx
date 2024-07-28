'use client';

import { useState, useEffect } from 'react';

const Home = () => {
  const [users, setUsers] = useState({message: ''});
  const apiUrl = 'http://localhost:5000/hello';

  useEffect(() => {
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);
  console.log(users)
  console.log(apiUrl)

  return (
    <div>
      <h1>User List</h1>
      {/* <ul>
        {users.map(user => (
          <li key={user.id}>{user.name} ({user.email})</li>
        ))}
      </ul> */}
      <p>{users.message}</p>
    </div>
  );
};

export default Home;
