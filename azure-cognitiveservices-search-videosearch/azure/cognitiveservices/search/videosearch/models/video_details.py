# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response import Response


class VideoDetails(Response):
    """VideoDetails.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar related_videos:
    :vartype related_videos:
     ~azure.cognitiveservices.search.videosearch.models.VideosModule
    :ivar video_result:
    :vartype video_result:
     ~azure.cognitiveservices.search.videosearch.models.VideoObject
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'related_videos': {'readonly': True},
        'video_result': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'related_videos': {'key': 'relatedVideos', 'type': 'VideosModule'},
        'video_result': {'key': 'videoResult', 'type': 'VideoObject'},
    }

    def __init__(self, **kwargs):
        super(VideoDetails, self).__init__(**kwargs)
        self.related_videos = None
        self.video_result = None
        self._type = 'VideoDetails'
