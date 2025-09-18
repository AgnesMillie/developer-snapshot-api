import { useState } from 'react';
import { Layout } from './components/Layout/Layout';
import { EmptyState } from './components/EmptyState/EmptyState';
import { ResultsDisplay } from './components/ResultsDisplay/ResultsDisplay';
import { fetchDeveloperSnapshot } from './services/apiService';
import type { Snapshot } from './types/snapshot';
// Importamos o styles do Layout para usar nossa nova classe
import layoutStyles from './components/Layout/Layout.module.css';

function App() {
  const [snapshot, setSnapshot] = useState<Snapshot | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (username: string) => {
    // ... (lógica do handleSearch continua a mesma) ...
    setIsLoading(true);
    setSnapshot(null);
    setError(null);
    try {
      const data = await fetchDeveloperSnapshot(username);
      setSnapshot(data);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Ocorreu um erro desconhecido.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const renderContent = () => {
    if (isLoading) {
      // Usamos a div com a classe de centralização
      return (
        <div className={layoutStyles.statusContainer}>
          <p>Analisando perfil... 🚀</p>
        </div>
      );
    }
    if (error) {
      // Usamos a div com a classe de centralização aqui também
      return (
        <div className={layoutStyles.statusContainer}>
          <p style={{ color: '#ff8a8a' }}>Erro: {error}</p>
        </div>
      );
    }
    if (snapshot) {
      return <ResultsDisplay snapshot={snapshot} />;
    }
    return <EmptyState onSearch={handleSearch} />;
  };

  return (
    <Layout>
      {renderContent()}
    </Layout>
  );
}

export default App;