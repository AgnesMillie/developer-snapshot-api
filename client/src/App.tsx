import { useState } from 'react';
import { Layout } from './components/Layout/Layout';
import { SearchForm } from './components/SearchForm/SearchForm';
import { fetchDeveloperSnapshot } from './services/apiService';
import type { Snapshot } from './types/snapshot';

function App() {
  // 1. Estados para gerenciar os dados, o carregamento e os erros.
  const [snapshot, setSnapshot] = useState<Snapshot | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // 2. A função de busca agora é assíncrona e lida com todo o fluxo.
  const handleSearch = async (username: string) => {
    // Reseta o estado anterior a cada nova busca
    setIsLoading(true);
    setSnapshot(null);
    setError(null);

    try {
      // Chama nosso serviço de API
      const data = await fetchDeveloperSnapshot(username);
      // Em caso de sucesso, armazena os dados no estado
      setSnapshot(data);
    } catch (err) {
      // Em caso de erro, armazena a mensagem de erro no estado
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Ocorreu um erro desconhecido.');
      }
    } finally {
      // Este bloco sempre executa, tanto em sucesso quanto em erro.
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <h1>Developer Snapshot</h1>
      <SearchForm onSearch={handleSearch} />

      <div className="results-container">
        {/* 3. Renderização Condicional: Mostra a UI de acordo com o estado. */}

        {/* Se estiver carregando, mostra a mensagem de loading */}
        {isLoading && <p>Carregando...</p>}

        {/* Se houver um erro, mostra a mensagem de erro */}
        {error && <p style={{ color: '#ff8a8a' }}>Erro: {error}</p>}

        {/* Se houver dados (snapshot), mostra os resultados */}
        {snapshot && (
          <div>
            <h2>Snapshot para: {snapshot.username}</h2>
            {/* A tag <pre> é ótima para exibir dados JSON de forma formatada para depuração */}
            <pre style={{ backgroundColor: '#1e1e1e', padding: '1rem', borderRadius: '6px', whiteSpace: 'pre-wrap' }}>
              {JSON.stringify(snapshot, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </Layout>
  );
}

export default App;