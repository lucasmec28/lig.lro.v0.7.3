# LRO 0.9.55 dev.1 — apoios locais, revisão privada

Extraia os quatro arquivos juntos. Instale `pip install -r requirements.txt` e execute `streamlit run app.py`. Nenhum código é baixado na inicialização.

## Preservação
Base 0.9.53: família U com dois chumbadores e arruela ajustada, motor do apoio direto .47 e vistas .51 preservados. Novas entradas não convertem projetos antigos.

## Novas verificações calculadas
- A1(a): alma da viga laminada em apoio de extremidade sobre concreto. Comprimento efetivo de contato é informado e deve incluir tolerâncias; sem chapa de distribuição ou chumbadores. Reação, área efetiva e pressão média são entregues ao civil, sem dimensionar concreto ou fundação. O caminho metálico local pode atender sem transformar essa interface em pendência. Calço/chapa não nulo importado fica fora do domínio.
- A1(e): alma da viga CONTÍNUA sobre coluna. Reação para apoio; cortantes independentes esquerdo/direito para os painéis. A verificação da viga não fecha a chapa de topo: faltam modelo validado de contato aço-aço, largura efetiva e flexão da chapa sobre a coluna W. Status explícito de caminho local pendente; não declarar esta variante completa. O detalhe não foi modificado.
- B1/B8: somente cantoneira SOLDADA À MESA de coluna W; viga e cantoneira laminada Grade 300 sem enrijecimento; equilíbrio entre flexão da aba e escoamento local, flambagem local, geometria, reação mínima. Grupo soldado: duas linhas verticais de comprimento efetivo Lv com resistência linear calculada automaticamente conforme ASI Handbook 1 (2007), pp.58–60: qRd = φ × 0,6 × fuw × (perna/√2), kr=1. Categoria SP ou GP; E41XX ou E48XX; filetes contínuos iguais a 90°, pernas de 6 ou 8 mm. Sem crédito de penetração adicional ou aumento por direção. O modo manual excepcional exige valor e fonte. A perna deve caber na espessura das peças e as duas soldas devem caber na largura da mesa. O cisalhamento local da alma da coluna é dispensado nesse detalhe de mesa pelo exemplo DG6 B12.1 p.41. O momento excêntrico transmitido à coluna é calculado conforme B10 p.38 e entregue ao projeto externo; não se usa estabilidade global para bloquear a verificação local. O caminho metálico local B1/B8 pode atender dentro deste domínio; contenção, preparação das superfícies, categoria de solda e montagem são requisitos de execução explícitos.
- B9 parafusado: caminho local fechado para quatro M20 classe 8.8N/S, malha simétrica 2×2, furos 22 mm, um plano de corte com rosca, cantoneira Grade 300 sobre MESA de coluna W contínua, sem calços. Inclui limite superior Vf, corte dos parafusos, contato/rasgamento nas duas peças, bordas, passos e envelope de montagem. Alma apoiada limitada a tw≤14,3 mm. O corte por parafuso deriva de 0,8×0,62×830×225=92.628 N, sem copiar tabela de resistências. DG6 B6/B9 despreza a tração adicional da excentricidade em seu modelo empírico; não se extrapola para ação normal, arrancamento, sismo, fadiga ou outros grupos. O momento excêntrico vai ao dimensionamento do membro coluna. Um exemplo explícito está disponível; projetos antigos sem dimensões permanecem pendentes, nunca recebem geometria presumida.
- Material B1/B9: Grade 300 tem fy=320 MPa para ta<11 mm, 300 para 11≤ta≤17 mm e 280 acima de 17 mm, fu=440 MPa (Handbook 1 p.78). B9 usa as faixas. B1 preserva 300 conservador abaixo de 11 e todos os resultados até 17; corrige a sobreestimativa anterior acima de 17 mm.
- A2: opção registra/desenha enrijecedores da viga apoiada SEM crédito resistente. Não substitui A5. Enrijecedores da viga receptora A1(c) permanecem na família existente, sem crédito e separados de A2.

## Limites
Somente perfis W laminados simétricos, gravidade vertical, vigas horizontais sem esconsidade. Nenhuma capacidade axial, capacidade dos parafusos localizadores por V/4, estabilidade global, torção ou aprovação da ligação completa é inferida. Geometria fora do domínio não deve ser extrapolada. Ação já ELU; sem nova majoração.

Referência histórica: ASI DG6, primeira edição 2007, baseado em AS 4100:1998. Os novos cálculos usam exclusivamente os coeficientes desse modelo, sem mistura com fatores NBR. Não significa conformidade automática com normas brasileiras ou australianas atuais.

## Lacunas verificadas na referência
A correção de desigualdade impressa na p.28 contradiz o próprio limite geométrico. Esta revisão REJEITA o ponto fora dos limites em vez de corrigir/clampá-lo. A unidade impressa de k2 nas p.31/35 está dimensionalmente errada; código usa N mm. É indispensável verificar o domínio material, raios reais, tolerâncias e caminho de carga.

## Uso e distribuição
REVISÃO PRIVADA, NÃO PUBLICAR OU COMERCIALIZAR. A edição consultada exige permissão escrita da ASI para informação utilizada em software comercial; a cópia possui licença nominal de terceiro. Nenhum PDF, tabela, figura, scan ou texto da publicação é incorporado. Croquis e explicações são originais. Obter referência devidamente licenciada e autorização aplicável antes de uso comercial/distribuição. Não foi realizado deploy, push ou cópia no computador do usuário.

## Referência da solda resolvida nesta revisão
O PDF fornecido “843176271-ASI-steel-connections” é o Handbook 1 de 2007. Foram verificados texto e pixels das pp.58–60: φ=0,80 SP ou 0,60 GP; fuw=410 MPa E41XX ou 480 MPa E48XX; garganta=perna/√2. O caso E48XX, SP e perna6 mm fornece 977,5044 N/mm (0,978 kN/mm arredondado), sem ajustar números a uma tabela.

kr=1 somente para o assento que não requer tratamento de emenda longa por sobreposição. Caso longo é explicitamente rejeitado, sem capacidade do grupo, pois a fonte consultada não fornece uma lei geral de redução. Não se copia a regra de parafusos. O comprimento efetivo é de tamanho pleno; não se aplica a regra de solda intermitente ao filete contínuo. A margem de 1 mm nas espessuras é uma restrição geométrica conservadora desta revisão, não uma afirmação de regra geral para qualquer solda. Categoria, procedimento e compatibilidade consumível/metal-base devem atender às especificações de execução referidas em Handbook 1 p.54 / AS 1554.1. Não é uma certificação de solda executada.

## Verificação e histórico dos testes
Testes independentes novos e específicos da solda automatizada; ensaios dos três modelos, UI/importação/exportação e launcher real. Fonte .53 comparada byte a byte, com alterações restritas aos apoios e identidade de versão. Capacidades do antigo apoio preservadas: 119558,333781861 N superior e 178599,6 N inferior. Os testes históricos .46 existentes têm 26 falhas também na base .51 intocada; elas não são regressões novas nem um passe da suíte completa. O teste vigente .51 passa. Registro completo e recibo entregues separadamente, fora dos quatro arquivos de implantação.

## Auditoria finita da chapa A1(e)
DG6 pp.2–7 não fornece procedimento independente da chapa de topo. AISC DG1 3ª edição §4.3.1 pp.20–23 supõe pressão uniforme sobre concreto, portanto não valida a inversão sobre mesas/alma discretas. SCI P207 Step 6A trata chapa de topo como enrijecedor em ligação de momento. Exemplos AISC/STI encontrados são de coluna HSS. Nenhum foi extrapolado para a coluna W. Para fechar o detalhe existente: esclarecimento técnico ASI da Fig.A1(e) ou análise validada com contato explícito, sem alteração silenciosa da geometria.

## Revisão 0.9.55: validação e alcance

B9 e a correção de material B1 foram revisados independentemente. O caminho local DG6 não é certificação de qualquer geometria: furos adicionais, entalhes, grupos arbitrários e ações não modeladas são excluídos. Não se afirma que rasgamento de um parafuso prova todos os blocos possíveis. Seção líquida da coluna sob N/M e estabilidade do membro permanecem no projeto externo.

A1(e) NÃO foi fechado ou alterado nesta etapa: chapa de topo e introdução da reação ainda têm pendência específica. A1(a), U com dois chumbadores e viga sobre viga foram preservados. Nenhum dimensionamento do bloco de concreto foi acrescentado.

Antes do empacotamento: 66 testes focados e 45 subtestes passaram, além da UI herdada; um teste histórico que exigia B9 sempre incompleto foi explicitamente substituído. PNG e seis páginas Word foram renderizados e inspecionados; força no desenho usa duas casas decimais. Testes adicionais verificam este ZIP e o launcher após extração. Não se afirma suíte integral nem aprovação estrutural.

Extraia os quatro arquivos juntos; não misture revisões. O pacote contém manifesto novo verificável com python verificar_pacote.py na fonte extraída. Preserva a base e todos os pacotes anteriores. Empacotamento local de revisão privada; sem upload, publicação, push, deploy ou acesso ao computador do usuário.
