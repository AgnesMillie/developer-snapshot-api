// 1. Importamos o 'contrato' de tipos que criamos.
// Isso garante que a função retornará dados no formato que esperamos.
import type { Snapshot } from '../types/snapshot';

// 2. Definimos a URL base da nossa API em um só lugar.
// Se um dia fizermos deploy, só precisaremos mudar esta linha.
const API_BASE_URL = 'http://localhost:8000/v1';

/**
 * Busca o snapshot de um desenvolvedor do nosso backend.
 * @param username O nome de usuário do GitHub para buscar.
 * @returns Uma Promise que resolve para o objeto Snapshot.
 * @throws Lança um erro com a mensagem apropriada se a API retornar um erro.
 */
// 3. Definimos a nossa função de serviço.
// A anotação ': Promise<Snapshot>' diz ao TypeScript: "Esta função assíncrona
// retornará, no futuro, um dado que corresponde à interface Snapshot".
export const fetchDeveloperSnapshot = async (username: string): Promise<Snapshot> => {
  // Construímos a URL completa para o endpoint desejado.
  const response = await fetch(`${API_BASE_URL}/users/${username}/snapshot`);

  // 4. Tratamento de Erro Robusto.
  // A API 'fetch' não lança um erro para respostas HTTP como 404 ou 500.
  // Precisamos verificar a propriedade 'response.ok' manualmente.
  if (!response.ok) {
    // Tentamos ler o corpo da resposta de erro para obter a mensagem de 'detail'
    // que nosso backend FastAPI envia (ex: "User not found").
    const errorData = await response.json();
    throw new Error(errorData.detail || `Erro ${response.status} na API`);
  }

  // 5. Se a resposta for bem-sucedida (status 2xx),
  // nós convertemos o corpo da resposta para JSON e o retornamos.
  // O TypeScript irá garantir que o que retornamos corresponde ao tipo 'Snapshot'.
  return response.json();
};