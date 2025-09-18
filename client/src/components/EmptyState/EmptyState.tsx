import React from 'react';
// Importamos o SearchForm para usá-lo dentro deste componente
import { SearchForm } from '../SearchForm/SearchForm';
import styles from './EmptyState.module.css';

// O EmptyState precisa receber a mesma prop 'onSearch' que o SearchForm,
// para que ele possa repassá-la.
type EmptyStateProps = {
  onSearch: (username: string) => void;
};

export const EmptyState: React.FC<EmptyStateProps> = ({ onSearch }) => {
  return (
    <div className={styles.container}>
      <span className={styles.icon}>🔎</span>
      <h1 className={styles.title}>Developer Snapshot</h1>
      <p className={styles.subtitle}>
        Obtenha insights qualitativos sobre o perfil de um desenvolvedor
        analisando seus repositórios e atividades no GitHub.
      </p>

      {/* Renderizamos o SearchForm e passamos a prop 'onSearch' para ele */}
      <SearchForm onSearch={onSearch} />
    </div>
  );
};