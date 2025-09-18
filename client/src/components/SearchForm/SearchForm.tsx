import React, { useState } from 'react';
import styles from './SearchForm.module.css';

type SearchFormProps = {
  onSearch: (username: string) => void;
};

export const SearchForm: React.FC<SearchFormProps> = ({ onSearch }) => {
  const [username, setUsername] = useState('');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (username.trim()) {
      onSearch(username.trim());
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <input
        type="text"
        className={styles.input}
        placeholder="Digite um username do GitHub..."
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button type="submit" className={styles.button}>
        Buscar
      </button>
    </form>
  );
};