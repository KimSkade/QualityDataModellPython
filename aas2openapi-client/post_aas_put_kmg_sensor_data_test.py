from aas2openapi_client import client
from aas2openapi_client.models.quality_data_aas import QualityDataAAS
from services.id_generator import generate_unique_id
from convert_kmg_data import load_kmp_data_in_aas, put_kmg_data
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync
from json_procedure import put_new_process_data
from aas2openapi_client.models.resource import *
from aas2openapi_client.models.new_values_machine_parameter import NewValuesMachineParameter
from aas2openapi_client.models.new_machine_parameter import NewMachineParameter
from aas2openapi_client.models.machine_parameter import MachineParameter
from aas2openapi_client.models.quality_data import *
from aas2openapi_client.models.procedure import *

client = client.Client(base_url="http://127.0.0.1:8000")


# AAS erstellen
aas_post = QualityDataAAS(
  id_short=generate_unique_id(),
  description='',
  id='12string',
  quality_data=QualityData(
    semantic_id='',
    id_short=generate_unique_id(),
    description='',
    id=generate_unique_id(),
    quality_feature= put_kmg_data(dateipfad="PruefplanValidierungsbauteil1_16.txt", breakpoint='END'),
  ),
  procedure=Procedure(
    id_short=generate_unique_id(),
    semantic_id='',
    description='',
    id=generate_unique_id(),
    process_data=put_new_process_data('0574_selected_features.json'),
  ),
  resource=Resource(
    description='',
    id_short=generate_unique_id(),
    id=generate_unique_id(),
    semantic_id='',
    machine_parameter=[MachineParameter(
      id_short=generate_unique_id(),
      semantic_id='',
      description='',
      value_max=3,
      value_min=1,
      value_description='Platzhalter',
    )],
    new_machine_parameter=NewMachineParameter(
      semantic_id='',
      id_short=generate_unique_id(),
      description='',
      new_values_machine_parameter=[NewValuesMachineParameter(
        description='',
        semantic_id='',
        id_short=generate_unique_id(),
        value=[1.0],
        timestamp='Platzhalter',
      )]
    )
  )
)

sync(client=client, json_body=aas_post)







