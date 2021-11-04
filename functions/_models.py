from typing import Optional, Dict, TYPE_CHECKING, List

from pydantic import BaseModel, StrictStr, constr, conint, conlist


class RequestContextAuthorizerInfo(BaseModel):
    user_email: StrictStr


class EventRequestContext(BaseModel):
    authorizer: RequestContextAuthorizerInfo


class EventModelBodyParameters(BaseModel):
    body: Optional[StrictStr] = None
    pathParameters: Dict[StrictStr, StrictStr]
    requestContext: EventRequestContext


if TYPE_CHECKING:
    _email_field: str
else:
    _email_field = constr(strict=True, regex=r"^\S+@\S+\.\S+$")


class RoleMember(BaseModel):
    email: _email_field


if TYPE_CHECKING:
    _role_member_list_field = List[RoleMember]
else:
    _role_member_list_field = conlist(item_type=RoleMember)


class RoleMemberListAdd(BaseModel):
    add: _role_member_list_field = []


class PostAppEnvAuthorization(BaseModel):
    envPracticioner: RoleMemberListAdd = RoleMemberListAdd()
    envConsumer: RoleMemberListAdd = RoleMemberListAdd()
    admin: RoleMemberListAdd = RoleMemberListAdd()


if TYPE_CHECKING:
    _memory_mb_field = int
    _cpu_millicores_field = int
else:
    _memory_mb_field = conint(strict=True, ge=200, le=9500)
    _cpu_millicores_field = conint(strict=True, ge=100, le=3000)

DEFAULT_MEMORY_MB = 2500
DEFAULT_CPU_MILLICORES = 1000


class ResourcesConfigurationModel(BaseModel):
    memoryMB: _memory_mb_field = DEFAULT_MEMORY_MB
    cpuMillicores: _cpu_millicores_field = DEFAULT_CPU_MILLICORES


if TYPE_CHECKING:
    _env_name_field = str
    _env_var_name_field = str
    _cached_files_s3_bucket_location = str
else:
    _env_name_field = constr(strict=True, min_length=1, max_length=10)
    _env_var_name_field = constr(strict=True, regex=r"(?i)^(?!DAVOR_)")
    _cached_files_s3_bucket_location = constr(strict=True, regex=r"^s3://[a-z0-9-]+(/[a-z0-9-]+)*$")

_env_var_field = Dict[_env_var_name_field, StrictStr]


class PostAppEventBody(BaseModel):
    environment: _env_name_field
    envVariables: _env_var_field = {}
    branchName: StrictStr
    logSharingAwsAccountIds: List[StrictStr] = []
    resourcesConfiguration: ResourcesConfigurationModel = ResourcesConfigurationModel()
    cachedFilesS3BucketLocation: Optional[_cached_files_s3_bucket_location] = None
    authorization: PostAppEnvAuthorization = PostAppEnvAuthorization()
