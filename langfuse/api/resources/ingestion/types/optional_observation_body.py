# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...commons.types.observation_level import ObservationLevel


class OptionalObservationBody(pydantic_v1.BaseModel):
    trace_id: typing.Optional[str] = pydantic_v1.Field(alias="traceId", default=None)
    name: typing.Optional[str] = None
    start_time: typing.Optional[dt.datetime] = pydantic_v1.Field(
        alias="startTime", default=None
    )
    metadata: typing.Optional[typing.Any] = None
    input: typing.Optional[typing.Any] = None
    output: typing.Optional[typing.Any] = None
    level: typing.Optional[ObservationLevel] = None
    status_message: typing.Optional[str] = pydantic_v1.Field(
        alias="statusMessage", default=None
    )
    parent_observation_id: typing.Optional[str] = pydantic_v1.Field(
        alias="parentObservationId", default=None
    )
    version: typing.Optional[str] = None
    environment: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        kwargs_with_defaults_exclude_none: typing.Any = {
            "by_alias": True,
            "exclude_none": True,
            **kwargs,
        }

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset),
            super().dict(**kwargs_with_defaults_exclude_none),
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
