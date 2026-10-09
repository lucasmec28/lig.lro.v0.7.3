# LRO Ligações 0.8.3 — pacote completo para repositório novo

## Os quatro arquivos que devem aparecer no GitHub

| Arquivo | Função |
|---|---|
| `app.py` | Arquivo principal selecionado no Streamlit |
| `codigo_lro.zip` | Todos os módulos, catálogo de perfis, exemplos e documentação |
| `requirements.txt` | Bibliotecas instaladas automaticamente pelo Streamlit |
| `README.md` | Estas instruções |

Extraia o ZIP principal `LRO_Ligacoes_COMPLETO_v0_8_3.zip`. Envie os **quatro arquivos resultantes** diretamente à raiz do repositório. Mantenha `codigo_lro.zip` compactado: o próprio aplicativo o abre ao iniciar. Nesta distribuição não é necessário criar nem enviar pastas `lro/`, `data/` ou `docs/` separadamente.

## GitHub: repositório novo

1. Crie um repositório vazio. Sugestão de nome: `lro-ligacoes-completo`.
2. Na página inicial do repositório vazio, clique em **uploading an existing file**. Em um repositório já inicializado, use **Add file → Upload files**.
3. Selecione ou arraste os **quatro arquivos** da tabela acima. O limite de arquivos por seleção não é problema neste pacote.
4. Confirme o envio em **Commit changes**.
5. Confira que `app.py`, `codigo_lro.zip`, `requirements.txt` e `README.md` aparecem lado a lado na raiz da branch que será publicada.

## Streamlit Community Cloud

1. Acesse <https://share.streamlit.io/> e clique em **Create app**.
2. Selecione seu repositório novo.
3. Em **Branch**, escolha a branch que contém os quatro arquivos, normalmente `main`.
4. Em **Main file path**, informe **`app.py`**.
5. Em **Advanced settings → Python version**, escolha **3.12**.
6. Publique. Não é necessário preencher **Secrets** para este aplicativo.
7. Ao abrir, confira a versão **0.8.3** e as cinco famílias do seletor **Tipo de ligação**.

Ao atualizar futuramente, envie os quatro arquivos do novo pacote juntos e reinicie o app. O inicializador identifica se `app.py` e `codigo_lro.zip` pertencem à mesma distribuição, evitando misturar módulos de versões diferentes.

## Ligações incluídas

- **Single plate viga–viga**, com complemento entre mesas e enrijecedor oposto opcionais.
- **Single plate viga–mesa da coluna**.
- **Viga–alma da coluna com duas talas**, nervura vertical e enrijecedores horizontais.
- **End plate rotulada** na mesa da coluna.
- **End plate engastada** na mesa da coluna, com extensão acima e abaixo ou somente acima, no domínio implementado.

- **Placa de base Tipo 1**, perfil I/H e quatro chumbadores externos, com N, M no eixo forte e V. Verifica chapa, contato, aço dos chumbadores e caminho de cortante declarado. Ancoragem no concreto, bloco armado, soldas e rigidez precisam de cálculo complementar.

As duas single plates são acessadas pela mesma família no seletor. O pacote inclui cálculo, desenhos proporcionais, projetos JSON, catálogo de perfis, geração de memória Word e documentação dos métodos.

## Melhorias das ligações já incluídas

- W200 e outros parâmetros fora da faixa ensaiada podem seguir com avisos de extrapolação, sem confirmar resistência ou rigidez fora desse domínio.
- Espaçamentos máximos e bordas máximas não atendidos permitem continuar o cálculo e exportar o Word, mantendo a não conformidade visível.
- A end plate engastada tem o campo **Linhas intermediárias entre as mesas** em **Chapa e parafusos**. Cada linha adiciona dois parafusos, somente para detalhamento, sem crédito resistente. Os novos furos são considerados nos ligamentos e blocos; o arranjo ampliado permanece com ressalva.
- A revisão das cinco ligações e seus limites está em `docs/AJUSTES_V074.md`, dentro de `codigo_lro.zip`.

**Se o repositório já está funcionando:** substitua seus quatro arquivos pelos quatro deste pacote e reinicie o app. Não é necessário criar outro repositório.

## Código e uso local

O `codigo_lro.zip` contém o código-fonte legível completo, testes e documentação, sem depender de arquivos de versões anteriores. Para publicação, envie-o compactado. Para auditar ou editar o código, extraia uma cópia em outra pasta. Nessa cópia, os comandos convencionais continuam disponíveis:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q tests
python -m streamlit run app.py
```

Também é possível abrir a distribuição de quatro arquivos localmente:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

O inicializador extrai o código para uma pasta temporária privada no servidor e o reutiliza durante a execução. Ele não grava nos arquivos do repositório e não depende de download de módulos externos em tempo de execução. Os projetos são importados/exportados por JSON, como antes.

## Referências de publicação

- GitHub: <https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository>
- Streamlit: <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>


## Correções da 0.7.5

A navegação entre famílias mantém o projeto em edição; rotulada e engastada conservam rascunhos independentes. Valores numéricos não finitos nunca produzem uma verificação favorável. Os modelos estruturais da 0.7.4 foram preservados, inclusive as ressalvas da W200 e as linhas intermediárias sem crédito resistente. Veja `docs/AJUSTES_V075.md` dentro de `codigo_lro.zip`. Salve o JSON para preservar o projeto além da sessão.


## Placas de base incluídas

Em **Placa de base · Tipo 1**, informe perfil, N/M/V já de cálculo, espessura e aço da chapa, bitola dos quatro chumbadores, a₁/a₂ e concreto/graute. Os seis regimes C1/C2/C3 e T1/T2/T3 são selecionados automaticamente. Há exemplos didáticos, desenho, JSON e memória Word. Nesta família, **N positivo significa compressão**, claramente identificado na tela.

Concreto normal com 20 ≤ fck ≤ 50 MPa. Chumbadores externos ASTM A36. Sem flexão biaxial, placa enrijecida ou chumbadores químicos. O cortante pode usar chumbadores com arruelas soldadas, atrito, chave de chapa retangular ou resistência externa documentada, no domínio de cada rota, sem somar os caminhos. As verificações locais e as pendências de cada modelo são descritas a seguir.

A conclusão separa as verificações dos componentes da base completa. Os testes não aprovam automaticamente o projeto. Não houve publicação automática.


## Incluído desde a 0.8.1: chave de chapa retangular

O caminho **Chave de chapa retangular · verificações locais** calcula contato no concreto, flexão e cisalhamento da chapa, relação entre espessuras e momento adicional do cortante: **Mef=M+V[tp+(bv+en)/2]**, com sinais. Use M/V na face superior da placa, antes dessa parcela. O app usa o graute real e não soma atrito. Há exemplo didático de cortante puro, desenho e memória Word.

As ações Vw/Mw para dimensionar as soldas são obtidas na resistência de contato do concreto. Soldas, metal-base, flexão local da fixação, ruptura do concreto e bloco armado continuam a complementar. “Atende” vale somente para cada verificação local. Chaves cruciformes/perfis W continuam no caminho documentado externamente; sua geometria não é convertida em chapa equivalente.

Projetos anteriores e os outros modelos de ligação foram preservados. Não houve publicação automática.


## Três opções de transferência do cortante

O seletor principal distingue **chumbadores**, **barra/chave de cisalhamento** e **atrito**, sem soma automática de resistências. Uma nova base abre em chumbadores com **quatro arruelas soldadas**, no domínio descrito abaixo. Atrito e resistência externa documentada continuam disponíveis. Projetos antigos conservam seu caminho e não são convertidos em aprovação nativa. Na rota externa, capacidade e referência são independentes das da chave; a confirmação de aplicabilidade é vinculada aos dados atuais e invalidada quando esses dados mudam.

A revisão geral do posicionamento de textos/cotas/chamadas nos desenhos ficou registrada como melhoria de baixa prioridade para etapa futura, conforme solicitado.


## Novo na 0.8.3: cortante nos chumbadores

O modelo nativo usa quatro barras ASTM A36 com arruelas especiais quadradas soldadas à placa, furo-padrão db+1,5 mm e dimensões reais de lado/espessura. Calcula as trações simultâneas por barra, a expressão especial da NBR 6.7.2.5, o limite adicional da interação geral de 6.3.3.4 e o limite local de concreto. Aplica o mínimo por barra antes da soma; no limite de tração, a reserva de cortante é zero. Não presume V/4 nem soma atrito ou chave.

A expressão publicada tem índice i na raiz e 1 no termo subtrativo. O app adota explicitamente a maior tração simultânea neste último termo como limite conservador e avisa quando as trações diferem. Isso não é apresentado como correção oficial da norma.

Cada solda recebe como ação de dimensionamento Fv,Rd sem redução. **Soldas, arruelas/transferência local, ancoragem no concreto, bloco e demais verificações da base continuam a complementar.** O limite local de concreto não substitui cone, arrancamento, pryout, bordas ou grupo. O resultado favorável dos componentes não aprova a base completa.

Há desenho das quatro arruelas reais, tabela de trações e resistências individuais, memória Word com equações editáveis e exemplos JSON. Método, domínio e ressalvas: `docs/CHUMBADORES_CORTANTE_V082.md`. Registro de software: `docs/VALIDACAO_V082.md`. A 0.8.1 permanece como distribuição independente.


## Novidades específicas da 0.8.3

- Verificação complementar do cone de arrancamento por tração, segundo o método ACI 318-19 apresentado no DG1, para ancoragem moldada no local com cabeça/porca/placa de apoio e concreto íntegro. Usa as trações simultâneas reais, bordas do bloco e sobreposição dos cones. Não aprova a ancoragem completa.
- Soldas da alma e das mesas escolhidas independentemente: chanfro de penetração total ou filete. Para filete, entrada por perna ou garganta com conversão conservando a dimensão física. Especificação e desenho; resistência geral N/M/V ainda não calculada.
- Graute com talude a 45°, sem aumentar artificialmente a área resistente de contato.
- Vínculo rotulado/engastado como intenção do modelo, sem certificação de rigidez; dois enrijecedores no plano da alma como detalhamento, sem crédito resistente.
- Tipos de chumbador e geometria da peça enterrada separados da arruela superior soldada. Gancho J e barra reta com mecanismo indefinido não recebem resistência de ancoragem inventada.

Consulte `docs/PLACAS_DE_BASE_V083.md`, `docs/CONE_CONCRETO_V083.md` e as pendências específicas exibidas pelo app. Históricos de versões anteriores descrevem o alcance daquelas versões.
