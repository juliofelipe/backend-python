from src.data.find_pet import FindPet
from src.infra.repo.pet_repository import PetRepository
from src.presenters.controllers import FindPetController


def find_pet_composer() -> FindPetController:
    """Composing Find Pet Route
    :param - None
    :return - Object with Find Pet Route
    """

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_route = FindPetController(use_case)

    return find_pet_route
