# LRO Ligações — 0.9.48 base U rotulada, revisão de desenvolvimento

Pacote completo, preparado somente em cloud. Nenhum push, deploy ou alteração no computador/OneDrive do usuário.

## Quatro arquivos na raiz

Mantenha `app.py`, `codigo_lro.zip`, `requirements.txt` e `README.md` juntos. Instale as dependências de requirements.txt e execute `streamlit run app.py`. Não descompacte codigo_lro.zip: a entrada verifica seu hash e extrai uma cópia privada. Reinicie o processo ao trocar versão.

## Novidade

Família separada “Placa de base · U rotulada”: um U sobre concreto, quatro barras, N/V sem momento externo. Centroide assimétrico, contato integral, placa com mecanismo U de compressão, balanços genéricos de tração, allowance 1,4 de alavanca nas barras, solda própria e integração com ancoragem ACI existente. Placa e pilar têm aços independentes. JSON, croqui, Word e CSV usam a mesma geometria/resultados; seis colunas e duas casas decimais.

É uma adaptação documentada de Ranzi–Kneen (2002), não substituição de U na rotina I/H e não declaração de cálculo literal AS4100. Consulte docs/channel_base_0948/METODO_E_DOMINIO.md dentro do código. Compressão parcial, chave e torção dos chumbadores não são cobertas. V por barras exige ey=0. O allowance de alavanca não é uma solução de contato/deformações local.

O U152×12,2 mantém tf médio e centroide reais. T=111,125 mm é referência Nucor C6×8.2; sua aplicação à série/peça fornecida precisa ser confirmada. A mínima espessura real da mesa é uma entrada separada inicialmente pendente. Exemplos são dados de teste, não cargas ou detalhes aprovados de uma obra.

As famílias anteriores e o apoio direto DG6 da .47 foram mantidos. A identidade global do pacote é 0.9.48-base-u-rotulada-dev.1; schemas/componentes legados conservam versões próprias. Registros históricos no código não substituem a evidência de testes desta revisão, entregue separadamente.

Resultados locais e pendências são explícitos. Estabilidade global, bloco armado/fundação e certificação de rigidez/rotação pertencem ao projeto do engenheiro. Testes de software não representam aprovação estrutural.
