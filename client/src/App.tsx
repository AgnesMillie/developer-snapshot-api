import { Layout } from './components/Layout/Layout';
import { SearchForm } from './components/SearchForm/SearchForm';

function App() {
  const handleSearch = (username: string) => {
    console.log("Buscando pelo usuário:", username);
  };

  return (
    <Layout>
      <h1>Developer Snapshot</h1>
      <SearchForm onSearch={handleSearch} />
      <div className="results-container">
        {/* O conteúdo do snapshot (loading, erro ou os dados) será renderizado aqui */}
      </div>
    </Layout>
  );
}

export default App;