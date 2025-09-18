import React from 'react';
import styles from './ArchetypesSection.module.css';

type ArchetypesSectionProps = {
  archetypes: Record<string, number>;
};

export const ArchetypesSection: React.FC<ArchetypesSectionProps> = ({ archetypes }) => {
  if (!archetypes || Object.keys(archetypes).length === 0) {
    return null;
  }

  const totalRepos = Object.values(archetypes).reduce((sum, count) => sum + count, 0);
  const sortedArchetypes = Object.entries(archetypes).sort(([, countA], [, countB]) => countB - countA);

  return (
    <div className={styles.container}>
      <h3 className={styles.title}>Arquétipos de Projeto</h3>
      <div className={styles.list}>
        {sortedArchetypes.map(([archetype, count]) => {
          const percentage = totalRepos > 0 ? (count / totalRepos) * 100 : 0;

          return (
            <div key={archetype} className={styles.item}>
              <span className={styles.label}>{archetype}</span>
              <div className={styles.barContainer}>
                <div
                  className={styles.bar}
                  style={{ width: `${percentage}%` }}
                >
                  {/* A contagem agora vive DENTRO da barra */}
                  <span className={styles.count}>{count}</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};