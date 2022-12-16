from django.http import HttpResponse

from .tasks import loaddata


def update_data(request):
    time_dict = loaddata()
    return HttpResponse(f'parse_time : {time_dict["parse_time"]}s, '
                        f'teams_time : {time_dict["teams_time"]}s, '
                        f'shares_time : {time_dict["shares_time"]}s, '
                        f'teamshares_time : {time_dict["teamshares_time"]}s, '
                        f'operations_time : {time_dict["operations_time"]}s, '
                        f'general_time : {time_dict["general_time"]}s')
