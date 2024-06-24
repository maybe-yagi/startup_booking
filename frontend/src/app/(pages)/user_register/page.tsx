'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

const AddUser = () => {
  const [form, setForm] = useState({
    name: '',
    nickname: '',
    email: '',
    student_num: '',
    role_id: '',
    password: ''
  });
  const router = useRouter();

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5000/user_register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(form)
    });

    if (response.ok) {
      router.push('/');
    }
  };

  return (
    <div>
      <h1>Add User</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" value={form.name} onChange={handleChange} required />
        <input type="text" name="nickname" placeholder="Nickname" value={form.nickname} onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
        <input type="text" name="student_num" placeholder="Student Number" value={form.student_num} onChange={handleChange} />
        <input type="text" name="role_id" placeholder="Role ID" value={form.role_id} onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} required />
        <button type="submit">Add User</button>
      </form>
      <a href="/">ユーザー一覧へ</a>
    </div>
  );
};

export default AddUser;
