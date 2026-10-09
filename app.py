"""LRO Ligações: entrada para GitHub/Streamlit com arquivos somente na raiz.

O código-fonte completo está em codigo_lro.zip, que deve acompanhar este arquivo.
Nenhum código é baixado da internet na inicialização do aplicativo.
"""
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import runpy
import sys
from tempfile import TemporaryDirectory
from zipfile import BadZipFile, ZipFile

import streamlit as st

BUNDLE_SHA256 = '5b8cbbf19d869dc58756e170c8fb81acdef5d73d4f9e6d24a77a6b9894051575'
BUNDLE_NAME = 'codigo_lro.zip'


@st.cache_resource(show_spinner=False)
def prepare_code(archive_bytes, digest):
    """Uma extração privada por processo, reaproveitada nas interações da tela."""
    if sha256(archive_bytes).hexdigest() != digest:
        raise ValueError('O arquivo de código não corresponde a esta versão do app.py.')
    holder = TemporaryDirectory(prefix='lro_ligacoes_073_')
    root = Path(holder.name)
    try:
        with ZipFile(BytesIO(archive_bytes)) as archive:
            for item in archive.infolist():
                path = Path(item.filename)
                if path.is_absolute() or '..' in path.parts:
                    raise ValueError('Caminho inválido no arquivo de código.')
            archive.extractall(root)
        for name in ('app.py', 'lro/models.py', 'lro/double_cover_ui.py',
                     'lro/end_plate_ui.py', 'data/profiles.json'):
            if not (root / name).is_file():
                raise ValueError('Arquivo obrigatório ausente: ' + name)
    except Exception:
        holder.cleanup()
        raise
    return root, holder


def main():
    archive_path = Path(__file__).resolve().with_name(BUNDLE_NAME)
    if not archive_path.is_file():
        st.error('Falta codigo_lro.zip. Envie esse arquivo, ainda compactado, '
                 'ao GitHub na mesma pasta de app.py e requirements.txt.')
        st.stop()
    try:
        data = archive_path.read_bytes()
        if sha256(data).hexdigest() != BUNDLE_SHA256:
            raise ValueError('app.py e codigo_lro.zip são de pacotes diferentes ou o ZIP foi alterado.')
        root, holder = prepare_code(data, BUNDLE_SHA256)
    except (OSError, ValueError, BadZipFile) as exc:
        st.error('Não foi possível abrir o pacote LRO: ' + str(exc))
        st.info('Reenvie os quatro arquivos do mesmo ZIP de instalação e reinicie o app.')
        st.stop()

    # Uma atualização deve iniciar um novo processo, sem misturar módulos antigos.
    for name, module in tuple(sys.modules.items()):
        if name == 'lro' or name.startswith('lro.'):
            module_file = getattr(module, '__file__', None)
            if module_file and not Path(module_file).resolve().is_relative_to(root):
                st.error('Uma versão anterior está carregada. Reinicie o app no Streamlit '
                         'para abrir todos os módulos da versão 0.7.3 juntos.')
                st.stop()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    runpy.run_path(str(root / 'app.py'), run_name='__main__')


if __name__ == '__main__':
    main()
