# LRO Ligações — revisão local 0.9.46 dev.2

Esta cópia acrescenta o apoio direto entre mesas com quatro M16 e furos circulares Ø18. Os resultados resistentes dessa família verificam somente escoamento e enrugamento locais das almas originais, no modelo nominal de compressão centrada. O caso informado tem V=2.610 kgf já em ELU (25,5953565 kN), N=My=Tz=0. O mínimo resistente de 45 kN é verificado separadamente; não é uma majoração da ação.

O par 8×60 mm da W410, altura nominal381,4 e recortes20×20, permanece construtivo. Não recebe capacidade calculada de barra, contato ajustado ou solda resistente, nem parcela presumida da reação. Não se usa o antigo valor idealizado de 328 kN para aprovar o resultado local.

Resistência local, geometria nominal e condições externas aparecem separadamente. Lucas informou 4 m, nó interno na região central da W410 e travamentos por contraventamentos/vigas intermediárias. Esses relatos não são uma comprovação calculada de comprimento destravado ou de impedimento de rotação. A estabilidade do sistema pertence ao projeto global do engenheiro.

A condição NBR 8800/5.7.8 da própria W360 no apoio continua explícita: o projeto deve garantir a contenção pertinente ou fornecer o detalhe exigido, conforme aplicabilidade. O par inferior e quatro parafusos entre mesas não comprovam esse requisito. Os resultados locais calculados não aprovam a ligação completa, a estabilidade, a fabricação, a liberação axial ou ações fora do domínio implementado. Nenhum contato, prying, tração de parafuso ou corte V/4 é resolvido por suposição.

O pacote completo usa identidade 0.9.46-apoio-direto-verificacoes-locais-revisao-dev.2. Os motores e schemas das 22 famílias anteriores conservam sua identidade 0.9.44 para preservar projetos, valores e resultados legados. O novo apoio direto usa schema3 e componente 0.9.46-direct-seat-local-review-dev.2; rascunhos de outra identidade são rejeitados explicitamente, sem conversão automática. Fontes, exemplos, testes e registros históricos estão incluídos. Os recibos atuais ficam em docs/validation_local_dev2 e docs/validation_local_direct_seat; registros antigos ficam identificados como histórico e não são prova desta revisão.

Para uso local, descompacte o pacote completo e mantenha app.py, codigo_lro.zip, requirements.txt e README.md juntos. Instale as dependências de requirements.txt e execute streamlit run app.py. Mantenha codigo_lro.zip compactado. Uma troca de revisão exige reiniciar o processo para evitar mistura de módulos.

Entrega para revisão local, sem publicação, push ou deploy. Referências e versões retidas não foram substituídas. O agregado histórico da 0.9.44 não foi reexecutado integralmente nesta revisão; não se declara aprovação de toda a suíte histórica.

A interface da família legada viga sobre viga usa a pergunta de alinhamento, mostra afastamento apenas quando aplicável e reúne My/Tz em entradas avançadas. Importações com posição desconhecida ou ações não nulas preservam seus valores; a interface não altera as fórmulas do motor legado.

Validação desta revisão: 64 testes independentes do núcleo local; 6 helpers e 59 assertions/12 reruns da UI local; 96 assertions/18 reruns do alinhamento legado, mais 3 testes focalizados; pacote completo testado pelo lançador com 44 assertions/9 execuções. Contagens separadas, sem soma com agregados históricos. Word: 3 páginas inspecionadas, 35 controles de QA. A tentativa inicial extensa do alinhamento ficou inconclusiva por tempo; a expectativa de formato científico foi corrigida no teste e o caso passou.
