from src.infra.model.resultModel import ResultErrorModel
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper

class GetByParamsProfilePermissionContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')
        profile_system_id = data.get('profile_system_id')
        system_permission_id = data.get('system_permission_id')

        if _id and not _id.isnumeric():
            self.add_error('_id', 'O id precisa ser um inteiro.')
        if profile_system_id and not profile_system_id.isnumeric():
            self.add_error('profile_system_id', 'O ID do perfil do sistema precisa ser um inteiro.')
        if system_permission_id and not system_permission_id.isnumeric():
            self.add_error('system_permission_id', 'O ID da permissão do sistema precisa ser um inteiro.')

        if not _id and not profile_system_id and not system_permission_id:
            self.add_error('id, profile_system_id, system_permission_id', 'É obrigatorio o envio de no minimo um parametro.')
        return self.valid()
