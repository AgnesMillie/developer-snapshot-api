import React from 'react';
import type { Repository } from '../../types/snapshot';
import styles from './RepositoriesSection.module.css';

// Função auxiliar para mapear linguagens a cores.
// Em um projeto maior, isso poderia vir de um arquivo de configuração.
const getLanguageColor = (language: string | null): string => {
  const colors: Record<string, string> = {
    'TypeScript': '#3178c6',
    'JavaScript': '#f1e05a',
    'Python': '#3572A5',
    'Java': '#b07219',
    'HTML': '#e34c26',
    'CSS': '#563d7c',
    'Ruby': '#701516',
  };
  return language ? colors[language] || '#ccc' : '#ccc';
};

type RepositoriesSectionProps = {
  repositories: Repository[];
};

export const RepositoriesSection: React.FC<RepositoriesSectionProps> = ({ repositories }) => {
  // Filtramos os repositórios que não são forks para focar no trabalho original.
  const originalRepos = repositories.filter(repo => !repo.fork);

  // Ordenamos os repositórios pelo número de estrelas (do maior para o menor).
  const sortedRepos = originalRepos.sort((a, b) => b.stargazers_count - a.stargazers_count);

  // Pegamos apenas os 6 repositórios mais populares.
  const topRepos = sortedRepos.slice(0, 6);

  if (topRepos.length === 0) {
    return null;
  }

  return (
    <div className={styles.container}>
      <h3 className={styles.title}>Repositórios Populares</h3>
      <div className={styles.grid}>
        {topRepos.map((repo) => (
          <a 
            key={repo.id} 
            href={repo.html_url} 
            target="_blank" 
            rel="noopener noreferrer" 
            className={styles.repoCard}
          >
            <span className={styles.repoName}>
              {repo.name}
            </span>
            <p className={styles.repoDescription}>
              {repo.description || 'Sem descrição.'}
            </p>
            <div className={styles.repoFooter}>
              {repo.language && (
                <span className={styles.stat}>
                  <span 
                    className={styles.languageCircle} 
                    style={{ backgroundColor: getLanguageColor(repo.language) }} 
                  />
                  {repo.language}
                </span>
              )}
              <span className={styles.stat}>
                ⭐ {repo.stargazers_count}
              </span>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
};