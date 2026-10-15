"""LRO Ligações: entrada local Streamlit com arquivos na raiz.

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

BUNDLE_SHA256 = '915e3f87c1aa2f6efff30bc6db9cd63c4f585c9d2e3f1e3145ff21eb78ffdbc2'
BUNDLE_NAME = 'codigo_lro.zip'
PACKAGE_ID = '0.9.59-endplate-sci-dev.1'


@st.cache_resource(show_spinner=False)
def prepare_code(archive_bytes, digest):
    """Uma extração privada por processo, reaproveitada nas interações da tela."""
    if sha256(archive_bytes).hexdigest() != digest:
        raise ValueError('O arquivo de código não corresponde a esta versão do app.py.')
    holder = TemporaryDirectory(prefix='lro958audit_')
    root = Path(holder.name)
    try:
        with ZipFile(BytesIO(archive_bytes)) as archive:
            for item in archive.infolist():
                path = Path(item.filename)
                if path.is_absolute() or '..' in path.parts:
                    raise ValueError('Caminho inválido no arquivo de código.')
            archive.extractall(root)
        for name in ('app.py', 'lro/models.py', 'lro/double_cover_ui.py',
                     'lro/end_plate_ui.py', 'data/profiles.json',
                     'lro/w_splice_slip.py','lro/w_splice_conventional.py','lro/bolted_seat.py','lro/seated_variants.py','lro/seated_variants_ui.py','lro/seated_variants_drawing.py','lro/seated_variants_report.py', 'lro/package_identity.py', 'lro/beam_direct_seat.py', 'lro/beam_direct_seat_ui.py', 'lro/beam_direct_seat_presentation.py', 'lro/beam_direct_seat_drawing.py', 'lro/beam_direct_seat_report.py', 'lro/channel_upper_washer.py','lro/channel_base_plate.py','lro/channel_base_plate_ui.py','lro/channel_catalog.py','data/gerdau_u.json'):
            if not (root / name).is_file():
                raise ValueError('Arquivo obrigatório ausente: ' + name)
        identity = runpy.run_path(str(root / 'lro/package_identity.py'))
        if identity.get('PACKAGE_ID') != PACKAGE_ID:
            raise ValueError('Identidade do pacote de revisao incompativel.')
    except Exception:
        holder.cleanup()
        raise
    return root, holder


def main():
    archive_path = Path(__file__).resolve().with_name(BUNDLE_NAME)
    if not archive_path.is_file():
        st.error('Falta codigo_lro.zip. Descompacte o pacote completo e mantenha esse ZIP '
                 'na mesma pasta de app.py e requirements.txt.')
        st.stop()
    try:
        data = archive_path.read_bytes()
        if sha256(data).hexdigest() != BUNDLE_SHA256:
            raise ValueError('app.py e codigo_lro.zip são de pacotes diferentes ou o ZIP foi alterado.')
        root, holder = prepare_code(data, BUNDLE_SHA256)
    except (OSError, ValueError, BadZipFile) as exc:
        st.error('Não foi possível abrir o pacote LRO: ' + str(exc))
        st.info('Use os arquivos da mesma revisao e reinicie o app local.')
        st.stop()

    # Uma atualização deve iniciar um novo processo, sem misturar módulos antigos.
    for name, module in tuple(sys.modules.items()):
        if name == 'lro' or name.startswith('lro.'):
            module_file = getattr(module, '__file__', None)
            if module_file and not Path(module_file).resolve().is_relative_to(root):
                st.error('Uma versão anterior está carregada. Reinicie o app no Streamlit '
                         'para abrir todos os modulos desta revisao juntos.')
                st.stop()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    runpy.run_path(str(root / 'app.py'), run_name='__main__')


if __name__ == '__main__':
    main()
