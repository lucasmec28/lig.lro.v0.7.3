# LRO Ligações 0.7.3 — pacote completo para repositório novo

## Os quatro arquivos que devem aparecer no GitHub

| Arquivo | Função |
|---|---|
| `app.py` | Arquivo principal selecionado no Streamlit |
| `codigo_lro.zip` | Todos os módulos, catálogo de perfis, exemplos e documentação |
| `requirements.txt` | Bibliotecas instaladas automaticamente pelo Streamlit |
| `README.md` | Estas instruções |

Extraia o ZIP principal `LRO_Ligacoes_COMPLETO_v0_7_3.zip`. Envie os **quatro arquivos resultantes** diretamente à raiz do repositório. Mantenha `codigo_lro.zip` compactado: o próprio aplicativo o abre ao iniciar. Nesta distribuição não é necessário criar nem enviar pastas `lro/`, `data/` ou `docs/` separadamente.

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
7. Ao abrir, confira a versão **0.7.3** e as quatro famílias do seletor **Tipo de ligação**.

Ao atualizar futuramente, envie os quatro arquivos do novo pacote juntos e reinicie o app. O inicializador identifica se `app.py` e `codigo_lro.zip` pertencem à mesma distribuição, evitando misturar módulos de versões diferentes.

## Ligações incluídas

- **Single plate viga–viga**, com complemento entre mesas e enrijecedor oposto opcionais.
- **Single plate viga–mesa da coluna**.
- **Viga–alma da coluna com duas talas**, nervura vertical e enrijecedores horizontais.
- **End plate rotulada** na mesa da coluna.
- **End plate engastada** na mesa da coluna, com extensão acima e abaixo ou somente acima, no domínio implementado.

As duas single plates são acessadas pela mesma família no seletor. O pacote inclui cálculo, desenhos proporcionais, projetos JSON, catálogo de perfis, geração de memória Word e documentação dos métodos.

## O que mudou nesta versão

Esta versão altera a distribuição e a inicialização. Os cálculos e os limites técnicos da versão 0.7.2 são preservados. O enrijecedor oposto continua sendo uma opção de detalhamento, sem aumento atribuído à resistência à punção; as premissas e exclusões permanecem na tela e no Word.

No print recebido em 09/10/2026, todos os caminhos de `lro/` e `data/` foram indicados como ausentes no local esperado. O novo formato reúne esses caminhos dentro de um único arquivo de código e não depende do envio de pastas pelo navegador.

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
