from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.get_user_interface import GetUserInterface

class GetUserView(ViewInterface):
    def __init__(self, controller: GetUserInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            query_parameter = body["query_parameter"]
            response = self.__controller.query_user(query_parameter)
            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })