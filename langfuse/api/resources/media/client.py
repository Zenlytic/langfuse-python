# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from .types.get_media_response import GetMediaResponse
from .types.get_media_upload_url_request import GetMediaUploadUrlRequest
from .types.get_media_upload_url_response import GetMediaUploadUrlResponse
from .types.patch_media_body import PatchMediaBody

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MediaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, media_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMediaResponse:
        """
        Get a media record

        Parameters
        ----------
        media_id : str
            The unique langfuse identifier of a media record

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMediaResponse

        Examples
        --------
        from langfuse.api.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.media.get(
            media_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/media/{jsonable_encoder(media_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetMediaResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch(
        self,
        media_id: str,
        *,
        request: PatchMediaBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Patch a media record

        Parameters
        ----------
        media_id : str
            The unique langfuse identifier of a media record

        request : PatchMediaBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from langfuse.api import PatchMediaBody
        from langfuse.api.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.media.patch(
            media_id="string",
            request=PatchMediaBody(
                uploaded_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                upload_http_status=1,
                upload_http_error="string",
                upload_time_ms=1,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/media/{jsonable_encoder(media_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_upload_url(
        self,
        *,
        request: GetMediaUploadUrlRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMediaUploadUrlResponse:
        """
        Get a presigned upload URL for a media record

        Parameters
        ----------
        request : GetMediaUploadUrlRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMediaUploadUrlResponse

        Examples
        --------
        from langfuse.api import GetMediaUploadUrlRequest, MediaContentType
        from langfuse.api.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.media.get_upload_url(
            request=GetMediaUploadUrlRequest(
                trace_id="string",
                observation_id="string",
                content_type=MediaContentType.IMAGE_PNG,
                content_length=1,
                sha_256_hash="string",
                field="string",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/media",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(
                    GetMediaUploadUrlResponse, _response.json()
                )  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMediaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, media_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMediaResponse:
        """
        Get a media record

        Parameters
        ----------
        media_id : str
            The unique langfuse identifier of a media record

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMediaResponse

        Examples
        --------
        import asyncio

        from langfuse.api.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.media.get(
                media_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/media/{jsonable_encoder(media_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetMediaResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch(
        self,
        media_id: str,
        *,
        request: PatchMediaBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Patch a media record

        Parameters
        ----------
        media_id : str
            The unique langfuse identifier of a media record

        request : PatchMediaBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from langfuse.api import PatchMediaBody
        from langfuse.api.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.media.patch(
                media_id="string",
                request=PatchMediaBody(
                    uploaded_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    upload_http_status=1,
                    upload_http_error="string",
                    upload_time_ms=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/media/{jsonable_encoder(media_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_upload_url(
        self,
        *,
        request: GetMediaUploadUrlRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMediaUploadUrlResponse:
        """
        Get a presigned upload URL for a media record

        Parameters
        ----------
        request : GetMediaUploadUrlRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMediaUploadUrlResponse

        Examples
        --------
        import asyncio

        from langfuse.api import GetMediaUploadUrlRequest, MediaContentType
        from langfuse.api.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.media.get_upload_url(
                request=GetMediaUploadUrlRequest(
                    trace_id="string",
                    observation_id="string",
                    content_type=MediaContentType.IMAGE_PNG,
                    content_length=1,
                    sha_256_hash="string",
                    field="string",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/media",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(
                    GetMediaUploadUrlResponse, _response.json()
                )  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
