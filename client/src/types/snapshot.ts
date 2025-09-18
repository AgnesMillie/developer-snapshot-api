// Define a forma de um objeto de repositório individual.
// Incluímos apenas os campos que podemos querer usar na UI.
export interface Repository {
  id: number;
  name: string;
  full_name: string;
  html_url: string;
  description: string | null; // A descrição pode ser nula
  fork: boolean;
  language: string | null;
  stargazers_count: number;
  forks_count: number;
  watchers_count: number;
  default_branch: string;
}

// Define a forma do objeto principal retornado pela nossa API de snapshot.
export interface Snapshot {
  username: string;
  snapshotDate: string; // Uma string de data no formato ISO
  inferredSkills: string[];
  mostImpactfulContribution: object; // Ainda é um placeholder
  collaborationStyle: string;
  // 'Record<string, number>' descreve um objeto com chaves string e valores numéricos
  // Ex: { "Frontend Web App": 5, "Generic Project": 3 }
  projectArchetypes: Record<string, number>;
  rawRepositoryCount: number;
  rawRepositoryData: Repository[]; // Um array de objetos do tipo Repository
}