# LRO Ligações 0.9.71 — abertura direta pelo catálogo

Pacote `0.9.71-abertura-direta-catalogo-dev.1`. A foto de cada cartão das 26 famílias abre seu formulário nativo diretamente, assim como o botão **Abrir ligação**. O cartão da família já aberta usa **Ver ligação atual** e preserva o projeto em andamento. O escopo fica em uma informação secundária do cartão; consultar essa informação não abre nem muda a família.

A seleção exata de família continua disponível: mudar a opção apenas prepara a escolha, e o botão superior a abre. Os filtros e o retorno ao catálogo não reconfiguram o projeto. As miniaturas continuam sendo exemplos de presets, não desenhos nem resultados do projeto atual.

Esta revisão altera somente a navegação do catálogo e sua identificação de pacote. Motores, formulários nativos, renderizadores, catálogos estruturais, exemplos e miniaturas existentes permanecem iguais à revisão 0.9.70. O componente local da foto transmite apenas a identificação da família e uma sequência de evento. O componente `lro.models.VERSION` continua `0.9.44-beam-on-beam-partial-dev`. As proteções contra entradas inválidas das emendas W são preservadas.

## Executar o pacote compacto

Descompacte o ZIP externo e mantenha juntos os quatro arquivos: `app.py`, `codigo_lro.zip`, `requirements.txt` e `README.md`. Com as dependências de `requirements.txt` disponíveis, execute `streamlit run app.py`. Não é necessário descompactar `codigo_lro.zip` para usar a aplicação. Ao atualizar de revisão, reinicie o processo Streamlit para evitar mistura de módulos.

O carregador confere o SHA-256, os caminhos internos, os arquivos essenciais e a identidade do pacote. A distribuição compacta preserva byte a byte os módulos, dados, exemplos e documentos de método. Testes, caches e evidências históricas volumosas ficam na fonte completa. Consulte `docs/DISTRIBUICAO_COMPACTA0971.md` dentro do ZIP interno. O manifesto atual é criado apenas na distribuição; os manifestos históricos permanecem inalterados. Para uma verificação independente, extraia o ZIP interno em outra pasta e execute `python verificar_pacote.py` nessa pasta.

Revisão local de desenvolvimento, sem publicação, push ou deploy. A evidência AppTest é funcional, sem validação visual em navegador. Testes de software não aprovam estruturalmente um projeto. As limitações dos métodos continuam aplicáveis.

## Histórico preservado

# LRO Ligações 0.9.70 — catálogo visual azul-marinho

Pacote `0.9.70-catalogo-marinho-dev.1`. O catálogo visual opcional organiza as 26 famílias existentes por interface, modelo, grupo e busca. Selecionar uma miniatura apenas prepara a escolha; abrir a família é uma ação explícita. Os formulários de cálculo e os desenhos do projeto atual continuam sendo os nativos de cada família. As miniaturas são exemplos de presets, não resultados do projeto atual.

O catálogo e o tema azul-marinho podem ser desativados. São recursos de apresentação e navegação; não alteram motores resistentes, projetos, unidades, métodos, limites técnicos nem exportações. A identidade do componente `lro.models.VERSION` permanece `0.9.44-beam-on-beam-partial-dev`. O módulo de identidade visual é reutilizável em futuros aplicativos; nenhum outro aplicativo foi modificado.

## Executar o pacote compacto

Descompacte o ZIP externo e mantenha juntos os quatro arquivos: `app.py`, `codigo_lro.zip`, `requirements.txt` e `README.md`. Com as dependências de `requirements.txt` disponíveis, execute `streamlit run app.py`. Não é necessário descompactar `codigo_lro.zip` para usar a aplicação. Ao atualizar de revisão, reinicie o processo Streamlit para evitar mistura de módulos.

O carregador confere o SHA-256, os caminhos internos, os arquivos essenciais e a identidade do pacote. A distribuição compacta preserva byte a byte os módulos, dados, exemplos e documentos de método. Testes, caches e evidências históricas volumosas ficam na fonte completa. Consulte `docs/DISTRIBUICAO_COMPACTA0970.md` dentro do ZIP interno. O manifesto atual é criado apenas na distribuição; os manifestos históricos permanecem inalterados. Para uma verificação independente, extraia o ZIP interno em outra pasta e execute `python verificar_pacote.py` nessa pasta.

Revisão local de desenvolvimento, sem publicação, push ou deploy. A evidência AppTest é funcional, sem validação visual em navegador. Testes de software não aprovam estruturalmente um projeto. As limitações dos métodos continuam aplicáveis.

## Histórico preservado

# LRO Ligações 0.9.69 — segurança de estado nas emendas W

Correção restrita à interface das emendas W M004 e convencional N/M/V: entradas atuais inválidas, inclusive valores finitos que excedem a faixa numérica após conversão de unidades, deixam de interromper a tela mantendo resultado/Word anterior em sessão. O cálculo atual é marcado como inválido, os arquivos anteriores são removidos e as exportações ficam indisponíveis até corrigir os dados. O último projeto aceito é preservado.

O defeito foi reproduzido com entradas extremas, não com ações usuais de projeto. Motores resistentes, geometrias, métodos, catálogos, desenhos e geradores de Word permanecem idênticos à 0.9.68. Não há nova rotina estrutural nem nova qualificação de métodos. A auditoria e a correção não abrangem as famílias paralisadas.

Use os quatro arquivos juntos. Revisão local, sem publicação, push ou deploy. Consulte docs/VALIDACAO0969.md.

# LRO Ligações 0.9.68

Pequeno ajuste de apresentação das placas de base: oculta campos de cabeça/porca/chapa para tipos sem esse apoio, preservando os valores salvos. Na base U, o envelope suplementar do cone só aparece com cone ativo. Orientação diferencia referências para projetar e dados reais para conferir. Não cria dimensionamento automático de fck, bordas ou embutimento; motores, catálogos, desenhos e relatórios permanecem inalterados.

## Novidades preservadas 0.9.67

Nervura interna retangular das duas talas: envoltória de soldas entre o grupo de três bordas e a barra vertical bi-engastada, incluindo sensibilidade ao cisalhamento. Novos grupos vetoriais 3D verificam as soldas horizontais–coluna com ações concomitantes. N/Q/M e seções líquidas são informativos; resistência/estabilidade da chapa perfurada, capacidade/rigidez das chapas receptoras e rotação continuam pendentes. Sem dispensa de FLT.

## Novidades preservadas 0.9.66

Soldas em três bordas também para single plate entre mesas, sob hipótese elástica de chapa rígida. Resistência da chapa completa, receptores e rotação permanecem pendentes. Cálculos convencionais e demais famílias preservados.

Use juntos app.py, codigo_lro.zip, requirements.txt e README.md. Não é necessário publicar a fonte completa de desenvolvimento.

## Novidades preservadas 0.9.65

Grupo elástico das soldas da nervura interna nas três bordas, com gargantas distintas e reações rastreáveis. A hipótese de chapa e apoios rígidos é explícita; resistência integral da nervura perfurada e receptores continuam pendentes.

## Novidades preservadas 0.9.64
- Nervura interna das duas talas: contato/rasgamento por parafuso, com ligamento medido na direção da força e contorno físico da chapa. Ramos que chegam às soldas permanecem limitados ao teto necessário, com transferência pendente.
- A rotina não qualifica a resistência integral da nervura de três bordas.

## Novidades preservadas 0.9.63
- End plates: entradas/geometrias inválidas não alcançam o desenho proporcional; valores não finitos ou conversões excedidas não substituem o último projeto nem liberam exportações.
- Word SCI recalculado pelas entradas atuais, impedindo reutilização de resultado antigo. Valores apresentados em português com vírgula decimal.
- Equações, materiais, fatores, famílias DG39 e limites de qualificação preservados. Não há ganho resistente atribuído a linhas adicionais ou nervuras de detalhamento.

## Novidades preservadas 0.9.62
- Duas talas: validação robusta do diâmetro de catálogo, momento assinado coerente para cortante reverso e bloqueio do desenho/exportação quando a geometria é inválida.
- Preservados grupo interno e folga inicial de 10 mm. A resistência integral da nervura interna perfurada permanece sem qualificação.

## Novidades preservadas 0.9.61
- Base engastada e end plate engastada: opção de nervuras de detalhamento, sem crédito resistente, com desenho e memorial. Os modelos de cálculo e suas falhas reais permanecem; variantes estruturais de end plate não são substituídas.
- Espessura inicial comercial imediatamente superior à alma, editável; geometria com patamares de 20 mm.

## Novidades preservadas 0.9.60
- Console enrijecido: nova família com reação vertical, nervura recortada, soldas e alma receptora. Interface, projeto JSON, CSV e Word em português. Resultado qualificado ao escopo local.
- Catálogo do console: dez perfis Gerdau com designação americana publicada e três referências AISC. As dimensões são nominais de catálogo, não medições reais. Materiais A36 ou A572 Gr.50 precisam corresponder ao certificado; A992 é reservado aos registros AISC.
- Duas talas: configuração inicial com parafusos internos, extensão zero e folga real de 10 mm. Projetos importados conservam seus valores. Esta melhoria geométrica não fecha pendências anteriores do método.
- End plate rotulada: aviso inicial claro de que a opção NBR N/V está em validação. A opção SCI continua selecionável, sem conversão automática entre métodos.

## Domínios dos métodos
O console utiliza AISC 360-16 LRFD e Manual AISC 15, detalhe de nervura recortada na alma de pilar. Não cobre ações horizontais independentes, levantamento, torção, momento imposto ou estabilidade global. Não constitui conversão de fatores AISC para NBR. Confira docs/DOMINIO_PILARES.txt e INTEGRACAO_CONSOLE.txt.
A opção SCI de end plate mantém SCI/BCSA P358 §4.7 e Eurocode UK: somente cisalhamento vertical na alma da coluna, aço S275/S355 efetivamente especificado, chapa S275 de 10/12 mm e M20 classe 8.8. Geometria Gerdau não equivale a aço EN. Referência: https://www.steelconstruction.info/images/a/a9/SCI_P358.pdf

## Distribuição e verificação
Pacote compacto preserva todos os módulos, dados e exemplos. Fonte integral e testes são preservados separadamente. O manifesto atual confere o pacote. Consulte docs/VALIDACAO0968.md para cobertura e limites. Testes de software não equivalem à aprovação estrutural de um projeto. Pendências técnicas permanecem identificadas nos métodos correspondentes.
