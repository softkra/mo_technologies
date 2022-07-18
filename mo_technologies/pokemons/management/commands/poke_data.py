import requests 
from django.core.management.base import BaseCommand
from pokemons.models import Pokemons, Logs
from pokemons.serializers import PokemonSerializer, LogsSerializer

class Command(BaseCommand):
    help = 'Get data from PokeAPI'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Indicates the pokemon number')

    def handle(self, *args, **kwargs):
        id = str(kwargs['id'])
        self.log_list = []
        self.create_pokemon(id)
    
    def create_pokemon(self, id):
        """
        Multiples requests to pokeapi and save necessary data 

        Keyword arguments:
        id -- Evolution chain ID
        """
        try:
            data = {}
            response = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{id}/")
            self.create_log_object(response)
            json_response = response.json()
            url_species = json_response["chain"]["species"]["url"]
            response_species = requests.get(url_species)
            self.create_log_object(response_species)
            varieties = response_species.json()['varieties']
            for row in varieties:
                pokemon_url = row['pokemon']['url']
                pokemon_response = requests.get(pokemon_url)
                self.create_log_object(pokemon_response)
                pokemon_response = pokemon_response.json()
                if pokemon_response.get('id', None):
                    if not Pokemons.objects.filter(id=pokemon_response['id']).exists():
                        data = {
                            "id": pokemon_response.get('id', ""),
                            "name": pokemon_response.get('name', ""),
                            "stats": pokemon_response.get('stats', []),
                            "height": pokemon_response.get('height', 0),
                            "weight": pokemon_response.get('weight', 0),
                            "evolution": json_response["chain"]["evolves_to"],
                        }
                        serializer = PokemonSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            self.stdout.write(f"Pokemon {serializer.data['name']} created with ID {serializer.data['id']}")
                        else:
                            print("Validation Errors: ", serializer.errors)
                    else:
                        self.stdout.write(f"Pokemon \'{pokemon_response['name']}\' already exist with ID {pokemon_response['id']}")
        except requests.exceptions.JSONDecodeError as e:
            self.stdout.write("An Json error ocurred!!! (The error was registered in admin logs)")
            log = self.log_list[-1]
            log['message'] = f"500: JSONDecodeError :{e}"
            self.log_list[-1] = log
        except KeyError as e:
            self.stdout.write("An Key error ocurred!!! (The error was registered in admin logs)")
            log = self.log_list[-1]
            log['message'] = f"500: Key Error :{e}"
            self.log_list[-1] = log
        finally:
            self.register_logs()
            self.stdout.write("Command Execution Finish!!!")

    def create_log_object(self, obj):
        """
        Create dict log.

        Keyword arguments:
        obj -- request response
        """
        log = {
            "request_url": obj.url,
            "response_status" : obj.status_code,
            "response_body" : obj.content.decode("utf-8"),
            "message" : ""
        }
        self.log_list.append(log)

    def register_logs(self):
        """
        Save requests content to log model
        """
        for row in self.log_list:
            serielizer = LogsSerializer(data=row)
            if serielizer.is_valid():
                serielizer.save()
        self.log_list = []
