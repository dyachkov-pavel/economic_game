import time

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from EconomicGame.celery import app
from teams.models import Operation, Share, TeamShare, TeamUser

from loaddata.google_sheets import DfGetter


@app.task
def loaddata():
    start_time = time.perf_counter()
    parsed_data = DfGetter()
    end_time = time.perf_counter()
    parse_time = end_time - start_time

    def loadteams(data):
        start_time = time.perf_counter()
        try:
            for index, row in data.iterrows():
                print(index, row)
            TeamUser.objects.all().exclude(is_superuser=True).delete()
            # new_users_list = []
            # for index, row in data.iterrows():
            #     new_users_list.append(
            #         TeamUser(account=row['number'],
            #                  password=make_password(password),
            #                  name=index,
            #                  balance=row['money'].replace(',', '.'),
            #                  debit=row['depozit'],
            #                  credit=row['credit'],)
            #     )
            # TeamUser.objects.bulk_create(new_users_list)

            TeamUser.objects.bulk_create([
                TeamUser(
                    account=row['number'],
                    password=make_password(str(row['key'])),
                    name=index,
                    balance=row['money'].replace(',', '.'),
                    debit=row['depozit'],
                    credit=row['credit'],
                ) for index, row in data.iterrows()
            ])
        except Exception as e:
            print('TeamUser error:', e)
        end_time = time.perf_counter()
        return (end_time - start_time)

    def loadshares(data):
        start_time = time.perf_counter()
        try:
            Share.objects.all().delete()
            Share.objects.bulk_create([
                Share(
                    name=row['name'],
                    price=row['price'],
                ) for index, row in data.iterrows()
            ])
        except Exception as e:
            print('Shares error:', e)
        end_time = time.perf_counter()
        return (end_time - start_time)

    def loadteamshares(data):
        start_time = time.perf_counter()
        try:
            TeamShare.objects.all().delete()
            teamshares = []
            for index, row in data.iterrows():
                try:
                    team = TeamUser.objects.get(name=row['team_id'])
                    share = Share.objects.get(name=row['share_id'])
                    teamshare = TeamShare(team=team,
                                        share=share,
                                        amount=row['amount'])
                    teamshares.append(teamshare)
                except ObjectDoesNotExist:
                    print(f'Team or share doesn`t exist')
            TeamShare.objects.bulk_create(teamshares)
        except Exception as e:
            print('TeamShares error:', e)
        end_time = time.perf_counter()
        return (end_time - start_time)

    def loadoperations(data):
        start_time = time.perf_counter()
        try:
            Operation.objects.all().delete()
            operations = []
            for index, row in data.iterrows():
                try:
                    team = TeamUser.objects.get(account=index)
                    operation = Operation(
                        money=row['op'],
                        team=team,
                    )
                    operations.append(operation)
                except ObjectDoesNotExist:
                    print(f'User with account = {index} doesn`t exist')
            Operation.objects.bulk_create(operations)
        except Exception as e:
            print('Operations error:', e)
        end_time = time.perf_counter()
        return (end_time - start_time)

    teams_time = loadteams(parsed_data.datateam)
    shares_time = loadshares(parsed_data.prices)
    teamshares_time = loadteamshares(parsed_data.stocks)
    operations_time = loadoperations(parsed_data.operations)

    general_time = time.perf_counter() - start_time
    return {'parse_time': parse_time,
            'teams_time': teams_time,
            'shares_time': shares_time,
            'teamshares_time': teamshares_time,
            'operations_time': operations_time,
            'general_time': general_time, }
