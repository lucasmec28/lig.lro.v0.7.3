"""LRO Ligações: entrada local Streamlit com arquivos na raiz.

O código-fonte completo está em codigo_lro.zip, que deve acompanhar este arquivo.
Nenhum código é baixado da internet na inicialização do aplicativo.
"""
from hashlib import sha256
from io import BytesIO
from pathlib import Path, PurePosixPath
import runpy
import sys
from tempfile import TemporaryDirectory
from zipfile import BadZipFile, ZipFile

import streamlit as st

BUNDLE_SHA256 = '370427cbcd169b2de9a0bc58c2d05e07419b80309e51d8bde30e08d64da33e99'
BUNDLE_NAME = 'codigo_lro.zip'
PACKAGE_ID = '0.9.73'
ADDON_NAME = 'dg39_candidate.zip'
ADDON_SHA256 = '4bd80463e09d646e4431e8e933ce318e693ad31408d3eb8e040a3202efe4c211'


@st.cache_resource(show_spinner=False)
def prepare_code(archive_bytes, digest, addon_bytes, addon_digest):
    """Uma extração privada por processo, reaproveitada nas interações da tela."""
    if sha256(archive_bytes).hexdigest() != digest:
        raise ValueError('O arquivo de código não corresponde a esta versão do app.py.')
    if sha256(addon_bytes).hexdigest() != addon_digest:
        raise ValueError('Extensão DG39 não corresponde a esta revisão.')
    holder = TemporaryDirectory(prefix='lro973coverplate_')
    root = Path(holder.name)
    try:
        with ZipFile(BytesIO(archive_bytes)) as archive:
            seen = set()
            for item in archive.infolist():
                path = PurePosixPath(item.filename)
                # Reject Windows paths and symlinks as well as POSIX traversal.
                if (path.is_absolute() or '..' in path.parts
                        or '\\' in item.filename or ':' in item.filename
                        or not path.parts or item.filename in seen
                        or (item.external_attr >> 16) & 0o170000 == 0o120000):
                    raise ValueError('Caminho inválido no arquivo de código.')
                seen.add(item.filename)
            if archive.testzip() is not None:
                raise ValueError('Arquivo de código corrompido.')
            archive.extractall(root)
        for name in ('lro/welded_coverplate_splice.py', 'lro/welded_coverplate_ui.py', 'lro/welded_coverplate_report.py', 'lro/welded_coverplate_drawing.py', 'app.py', 'lro/models.py', 'lro/double_cover_ui.py',
                     'lro/double_angle_candidates.py', 'lro/double_angle_candidates_ui.py',
                     'lro/guided_selection.py', 'lro/catalogue_ui.py', 'lro/visual_identity.py',
                     'lro/catalogue_image.py', 'data/catalogue_image_component/index.html',
                     'data/catalogue_native.json', 'docs/WELDED_COVERPLATE0973_MANIFEST.json',
                     'lro/end_plate_ui.py', 'data/profiles.json',
                     'lro/w_splice_slip.py','lro/w_splice_conventional.py','lro/bolted_seat.py','lro/seated_variants.py','lro/seated_variants_ui.py','lro/seated_variants_drawing.py','lro/seated_variants_report.py', 'lro/package_identity.py', 'lro/beam_direct_seat.py', 'lro/beam_direct_seat_ui.py', 'lro/beam_direct_seat_presentation.py', 'lro/beam_direct_seat_drawing.py', 'lro/beam_direct_seat_report.py', 'lro/channel_upper_washer.py','lro/channel_base_plate.py','lro/channel_base_plate_ui.py','lro/channel_catalog.py','data/gerdau_u.json'):
            if not (root / name).is_file():
                raise ValueError('Arquivo obrigatório ausente: ' + name)
        # Extensão pequena, local e versionada; não altera o bundle histórico.
        with ZipFile(BytesIO(addon_bytes)) as addon:
            seen_addon = set()
            for item in addon.infolist():
                path = PurePosixPath(item.filename)
                allowed = item.filename == 'app.py' or (len(path.parts) == 2 and path.parts[0] == 'dg39_top_column_candidate' and path.suffix == '.py')
                if (not allowed or path.is_absolute() or '..' in path.parts
                        or '\\' in item.filename or ':' in item.filename
                        or item.filename in seen_addon
                        or (item.external_attr >> 16) & 0o170000 == 0o120000):
                    raise ValueError('Caminho inválido na extensão DG39.')
                seen_addon.add(item.filename)
            required_addon = {'app.py', 'dg39_top_column_candidate/__init__.py', 'dg39_top_column_candidate/ui.py', 'dg39_top_column_candidate/direct4e_route.py'}
            if not required_addon.issubset(seen_addon) or addon.testzip() is not None:
                raise ValueError('Extensão DG39 incompleta ou corrompida.')
            addon.extractall(root)
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
        addon_data = Path(__file__).resolve().with_name(ADDON_NAME).read_bytes()
        root, holder = prepare_code(data, BUNDLE_SHA256, addon_data, ADDON_SHA256)
    except (OSError, ValueError, BadZipFile) as exc:
        st.error('Não foi possível abrir o pacote LRO: ' + str(exc))
        st.info('Use os arquivos da mesma revisao e reinicie o app local.')
        st.stop()

    # Uma atualização deve iniciar um novo processo, sem misturar módulos antigos.
    for name, module in tuple(sys.modules.items()):
        if name in ('lro','dg39_top_column_candidate') or name.startswith(('lro.', 'dg39_top_column_candidate.', 'stiffened_base_app_candidate_20261017', 'stiffened_base_kernels_candidate_20261017')):
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
