import React from 'react';
import type { Snapshot } from '../../types/snapshot';
import styles from './ResultsDisplay.module.css';
import { SkillsSection } from '../SkillsSection/SkillsSection';
import { ArchetypesSection } from '../ArchetypesSection/ArchetypesSection';
import { RepositoriesSection } from '../RepositoriesSection/RepositoriesSection';

type ResultsDisplayProps = {
  snapshot: Snapshot;
};

export const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ snapshot }) => {
  return (
    <div className={styles.container}>
      <h2>Análise para o usuário: {snapshot.username}</h2>

      <hr className={styles.divider} />

      <SkillsSection skills={snapshot.inferredSkills} />

      <ArchetypesSection archetypes={snapshot.projectArchetypes} />

      {/* 2. Usamos o componente RepositoriesSection aqui. */}
      {/* Passamos o array completo de 'rawRepositoryData' para a propriedade
          'repositories' que o componente espera. */}
      <RepositoriesSection repositories={snapshot.rawRepositoryData} />
    </div>
  );
};