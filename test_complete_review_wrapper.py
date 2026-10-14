"""Functional test of the exact packaged payload in a fresh bounded process."""
from pathlib import Path
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
import json
import sys
import zipfile

from streamlit.runtime.memory_media_file_storage import MemoryMediaFileStorage
from streamlit.testing.v1 import AppTest

package = Path(sys.argv[1]).resolve()
receipt_path = package / 'WRAPPER_FUNCTIONAL_TEST_RECEIPT.json'
files = {}
count = 0
runs = 0
original = MemoryMediaFileStorage.load_and_get_id


def tap(storage, *args, **kwargs):
    identifier = original(storage, *args, **kwargs)
    files[identifier] = storage._files_by_id[identifier].content
    return identifier


MemoryMediaFileStorage.load_and_get_id = tap


def check(value, note):
    global count
    assert value, note
    count += 1


def clean(at):
    global runs
    runs += 1
    check(not at.exception, [x.message for x in at.exception])


def exported(at, label):
    widget = next(w for w in at.get('download_button') if w.label == label)
    return json.loads(files[Path(widget.proto.url).name.rsplit('.', 1)[0]])


def upload(at, data, label):
    at.file_uploader[0].upload('project.json', json.dumps(data, ensure_ascii=False).encode(), 'application/json').run()
    clean(at)
    next(w for w in at.button if w.label == label).click().run()
    clean(at)


print('STAGE exact full wrapper and current local route', flush=True)
at = AppTest.from_file(str(package / 'app.py'), default_timeout=25)
at.session_state['connection_family'] = 'Viga sobre viga — apoio direto entre mesas'
at.run()
clean(at)
print('INITIAL errors', [x.value for x in at.error], flush=True)
print('INITIAL selectboxes', [(x.key, x.value) for x in at.selectbox], flush=True)
core = sys.modules['lro.beam_direct_seat']
ui = sys.modules['lro.beam_direct_seat_ui']
identity = sys.modules['lro.package_identity']
models = sys.modules['lro.models']
native = deepcopy(at.session_state[ui.STATE + 'project'])
result = at.session_state[ui.STATE + 'result']
check(identity.PACKAGE_ID == '0.9.46-apoio-direto-verificacoes-locais-revisao-dev.2', 'package identity')
check(native['schema_version'] == 3, 'current schema3')
check(native == exported(at, 'Salvar projeto de apoio direto .json'), 'actual download matches session project')
check(core.BeamDirectSeat.from_dict(native).to_dict() == native, 'native canonical roundtrip')
check(result['local_checks_satisfied'] and result['local_strength_checks_satisfied'] and result['local_geometry_checks_satisfied'], 'local flags')
check(not result['pair_strength_credit'] and not result['pair_dimensioned'], 'constructive pair only')
check(not result['global_pass'] and not result['engineering_approved'], 'no overall approval')
check(len([r for r in result['checks'] if r['category'] == 'RESISTANCE']) == 4, 'four web resistance modes only')
check(next(s for s in result['scopes'] if s['id'] == 'local_necessary_5_7_8')['status'] == 'PENDING', 'local required interface remains explicit')
check(next(s for s in result['scopes'] if s['id'] == 'external_stability_5_7_5')['status'] == 'EXTERNAL_REQUIRED', 'stability external')
check(native['connection']['external_length_reported_mm'] == 4000., 'provided length, no computed stability')
check(result['actions']['V_ELU_N'] == 25595.3565 and result['actions']['check_force_N'] == 45000., 'actual ELU and separate minimum')

print('STAGE actual native upload, precision and recalculation', flush=True)
c = core.BeamDirectSeat.from_dict(native)
custom = replace(c, V=25595.35650000013, N=-12.345678901, applied_moment_y=-.00123456789,
                 torsion=1e-323, notes='Precisão do JSON no pacote completo; escopo preservado.')
upload(at, custom.to_dict(), 'Carregar apoio direto')
check(at.session_state[ui.STATE + 'project'] == custom.to_dict(), 'native precision import')
check(exported(at, 'Salvar projeto de apoio direto .json') == custom.to_dict(), 'native precision download')
check(at.session_state[ui.STATE + 'result']['status'] == 'OUTSIDE_SCOPE', 'nonzero actions outside scope')
at.number_input(key=ui.PREFIX + 'N_kgf').set_value(2.123456789).run()
clean(at)
edited = deepcopy(at.session_state[ui.STATE + 'project'])
check(edited['connection']['N'] == 2.123456789 * models.KGF, 'edited N recalculated')
check(edited['connection']['applied_moment_y'] == custom.applied_moment_y and edited['connection']['torsion'] == custom.torsion, 'advanced actions retained')
check(edited == exported(at, 'Salvar projeto de apoio direto .json'), 'edited native download')

print('STAGE actual legacy family, old JSON and alignment interface', flush=True)
legacy = sys.modules['lro.beam_on_beam']
with zipfile.ZipFile(package / 'codigo_lro.zip') as archive:
    historical = json.loads(archive.read('examples/beam_on_beam_actual_partial.json'))
at.selectbox(key='connection_family').set_value(legacy.FAMILY).run()
clean(at)
legacy_ui = sys.modules['lro.beam_on_beam_ui']
print('LEGACY labels', [w.label for w in at.button], [w.label for w in at.get('download_button')], flush=True)
check(any(w.label == 'Nó alinhado ao eixo da viga de apoio?' for w in at.radio), 'original requested alignment question')
check(any('Entradas avançadas' in w.label and 'My' in w.label and 'Tz' in w.label for w in at.expander), 'advanced actions section')
old_c = legacy.BeamOnBeam.from_dict(historical)
check(old_c.to_dict() == historical, 'old native JSON unchanged')
check(sha256(Path(legacy.__file__).read_bytes()).hexdigest() == '9d3d52abe7eb3533b4def96c517056ab678b47470dcd14bbb40f3b1d665180f8', 'legacy engine bytes unchanged')
upload_label = next(w.label for w in at.button if 'Carregar' in w.label)
download_label = next(w.label for w in at.get('download_button') if '.json' in w.label)
upload(at, historical, upload_label)
check(at.session_state[legacy_ui.STATE + 'project'] == historical, 'actual old JSON upload preserves all input values')
check(exported(at, download_label) == historical, 'actual old JSON download preserves unknowns and values')
check(at.session_state[legacy_ui.STATE + 'result'] == legacy.evaluate(old_c), 'legacy result matches unchanged engine')
alignment = next(w for w in at.radio if w.label == 'Nó alinhado ao eixo da viga de apoio?')
check(alignment.value == 'Não informado', 'historical unknown alignment remains unknown')
alignment.set_value('Sim').run()
clean(at)
check(at.session_state[legacy_ui.STATE + 'project']['connection']['reference_x'] == 0., 'explicit aligned choice')
check(at.session_state[legacy_ui.STATE + 'project']['connection']['applied_moment_y'] == historical['connection']['applied_moment_y'], 'alignment does not erase My')
check(at.session_state[legacy_ui.STATE + 'project']['connection']['torsion'] == historical['connection']['torsion'], 'alignment does not erase torsion')
check(at.session_state[legacy_ui.STATE + 'project'] == exported(at, download_label), 'aligned export')

print('STAGE return to current local family and exact payload manifest', flush=True)
at.selectbox(key='connection_family').set_value(core.FAMILY).run()
clean(at)
check(at.session_state[ui.STATE + 'project'] == edited, 'local draft survives legacy route')
check(edited == exported(at, 'Salvar projeto de apoio direto .json'), 'local download after return')
verifier_path = Path(core.__file__).resolve().parents[1] / 'verificar_pacote.py'
import runpy
verifier = runpy.run_path(str(verifier_path))
check(verifier['verify'](verifier_path.parent) == [], 'actual extracted payload manifest')
with zipfile.ZipFile(package / 'codigo_lro.zip') as archive:
    check(archive.testzip() is None, 'actual payload CRC')
    check(archive.read('lro/beam_direct_seat.py') == Path(core.__file__).read_bytes(), 'executed current core is actual packaged core')
receipt = {'outcome': 'PASS', 'assertions_executed': count, 'AppTest_runs': runs,
           'payload_sha256': sha256((package / 'codigo_lro.zip').read_bytes()).hexdigest(),
           'wrapper_sha256': sha256((package / 'app.py').read_bytes()).hexdigest(),
           'package_id': identity.PACKAGE_ID,
           'core_sha256': sha256(Path(core.__file__).read_bytes()).hexdigest(),
           'legacy_core_sha256': sha256(Path(legacy.__file__).read_bytes()).hexdigest(),
           'scope': 'Exact packaged wrapper, dispatcher, actual JSON upload/download, current and legacy routes, precision, recalc and alignment; not physical engineering approval',
           'engineering_approved': False, 'global_pass': False}
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False), flush=True)
