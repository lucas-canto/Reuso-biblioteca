# 📊 Comparação de Bibliotecas HTTP (Python)

| Critério               | requests                        | httpx                           |
|------------------------|----------------------------------|----------------------------------|
| **Última atualização** | 2024-07                         | 2024-09                         |
| **Downloads/semana**   | +100 milhões                    | +6 milhões                      |
| **Licença**            | Apache 2.0                      | BSD 3-Clause                    |
| **Complexidade da API**| Baixa (fácil de usar)           | Média (suporte a async e sync)  |
| **Suporte a Async**    | ❌ Não                           | ✅ Sim                           |
| **Documentação**       | Excelente                       | Boa                              |
| **Observações**        | Estável e amplamente usada       | Mais moderna, suporta HTTP/2     |
### 🧠 Decisão Técnica
- **Biblioteca escolhida:** requests  
- **Motivo:** É simples, muito utilizada, possui excelente documentação e atende bem à necessidade de chamadas HTTP síncronas.  
- **Alternativa descartada:** httpx (apesar de moderna e suportar async, é mais complexa e não necessária neste contexto).
