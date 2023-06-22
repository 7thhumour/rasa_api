# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict

class CreateAccountForm(FormValidationAction):
    def name(self) -> Text:
        return "create_account_form"

    @staticmethod
    def required_slots(tracker):
        return ["email, name, address, number, age"]

    def submit(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "email": [
                self.from_entity(entity="email"),
                self.from_intent(intent="deny", value="None")
            ],
            "name":[
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "address":[
                self.from_text(intent="inform"),
            ],
            "number":[
                self.from_text(intent="inform"),
            ],
            "age":[
                self.from_text(intent="inform"),
            ],
        }