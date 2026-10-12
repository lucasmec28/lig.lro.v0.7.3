# LRO Ligações 0.9.35-corner-compression-dev

APP completo para revisão técnica do escopo limitado de ligação de canto soldada com 2L-T simétrico em compressão no eixo forte.

## Instalação

Mantenha exatamente quatro arquivos na raiz: app.py, codigo_lro.zip, requirements.txt e README.md. Use app.py como entrada Streamlit e mantenha codigo_lro.zip compactado. Não misture versões. Reinicie após atualizar os quatro arquivos. Nenhum código é baixado durante a inicialização.

## Validação e limites

5269 casos distintos aprovados. 1 caso permanece falha bruta porque o oráculo externo histórico de contato dos parafusos não está disponível; ele não foi contado como aprovado. Nenhuma regressão inesperada foi observada. O registro completo está em docs/VALIDATION0935.json; observações de reexecução do pacote não foram adicionadas à contagem de testes-fonte. Uma correção localizada no rodapé do desenho ocorreu durante o agregado; os 115 testes afetados, já incluídos na contagem, e 22 cenários de saídas foram reexecutados nos bytes finais. Não se afirma um agregado com runtime integralmente inalterado. Não se afirma certificação estrutural global, fabricação ou WPS. Nenhuma publicação ou implantação foi feita.

A compressão exige a geometria e os vínculos definidos no contrato. Os vetores assinados das forças reais são preservados; o mínimo de 45 kN é tratado como caso de dimensionamento explícito das interfaces soldadas.

## Exemplos e auditoria

O APP é independente. Projetos JSON nativos, resultados, testes, oráculos, geradores e verificações executáveis permanecem incorporados. O companheiro EXEMPLOS 0.9.35 contém renderizações atuais validadas; AUDITORIA 0.9.35 conserva capturas forenses da revisão independente. Os companheiros opcionais históricos 0.9.34 permanecem inalterados, com suas versões originais, e não são reenviados. Nenhum companheiro é necessário para execução ou verificação portátil atual.

Para estudar o código, extraia uma cópia separada de codigo_lro.zip. docs/DISTRIBUTION_SPLIT0935.json registra os caminhos e hashes das relocações históricas aprovadas. docs/release_manifest.json e verificar_pacote.py conferem o conteúdo distribuído. Registros anteriores foram preservados em docs/packaging_history/.
