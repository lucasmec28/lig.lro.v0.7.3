# LRO Ligações 0.9.65 — soldas de três bordas nas duas talas

Use juntos app.py, codigo_lro.zip, requirements.txt e README.md. Não é necessário publicar a fonte completa de desenvolvimento.

## Novidades 0.9.65

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
Pacote compacto preserva todos os módulos, dados e exemplos. Fonte integral e testes são preservados separadamente. O manifesto atual confere o pacote. Consulte docs/VALIDACAO0965.md para cobertura e limites. Testes de software não equivalem à aprovação estrutural de um projeto. Pendências técnicas permanecem identificadas nos métodos correspondentes.

## Pacote compacto
Distribuição de uso com os mesmos cálculos, recursos e exemplos. A suíte de testes e subpastas de evidências históricas não acompanham este ZIP; foram preservadas na fonte completa. Consulte docs/DISTRIBUICAO_COMPACTA0965.md.
