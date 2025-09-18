import { useState } from 'react';
import { Layout } from './components/Layout/Layout';
// 1. Importamos nossos novos componentes principais
import { EmptyState } from './components/EmptyState/EmptyState';
import { ResultsDisplay } from './components/ResultsDisplay/ResultsDisplay';
// Importamos o serviço e os tipos como antes
import { fetchDeveloperSnapshot } from './services/apiService';
import type { Snapshot } from './types/snapshot';

function App() {
  const [snapshot, setSnapshot] = useState<Snapshot | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (username: string) => {
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

  // 2. Esta função decide o que mostrar na tela.
  const renderContent = () => {
    if (isLoading) {
      return <p>Analisando perfil... 🚀</p>;
    }
    if (error) {
      return <p style={{ color: '#ff8a8a' }}>Erro: {error}</p>;
    }
    if (snapshot) {
      // Se temos dados, mostramos o componente de resultados
      return <ResultsDisplay snapshot={snapshot} />;
    }
    // Se nenhuma das condições acima for verdade, estamos no estado inicial.
    // Mostramos nossa tela de boas-vindas, passando a função de busca para ela.
    return <EmptyState onSearch={handleSearch} />;
  };

  return (
    // 3. O nosso JSX principal agora é muito mais limpo.
    //    Ele apenas renderiza o Layout e o conteúdo decidido pela função renderContent.
    <Layout>
      {renderContent()}
    </Layout>
  );
}

export default App;