# LRO Ligações 0.9.37-one-root-compression-dev

Ligação soldada 2L-T com uma raiz na mesa W: compressão axial local condicionada, mantendo as 19 rotas.

## Instalação

Mantenha exatamente quatro arquivos na raiz: app.py, codigo_lro.zip, requirements.txt e README.md. Use app.py como entrada Streamlit e mantenha codigo_lro.zip compactado. Não misture versões. Reinicie após atualizar os quatro arquivos. Nenhum código é baixado durante a inicialização.

## Resultado e limites

SRC1 mantém a geometria original e a força real de −200 kN: falha local por escoamento, η=1,079466667, com vínculos reais de rotação e do receptor W ainda não comprovados. Não se fabricam travamentos nem se usa a distância à extremidade como vão lateral. Casos sintéticos ou declarações de teste não comprovam condições físicas reais.

A suíte integral executou 5,566 casos distintos: 5,565 aprovados e 1 falha herdada pela ausência do oráculo externo histórico de contato dos parafusos, sem substituição ou contagem como aprovação. Zero erros e pulados, zero regressões inesperadas. Replays independentes e verificações de distribuição usam unidades separadas e não são somados. Consulte docs/VALIDATION0937.json e docs/ERRATA_NBR8800_0937.md.

## Arquivos opcionais

O APP é independente. Projetos JSON nativos, resultados, testes, oráculos numéricos, geradores, replays executáveis, referências textuais e evidência integral da suíte atual permanecem incorporados. EXEMPLOS contém renderizações úteis atuais e somente os arquivos históricos exatos eventualmente relocados, identificados por versão original e hash. Companheiros antigos não foram reenviados ou renomeados. AUDITORIA é um resumo verificável com recibos e evidência reproduzível; não contém todas as capturas brutas. O índice exato docs/REFERENCE_PAGE_INDEX0937.json informa quais imagens de páginas de referência permanecem no APP e quais ficam somente nos originais locais preservados; não há pacote externo separado dessas imagens.

Para estudar o código, extraia uma cópia separada de codigo_lro.zip. docs/DISTRIBUTION_SPLIT0937.json registra as relocações; docs/release_manifest.json e verificar_pacote.py verificam o conteúdo distribuído. Não houve publicação, push ou deploy. Nenhum resultado constitui aprovação global, comprovação dos vínculos reais ou autorização de fabricação.
