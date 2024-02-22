from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.post_user_interface import PostUserInterface

class PostUserView(ViewInterface):
    def __init__(self, controller: PostUserInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            first_name = body["first_name"]
            second_name = body["second_name"]
            elements = {"first_name": first_name, "second_name": second_name}
            response = self.__controller.insert_user(elements)
            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })