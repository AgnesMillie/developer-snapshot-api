import React from 'react';
import styles from './Layout.module.css';

type LayoutProps = {
  children: React.ReactNode;
};

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <main className={styles.container}>
      {children}
    </main>
  );
};