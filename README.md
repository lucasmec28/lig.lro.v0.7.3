# LRO Ligações 0.9.41-mre12-end-plate-dev

Esta versão acrescenta a ligação rígida MRE1/2: chapa de topo com 12 parafusos e sem nervuras, com seis parafusos ativos em tração e seis do lado comprimido recebendo o cortante. Demanda de espessura e classificação nominal são apresentadas separadamente. A precisão nativa dos dados é preservada; a apresentação usa até duas casas decimais.

## Instalação

Mantenha exatamente quatro arquivos na raiz: app.py, codigo_lro.zip, requirements.txt e README.md. Use app.py como entrada Streamlit, mantenha codigo_lro.zip compactado e reinicie após atualizar os quatro arquivos juntos. Nenhum código é baixado na inicialização.

## Alcance e verificação

Consulte docs/END_PLATE_MRE12_0941.md e docs/qualification_mre12_0941/CONTRACT.md para o método, domínio e limites. A verificação respeita o sinal do momento e do cortante, os grupos físicos de parafusos e os comprimentos de transferência locais. Restrições, contatos, CJP e hipóteses globais permanecem condições declaradas, sem aprovação automática de condições físicas desconhecidas, da estrutura global ou de fabricação.

A validação final cobre 5949 casos distintos: 5948 aprovados, uma falha herdada pela ausência do oráculo externo original de contato dos parafusos, zero erros e zero pulados. A falha não foi substituída nem contada como aprovação. Consulte docs/VALIDATION0941.json. Replays independentes, rotas de interface e testes de distribuição têm contagens separadas.

## Arquivos opcionais

O APP é independente e retém o runtime, projetos nativos, resultados, testes, oráculos, geradores, métodos e evidência reproduzível e integral da suíte atual. EXEMPLOS reúne renderizações atuais selecionadas, identificadas pela versão e hashes reais da geração, e eventuais renderizações históricas exatamente aprovadas para respeitar o limite. As omissões herdadas permanecem nos companheiros históricos já entregues; esses companheiros não são reenviados nem renomeados. AUDITORIA contém recibos, inventários e evidência reproduzível compacta, sem alegar conter todas as capturas brutas.

Imagens de páginas de referência permanecem preservadas e indexadas em docs/REFERENCE_PAGE_INDEX0941.json, sem pacote externo dessas imagens. docs/DISTRIBUTION_SPLIT0941.json registra as omissões aprovadas exclusivamente no estágio de distribuição. docs/release_manifest.json e verificar_pacote.py conferem o conteúdo distribuído. Nenhuma publicação, upload, push ou implantação faz parte desta construção.
