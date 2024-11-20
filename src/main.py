from Containers import Application
from dotenv import load_dotenv
import os
from domain.exceptions.application_error import ApplicationError

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Access the Application container which includes the Services container
    application_container = Application()

    load_dotenv(dotenv_path='src/config/app.env')

    # Get the variables
    millennium_falcon_file_path = os.getenv('MILLENNIUM_FALCON_FILE_PATH')
    empire_json_file_path = os.getenv('EMPIRE_JSON_FILE_PATH')

    try:
        # Retrieve the C3POService instance from the container (with its dependencies injected)
        c3po_service = application_container.services.C3PO_Service(millennium_falcon_file_path)
        # Call the giveMeTheOdds function from the C3POService
        odds = c3po_service.giveMeTheOdds(empire_json_file_path)
        print(f"The odds of success are: {odds}")
    except ApplicationError as e:
        print(e.__str__())
    except Exception as e:
        print(e.__str__())



