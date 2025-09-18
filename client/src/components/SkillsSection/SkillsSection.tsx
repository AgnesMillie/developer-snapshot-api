import React from 'react';
import styles from './SkillsSection.module.css';

type SkillsSectionProps = {
  skills: string[]; // Espera receber um array de strings
};

export const SkillsSection: React.FC<SkillsSectionProps> = ({ skills }) => {
  // Se não houver habilidades, não renderizamos nada.
  if (!skills || skills.length === 0) {
    return null;
  }

  return (
    <div className={styles.container}>
      <h3 className={styles.title}>Habilidades Inferidas</h3>
      <div className={styles.list}>
        {/* Usamos .map() para iterar sobre o array de 'skills'.
          Para cada 'skill' no array, retornamos um elemento <span>.
          A propriedade 'key' é essencial no React para listas. Ela ajuda o React
          a identificar quais itens mudaram, foram adicionados ou removidos.
          Usamos a própria string da skill como chave, já que elas são únicas.
        */}
        {skills.map((skill) => (
          <span key={skill} className={styles.skillTag}>
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
};